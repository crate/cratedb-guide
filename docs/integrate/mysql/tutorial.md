(mariadb-tutorial)=
(mysql-tutorial)=
# Load data from MySQL or MariaDB into CrateDB

The tutorial will walk you through starting [MariaDB] and CrateDB,
inserting a record into MySQL, loading data into a CrateDB table,
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
  --publish=4200:4200 --publish=5432:5432 \
  --env=CRATE_HEAP_SIZE=2g docker.io/crate -Cdiscovery.type=single-node
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
alias ctk="docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk"
alias mariadb="docker run --rm -i --network=cratedb-demo docker.io/mariadb mariadb"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash @args }
function ctk { docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk @args }
function mariadb { docker run --rm -i --network=cratedb-demo docker.io/mariadb mariadb @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash $*
doskey ctk=docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk $*
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
CREATE DATABASE demo;
USE demo;
CREATE TABLE IF NOT EXISTS testdrive (id BIGINT, data JSON);
INSERT INTO testdrive (id, data) VALUES (1, '{"temperature": 42.84, "humidity": 83.1}');
INSERT INTO testdrive (id, data) VALUES (2, '{"temperature": 84.84, "humidity": 56.99}');
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
CREATE DATABASE demo;
USE demo;
CREATE TABLE IF NOT EXISTS testdrive (id BIGINT, data JSON);
INSERT INTO testdrive (id, data) VALUES (1, '{"temperature": 42.84, "humidity": 83.1}');
INSERT INTO testdrive (id, data) VALUES (2, '{"temperature": 84.84, "humidity": 56.99}');
'@
mariadb @args -e $sql
```
:::
::::

Write a few sample records to MariaDB.
```shell
mariadb --protocol=tcp --host=mariadb --user=root --password=secret <<SQL
CREATE DATABASE demo;
USE demo;
CREATE TABLE IF NOT EXISTS testdrive (id BIGINT, data JSON);
INSERT INTO testdrive (id, data) VALUES (1, '{"temperature": 42.84, "humidity": 83.1}');
INSERT INTO testdrive (id, data) VALUES (2, '{"temperature": 84.84, "humidity": 56.99}');
SQL
```

Invoke the data transfer pipeline.
```shell
ctk load table \
  "mysql://root:secret@mariadb:3306/demo?table=testdrive" \
  --cluster-url="crate://crate:crate@cratedb:4200/doc/testdrive"
```

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM doc.testdrive"
```


[MariaDB]: https://mariadb.com/
[MySQL]: https://www.mysql.com/
