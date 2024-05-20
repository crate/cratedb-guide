(integrate-influxdb)=
(import-influxdb)=
# Import data from InfluxDB

In this quick tutorial we use the InfluxDB I/O subsystem of CrateDB Toolkit
to import data from InfluxDB into CrateDB.

(integrate-influxdb-quickstart)=
## Quickstart

There are multiple ways to get and use this tool, to avoid 
unnecessary installations we will use Docker to run the services.
**Docker is needed for this:**

:::{code} console
docker run --rm --network=host ghcr.io/daq-tools/influxio \
    influxio copy \
    "http://example:token@localhost:8086/testdrive/demo" \
    "crate://crate@localhost:4200/testdrive/demo"
:::

(setup-influxdb)=
### InfluxDB setup

Following is an example configuration of InfluxDB and some sample data
should you need it. **Prerequisite for these to work is a running 
instance of InfluxDB.**

Initial InfluxDB configuration:

:::{code} console
docker run --rm -it --publish=8086:8086 --name influxdb\
    --env=DOCKER_INFLUXDB_INIT_MODE=setup \
    --env=DOCKER_INFLUXDB_INIT_USERNAME=user1 \
    --env=DOCKER_INFLUXDB_INIT_PASSWORD=secret1234 \
    --env=DOCKER_INFLUXDB_INIT_ORG=example \
    --env=DOCKER_INFLUXDB_INIT_BUCKET=testdrive \
    --env=DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=token \
    --volume="$PWD/var/lib/influxdb2:/var/lib/influxdb2" \
    influxdb:latest
:::

Write sample data to InfluxDB:

:::{code} console
docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=27.4,humidity=92.3,windspeed=4.5 1588363200"
docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=28.2,humidity=88.7,windspeed=4.7 1588549600"
docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=27.9,humidity=91.6,windspeed=3.2 1588736000"
docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=29.1,humidity=88.1,windspeed=2.4 1588922400"
docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=28.6,humidity=93.4,windspeed=2.9 1589108800"
:::

(export-data)=
### Export

Now you can export the data into CrateDB. **Prerequisite for these to work
is a running instance of CrateDB.**

First, create these aliases so the next part is a bit easier:

:::{code} console
alias crash="docker run --rm -it ghcr.io/crate-workbench/cratedb-toolkit:latest crash"
alias ctk="docker run --rm -it ghcr.io/crate-workbench/cratedb-toolkit:latest ctk"
:::

Now you can import data to your CrateDB instance:

:::{code} console
export CRATEDB_SQLALCHEMY_URL=crate://crate@localhost:4200/testdrive/demo
ctk load table influxdb2://example:token@localhost:8086/testdrive/demo
:::

And verify that data is indeed in your CrateDB cluster:

:::{code} console
crash --command "SELECT * FROM testdrive.demo;"
:::

## More information

There are many more ways to apply the I/O subsystem of CrateDB Toolkit as 
pipeline elements in your daily data operations routines. Please visit the 
[CrateDB Toolkit I/O Documentation], to learn more about what's possible.

The InfluxDB I/O subsystem is based on the [influxio] package. Please also
check its documentation to learn about more of its capabilities, supporting
you when working with InfluxDB.

[influxio]: https://influxio.readthedocs.io/
[CrateDB Toolkit I/O Documentation]: https://cratedb-toolkit.readthedocs.io/io/influxdb/loader.html
