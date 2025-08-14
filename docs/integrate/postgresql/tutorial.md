(postgresql-tutorial)=
# Load data from PostgreSQL into CrateDB

The tutorial will walk you through starting [PostgreSQL] and CrateDB,
inserting a record into PostgreSQL, loading data into a CrateDB table,
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
  --publish=4200:4200 --publish=5432:5432 --env=CRATE_HEAP_SIZE=2g \
  docker.io/crate -Cdiscovery.type=single-node
```

Start PostgreSQL.
```shell
docker run --rm --name=postgresql --network=cratedb-demo \
  --publish=6432:5432 --env "POSTGRES_HOST_AUTH_METHOD=trust" \
  docker.io/postgres postgres -c log_statement=all
```
:::{note}
Because CrateDB is configured to listen on port `5432` with its PostgreSQL
interface, let's use a different port for PostgreSQL itself.
:::

Prepare shortcuts for the CrateDB shell, CrateDB Toolkit, and the PostgreSQL client
programs.

::::{tab-set}

:::{tab-item} Linux and macOS
To make the settings persistent, add them to your shell profile (`~/.profile`).
```shell
alias crash="docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash"
alias ctk-ingest="docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk"
alias psql="docker run --rm -i --network=cratedb-demo docker.io/postgres psql"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash @args }
function ctk-ingest { docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk @args }
function psql { docker run --rm -i --network=cratedb-demo docker.io/postgres psql @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash $*
doskey ctk-ingest=docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk $*
doskey psql=docker run --rm -i --network=cratedb-demo docker.io/postgres psql $*
```
:::

::::

## Usage

Write a few sample records to PostgreSQL.
```shell
psql "postgresql://postgres:postgres@postgresql:5432/" <<SQL
CREATE DATABASE test;
\connect test;
CREATE TABLE IF NOT EXISTS demo (id BIGINT, data JSONB);
INSERT INTO demo (id, data) VALUES (1, '{"temperature": 42.84, "humidity": 83.1}');
INSERT INTO demo (id, data) VALUES (2, '{"temperature": 84.84, "humidity": 56.99}');
SQL
```

Invoke the data transfer pipeline.
```shell
ctk-ingest load table \
  "postgresql://postgres:postgres@postgresql:5432/test?table=public.demo" \
  --cluster-url="crate://crate:crate@cratedb:4200/doc/postgresql_demo"
```

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM doc.postgresql_demo"
```


[PostgreSQL]: https://www.postgresql.org/
