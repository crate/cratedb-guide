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
traces, metrics, and logs.

OpenTelemetry provides a unified framework and the APIs/SDKs to instrument
applications, allowing for the use of a single standard across different
observability tools.

The [OpenTelemetry Collector] and its [Prometheus Remote Write Exporter] can
be used to submit and store [metrics] data into CrateDB.

:::{rubric} Synopsis
:::

Configure OpenTelemetry Collector to send metrics data to the [CrateDB Prometheus Adapter].

:::{literalinclude} collector/otelcol.yaml
:lines: 26-34
:::
:::{literalinclude} collector/otelcol.yaml
:lines: 38-43
:::


:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Tutorial: Use OTel Collector and CrateDB
:link: opentelemetry-otelcol-tutorial
:link-type: ref
How to configure OpenTelemetry Collector to submit metrics to CrateDB.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Collector Tutorial <collector/tutorial>
:::


[CrateDB Prometheus Adapter]: https://github.com/crate/cratedb-prometheus-adapter
[logs]: https://opentelemetry.io/docs/concepts/signals/logs/
[metrics]: https://opentelemetry.io/docs/concepts/signals/metrics/
[OpenTelemetry]: https://opentelemetry.io/docs/what-is-opentelemetry/
[OpenTelemetry Collector]: https://opentelemetry.io/docs/collector/
[Prometheus Remote Write Exporter]: https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/prometheusremotewriteexporter
[traces]: https://opentelemetry.io/docs/concepts/signals/traces/
