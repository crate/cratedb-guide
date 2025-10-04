(telegraf-usage)=
# Load data into CrateDB using Telegraf

This usage guide walks you through starting the [Telegraf] agent and CrateDB,
then configuring Telegraf to submit system metrics to CrateDB.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`
- {download}`telegraf.conf`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

## Submit data

The `telegraf.conf` configures Telegraf to enable collecting readings about
CPU usage on the local computer. 
Telegraf is a plugin-driven tool and has plugins to collect many different types
of metrics. Because we just want to test things out, a single sensor is sufficient.

## Explore data

After 10 seconds, which is the default output flush interval of Telegraf, the first
metrics will appear in the `metrics` table in CrateDB. To adjust the value, navigate
to `flush_interval = "10s"` in `telegraf.conf`.

Inspect data stored in CrateDB.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.metrics LIMIT 5;"
```
```psql
+----------------------+---------------+------+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
|              hash_id |     timestamp | name | tags                                     | fields                                                                                                                                                                                    |           day |
+----------------------+---------------+------+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| -2149377133708231861 | 1759686560000 | cpu  | {"cpu": "cpu5", "host": "02880df5c05e"}  | {"usage_guest": 0, "usage_guest_nice": 0, "usage_idle": 98, "usage_iowait": 0, "usage_irq": 0, "usage_nice": 0, "usage_softirq": 0, "usage_steal": 0, "usage_system": 0, "usage_user": 0} | 1759622400000 |
| -4525358308278119095 | 1759686560000 | cpu  | {"cpu": "cpu13", "host": "02880df5c05e"} | {"usage_guest": 0, "usage_guest_nice": 0, "usage_idle": 98, "usage_iowait": 0, "usage_irq": 0, "usage_nice": 0, "usage_softirq": 0, "usage_steal": 0, "usage_system": 0, "usage_user": 1} | 1759622400000 |
|  6120994000579036036 | 1759686560000 | cpu  | {"cpu": "cpu14", "host": "02880df5c05e"} | {"usage_guest": 0, "usage_guest_nice": 0, "usage_idle": 99, "usage_iowait": 0, "usage_irq": 0, "usage_nice": 0, "usage_softirq": 0, "usage_steal": 0, "usage_system": 0, "usage_user": 0} | 1759622400000 |
|   869454636336868835 | 1759686560000 | cpu  | {"cpu": "cpu1", "host": "02880df5c05e"}  | {"usage_guest": 0, "usage_guest_nice": 0, "usage_idle": 99, "usage_iowait": 0, "usage_irq": 0, "usage_nice": 0, "usage_softirq": 0, "usage_steal": 0, "usage_system": 0, "usage_user": 0} | 1759622400000 |
|   722018796549427924 | 1759686560000 | cpu  | {"cpu": "cpu8", "host": "02880df5c05e"}  | {"usage_guest": 0, "usage_guest_nice": 0, "usage_idle": 97, "usage_iowait": 0, "usage_irq": 0, "usage_nice": 0, "usage_softirq": 0, "usage_steal": 0, "usage_system": 0, "usage_user": 1} | 1759622400000 |
+----------------------+---------------+------+------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
SELECT 5 rows in set (0.009 sec)
```


[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
