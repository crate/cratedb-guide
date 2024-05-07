(integrate-influxdb)=
(import-influxdb)=
# Import data from InfluxDB

In this quick tutorial we use the InfluxDB I/O subsystem of CrateDB Toolkit
to import data from InfluxDB into CrateDB.

(setup-influxio)=
## Setup

`influxio` can be installed with pip:

:::{code} console
pip install influxio
:::

You will also need the [cratedb-toolkit](https://github.com/crate-workbench/cratedb-toolkit/tree/main/cratedb_toolkit/io#installation)
to load the data into your CrateDB instance. It can be installed with:

:::{code} console
pip install --upgrade 'cratedb-toolkit[all]'
:::

(setup-influxdb)=
### InfluxDB setup

The following InfluxDB setup will be used in this tutorial:

:::{code} console
influx setup \
  --username user1 \
  --password 49jk8FQB$]1 \
  --token token123 \
  --org example \
  --bucket testdrive \
  --force
:::

With the following sample data loaded in InfluxDB:

:::{code} console
influx write --bucket=testdrive --org=example --precision=s "demo,region=amazonas temperature=27.4,humidity=92.3,windspeed=4.5 1588363200"
influx write --bucket=testdrive --org=example --precision=s "demo,region=amazonas temperature=28.2,humidity=88.7,windspeed=4.7 1588549600"
influx write --bucket=testdrive --org=example --precision=s "demo,region=amazonas temperature=27.9,humidity=91.6,windspeed=3.2 1588736000"
influx write --bucket=testdrive --org=example --precision=s "demo,region=amazonas temperature=29.1,humidity=88.1,windspeed=2.4 1588922400"
influx write --bucket=testdrive --org=example --precision=s "demo,region=amazonas temperature=28.6,humidity=93.4,windspeed=2.9 1589108800"
:::

(export-data)=
### Export

Now you can export the data into CrateDB:

:::{code} console
export CRATEDB_SQLALCHEMY_URL=crate://crate@localhost:4200/testdrive/demo
ctk load table influxdb2://example:token123@localhost:8086/testdrive/demo
:::

And verify that data is indeed in your CrateDB cluster:

:::{code} console
crash --command "SELECT * FROM testdrive.demo;"
:::

(cmd-use)=
## Command line use

Below are various examples of usage.

(cmd-help)=
### Help

:::{code} console
influxio --help
influxio info
influxio copy --help
:::

(cmd-import)=
### Import

:::{code} console
    # From test data to API.
    # Choose one of dummy, mixed, dateindex, wide.
    influxio copy \
        "testdata://dateindex/" \
        "http://example:token@localhost:8086/testdrive/demo"

    # With selected amount of rows.
    influxio copy \
        "testdata://dateindex/?rows=42" \
        "http://example:token@localhost:8086/testdrive/demo"

    # With selected amount of rows and columns (only supported by certain test data sources).
    influxio copy \
        "testdata://wide/?rows=42&columns=42" \
        "http://example:token@localhost:8086/testdrive/demo"

    # From line protocol file to InfluxDB API.
    influxio copy \
        "file://tests/testdata/basic.lp" \
        "http://example:token@localhost:8086/testdrive/demo"

    # From line protocol file to InfluxDB API.
    influxio copy \
        "https://github.com/influxdata/influxdb2-sample-data/raw/master/air-sensor-data/air-sensor-data.lp" \
        "http://example:token@localhost:8086/testdrive/demo"

    # From line protocol file to any database supported by SQLAlchemy.
    influxio copy \
        "file://export.lp" \
        "sqlite://export.sqlite?table=export"
:::

(cmd-export-from-api)=
### Export from api

:::{code} console
    # From API to database file.
    influxio copy \
        "http://example:token@localhost:8086/testdrive/demo" \
        "sqlite:///export.sqlite?table=demo"

    # From API to database server.
    influxio copy \
        "http://example:token@localhost:8086/testdrive/demo" \
        "crate://crate@localhost:4200/testdrive?table=demo"

    # From API to line protocol file.
    influxio copy \
        "http://example:token@localhost:8086/testdrive/demo" \
        "file://export.lp"

    # From API to line protocol on stdout.
    influxio copy \
        "http://example:token@localhost:8086/testdrive/demo" \
        "file://-?format=lp"
:::

(cmd-export-from-data-dir)=
### Export from data directory

:::{code} console
    # From InfluxDB data directory to line protocol file.
    influxio copy \
        "file:///path/to/influxdb/engine?bucket-id=372d1908eab801a6&measurement=demo" \
        "file://export.lp"

    # From InfluxDB data directory to line protocol file, compressed with gzip.
    influxio copy \
        "file:///path/to/influxdb/engine?bucket-id=372d1908eab801a6&measurement=demo" \
        "file://export.lp.gz"

    # From InfluxDB data directory to line protocol on stdout.
    influxio copy \
        "file:///path/to/influxdb/engine?bucket-id=372d1908eab801a6&measurement=demo" \
        ""file://-?format=lp"
:::

(cmd-oci)=
### OCI 

OCI images are available on the GitHub Container Registry (GHCR).
In order to run them on Podman or Docker, invoke:

:::{code} console
docker run --rm --network=host ghcr.io/daq-tools/influxio \
    influxio copy \
    "http://example:token@localhost:8086/testdrive/demo" \
    "stdout://export.lp"
:::

If you want to work with files on your filesystem, you will need to either
mount the working directory into the container using the --volume option,
or use the --interactive option to consume STDIN, like:

:::{code} console
docker run --rm --volume=$(pwd):/data ghcr.io/daq-tools/influxio \
    influxio copy "file:///data/export.lp" "sqlite:///data/export.sqlite?table=export"

cat export.lp | \
docker run --rm --interactive --network=host ghcr.io/daq-tools/influxio \
    influxio copy "stdin://?format=lp" "crate://crate@localhost:4200/testdrive/export"
:::
