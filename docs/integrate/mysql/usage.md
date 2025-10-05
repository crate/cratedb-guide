(mariadb-usage)=
(mysql-usage)=
# Load data from MySQL or MariaDB into CrateDB

The usage guide will walk you through starting [MariaDB] and CrateDB,
inserting a record into MariaDB, loading data into a CrateDB table,
and validating that the data has been stored successfully.
The data transfer is supported by the
{ref}`CrateDB Toolkit Ingestr I/O <ctk:ingestr>` data pipeline elements.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

## Submit data

Write a few sample records to MariaDB.

::::{tab-set}
:::{tab-item} Linux, macOS, WSL
```shell
docker compose run --rm --no-TTY mariadb mariadb --protocol=tcp --host=mariadb --user=root --password=secret <<SQL
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
docker compose run --rm --no-TTY mariadb mariadb @args -e $sql
```
:::
::::

Invoke the data transfer pipeline.
```shell
docker compose run --rm --no-TTY ctk-ingest ctk load table \
  "mysql://root:secret@mariadb:3306/?table=test.demo" \
  --cluster-url="crate://crate:crate@cratedb:4200/doc/mysql_demo"
```

## Explore data

Inspect data stored in CrateDB.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.mysql_demo"
```
```psql
+----+-------------------------------------------+
| id | data                                      |
+----+-------------------------------------------+
|  2 | {"temperature": 84.84, "humidity": 56.99} |
|  1 | {"temperature": 42.84, "humidity": 83.1}  |
+----+-------------------------------------------+
SELECT 2 rows in set (0.016 sec)
```


[MariaDB]: https://mariadb.com/
[MySQL]: https://www.mysql.com/
