(opentelemetry-otelcol-tutorial)=
# Connect the OpenTelemetry Collector to CrateDB

This tutorial walks you through configuring the [OpenTelemetry Collector],
its built-in [Prometheus Remote Write Exporter], and the
[CrateDB Prometheus Adapter], to receive [OpenTelemetry] [metrics] and
store them into CrateDB.

## Prerequisites

Docker is used for running all components. This approach works consistently
across Linux, macOS, and Windows. Alternatively, you can use Podman.

### Commands

Prepare shortcut for {ref}`crate-crash:index` command.

::::{tab-set}
:sync-group: os

:::{tab-item} Linux and macOS
:sync: unix
Add these settings to your shell profile (`~/.profile`) to make them persistent.
```shell
alias crash="docker run --rm -it --network=host crate/crate:latest crash"
alias nc="docker run --rm -i --network=cratedb-demo docker.io/toolbelt/netcat:2025-08-23"
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
Add these settings to your PowerShell profile (`$PROFILE`) to make them persistent.
```powershell
function crash { docker run --rm -i --network=host crate/crate:latest crash @args }
function nc { docker run --rm -i --network=cratedb-demo docker.io/toolbelt/netcat:2025-08-23 @args }
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
doskey crash=docker run --rm -i --network=host crate/crate:latest crash $*
doskey nc=docker run --rm -i --network=cratedb-demo docker.io/toolbelt/netcat:2025-08-23 $*
```
:::

::::

### Services

Save the files {download}`compose.yaml`,
{download}`cratedb-prometheus-adapter.yaml`,
{download}`otelcol.yaml` and {download}`ddl.sql`
to your machine and start all services using
Docker Compose or Podman Compose.
```shell
docker compose up
```

## Submit data

### Use netcat

Use [netcat] to submit metrics using the [Carbon plaintext protocol].
```shell
printf "temperature;job=app 42.42 1758486061\nhumidity;job=app 84.84 1758486061" \
  | nc -c localhost 2003
```

### Use Python

Use the OTel Python language SDK to submit metrics. To do that,
save the Python OTel example file {download}`example.py` to your machine and
use the `opentelemetry-instrument` program to invoke your Python application.
```shell
opentelemetry-instrument --service_name=app python example.py
```
:::{literalinclude} example.py
:::
The [uv] utility can invoke the demo program including dependencies,
otherwise install them using `pip install opentelemetry-distro opentelemetry-exporter-otlp`
or similarly.
```shell
uv run --with=opentelemetry-distro --with=opentelemetry-exporter-otlp \
  opentelemetry-instrument --service_name=app python example.py
```

### Use any language

Use any of the available [OpenTelemetry language APIs & SDKs] for C++, C#/.NET,
Erlang/Elixir, Go, Java, JavaScript, PHP, Python, Ruby, Rust, or Swift. 

## Explore data

CrateDB stored the metrics in the designated table, ready for inspection and analysis.
```shell
crash --hosts "http://crate:crate@localhost:4200/" \
  -c "SELECT * FROM testdrive.metrics ORDER BY timestamp LIMIT 5;"
```
```psql
+---------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+---------------------+----------------+
|     timestamp | labels_hash      | labels                                                                                                                                                                                                                     | value |            valueRaw | day__generated |
+---------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+---------------------+----------------+
| 1758480857158 | 64614d7f1ef80933 | {"__name__": "target_info", "job": "app", "subsystem": "otel-testdrive", "telemetry_auto_version": "0.58b0", "telemetry_sdk_language": "python", "telemetry_sdk_name": "opentelemetry", "telemetry_sdk_version": "1.37.0"} |  1.0  | 4607182418800017408 |  1758412800000 |
| 1758480857158 | 7c6f57205e58af4c | {"__name__": "temperature", "job": "app", "subsystem": "otel-testdrive"}                                                                                                                                                   | 42.42 | 4631166901565532406 |  1758412800000 |
| 1758480857158 | 3fce270356467381 | {"__name__": "humidity", "job": "app", "subsystem": "otel-testdrive"}                                                                                                                                                      | 84.84 | 4635670501192902902 |  1758412800000 |
+---------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------+---------------------+----------------+
SELECT 3 rows in set (0.005 sec)
```


[Carbon plaintext protocol]: https://graphite.readthedocs.io/en/latest/feeding-carbon.html
[CrateDB Prometheus Adapter]: https://github.com/crate/cratedb-prometheus-adapter
[metrics]: https://opentelemetry.io/docs/concepts/signals/metrics/
[netcat]: https://en.wikipedia.org/wiki/Netcat
[OpenTelemetry]: https://opentelemetry.io/docs/what-is-opentelemetry/
[OpenTelemetry Collector]: https://opentelemetry.io/docs/collector/
[OpenTelemetry language APIs & SDKs]: https://opentelemetry.io/docs/languages/
[Prometheus Remote Write Exporter]: https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/prometheusremotewriteexporter
[uv]: https://docs.astral.sh/uv/
