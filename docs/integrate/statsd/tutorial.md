(statsd-tutorial)=
# Load data into CrateDB using StatsD and Telegraf

This tutorial walks you through configuring [Telegraf] to receive [StatsD]
metrics and store them into CrateDB.

## Prerequisites

Docker is used for running all components. This approach works consistently
across Linux, macOS, and Windows. Alternatively, you can use Podman.

### CLI

Prepare shortcut for the psql command.

::::{tab-set}
:sync-group: os

:::{tab-item} Linux and macOS
:sync: unix
Add these settings to your shell profile (`~/.profile`) to make them persistent.
```shell
alias nc="docker run --rm -i --network=cratedb-demo docker.io/toolbelt/netcat:2025-08-23"
alias psql="docker run --rm -i --network=cratedb-demo docker.io/postgres:16 psql"
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
Add these settings to your PowerShell profile (`$PROFILE`) to make them persistent.
```powershell
function nc { docker run --rm -i --network=cratedb-demo docker.io/toolbelt/netcat:2025-08-23 @args }
function psql { docker run --rm -i --network=cratedb-demo docker.io/postgres:16 psql @args }
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
doskey nc=docker run --rm -i --network=cratedb-demo docker.io/toolbelt/netcat:2025-08-23 $*
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


## Configure Telegraf

Use the configuration blueprint below to configure Telegraf to receive StatsD
metrics and store them in CrateDB. Adjust the configuration to match your
environment and save this file as `telegraf.conf`.

:::{literalinclude} telegraf.conf
:::


## Start Telegraf

::::{tab-set}
:sync-group: os

:::{tab-item} Linux and macOS
:sync: unix
```shell
docker run --name=telegraf --rm -it --network=cratedb-demo \
  --volume "$(pwd)"/telegraf.conf:/etc/telegraf/telegraf.conf \
  --publish 8125:8125/udp \
  docker.io/telegraf
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
```powershell
docker run --name=telegraf --rm -it --network=cratedb-demo `
  --volume "${PWD}\telegraf.conf:/etc/telegraf/telegraf.conf" `
  --publish 8125:8125/udp `
  docker.io/telegraf
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
docker run --name=telegraf --rm -it --network=cratedb-demo ^
  --volume "%cd%\telegraf.conf:/etc/telegraf/telegraf.conf" ^
  --publish 8125:8125/udp ^
  docker.io/telegraf
```
:::
::::

## Submit data

### netcat
Use [netcat] for submitting data.
```shell
echo "temperature:42|g\nhumidity:84|g" | nc -C -w 1 -u telegraf 8125
```

### Python
Use the [statsd package] to submit data from your Python application.
```shell
uv pip install statsd
```
```python
from statsd import StatsClient

statsd = StatsClient("localhost", 8125)
statsd.gauge("temperature", 42)
statsd.gauge("humidity", 84)
statsd.close()
```

### Any

Use any of the available [StatsD client libraries] for Node.js, Java, Python,
Ruby, Perl, PHP, Clojure, Io, C, C++, .NET, Go, Apache, Varnish, PowerShell,
Browser, Objective-C, ActionScript, WordPress, Drupal, Haskell, R, Lua, or
Nim.

## Explore data

After Telegraf receives data, CrateDB stores the metrics in the designated table,
ready for inspection.

```shell
psql "postgresql://crate:crate@cratedb:5432/" -c "SELECT * FROM doc.metrics ORDER BY timestamp LIMIT 5;"
```
```psql
       hash_id        |         timestamp          |    name     |                     tags                      |    fields    |            day
----------------------+----------------------------+-------------+-----------------------------------------------+--------------+----------------------------
 -8005856065082590291 | 2025-09-20 19:30:45.000+00 | temperature | {"host":"2748411a9651","metric_type":"gauge"} | {"value":42} | 2025-09-20 00:00:00.000+00
  7068016256787696496 | 2025-09-20 19:30:45.000+00 | humidity    | {"host":"2748411a9651","metric_type":"gauge"} | {"value":84} | 2025-09-20 00:00:00.000+00
(2 rows)
```


[netcat]: https://en.wikipedia.org/wiki/Netcat
[StatsD]: https://github.com/statsd/statsd
[statsd package]: https://pypi.org/project/statsd/
[StatsD client libraries]: https://github.com/statsd/statsd/wiki#client-implementations
[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
