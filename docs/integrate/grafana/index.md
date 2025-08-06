(grafana)=
# Grafana

:::{rubric} About
:::

```{div}
:style: "float: right; margin-left: 1em"
[![](https://cratedb.com/hs-fs/hubfs/Imported_Blog_Media/grafana-logo-1-520x126.png?width=1040&height=252&name=grafana-logo-1-520x126.png){w=180px}](https://grafana.com/grafana/)
```

[Grafana OSS] is the leading open-source metrics visualization tool that helps you
build real-time dashboards, graphs, and many other sorts of data visualizations.
[Grafana Cloud] is a fully-managed service offered by [Grafana Labs].

Grafana complements CrateDB in monitoring and visualizing large volumes of machine
data in real-time.

Connecting to a CrateDB cluster will use the Grafana PostgreSQL data source adapter.
The following tutorials outline how to configure Grafana to connect to CrateDB, and
how to run a database query. 

![image](https://github.com/crate/cratedb-guide/raw/a9c8c03384/docs/_assets/img/integrations/grafana/grafana-connection.png){h=200px}
![image](https://github.com/crate/cratedb-guide/raw/a9c8c03384/docs/_assets/img/integrations/grafana/grafana-panel1.png){h=200px}


:::{dropdown} **Managed Grafana**
```{div}
:style: "float: right"
[![](https://cratedb.com/hs-fs/hubfs/Imported_Blog_Media/grafana-logo-1-520x126.png?width=1040&height=252&name=grafana-logo-1-520x126.png){w=180px}](https://grafana.com/grafana/)
```

Get Grafana fully managed with [Grafana Cloud].

- Offered as a fully managed service, Grafana Cloud is the fastest way to adopt
  Grafana and includes a scalable, managed backend for metrics, logs, and traces.
- Managed and administered by Grafana Labs with free and paid options for
  individuals, teams, and large enterprises.
- Includes a robust free tier with access to 10k metrics, 50GB logs, 50GB traces,
  50GB profiles, and 500VUh of k6 testing for 3 users.

```{div}
:style: "clear: both"
```
:::

:::{rubric} Learn
:::

:::{toctree}
:maxdepth: 1

learn
:::


```{seealso}
[CrateDB and Grafana]
```


[CrateDB and Grafana]: https://cratedb.com/integrations/cratedb-and-grafana
[Grafana Cloud]: https://grafana.com/grafana/
[Grafana Labs]: https://grafana.com/about/team/
[Grafana OSS]: https://grafana.com/oss/grafana/
