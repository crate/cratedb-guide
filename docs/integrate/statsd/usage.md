(statsd-usage)=
# Load data into CrateDB using StatsD and Telegraf

This usage guide walks you through configuring [Telegraf] to receive [StatsD]
metrics and store them into CrateDB.

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

### netcat
Use [netcat] for submitting data.
```shell
echo "temperature:42|g" | docker compose run --rm nc -C -w 1 -u telegraf 8125
echo "humidity:84|g"    | docker compose run --rm nc -C -w 1 -u telegraf 8125
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
docker compose run --rm psql psql "postgresql://crate:crate@cratedb:5432/" -c "SELECT * FROM doc.metrics ORDER BY timestamp LIMIT 5;"
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
