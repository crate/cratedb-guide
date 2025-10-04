(opentelemetry-otelcol-usage)=
# Connect the OpenTelemetry Collector to CrateDB

Configure the [OpenTelemetry Collector], its built-in [Prometheus Remote Write Exporter], 
and the [CrateDB Prometheus Adapter] to receive [OpenTelemetry] [metrics] and store them
into CrateDB.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`.env`
- {download}`compose.yaml`
- {download}`cratedb-prometheus-adapter.yaml`
- {download}`ddl.sql`
- {download}`example.py`
- {download}`otelcol.yaml`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

## Submit data

### Use netcat

Use [netcat] to submit metrics using the [Carbon plaintext protocol].
```shell
printf "temperature;job=app 42.42 1758486061\nhumidity;job=app 84.84 1758486061" | docker compose run --rm nc -C -w1 otelcol 2003
```

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
docker compose exec cratedb crash -c "SELECT * FROM testdrive.metrics ORDER BY timestamp LIMIT 5;"
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
