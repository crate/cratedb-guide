(opentelemetry)=
# OpenTelemetry

```{div} .float-right
[![OpenTelemetry logo](https://opentelemetry.io/img/logos/opentelemetry-horizontal-color.svg){height=100px loading=lazy}][OpenTelemetry]
```
```{div} .clearfix
```

:::{rubric} About
:::

[OpenTelemetry] (OTel) is an open-source observability framework and toolkit
designed to facilitate the export and collection of telemetry data such as
[traces], [metrics], and [logs].

OpenTelemetry provides a unified framework and the APIs/SDKs to instrument
applications, allowing for the use of a single standard across different
observability tools.

The [OpenTelemetry Collector] and its [Prometheus Remote Write Exporter] can
be used to submit and store [metrics] data into CrateDB. Alternatively, you
can use [Telegraf].

:::{rubric} Synopsis
:::

Configure OpenTelemetry Collector to send metrics data to the
[CrateDB Prometheus Adapter] by configuring the `prometheusremotewrite`
exporter endpoint.

```yaml
exporters:
  prometheusremotewrite:
    endpoint: "http://cratedb-prometheus-adapter:9268/write"
    remote_write_queue:
      enabled: false
    external_labels:
      subsystem: "otel-testdrive"
  debug:
    verbosity: detailed
```
```yaml
service:
  pipelines:
    metrics:
      receivers: [otlp, carbon]
      processors: [batch]
      exporters: [debug, prometheusremotewrite]
```

Configure Telegraf to store OpenTelemetry metrics data into CrateDB.

```ini
# OpenTelemetry Input Plugin
# https://github.com/influxdata/telegraf/blob/release-1.36/plugins/inputs/opentelemetry/README.md
[[inputs.opentelemetry]]
```
```ini
# CrateDB Output Plugin
# https://github.com/influxdata/telegraf/tree/master/plugins/outputs/cratedb
[[outputs.cratedb]]

  ## Connection parameters for accessing the database.
  ## See https://pkg.go.dev/github.com/jackc/pgx/v4#ParseConfig for available options.
  url = "postgres://crate:crate@cratedb/?sslmode=disable"

  ## Timeout for all CrateDB queries.
  # timeout = "5s"

  ## Name of the table to store metrics in.
  table = "metrics"

  ## If true, and the metrics table does not exist, create it automatically.
  table_create = true

  ## The character(s) to replace any '.' in an object key with
  # key_separator = "_"
```

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Guide: Use OTel Collector and CrateDB
:link: opentelemetry-otelcol-usage
:link-type: ref
How to configure OpenTelemetry Collector to submit metrics to CrateDB.
:::

:::{grid-item-card} Guide: Use Telegraf and CrateDB
:link: opentelemetry-telegraf-usage
:link-type: ref
How to configure Telegraf to submit OpenTelemetry metrics to CrateDB.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Collector Usage <collector/usage>
Telegraf Usage <telegraf/usage>
:::


[CrateDB Prometheus Adapter]: https://github.com/crate/cratedb-prometheus-adapter
[logs]: https://opentelemetry.io/docs/concepts/signals/logs/
[metrics]: https://opentelemetry.io/docs/concepts/signals/metrics/
[OpenTelemetry]: https://opentelemetry.io/docs/what-is-opentelemetry/
[OpenTelemetry Collector]: https://opentelemetry.io/docs/collector/
[Prometheus Remote Write Exporter]: https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/prometheusremotewriteexporter
[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
[traces]: https://opentelemetry.io/docs/concepts/signals/traces/
