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
$ docker run --rm --network=my_network ghcr.io/daq-tools/influxio \
 influxio copy \
 "http://example:token@influxdb:8086/testdrive/demo" \
 "crate://crate@crate:4200/testdrive/demo"
:::

(docker-setup)=

### Docker network

First we need to create a user-defined bridge network in Docker, such
as _my_network_ in our case. This enables reliable communication between
containers using their names as hostnames:

:::{code} console
$ docker network create my_network
:::

(cratedb-setup)=

### CrateDB setup

If you don't have a CrateDB instance running yet, feel free to use this.
It quickly spins up a correctly configured instance of CrateDB with network
and hostname used in later commands.

:::{code} console
$ docker run -d --name crate --network my_network --hostname crate -p 4200:4200 crate/crate:latest
:::

(setup-influxdb)=

### InfluxDB setup

Following is an example configuration of InfluxDB and some sample data
should you need it. **Prerequisite for these to work is a running
instance of InfluxDB.**

Initial InfluxDB configuration:

:::{code} console
$ docker run -d --name influxdb --network my_network -p 8086:8086 \
 --env=DOCKER_INFLUXDB_INIT_MODE=setup \
 --env=DOCKER_INFLUXDB_INIT_USERNAME=user1 \
 --env=DOCKER_INFLUXDB_INIT_PASSWORD=secret1234 \
 --env=DOCKER_INFLUXDB_INIT_ORG=example \
 --env=DOCKER_INFLUXDB_INIT_BUCKET=testdrive \
 --env=DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=token \
 influxdb:latest
:::

Write sample data to InfluxDB:

:::{code} console
$ docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=27.4,humidity=92.3,windspeed=4.5 1588363200"
$ docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=28.2,humidity=88.7,windspeed=4.7 1588549600"
$ docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=27.9,humidity=91.6,windspeed=3.2 1588736000"
$ docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=29.1,humidity=88.1,windspeed=2.4 1588922400"
$ docker exec influxdb influx write --bucket=testdrive --org=example --precision=s --token=token "demo,region=amazonas temperature=28.6,humidity=93.4,windspeed=2.9 1589108800"
:::

(export-data)=

### Export

Now you can export the data into CrateDB. **Prerequisite for these to work
is a running instance of CrateDB.**

First, create these aliases so the next part is a bit easier:

:::{code} console
$ export CRATEDB_SQLALCHEMY_URL=crate://crate@crate:4200/testdrive/demo
$ alias crash="docker run --rm -it --network my_network ghcr.io/crate-workbench/cratedb-toolkit:latest crash --hosts crate:4200"
$ alias ctk="docker run --rm -it --network my_network --env='CRATEDB_SQLALCHEMY_URL=${CRATEDB_SQLALCHEMY_URL}' ghcr.io/crate-workbench/cratedb-toolkit:latest ctk"
:::

Now you can import data to your CrateDB instance:

:::{code} console
$ ctk load table \
 influxdb2://example:token@influxdb:8086/testdrive/demo \
 --cratedb-sqlalchemy-url "crate://crate@crate:4200/testdrive/demo"
:::

And verify that data is indeed in your CrateDB cluster:

:::{code} console
$ crash --command "SELECT * FROM testdrive.demo;"
:::

If everything worked correctly, *crash* should return something like this:

:::{code} console
$ crash --command "SELECT * FROM testdrive.demo;"

CONNECT OK
+---------------+-------------+----------+----------+-------------+-----------+
|          time | measurement | region   | humidity | temperature | windspeed |
+---------------+-------------+----------+----------+-------------+-----------+
| 1588549600000 | demo        | amazonas |     88.7 |        28.2 |       4.7 |
| 1589108800000 | demo        | amazonas |     93.4 |        28.6 |       2.9 |
| 1588922400000 | demo        | amazonas |     88.1 |        29.1 |       2.4 |
| 1588363200000 | demo        | amazonas |     92.3 |        27.4 |       4.5 |
| 1588736000000 | demo        | amazonas |     91.6 |        27.9 |       3.2 |
+---------------+-------------+----------+----------+-------------+-----------+
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
