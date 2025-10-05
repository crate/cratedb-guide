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

Docker is used for running all components. This approach works consistently
across Linux, macOS, and Windows. Alternatively, you can use Podman.

Create a shared network.
```shell
docker network create cratedb-demo
```

Start CrateDB.
```shell
docker run --rm --name=cratedb --network=cratedb-demo \
  --publish=4200:4200 \
  --volume="$PWD/var/lib/cratedb:/data" \
  docker.io/crate -Cdiscovery.type=single-node
```

Start InfluxDB.
```shell
docker run --rm --name=influxdb --network=cratedb-demo \
  --publish=8086:8086 \
  --env=DOCKER_INFLUXDB_INIT_MODE=setup \
  --env=DOCKER_INFLUXDB_INIT_USERNAME=admin \
  --env=DOCKER_INFLUXDB_INIT_PASSWORD=secret0000 \
  --env=DOCKER_INFLUXDB_INIT_ORG=example \
  --env=DOCKER_INFLUXDB_INIT_BUCKET=testdrive \
  --env=DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=token \
  docker.io/influxdb:2
```

Prepare shortcuts for the CrateDB shell, CrateDB Toolkit, and the InfluxDB client
programs.

::::{tab-set}

:::{tab-item} Linux and macOS
To make the settings persistent, add them to your shell profile (`~/.profile`).
```shell
alias crash="docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash"
alias ctk="docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk"
alias influx="docker exec influxdb influx"
alias influx-write="influx write --bucket=testdrive --org=example --token=token --precision=s"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash @args }
function ctk { docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk @args }
function influx { docker exec influxdb influx @args }
function influx-write { influx write --bucket=testdrive --org=example --token=token --precision=s @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash $*
doskey ctk=docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk $*
doskey influx=docker exec influxdb influx $*
doskey influx-write=influx write --bucket=testdrive --org=example --token=token --precision=s $*
```
:::

::::

## Usage

Write a few sample records to InfluxDB.
```shell
influx-write "demo,region=amazonas temperature=27.4,humidity=92.3,windspeed=4.5 1588363200"
influx-write "demo,region=amazonas temperature=28.2,humidity=88.7,windspeed=4.7 1588549600"
influx-write "demo,region=amazonas temperature=27.9,humidity=91.6,windspeed=3.2 1588736000"
influx-write "demo,region=amazonas temperature=29.1,humidity=88.1,windspeed=2.4 1588922400"
influx-write "demo,region=amazonas temperature=28.6,humidity=93.4,windspeed=2.9 1589108800"
```

Invoke the data transfer pipeline, importing data from
InfluxDB bucket/measurement into CrateDB schema/table.
```shell
ctk load table \
  "influxdb2://example:token@influxdb:8086/testdrive/demo" \
  --cluster-url="crate://crate@cratedb:4200/doc/testdrive"
```

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM doc.testdrive"
```


[CrateDB]: https://github.com/crate/crate
[CrateDB Toolkit InfluxDB I/O subsystem]: https://cratedb-toolkit.readthedocs.io/io/influxdb/loader.html
[InfluxDB]: https://github.com/influxdata/influxdb
