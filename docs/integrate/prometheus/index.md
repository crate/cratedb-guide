(prometheus)=
# Prometheus

:::{rubric} About
:::

```{div}
:style: "float: right; margin-left: 0.3em"
[![](https://github.com/crate/crate-clients-tools/assets/453543/8ddb109f-b45f-46b0-8103-30ba491f7142){w=180px}](https://prometheus.io/)
```

[Prometheus] is an open-source systems monitoring and alerting toolkit
for collecting metrics data from applications and infrastructures.

Prometheus collects and stores its metrics as time series data, i.e.
metrics information is stored with the timestamp at which it was recorded,
alongside optional key-value pairs called labels.

:::{rubric} Features
:::
Prometheus's main features are:

- a multi-dimensional data model with time series data identified by metric name and key/value pairs
- PromQL, a flexible query language to leverage this dimensionality
- no reliance on distributed storage; single server nodes are autonomous
- time series collection happens via a pull model over HTTP
- pushing time series is supported via an intermediary gateway
- targets are discovered via service discovery or static configuration
- multiple modes of graphing and dashboarding support


:::{rubric} Remote Endpoints and Storage
:::
The [Prometheus remote endpoints and storage] subsystem, based on its
[remote write] and [remote read] features, allows to transparently
send and receive metric samples. It is primarily intended for long term
storage.

This is where CrateDB comes into place. Using the [CrateDB Prometheus
Adapter], one can easily store the collected metrics data in CrateDB and
take advantage of its high ingestion and query speed and friendly UI to
massively scale-out Prometheus.

![](https://github.com/crate/crate-clients-tools/assets/453543/26b47686-889a-4137-a87f-d6a6b38d56d2){h=200px}

```{div}
:style: "clear: both"
```

:::{rubric} Learn
:::

- [CrateDB as a long term metrics store for Prometheus](#metrics-store-prometheus)
- [Webinar: Using Prometheus and Grafana with CrateDB Cloud]

```{seealso}
- [CrateDB and Prometheus]
- [CrateDB Prometheus Adapter]
```


[CrateDB and Prometheus]: https://cratedb.com/integrations/cratedb-and-prometheus
[CrateDB Prometheus Adapter]: https://github.com/crate/cratedb-prometheus-adapter
[Prometheus remote endpoints and storage]: https://prometheus.io/docs/operating/integrations/#remote-endpoints-and-storage
[Prometheus]: https://prometheus.io/
[remote read]: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_read
[remote write]: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write
[Webinar: Using Prometheus and Grafana with CrateDB Cloud]: https://cratedb.com/resources/webinars/lp-wb-prometheus-grafana
