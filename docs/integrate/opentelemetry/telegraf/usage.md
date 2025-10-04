(opentelemetry-telegraf-usage)=
# Store OpenTelemetry metrics using Telegraf and CrateDB

This how-to guide walks you through configuring [Telegraf] to receive
[OpenTelemetry] [metrics] and store them into CrateDB.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`.env`
- {download}`compose.yaml`
- {download}`example.py`
- {download}`telegraf.conf`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

## Submit data

### Use Python

To submit metrics using the OpenTelemetry Python SDK, choose one of these
approaches:

**Option 1: Using uv (recommended)**
```shell
docker compose run --rm --env-from-file=.env uv uv run --with=opentelemetry-distro --with=opentelemetry-exporter-otlp opentelemetry-instrument python /src/example.py
```

**Option 2: Using pip**

First, install dependencies:
```shell
pip install opentelemetry-distro opentelemetry-exporter-otlp
```
Then run the example:
```shell
opentelemetry-instrument --service_name=app python example.py
```

::::{dropdown} Display example\.py
:::{literalinclude} example.py
:::
::::

### Use any language

Use any of the available [OpenTelemetry language APIs & SDKs] for C++, C#/.NET,
Erlang/Elixir, Go, Java, JavaScript, PHP, Python, Ruby, Rust, or Swift. 

## Explore data

CrateDB stores the metrics in the designated table, ready for inspection and analysis.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.metrics ORDER BY timestamp LIMIT 5;"
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
