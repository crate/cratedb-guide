(influxdb-tutorial)=
# Import data from InfluxDB

In this quick tutorial, you will use the [CrateDB Toolkit InfluxDB I/O subsystem]
to import data from [InfluxDB] into [CrateDB]. You can also import data directly
from files in InfluxDB line protocol format.

## Synopsis

### InfluxDB Server
Transfer data from InfluxDB bucket/measurement into CrateDB schema/table.
```shell
ctk load table \
  "influxdb2://example:token@influxdb.example.org:8086/testdrive/demo" \
  --cratedb-sqlalchemy-url="crate://user:password@cratedb.example.org:4200/testdrive/demo"
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
  --cratedb-sqlalchemy-url="crate://user:password@cratedb.example.org:4200/testdrive/air-sensor-data"
```
Query data in CrateDB.
```shell
export CRATEPW=password
crash --host=cratedb.example.org --username=user --command='SELECT * FROM testdrive."air-sensor-data";'
```


## Data Model

InfluxDB stores time series data in buckets and measurements. CrateDB stores
data in schemas and tables.

- A **bucket** is a named location with a retention policy where time series data is stored.
- A **series** is a logical grouping of data defined by shared measurement, tag, and field.
- A **measurement** is similar to an SQL database table.
- A **tag** is similar to an indexed column in an SQL database.
- A **field** is similar to an un-indexed column in an SQL database.
- A **point** is similar to an SQL row.

> via: [What are series and bucket in InfluxDB]

## Tutorial

The tutorial heavily uses Docker to provide services and to run jobs.
Alternatively, you can use the drop-in replacement Podman.
The walkthrough uses basic example setup including InfluxDB 2.x and
a few samples worth of data that is being transferred to CrateDB.

### Services

Prerequisites are running instances of CrateDB and InfluxDB.

Start InfluxDB.
:::{code} shell
docker run --rm -it --name=influxdb \
  --publish=8086:8086 \
  --env=DOCKER_INFLUXDB_INIT_MODE=setup \
  --env=DOCKER_INFLUXDB_INIT_USERNAME=admin \
  --env=DOCKER_INFLUXDB_INIT_PASSWORD=secret0000 \
  --env=DOCKER_INFLUXDB_INIT_ORG=example \
  --env=DOCKER_INFLUXDB_INIT_BUCKET=testdrive \
  --env=DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=token \
  --volume="$PWD/var/lib/influxdb2:/var/lib/influxdb2" \
  influxdb:2
:::

Start CrateDB.
:::{code} shell
docker run --rm -it --name=cratedb \
  --publish=4200:4200 \
  --volume="$PWD/var/lib/cratedb:/data" \
  crate:latest -Cdiscovery.type=single-node
:::

### Sample Data
Command shortcuts. 
:::{code} shell
alias influx="docker exec influxdb influx"
alias influx-write="influx write --bucket=testdrive --org=example --token=token --precision=s"
:::

Write a few samples worth of data to InfluxDB.
:::{code} shell
influx-write "demo,region=amazonas temperature=27.4,humidity=92.3,windspeed=4.5 1588363200"
influx-write "demo,region=amazonas temperature=28.2,humidity=88.7,windspeed=4.7 1588549600"
influx-write "demo,region=amazonas temperature=27.9,humidity=91.6,windspeed=3.2 1588736000"
influx-write "demo,region=amazonas temperature=29.1,humidity=88.1,windspeed=2.4 1588922400"
influx-write "demo,region=amazonas temperature=28.6,humidity=93.4,windspeed=2.9 1589108800"
:::

### Data Import

First, create these command aliases, for better UX.
:::{code} shell
alias crash="docker run --rm -it --link=cratedb ghcr.io/crate/cratedb-toolkit:latest crash"
alias ctk="docker run --rm -it --link=cratedb --link=influxdb ghcr.io/crate/cratedb-toolkit:latest ctk"
:::

Now, import data from InfluxDB bucket/measurement into CrateDB schema/table.
:::{code} shell
ctk load table \
  "influxdb2://example:token@influxdb:8086/testdrive/demo" \
  --cratedb-sqlalchemy-url="crate://crate@cratedb:4200/testdrive/demo"
:::

Verify that relevant data has been transferred to CrateDB.
:::{code} shell
crash --host=cratedb --command="SELECT * FROM testdrive.demo;"
:::

## Cloud to Cloud

The procedure for importing data from [InfluxDB Cloud] into [CrateDB Cloud] is
similar, with a few small adjustments.

First, helpful aliases again:
:::{code} shell
alias ctk="docker run --rm -it ghcr.io/crate/cratedb-toolkit:latest ctk"
alias crash="docker run --rm -it ghcr.io/crate/cratedb-toolkit:latest crash"
:::

You will need your credentials for both CrateDB and InfluxDB. 
These are, with examples:

:::{rubric} CrateDB Cloud
:::
- Host: ```purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net```
- Username: ```admin```
- Password: ```dZ..qB```

:::{rubric} InfluxDB Cloud
:::
- Host: ```eu-central-1-1.aws.cloud2.influxdata.com```
- Organization ID: ```9fafc869a91a3406```
- All-Access API token: ```T2..==```

For CrateDB, the credentials are displayed at time of cluster creation.
For InfluxDB, they can be found in the [cloud platform] itself.

Now, same as before, import data from InfluxDB bucket/measurement into 
CrateDB schema/table.
:::{code} shell
export CRATEPW='dZ..qB'
ctk load table \
  "influxdb2://9f..06:T2..==@eu-central-1-1.aws.cloud2.influxdata.com/testdrive/demo?ssl=true" \
  --cratedb-sqlalchemy-url="crate://admin:${CRATEPW}@purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net:4200/testdrive/demo?ssl=true"
:::

::: {note}
Note the **necessary** `ssl=true` query parameter at the end of both database connection URLs
when working on Cloud-to-Cloud transfers.
:::

Verify that relevant data has been transferred to CrateDB.
:::{code} shell
export CRATEPW='dZ..qB'
crash --hosts 'https://admin:${CRATEPW}@purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net:4200' --command 'SELECT * FROM testdrive.demo;'
:::

## More information

There are more ways to apply the I/O subsystem of CrateDB Toolkit as
pipeline elements in your daily data operations routines. Please visit the 
[CrateDB Toolkit InfluxDB I/O subsystem] documentation, to learn more about what's possible.

The InfluxDB I/O subsystem is based on the [influxio] package. See its
documentation for additional capabilities when working with InfluxDB.

:::{note}
**Important:** If you discover any issues with this adapter, please
[report them] back to us.
:::


[cloud platform]: https://docs.influxdata.com/influxdb/cloud/admin
[CrateDB]: https://github.com/crate/crate
[CrateDB Cloud]: https://console.cratedb.cloud/
[CrateDB Toolkit InfluxDB I/O subsystem]: https://cratedb-toolkit.readthedocs.io/io/influxdb/loader.html
[InfluxDB]: https://github.com/influxdata/influxdb
[InfluxDB Cloud]: https://cloud2.influxdata.com/
[influxio]: https://influxio.readthedocs.io/
[report them]: https://github.com/crate/cratedb-toolkit/issues
[What are series and bucket in InfluxDB]: https://stackoverflow.com/questions/58190272/what-are-series-and-bucket-in-influxdb/69951376#69951376
