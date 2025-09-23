(prometheus)=
# Prometheus

```{div} .float-right
[![Prometheus logo](https://github.com/crate/crate-clients-tools/assets/453543/8ddb109f-b45f-46b0-8103-30ba491f7142){height=60px loading=lazy}][Prometheus]
```
```{div} .clearfix
```


## About

[Prometheus] is an open-source systems monitoring and alerting toolkit
for collecting metrics data from applications and infrastructures.
[CrateDB] can be used as a long-term storage for Prometheus metrics.

::::{dropdown} **Details**

Prometheus collects and stores its metrics as time series data, i.e.
metrics information is stored with the timestamp at which it was recorded,
alongside optional key-value pairs called labels.

:::{rubric} Features
:::
Prometheus's main features are:

- a multidimensional data model with time series data identified by metric name and key/value pairs
- PromQL, a flexible query language to leverage this dimensionality
- no reliance on distributed storage; single server nodes are autonomous
- time series collection happens via a pull model over HTTP
- pushing time series is supported via an intermediary gateway
- targets are discovered via service discovery or static configuration
- multiple modes of graphing and dashboarding support

![Prometheus architecture overview](https://github.com/crate/crate-clients-tools/assets/453543/26b47686-889a-4137-a87f-d6a6b38d56d2){h=200px}

::::


## Learn

:::{rubric} Remote Endpoints and Storage
:::

The [Prometheus remote endpoints and storage] subsystem, based on its
[remote write] and [remote read] features, allows to transparently
send and receive metric samples. It is primarily intended for long-term
storage.

This is where CrateDB comes into place: The [CrateDB Prometheus
Adapter] stores collected metrics data into CrateDB and
takes advantage of its high ingestion and query speed to
massively scale-out Prometheus.

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Blog: Getting started
:link: https://cratedb.com/blog/getting-started-prometheus-cratedb-long-term-storage
:link-type: url
Getting started with Prometheus and CrateDB for long-term storage.
:::

:::{grid-item-card} Store Prometheus long-term metrics into CrateDB
:link: prometheus-usage
:link-type: ref
Set up CrateDB as a long-term metrics store for Prometheus using Docker Compose.
:::

::::

:::{rubric} Webinars
:::

::::{info-card}

:::{grid-item}
:columns: 8

{material-outlined}`manage_history;2em` &nbsp; **CrateDB as Prometheus Long-Term Storage**

Learn how to start Prometheus, CrateDB, and the CrateDB Prometheus Adapter with
Docker Compose, and how to configure Prometheus to use CrateDB as remote storage.

This webinar accompanies the "Storing long-term metrics with Prometheus in CrateDB"
usage guide.

[Prometheus with CrateDB: Long-Term Metrics Storage]
:::

:::{grid-item}
:columns: 4

<iframe width="240" loading="lazy" src="https://www.youtube-nocookie.com/embed/EfIlRXVyfZM?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
:::

::::


:::{rubric} Repositories
:::

[CrateDB] •
[Prometheus] •
[CrateDB Prometheus Adapter]


```{seealso}
[CrateDB and Prometheus]
```


:::{toctree}
:maxdepth: 1
:hidden:
Usage <usage>
:::


[CrateDB]: https://github.com/crate/crate
[CrateDB and Prometheus]: https://cratedb.com/integrations/cratedb-and-prometheus
[CrateDB Prometheus Adapter]: https://github.com/crate/cratedb-prometheus-adapter
[Prometheus]: https://prometheus.io/
[Prometheus remote endpoints and storage]: https://prometheus.io/docs/operating/integrations/#remote-endpoints-and-storage
[Prometheus with CrateDB: Long-Term Metrics Storage]: https://youtu.be/EfIlRXVyfZM?feature=shared
[remote read]: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_read
[remote write]: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write
