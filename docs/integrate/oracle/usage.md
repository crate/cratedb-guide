(oracle-usage)=
# Load data from Oracle into CrateDB

The usage guide will walk you through starting the [Oracle Database] and CrateDB,
inserting a record into Oracle, loading data into a CrateDB table,
and validating that the data has been stored successfully.
The data transfer is supported by the
{ref}`CrateDB Toolkit Ingestr I/O <ctk:ingestr>` data pipeline elements.

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
  --publish=4200:4200 --publish=5432:5432 \
  docker.io/crate -Cdiscovery.type=single-node
```

Start Oracle DBMS.
```shell
docker run --rm --name=oracle --network=cratedb-demo \
  --publish=1521:1521 \
  --env=ORACLE_PASSWORD=secret \
  docker.io/gvenzl/oracle-free:23-slim
```

Prepare shortcuts for the CrateDB shell, CrateDB Toolkit, and the Oracle client
programs.

::::{tab-set}

:::{tab-item} Linux and macOS
To make the settings persistent, add them to your shell profile (`~/.profile`).
```shell
alias crash="docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest crash"
alias ctk-ingest="docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk"
alias sqlplus="docker run --rm -it --network=cratedb-demo --volume=$(PWD):/demo --env=ORACLE_PASSWORD=secret --entrypoint=sqlplus docker.io/gvenzl/oracle-free:23-slim"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest crash @args }
function ctk-ingest { docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk @args }
function sqlplus { docker run --rm -it --network=cratedb-demo --volume=${PWD}:/demo --env=ORACLE_PASSWORD=secret --entrypoint=sqlplus docker.io/gvenzl/oracle-free:23-slim @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest crash $*
doskey ctk-ingest=docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk $*
doskey sqlplus=docker run --rm -it --network=cratedb-demo --volume=%cd%:/demo --env=ORACLE_PASSWORD=secret --entrypoint=sqlplus docker.io/gvenzl/oracle-free:23-slim $*
```
:::

::::

## Usage

Write a few sample records to Oracle.
```shell
cat >init.sql <<SQL
CREATE TABLE IF NOT EXISTS demo (id NUMBER, temperature FLOAT, humidity FLOAT);
INSERT INTO demo (id, temperature, humidity) VALUES (1, 42.84, 83.1);
INSERT INTO demo (id, temperature, humidity) VALUES (2, 84.84, 56.99);
SELECT * FROM demo;
exit;
SQL
```
```shell
sqlplus sys/secret@oracle/freepdb1 as sysdba @/demo/init.sql
```

Invoke the data transfer pipeline.
```shell
ctk-ingest load table \
  "oracle://sys:secret@oracle:1521/?service_name=freepdb1&table=sys.demo&mode=sysdba" \
  --cluster-url="crate://crate:crate@cratedb:4200/doc/oracle_demo"
```

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM doc.oracle_demo"
```


[Oracle Database]: https://www.oracle.com/database/
