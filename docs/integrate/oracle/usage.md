(oracle-usage)=
# Load data from Oracle into CrateDB

The usage guide will walk you through starting the [Oracle Database] and CrateDB,
inserting a record into Oracle, loading data into a CrateDB table,
and validating that the data has been stored successfully.
The data transfer is supported by the
{ref}`CrateDB Toolkit Ingestr I/O <ctk:ingestr>` data pipeline elements.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`
- {download}`init.sql`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

## Submit data

Write a few sample records to Oracle.
```shell
docker compose run --rm --no-TTY sqlplus sys/secret@oracledb/freepdb1 as sysdba @/demo/init.sql
```

Invoke the data transfer pipeline.
```shell
docker compose run --rm --no-TTY ctk-ingest ctk load table \
  "oracle://sys:secret@oracledb:1521/?service_name=freepdb1&table=sys.demo&mode=sysdba" \
  --cluster-url="crate://crate:crate@cratedb:4200/doc/oracle_demo"
```

## Explore data

Inspect data stored in CrateDB.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.oracle_demo"
```
```psql
+----+-------------+----------+
| id | temperature | humidity |
+----+-------------+----------+
|  1 |       42.84 |    83.1  |
|  2 |       84.84 |    56.99 |
+----+-------------+----------+
SELECT 2 rows in set (0.061 sec)
```


[Oracle Database]: https://www.oracle.com/database/
