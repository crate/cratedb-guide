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

Configure OpenTelemetry Collector to send metrics data to the [CrateDB Prometheus Adapter].

:::{literalinclude} collector/otelcol.yaml
:lines: 26-34
:::
:::{literalinclude} collector/otelcol.yaml
:lines: 38-43
:::

Configure Telegraf to store OpenTelemetry metrics data into CrateDB.

:::{literalinclude} telegraf/telegraf.conf
:lines: 1-6
:::
:::{literalinclude} telegraf/telegraf.conf
:lines: 27-33
:::


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
