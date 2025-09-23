(metrics)=
(metrics-store)=
(telemetry)=
(integrate-metrics)=
# Metrics, telemetry, and logs

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 9 9 9

:::{rubric} Introduction
:::

CrateDB works well for storing massive amounts of telemetry data, such as metrics and logs.

CrateDB can serve as an alternative to time-series databases and metric stores
like RRD, Whisper (Graphite), InfluxDB, Prometheus, Cortex, Mimir, Thanos,
or VictoriaMetrics,
while adding long‑term storage, standard database interfaces, SQL,
and horizontal scalability.

CrateDB integrates with metrics collection agents, brokers, and stores.
This documentation section lists applications and daemons which can
be used together with CrateDB, and educates about how to use them optimally.

::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Related
:::
- {ref}`timeseries`
- {ref}`machine-learning`
- {ref}`analytics`
- [Log Database]
::::

:::::


:::{rubric} Integrations
:::

Storing metrics data for the long term is a common need in systems monitoring
scenarios. CrateDB offers corresponding integration adapters.

:::::{grid} auto 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} collectd
:link: collectd
:link-type: ref
Send metrics with collectd, a system and application metrics collection daemon.
::::

::::{grid-item-card} Prometheus
:link: prometheus
:link-type: ref
Prometheus is an open-source systems monitoring and alerting toolkit
for collecting metrics data from applications and infrastructures.
::::

::::{grid-item-card} rsyslog
:link: rsyslog
:link-type: ref
Send logs with rsyslog, a rocket‑fast system for log processing.
::::

::::{grid-item-card} Telegraf
:link: telegraf
:link-type: ref
Telegraf is a leading open source server agent to help you collect metrics
from your stacks, sensors, and systems.
::::

:::::


:::{rubric} Learn more
:::

- [Getting Started With Prometheus and CrateDB for Long Term Storage]
- [Prometheus with CrateDB: Long Term Metrics Storage]
- [Storing long term metrics with Prometheus in CrateDB]


[Getting Started With Prometheus and CrateDB for Long Term Storage]: https://cratedb.com/blog/getting-started-prometheus-cratedb-long-term-storage
[Log Database]: https://cratedb.com/solutions/log-database
[Prometheus with CrateDB: Long Term Metrics Storage]: https://youtu.be/EfIlRXVyfZM?feature=shared
[Storing long term metrics with Prometheus in CrateDB]: https://community.cratedb.com/t/storing-long-term-metrics-with-prometheus-in-cratedb/1012
