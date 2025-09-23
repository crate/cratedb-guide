(collectd-usage-base)=
# Load data into CrateDB using collectd

This usage guide shows how to configure and start [collectd] and CrateDB
so that collectd sends system metrics and CrateDB stores them.

## Prerequisites

Docker runs all components consistently across Linux, macOS, and Windows.
If you use Podman, substitute podman for docker in the commands.

### Commands

Prepare shortcut for the psql command.

::::{tab-set}
:sync-group: os

:::{tab-item} Linux and macOS
:sync: unix
To make the settings persistent, add them to your shell profile (`~/.profile`).
```shell
alias psql="docker run --rm -i --network=cratedb-demo docker.io/postgres:16 psql"
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function psql { docker run --rm -i --network=cratedb-demo docker.io/postgres:16 psql @args }
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
doskey psql=docker run --rm -i --network=cratedb-demo docker.io/postgres:16 psql $*
```
:::

::::

### CrateDB

Create a shared network.
```shell
docker network create cratedb-demo
```

Start CrateDB.
```shell
docker run --name=cratedb --rm -it --network=cratedb-demo \
  --publish=4200:4200 --publish=5432:5432 \
  --env=CRATE_HEAP_SIZE=2g docker.io/crate -Cdiscovery.type=single-node
```

## Configure

### Provision database

Create a database table that stores collected metrics.
```shell
psql "postgresql://crate:crate@cratedb:5432/" <<SQL
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

### Build collectd

collectd is not available as an OCI image, so either install it standalone,
or use these instructions to build an OCI image to run on Docker or Podman.
Store this file under the name `Dockerfile`, then invoke the command
displayed below.

:::{literalinclude} Dockerfile
:::
```shell
docker build -t local/collectd -f Dockerfile .
```

### Configure collectd

To send the collected data to CrateDB, configure collectd by loading its
[`postgresql` plugin] and supplying settings. Store this file under
the name `collectd-cratedb.conf`.

:::{literalinclude} collectd-cratedb.conf
:::

## Start collectd

::::{tab-set}
:sync-group: os

:::{tab-item} Linux and macOS
:sync: unix
```shell
docker run --name=collectd --rm -it --network=cratedb-demo \
  --volume ${PWD}/collectd-cratedb.conf:/etc/collectd/collectd.conf.d/collectd-cratedb.conf \
  local/collectd
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
```powershell
docker run --name=collectd --rm -it --network=cratedb-demo `
  --volume "${PWD}\collectd-cratedb.conf:/etc/collectd/collectd.conf.d/collectd-cratedb.conf" `
  local/collectd
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
docker run --name=collectd --rm -it --network=cratedb-demo ^
  --volume "%cd%\collectd-cratedb.conf:/etc/collectd/collectd.conf.d/collectd-cratedb.conf" ^
  local/collectd
```
:::
::::

## Explore data

After the first scraping interval, metrics will show up in the
designated table in CrateDB, ready to be inspected.
```shell
psql "postgresql://crate:crate@cratedb:5432/" -c "SELECT * FROM doc.collectd_data ORDER BY p_time LIMIT 5;"
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
