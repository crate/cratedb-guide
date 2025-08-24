(telegraf-tutorial)=
# Load data into CrateDB using Telegraf

The tutorial will walk you through starting the [Telegraf] agent/broker
and CrateDB, and configuring Telegraf to submit system metrics measurement
values to CrateDB.

## Prerequisites

Docker is used for running all components. This approach works consistently
across Linux, macOS, and Windows. Alternatively, you can use Podman.

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

Prepare shortcut for the CrateDB shell.

::::{tab-set}

:::{tab-item} Linux and macOS
To make the settings persistent, add them to your shell profile (`~/.profile`).
```shell
alias crash="docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash $*
```
:::

::::


## Usage

Configure Telegraf by creating a configuration blueprint and adjusting it.
Telegraf is a plugin-driven tool and has plugins to collect many different types
of metrics. Because we just want to test things out, we are using `--input-filter cpu`
to limit input plugins so that Telegraf only collects readings about CPU usage
on the local computer. To send the collected data to CrateDB, use
`--output-filter cratedb`.
```shell
docker run --rm docker.io/telegraf \
  --input-filter cpu \
  --output-filter cratedb \
  config > telegraf.conf
```

The database connection URL is a `pgx/v4` connection string. Configure
`table_create = true` to automatically let Telegraf create the metrics table
if it doesn't exist.
```shell
sed -i 's!postgres://user:password@localhost/schema?sslmode=disable!postgres://crate@cratedb/doc?sslmode=disable!g' telegraf.conf
sed -i 's!# table_create = false!table_create = true!' telegraf.conf
```

Start Telegraf.
```shell
docker run --name=telegraf --rm -it --network=cratedb-demo \
  --volume $(pwd)/telegraf.conf:/etc/telegraf/telegraf.conf \
  docker.io/telegraf
```

After 10 seconds, which is the default output flush interval of Telegraf, the first
metrics will appear in the `metrics` table in CrateDB. To adjust the value, navigate
to `flush_interval = "10s"` in `telegraf.conf`.

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM doc.metrics;"
```


[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
