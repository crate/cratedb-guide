(opentelemetry-telegraf-usage)=
# Store OpenTelemetry metrics using Telegraf and CrateDB

This how-to guide walks you through configuring [Telegraf] to receive
[OpenTelemetry] [metrics] and store them into CrateDB.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

### Commands

Prepare shortcut for {ref}`crate-crash:index` command.

::::{tab-set}
:sync-group: os

:::{tab-item} Linux, macOS, WSL
:sync: unix
Add these settings to your shell profile (`~/.profile`) to make them persistent.
```shell
alias crash="docker compose exec -it cratedb crash"
```
:::
:::{tab-item} Windows PowerShell
:sync: powershell
Add these settings to your PowerShell profile (`$PROFILE`) to make them persistent.
```powershell
function crash { docker compose exec -it cratedb crash @args }
```
:::
:::{tab-item} Windows Command
:sync: dos
```shell
doskey crash=docker compose exec -it cratedb crash $*
REM Note: doskey macros reset each session. To persist, configure an AutoRun command
REM pointing to a macro file, or re-run these in your shell startup script.
```
:::

::::

### Services

Save {download}`compose.yaml` and {download}`telegraf.conf`, then start
services using Docker Compose or Podman Compose.

```shell
docker compose up
```

## Submit data

### Use Python

To submit metrics using the OpenTelemetry Python SDK, download the example file
{download}`example.py` to your machine and choose one of these approaches:

**Option 1: Using uv (recommended)**
```shell
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
export OTEL_SERVICE_NAME=app
uv run --with=opentelemetry-distro --with=opentelemetry-exporter-otlp opentelemetry-instrument python example.py
```

**Option 2: Using pip**
Install dependencies:
```shell
pip install opentelemetry-distro opentelemetry-exporter-otlp
```
Then run the example:
```shell
opentelemetry-instrument --service_name=app python example.py
```

:::{literalinclude} example.py
:::

### Use any language

Use any of the available [OpenTelemetry language APIs & SDKs] for C++, C#/.NET,
Erlang/Elixir, Go, Java, JavaScript, PHP, Python, Ruby, Rust, or Swift. 

## Explore data

CrateDB stores the metrics in the designated table, ready for inspection and analysis.
```shell
crash --hosts "http://crate:crate@localhost:4200/" -c "SELECT * FROM metrics ORDER BY timestamp LIMIT 5;"
```
```psql
+---------------------+---------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
|             hash_id |     timestamp | name        | tags                                                                                                                                                                                                                                           | fields           |           day |
+---------------------+---------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
| 4549776513022193265 | 1758500094846 | temperature | {"host": "2805bf17ee55", "otel_library_name": "testdrive.meter.name", "service_name": "app", "telemetry_auto_version": "0.58b0", "telemetry_sdk_language": "python", "telemetry_sdk_name": "opentelemetry", "telemetry_sdk_version": "1.37.0"} | {"gauge": 42.42} | 1758499200000 |
| -926134856403504308 | 1758500094846 | humidity    | {"host": "2805bf17ee55", "otel_library_name": "testdrive.meter.name", "service_name": "app", "telemetry_auto_version": "0.58b0", "telemetry_sdk_language": "python", "telemetry_sdk_name": "opentelemetry", "telemetry_sdk_version": "1.37.0"} | {"gauge": 84.84} | 1758499200000 |
+---------------------+---------------+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+---------------+
SELECT 2 rows in set (0.049 sec)
```


[metrics]: https://opentelemetry.io/docs/concepts/signals/metrics/
[OpenTelemetry]: https://opentelemetry.io/docs/what-is-opentelemetry/
[OpenTelemetry language APIs & SDKs]: https://opentelemetry.io/docs/languages/
[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
[uv]: https://docs.astral.sh/uv/
