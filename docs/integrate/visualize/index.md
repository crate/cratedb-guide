(visualization)=

# Data Visualization

Guidelines about data analysis and visualization with CrateDB.

:::{include} /_include/links.md
:::


:::{toctree}
:maxdepth: 1

../apache-superset/index
:::


## Cluvio

- [Data Analysis with Cluvio and CrateDB]


## Explo

- [Introduction to Time Series Visualization in CrateDB and Explo]


## Grafana

- {ref}`integrations-grafana`


(datashader)=
## hvPlot and Datashader

:::{include} /_include/card/timeseries-datashader.md
:::


## Metabase

- {ref}`integrations-metabase`
- [Real-time data analytics with Metabase and CrateDB]
- https://github.com/paoliniluis/metabase-cratedb


## pandas

- [From data storage to data analysis\: Tutorial on CrateDB and pandas]


(plotly)=
## Plotly / Dash

:::{include} /_include/card/timeseries-explore.md
:::

Alternatively, you are welcome to explore the canonical [Dash Examples].



## R

```{toctree}
:maxdepth: 1

r
```


```{toctree}
:hidden:

grafana
metabase
```


[Dash Examples]: https://plotly.com/examples/
[Data Analysis with Cluvio and CrateDB]: https://community.cratedb.com/t/data-analysis-with-cluvio-and-cratedb/1571
[From data storage to data analysis\: Tutorial on CrateDB and pandas]: https://community.cratedb.com/t/from-data-storage-to-data-analysis-tutorial-on-cratedb-and-pandas/1440
[Introduction to Time Series Visualization in CrateDB and Explo]: https://cratedb.com/blog/introduction-to-time-series-visualization-in-cratedb-and-explo
[Real-time data analytics with Metabase and CrateDB]: https://www.metabase.com/community_posts/real-time-data-analytics-with-metabase-and-cratedb
[Time Series with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/timeseries/explore
[Using Grafana with CrateDB Cloud]: #integrations-grafana
[Using Metabase with CrateDB Cloud]: #integrations-metabase
