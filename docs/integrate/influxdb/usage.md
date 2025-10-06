(influxdb-usage)=
# Import data from InfluxDB

In this quick usage guide, you will use the [CrateDB Toolkit InfluxDB I/O subsystem]
to import data from [InfluxDB] into [CrateDB]. You can also import data directly
from files in InfluxDB line protocol format.

## Synopsis

### InfluxDB Server
Transfer data from InfluxDB bucket/measurement into CrateDB schema/table.
```shell
ctk load table \
  "influxdb2://example:token@influxdb.example.org:8086/testdrive/demo" \
  --cluster-url="crate://user:password@cratedb.example.org:4200/testdrive/demo"
```
Query data in CrateDB.
```shell
export CRATEPW=password
crash --host=cratedb.example.org --username=user --command='SELECT * FROM testdrive.demo;'
```

### InfluxDB Line Protocol
Transfer data from InfluxDB line protocol file into CrateDB schema/table.
```shell
ctk load table \
  "https://github.com/influxdata/influxdb2-sample-data/raw/master/air-sensor-data/air-sensor-data.lp" \
  --cluster-url="crate://user:password@cratedb.example.org:4200/testdrive/air-sensor-data"
```
Query data in CrateDB.
```shell
export CRATEPW=password
crash --host=cratedb.example.org --username=user --command='SELECT * FROM testdrive."air-sensor-data";'
```

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

## Submit data

Write a few sample records to InfluxDB.
```shell
docker compose exec influxdb influx write --bucket=testdrive --org=example --token=token --precision=s "demo,region=amazonas temperature=27.4,humidity=92.3,windspeed=4.5 1588363200"
docker compose exec influxdb influx write --bucket=testdrive --org=example --token=token --precision=s "demo,region=amazonas temperature=28.2,humidity=88.7,windspeed=4.7 1588549600"
docker compose exec influxdb influx write --bucket=testdrive --org=example --token=token --precision=s "demo,region=amazonas temperature=27.9,humidity=91.6,windspeed=3.2 1588736000"
docker compose exec influxdb influx write --bucket=testdrive --org=example --token=token --precision=s "demo,region=amazonas temperature=29.1,humidity=88.1,windspeed=2.4 1588922400"
docker compose exec influxdb influx write --bucket=testdrive --org=example --token=token --precision=s "demo,region=amazonas temperature=28.6,humidity=93.4,windspeed=2.9 1589108800"
```

Invoke the data transfer pipeline, importing data from
InfluxDB bucket/measurement into CrateDB schema/table.
```shell
docker compose run --rm --no-TTY cratedb-toolkit ctk load table "influxdb2://example:token@influxdb:8086/testdrive/demo" --cluster-url="crate://crate@cratedb:4200/doc/influxdb_demo"
```

## Explore data

Inspect data stored in CrateDB.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.influxdb_demo"
```
```psql
+---------------+----------+----------+-------------+-----------+
|          time | region   | humidity | temperature | windspeed |
+---------------+----------+----------+-------------+-----------+
| 1588549600000 | amazonas |     88.7 |        28.2 |       4.7 |
| 1588363200000 | amazonas |     92.3 |        27.4 |       4.5 |
+---------------+----------+----------+-------------+-----------+
SELECT 2 rows in set (0.027 sec)
```


[CrateDB]: https://github.com/crate/crate
[CrateDB Toolkit InfluxDB I/O subsystem]: https://cratedb-toolkit.readthedocs.io/io/influxdb/loader.html
[InfluxDB]: https://github.com/influxdata/influxdb
