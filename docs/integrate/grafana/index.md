(grafana)=
# Grafana

```{div} .float-right
[![Grafana logo](https://cratedb.com/hs-fs/hubfs/Imported_Blog_Media/grafana-logo-1-520x126.png?width=1040&height=252&name=grafana-logo-1-520x126.png){height=60px loading=lazy}][Grafana OSS]
```
```{div} .clearfix
```

:::{rubric} About
:::

[Grafana OSS] is the leading open-source metrics visualization tool that helps you
build real-time dashboards, graphs, and many other sorts of data visualizations.
[Grafana Cloud] is a fully-managed service offered by [Grafana Labs].


:::{dropdown} **Managed Grafana**
Get Grafana fully managed with [Grafana Cloud].

- Offered as a fully managed service, Grafana Cloud is the fastest way to adopt
  Grafana and includes a scalable, managed backend for metrics, logs, and traces.
- Managed and administered by Grafana Labs with free and paid options for
  individuals, teams, and large enterprises.
- Includes a robust free tier with access to 10k metrics, 50GB logs, 50GB traces,
  50GB profiles, and 500VUh of k6 testing for 3 users.
:::

:::{rubric} Learn
:::

::::{grid} 2

:::{grid-item-card} Visualize data with Grafana
:link: grafana-tutorial
:link-type: ref
Grafana complements CrateDB in monitoring and visualizing large volumes of
machine data in real-time.

Select and import a dataset into CrateDB, connect Grafana to CrateDB,
and create your first dashboard.
+++
Connecting to a CrateDB cluster uses the Grafana PostgreSQL data source adapter.
:::

:::{grid-item}
![Grafana PostgreSQL data source configuration](https://github.com/crate/cratedb-guide/raw/a9c8c03384/docs/_assets/img/integrations/grafana/grafana-connection.png){h=200px}

![Grafana example panel showing data from CrateDB](https://github.com/crate/cratedb-guide/raw/a9c8c03384/docs/_assets/img/integrations/grafana/grafana-panel1.png){h=200px}
:::

::::

:::{rubric} See also
:::

::::{grid} 2

:::{grid-item-card} Tutorial: Monitoring CrateDB with Prometheus and Grafana
:link: monitoring-prometheus-grafana
:link-type: ref
Production-grade monitoring and graphing of CrateDB metrics.
:::

::::

:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
:::


```{seealso}
[CrateDB and Grafana]
```


[CrateDB and Grafana]: https://cratedb.com/integrations/cratedb-and-grafana
[Grafana Cloud]: https://grafana.com/grafana/
[Grafana Labs]: https://grafana.com/about/team/
[Grafana OSS]: https://grafana.com/oss/grafana/
