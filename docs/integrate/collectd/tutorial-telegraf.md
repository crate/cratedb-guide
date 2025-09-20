(collectd-tutorial-telegraf)=
# Load data into CrateDB using collectd and Telegraf

This tutorial walks you through configuring and starting the [collectd]
and [Telegraf] agents and daemons, and CrateDB, to submit and store
system metrics into CrateDB.

## Prerequisites

Docker is used for running all components. This approach works consistently
across Linux, macOS, and Windows. Alternatively, you can use Podman.

### CLI

Prepare shortcut for the psql command.

::::{tab-set}
:sync-group: os

:::{tab-item} Linux and macOS
:sync: unix
To make the settings persistent, add them to your shell profile (`~/.profile`).
```shell
alias psql="docker run --rm -i --network=cratedb-demo docker.io/postgres psql"
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function psql { docker run --rm -i --network=cratedb-demo docker.io/postgres psql @args }
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
doskey psql=docker run --rm -i --network=cratedb-demo docker.io/postgres psql $*
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

### collectd

collectd is not available per OCI image, so either install standalone,
or use these instructions for building an OCI to invoke on Docker or Podman.
Store this file under the name `Dockername`, then invoke the command
displayed below.

:::{literalinclude} Dockerfile
:::
```shell
docker build -t local/collectd -f Dockerfile .
```

## Configure

### Telegraf

Configure Telegraf to receive metrics from collectd agents and to store them
in CrateDB, by using the configuration blueprint outlined below, possibly
adjusting it to match your environment. Store this file under the name
`telegraf.conf`.

:::{literalinclude} telegraf.conf
:::

### collectd

To send the collected data to Telegraf, configure collectd by loading its
[`network` plugin] and supplying settings. Store this file under
the name `collectd-telegraf.conf`.

:::{literalinclude} collectd-telegraf.conf
:::


## Start services

### Telegraf

Start Telegraf.
::::{tab-set}
:sync-group: os

:::{tab-item} Linux and macOS
:sync: unix
```shell
docker run --name=telegraf --rm -it --network=cratedb-demo \
  --volume "$(pwd)"/telegraf.conf:/etc/telegraf/telegraf.conf \
  docker.io/telegraf
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
```powershell
docker run --name=telegraf --rm -it --network=cratedb-demo `
  --volume "${PWD}\telegraf.conf:/etc/telegraf/telegraf.conf" `
  docker.io/telegraf
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
docker run --name=telegraf --rm -it --network=cratedb-demo ^
  --volume "%cd%\telegraf.conf:/etc/telegraf/telegraf.conf" ^
  docker.io/telegraf
```
:::
::::

### collectd

Start collectd.
::::{tab-set}
:sync-group: os

:::{tab-item} Linux and macOS
:sync: unix
```shell
docker run --name=collectd --rm -it --network=cratedb-demo \
  --volume ${PWD}/collectd-telegraf.conf:/etc/collectd/collectd.conf.d/collectd-telegraf.conf \
  local/collectd
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
```powershell
docker run --name=collectd --rm -it --network=cratedb-demo `
  --volume "${PWD}\collectd-telegraf.conf:/etc/collectd/collectd.conf.d/collectd-telegraf.conf" `
  local/collectd
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
docker run --name=collectd --rm -it --network=cratedb-demo ^
  --volume "%cd%\collectd-telegraf.conf:/etc/collectd/collectd.conf.d/collectd-telegraf.conf" ^
  local/collectd
```
:::
::::

## Explore data

After starting the daemon, the first metrics will appear in the designated table in
CrateDB, ready to be inspected.
```shell
psql "postgresql://crate:crate@cratedb:5432/" -c "SELECT * FROM doc.metrics LIMIT 5;"
```
```psql
       hash_id        |         timestamp          | name |                 tags                 |                                                                                                                  fields                                                                                                                   |            day
----------------------+----------------------------+------+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------
 -6569628117176094941 | 2025-09-20 14:32:40.000+00 | cpu  | {"host":"2dfa19dd92c5","cpu":"cpu2"} | {"usage_nice":0,"usage_system":0.10121457489876418,"usage_irq":0,"usage_guest":0,"usage_user":0.2024291497975643,"usage_guest_nice":0,"usage_idle":99.59514170040524,"usage_steal":0,"usage_iowait":0,"usage_softirq":0.1012145748987844} | 2025-09-20 00:00:00.000+00
 -7809648236107165241 | 2025-09-20 14:32:50.000+00 | cpu  | {"host":"2dfa19dd92c5","cpu":"cpu1"} | {"usage_nice":0,"usage_system":0.2026342451874346,"usage_irq":0,"usage_guest":0,"usage_user":0.4052684903748692,"usage_guest_nice":0,"usage_idle":99.39209726444284,"usage_steal":0,"usage_iowait":0,"usage_softirq":0.0}                 | 2025-09-20 00:00:00.000+00
 -4885756654980088201 | 2025-09-20 14:32:50.000+00 | cpu  | {"host":"2dfa19dd92c5","cpu":"cpu4"} | {"usage_nice":0,"usage_system":0.3036437246963644,"usage_irq":0,"usage_guest":0,"usage_user":0.9109311740890573,"usage_guest_nice":0,"usage_idle":98.7854251012157,"usage_steal":0,"usage_iowait":0,"usage_softirq":0.0}                  | 2025-09-20 00:00:00.000+00
 -7517319202875331428 | 2025-09-20 14:32:50.000+00 | cpu  | {"host":"2dfa19dd92c5","cpu":"cpu5"} | {"usage_nice":0,"usage_system":0.3030303030302978,"usage_irq":0,"usage_guest":0,"usage_user":0.40404040404040903,"usage_guest_nice":0,"usage_idle":99.09090909090767,"usage_steal":0,"usage_iowait":0,"usage_softirq":0.0}                | 2025-09-20 00:00:00.000+00
  -743702115999591805 | 2025-09-20 14:32:50.000+00 | cpu  | {"host":"2dfa19dd92c5","cpu":"cpu7"} | {"usage_nice":0,"usage_system":0.20181634712409718,"usage_irq":0,"usage_guest":0,"usage_user":0.30272452068616373,"usage_guest_nice":0,"usage_idle":99.39455095862365,"usage_steal":0,"usage_iowait":0,"usage_softirq":0.0}               | 2025-09-20 00:00:00.000+00
(5 rows)
```


[collectd]: https://collectd.org/
[`network` plugin]: https://collectd.org/documentation/manpages/collectd.conf.html#plugin-network
[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
