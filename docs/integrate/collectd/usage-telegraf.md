(collectd-usage-telegraf)=
# Load data into CrateDB using collectd and Telegraf

This usage guide shows how to configure and start [collectd], [Telegraf]
and CrateDB so that collectd sends system metrics to Telegraf, which
stores it into CrateDB using the built-in [CrateDB Output Plugin for Telegraf].

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`
- {download}`Dockerfile`
- {download}`telegraf.conf`
- {download}`collectd-telegraf.conf`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

To send the collected data to Telegraf, collectd is configured to load its
[`network` plugin].

::::{dropdown} collectd configuration `collectd-telegraf.conf`
:::{literalinclude} collectd-telegraf.conf
:::
::::

## Explore data

After the first scraping interval, metrics will show up in the
designated table in CrateDB, ready to be inspected.
```shell
docker compose run --rm --no-TTY postgresql psql "postgresql://crate:crate@cratedb:5432/" -c "SELECT * FROM doc.metrics LIMIT 5;"
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
[CrateDB Output Plugin for Telegraf]: https://github.com/influxdata/telegraf/tree/master/plugins/outputs/cratedb
[`network` plugin]: https://collectd.org/documentation/manpages/collectd.conf.html#plugin-network
[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
