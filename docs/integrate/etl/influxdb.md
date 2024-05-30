(integrate-influxdb)=
(integrate-influxdb-quickstart)=
(import-influxdb)=
# Import data from InfluxDB

In this quick tutorial we use the InfluxDB I/O subsystem of CrateDB Toolkit
to demonstrate importing data from InfluxDB into CrateDB.

## Synopsis
Transfer data from InfluxDB bucket/measurement into CrateDB schema/table.
:::{code} shell
ctk load table \
  "influxdb2://example:token@influxdb.example.org:8086/testdrive/demo" \
  --cratedb-sqlalchemy-url="crate://user:password@cratedb.example.org:4200/testdrive/demo"
:::

Query data in CrateDB.
:::{code} shell
export CRATEPW=password
crash --host=cratedb.example.org --username=user --command="SELECT * FROM testdrive.demo;"
:::

## Tutorial

The tutorial heavily uses Docker to provide services and to run jobs.
Alternatively, you can use the drop-in replacement Podman.
The walkthrough is a basic example setup using InfluxDB, including
a few samples worth of data.

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
alias crash="docker run --rm -it --link=cratedb ghcr.io/crate-workbench/cratedb-toolkit:latest crash"
alias ctk="docker run --rm -it --link=cratedb --link=influxdb ghcr.io/crate-workbench/cratedb-toolkit:latest ctk"
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

If you're interested in importing data from [InfluxDB Cloud] into
[CrateDB Cloud], the procedure is similar with small adjustments.

First, helpful aliases again:
:::{code} shell
alias ctk="docker run --rm -it ghcr.io/crate-workbench/cratedb-toolkit:latest ctk"
alias crash="docker run --rm -it ghcr.io/crate-workbench/cratedb-toolkit:latest crash"
:::

You will need your credentials for both CrateDB and InfluxDB. 
These are, with examples:

**CrateDB Cloud**
* Host: ```purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net```
* Username: ```admin```
* Password: ```dZ..qB```

**InfluxDB Cloud**
  * Host: ```eu-central-1-1.aws.cloud2.influxdata.com```
  * Organization ID: ```9fafc869a91a3406```
  * All-Access API token: ```T2..==```

For CrateDB, the credentials are displayed at time of cluster creation.
For InfluxDB, they can be found in the [cloud platform] itself.

Now, same as before, import data from InfluxDB bucket/measurement into 
CrateDB schema/table.
:::{code} shell
ctk load table \
  "influxdb2://9f..06:T2..==@eu-central-1-1.aws.cloud2.influxdata.com/testdrive/demo?ssl=true" \
  --cratedb-sqlalchemy-url="crate://admin:dZ..qB@purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net:4200/testdrive/demo?ssl=true"
:::

::: {note}
Note the **necessary** `ssl=true` query parameter at the end of both database connection URLs
when working on Cloud-to-Cloud transfers.
:::

Verify that relevant data has been transferred to CrateDB.
:::{code} shell
crash --hosts 'https://admin:dZ..qB@purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net:4200' --command 'SELECT * FROM testdrive.demo;'
:::

## More information

There are more ways to apply the I/O subsystem of CrateDB Toolkit as
pipeline elements in your daily data operations routines. Please visit the 
[CrateDB Toolkit I/O Documentation], to learn more about what's possible.

The InfluxDB I/O subsystem is based on the [influxio] package. Please also
check its documentation to learn about more of its capabilities, supporting
you when working with InfluxDB.

[cloud platform]: https://docs.influxdata.com/influxdb/cloud/admin
[CrateDB Cloud]: https://console.cratedb.cloud/
[CrateDB Toolkit I/O Documentation]: https://cratedb-toolkit.readthedocs.io/io/influxdb/loader.html
[InfluxDB Cloud]: https://cloud2.influxdata.com/
[influxio]: https://influxio.readthedocs.io/
