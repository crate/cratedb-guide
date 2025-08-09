(risingwave-iceberg)=

# Stream processing from Iceberg tables to CrateDB using RisingWave

[RisingWave] is a stream processing platform that allows configuring data
sources, views on that data, and destinations where results are materialized.

This guide aims to show you an example with data coming from an Iceberg table
and aggregations materialized in real-time in CrateDB.

## Environment setup

For this example, we will spin up 3 containers using [Podman]

Let's first start a [Minio] instance:

```bash
podman run -d --name minio -p 9000:9000 -p 9001:9001 \
  -e MINIO_ROOT_USER=minioadmin \
  -e MINIO_ROOT_PASSWORD=minioadmin \
  quay.io/minio/minio server /data --console-address ":9001"
```

Now let's create a bucket called `warehouse`, for this point a browser to
`http://localhost:9001`, log in with `minioadmin`/`minioadmin`, click 
"Create bucket", name it `warehouse`, and click again on "Create bucket".

Then we will spin up an instance of RisingWave:

```bash
podman run -d --name risingwave -it -p 4566:4566 -p 5691:5691 docker.io/risingwavelabs/risingwave:v2.4.0 single_node
```

And finally, an instance of CrateDB:

```bash
podman run -d --name cratedb --publish=4200:4200 --publish=5432:5432 --env CRATE_HEAP_SIZE=1g docker.io/crate/crate:5.10.7 -Cdiscovery.type=single-node
```

We will need three terminals for this demonstration.

On the first terminal, we will use [PyIceberg] and [IPython] to create an Iceberg
table, and later we will add data and see how aggregations materialize in
CrateDB in real-time.

On the second terminal, we will do the RisingWave and CrateDB setups, and we will
leave a Python script running for the streaming of changes.

And on the third terminal, we will review how data appears in CrateDB.

## Creating an Iceberg table

Let's start on the first terminal. We use a Python script to create an Iceberg
table on the bucket we created earlier on Minio, and as we want to keep things
simple, we will use an ephemeral in-memory catalog.

```bash
pip install pyiceberg pyarrow s3fs
ipython3
```

```python
from datetime import datetime

import pyarrow as pa
from pyiceberg.catalog.sql import SqlCatalog
from pyiceberg.schema import Schema
from pyiceberg.types import DoubleType, LongType, NestedField, TimestampType

catalog = SqlCatalog(
    "default",
    **{
        "uri": "sqlite:///:memory:",
        "warehouse": f"s3://warehouse",
        "s3.endpoint": "http://localhost:9000",
        "py-io-impl": "pyiceberg.io.pyarrow.PyArrowFileIO",
        "s3.access-key-id": "minioadmin",
        "s3.secret-access-key": "minioadmin",
    },
)

schema = Schema(
    NestedField(field_id=1, name="sensor_id", field_type=LongType()),
    NestedField(field_id=2, name="ts", field_type=TimestampType()),
    NestedField(field_id=3, name="reading", field_type=DoubleType()),
)

catalog.create_namespace("db")

table = catalog.create_table(
    identifier="db.sensors_readings", schema=schema, properties={"format-version": "2"}
)


def create_risingwave_compatible_metadata(table, version):
    metadata_location = table.metadata_location
    metadata_dir = metadata_location.rsplit("/", 1)[0]
    version_hint_path = f"{metadata_dir}/version-hint.text"
    output_file = table.io.new_output(version_hint_path)
    with output_file.create(overwrite=True) as f:
        f.write(version.encode("utf-8"))
    v1_metadata_path = f"{metadata_dir}/v{version}.metadata.json"
    input_file = table.io.new_input(metadata_location)
    with input_file.open() as f_in:
        content = f_in.read()
    output_file = table.io.new_output(v1_metadata_path)
    with output_file.create() as f_out:
        f_out.write(content)


create_risingwave_compatible_metadata(table, "1")
```

## RisingWave and CrateDB setups

Let's now switch to the second terminal.

To interact with both CrateDB and RisingWave we will use the `psql` command line
utility, let's install it:

```bash
sudo apt-get install -y postgresql-client
```

Now let's connect first to CrateDB to create a table where we will keep the
average reading for each sensor:

```bash
psql -h localhost -U crate
```

```sql
CREATE TABLE public.average_sensor_readings (
    sensor_id BIGINT PRIMARY KEY,
    average_reading DOUBLE
);
```

