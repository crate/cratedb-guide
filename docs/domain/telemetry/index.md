(metrics-store)=

# Telemetry Data Store

CrateDB works well for storing massive amounts of telemetry data,
such as metrics and logs.

It is a spiritual successor, or alternative to, rrdtool, Graphite, InfluxDB,
Prometheus, Mimir, or Thanos, but with the benefits of long term storage
capabilities, standard database interfaces, SQL query language, and
horizontal scalability as you go.

:Tags:
  {tags-primary}`Long Term Storage`
  {tags-primary}`Metrics`
  {tags-primary}`Monitoring`
  {tags-primary}`Graphing`
  {tags-primary}`Observability`
  {tags-primary}`Telemetry`
  {tags-primary}`Logging`

:Technologies:
  {tags-info}`Collector Agents`
  {tags-info}`Metric Brokers`
  {tags-info}`Prometheus`
  {tags-info}`Grafana`

:Monitoring Domains:
  {tags-secondary}`Application`
  {tags-secondary}`Datacenter`
  {tags-secondary}`Network`
  {tags-secondary}`Sensor`
  {tags-secondary}`Service`
  {tags-secondary}`System`

:Related:
  [](#timeseries) •
  [](#machine-learning) •
  [](#analytics)

:Product:
  [Log Database]


(metrics-store-prometheus)=

## Prometheus

Using CrateDB as a long term storage for your Prometheus metrics.

:Repositories:
  [CrateDB] •
  [Prometheus] •
  [CrateDB Prometheus Adapter]

:Tutorial:
  [Storing long term metrics with Prometheus in CrateDB]

:Blog:
  [Getting Started With Prometheus and CrateDB for Long Term Storage]


::::{info-card}

:::{grid-item}
:columns: 8

{material-outlined}`manage_history;2em` &nbsp; **CrateDB as Prometheus Long Term Storage**

This video illustrates how to start Prometheus, CrateDB, and CrateDB
Prometheus Adapter with Docker Compose, and how to configure Prometheus
to use CrateDB as remote storage.

[Prometheus with CrateDB: Long Term Metrics Storage]
:::

:::{grid-item} &nbsp;
:columns: 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/EfIlRXVyfZM?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Date:** 14 Jul 2022 \
**Speaker:** Johannes Faigle
:::

::::



[CrateDB]: https://github.com/crate/crate
[CrateDB Prometheus Adapter]: https://github.com/crate/cratedb-prometheus-adapter
[Getting Started With Prometheus and CrateDB for Long Term Storage]: https://cratedb.com/blog/getting-started-prometheus-cratedb-long-term-storage
[Log Database]: https://cratedb.com/solutions/log-database
[Prometheus]: https://github.com/prometheus/prometheus
[Prometheus with CrateDB: Long Term Metrics Storage]: https://youtu.be/EfIlRXVyfZM?feature=shared
[Storing long term metrics with Prometheus in CrateDB]: https://community.cratedb.com/t/storing-long-term-metrics-with-prometheus-in-cratedb/1012
