(postgresql-usage)=
# Load data from PostgreSQL into CrateDB

The usage guide will walk you through starting [PostgreSQL] and CrateDB,
inserting a record into PostgreSQL, loading data into a CrateDB table,
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

:::{note}
CrateDB is configured to listen on port `5432`,
while PostgreSQL is configured to listen on port `6432`.
:::
:::{note}
PostgreSQL is configured using `POSTGRES_HOST_AUTH_METHOD=trust`.
This allows anonymous access for demonstration purposes only.
Do not expose it to untrusted networks. For production, configure
authentication/TLS.
:::

## Submit data

Write a few sample records to PostgreSQL.
```shell
docker compose run --rm --no-TTY psql psql "postgresql://postgres:postgres@postgresql:5432/" <<SQL
CREATE DATABASE test;
\connect test;
CREATE TABLE IF NOT EXISTS demo (id BIGINT, data JSONB);
INSERT INTO demo (id, data) VALUES (1, '{"temperature": 42.84, "humidity": 83.1}');
INSERT INTO demo (id, data) VALUES (2, '{"temperature": 84.84, "humidity": 56.99}');
SQL
```

Invoke the data transfer pipeline.
```shell
docker compose run --rm --no-TTY ctk-ingest ctk load table "postgresql://postgres:postgres@postgresql:5432/test?table=public.demo" --cluster-url="crate://crate:crate@cratedb:4200/doc/postgresql_demo"
```

## Explore data

Inspect data stored in CrateDB.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.postgresql_demo"
```
```psql
+----+-------------------------------------------+
| id | data                                      |
+----+-------------------------------------------+
|  1 | {"humidity": 83.1, "temperature": 42.84}  |
|  2 | {"humidity": 56.99, "temperature": 84.84} |
+----+-------------------------------------------+
SELECT 2 rows in set (0.017 sec)
```


[PostgreSQL]: https://www.postgresql.org/