Ctrl+D

Now we need to tell RisingWave to source the data from the Iceberg table:

```bash
psql -h localhost -p 4566 -d dev -U root
```

```sql
CREATE SOURCE sensors_readings
WITH (
    connector = 'iceberg',
    database.name='db.db',
    warehouse.path='s3://warehouse/',
    table.name='sensors_readings',
    s3.endpoint = 'http://host.containers.internal:9000',
    s3.access.key = 'minioadmin',
    s3.secret.key = 'minioadmin',
    s3.region = 'minio'
);
```

And to materialize the averages:

```sql
CREATE MATERIALIZED VIEW average_sensor_readings AS
SELECT
    sensor_id,
    AVG(reading) AS average_reading
FROM sensors_readings
GROUP BY sensor_id;
```

Ctrl+D

And we will now install some dependencies:

```bash
pip install pandas records sqlalchemy-cratedb
pip install psycopg2-binary
pip install --upgrade packaging
pip install --upgrade 'risingwave-py @ git+https://github.com/risingwavelabs/risingwave-py.git@833ca13041cb73cd96fa5cb1c898db2a558d5d8c'
```

And kick off the Python script that will keep CrateDB up-to-date in real-time:

```bash
cat <<EOF >>cratedb_event_handler.py
```

```python
import threading

import pandas as pd
import records
from risingwave import OutputFormat, RisingWave, RisingWaveConnOptions

rw = RisingWave(
    RisingWaveConnOptions.from_connection_info(
        host="localhost", port=4566, user="root", password="root", database="dev"
    )
)


def cratedb_event_handler(event: pd.DataFrame):
    cratedb = records.Database("crate://", echo=True)
    for _, row in event.iterrows():
        if row["op"] == "Insert" or row["op"] == "UpdateInsert":
            cratedb.query(
                "INSERT INTO public.average_sensor_readings (sensor_id,average_reading) VALUES (:sensor_id,:average_reading);",
                **dict(
                    sensor_id=row["sensor_id"],
                    average_reading=row["average_reading"],
                ),
            )
        if row["op"] == "Delete" or row["op"] == "UpdateDelete":
            cratedb.query(
                "DELETE FROM public.average_sensor_readings WHERE sensor_id=:sensor_id;",
                **dict(sensor_id=row["sensor_id"]),
            )


def subscribe_average_sensor_readings_change():
    rw.on_change(
        subscribe_from="average_sensor_readings",
        handler=cratedb_event_handler,
        output_format=OutputFormat.DATAFRAME,
    )


threading.Thread(target=subscribe_average_sensor_readings_change).start()
```

```bash
EOF

python cratedb_event_handler.py
```

## Adding some data and seeing results materialize in real-time

Let's go back to the first terminal and run:

```python
data = pa.Table.from_pydict(
    {
        "sensor_id": [1, 1],
        "ts": [
            datetime.strptime("2025-05-14 14:00", "%Y-%m-%d %H:%M"),
            datetime.strptime("2025-05-14 15:00", "%Y-%m-%d %H:%M"),
        ],
        "reading": [1.2, 3.4],
    }
)

table.append(data)

create_risingwave_compatible_metadata(table, "2")
```

Now let's go to the third terminal. Let connect to CrateDB:

```bash
psql -h localhost -U crate
```

And let's inspect the average_sensor_readings table:

```sql
SELECT * FROM public.average_sensor_readings;
```

The average for sensor 1 is 2.3

Let's go back to the first terminal and run:

```python
data = pa.Table.from_pydict(
    {
        "sensor_id": [1, 1],
        "ts": [
            datetime.strptime("2025-06-04 14:00", "%Y-%m-%d %H:%M"),
            datetime.strptime("2025-06-04 15:00", "%Y-%m-%d %H:%M"),
        ],
        "reading": [5.6, 7.8],
    }
)

table.append(data)

create_risingwave_compatible_metadata(table, "3")
```

If we now check `average_sensor_readings` from the third terminal, we will see
that the average has already changed to 4.5.

[RisingWave]: https://github.com/risingwavelabs/risingwave
[Podman]: https://github.com/containers/podman
[Minio]: https://github.com/minio/minio
[PyIceberg]: https://github.com/apache/iceberg-python
[IPython]: https://github.com/ipython/ipython
