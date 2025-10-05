(mariadb-usage)=
(mysql-usage)=
# Load data from MySQL or MariaDB into CrateDB

The usage guide will walk you through starting [MariaDB] and CrateDB,
inserting a record into MariaDB, loading data into a CrateDB table,
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
docker run --name=cratedb --rm --network=cratedb-demo \
  --publish=4200:4200 --publish=5432:5432 --env=CRATE_HEAP_SIZE=2g \
  docker.io/crate -Cdiscovery.type=single-node
```

Start MariaDB.
```shell
docker run --name=mariadb --rm --network=cratedb-demo \
  --publish=3306:3306 --env "MARIADB_ROOT_PASSWORD=secret" \
  docker.io/mariadb
```

Prepare shortcuts for the CrateDB shell, CrateDB Toolkit, and the MariaDB client
programs.

::::{tab-set}

:::{tab-item} Linux and macOS
To make the settings persistent, add them to your shell profile (`~/.profile`).
```shell
alias crash="docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash"
alias ctk-ingest="docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk"
alias mariadb="docker run --rm -i --network=cratedb-demo docker.io/mariadb mariadb"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash @args }
function ctk-ingest { docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk @args }
function mariadb { docker run --rm -i --network=cratedb-demo docker.io/mariadb mariadb @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash $*
doskey ctk-ingest=docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit-ingest ctk $*
doskey mariadb=docker run --rm -i --network=cratedb-demo docker.io/mariadb mariadb $*
```
:::

::::

## Usage

Write a few sample records to MariaDB.

::::{tab-set}
:::{tab-item} Linux and macOS
```shell
mariadb --protocol=tcp --host=mariadb --user=root --password=secret <<SQL
CREATE DATABASE IF NOT EXISTS test;
USE test;
CREATE TABLE IF NOT EXISTS demo (id BIGINT, data JSON);
INSERT INTO demo (id, data) VALUES (1, '{"temperature": 42.84, "humidity": 83.1}');
INSERT INTO demo (id, data) VALUES (2, '{"temperature": 84.84, "humidity": 56.99}');
SQL
```
:::
:::{tab-item} Windows PowerShell
```powershell
$args = @(
  "--protocol=tcp",
  "--host=mariadb",
  "--user=root",
  "--password=secret"
)
$sql = @'
CREATE DATABASE IF NOT EXISTS test;
USE test;
CREATE TABLE IF NOT EXISTS demo (id BIGINT, data JSON);
INSERT INTO demo (id, data) VALUES (1, '{"temperature": 42.84, "humidity": 83.1}');
INSERT INTO demo (id, data) VALUES (2, '{"temperature": 84.84, "humidity": 56.99}');
'@
mariadb @args -e $sql
```
:::
::::

Invoke the data transfer pipeline.
```shell
ctk-ingest load table \
  "mysql://root:secret@mariadb:3306/?table=test.demo" \
  --cluster-url="crate://crate:crate@cratedb:4200/doc/mysql_demo"
```

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM doc.mysql_demo"
```


[MariaDB]: https://mariadb.com/
[MySQL]: https://www.mysql.com/
