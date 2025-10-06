(collectd-usage-base)=
# Load data into CrateDB using collectd

This usage guide shows how to configure and start [collectd] and CrateDB
so that collectd sends system metrics and CrateDB stores them.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`
- {download}`Dockerfile`
- {download}`collectd-cratedb.conf`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

To send the collected data to CrateDB, collectd is configured to load its
[`postgresql` plugin].

::::{dropdown} collectd configuration `collectd-cratedb.conf`
:::{literalinclude} collectd-cratedb.conf
:::
::::

### Provision database

Create a database table that stores collected metrics.
```shell
docker compose run --rm --no-TTY postgresql psql "postgresql://crate:crate@cratedb:5432/" <<SQL
CREATE TABLE doc.collectd_data (
   p_time timestamp with time zone,
   p_host TEXT,
   p_plugin TEXT,
   p_plugin_instance TEXT,
   p_type TEXT,
   p_type_instance TEXT,
   p_value_names TEXT,
   p_type_names TEXT,
   p_values TEXT,
   month GENERATED ALWAYS AS date_trunc('month',p_time)
) PARTITIONED BY (month);
SQL
```

## Explore data

After the first scraping interval, metrics will show up in the
designated table in CrateDB, ready to be inspected.
```shell
docker compose run --rm --no-TTY postgresql psql "postgresql://crate:crate@cratedb:5432/" -c "SELECT * FROM doc.collectd_data ORDER BY p_time LIMIT 5;"
```
```psql
           p_time           |    p_host    | p_plugin  | p_plugin_instance |   p_type   | p_type_instance | p_value_names |   p_type_names    |   p_values   |           month
----------------------------+--------------+-----------+-------------------+------------+-----------------+---------------+-------------------+--------------+----------------------------
 2025-09-20 13:57:12.822+00 | 9cde293016c2 | interface | gre0              | if_errors  |                 | {'rx','tx'}   | {'gauge','gauge'} | {nan,nan}    | 2025-09-01 00:00:00.000+00
 2025-09-20 13:57:12.822+00 | 9cde293016c2 | memory    |                   | memory     | cached          | {'value'}     | {'gauge'}         | {4600500224} | 2025-09-01 00:00:00.000+00
 2025-09-20 13:57:12.822+00 | 9cde293016c2 | interface | gre0              | if_dropped |                 | {'rx','tx'}   | {'gauge','gauge'} | {nan,nan}    | 2025-09-01 00:00:00.000+00
 2025-09-20 13:57:12.822+00 | 9cde293016c2 | interface | erspan0           | if_octets  |                 | {'rx','tx'}   | {'gauge','gauge'} | {nan,nan}    | 2025-09-01 00:00:00.000+00
 2025-09-20 13:57:12.822+00 | 9cde293016c2 | interface | ip_vti0           | if_dropped |                 | {'rx','tx'}   | {'gauge','gauge'} | {nan,nan}    | 2025-09-01 00:00:00.000+00
(5 rows)
```


[collectd]: https://collectd.org/
[`postgresql` plugin]: https://collectd.org/documentation/manpages/collectd.conf.html#plugin-postgresql
