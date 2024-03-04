(visualization)=

# Data Visualization

Guidelines about data analysis and visualization with CrateDB.


## Apache Superset / Preset

**Product**
- [Introduction to time series visualization in CrateDB and Apache Superset (Blog)]
- [Use CrateDB and Apache Superset for Open Source Data Warehousing and Visualization (Blog)]
- [Introduction to time series visualization in CrateDB and Apache Superset (Webinar)]
- [Introduction to time series Visualization in CrateDB and Apache Superset (Preset.io)]

**Development**
- [Set up Apache Superset with CrateDB]
- [Set up an Apache Superset development sandbox with CrateDB]
- [Verify Apache Superset with CrateDB]


## Cluvio

- [Data Analysis with Cluvio and CrateDB]


## Explo

- [Introduction to Time Series Visualization in CrateDB and Explo]


## Grafana

- [Using Grafana with CrateDB Cloud]


(datashader)=
## hvPlot and Datashader

The `cloud-datashader.ipynb` notebook explores the [HoloViews] and [Datashader] frameworks
and outlines how to use them to plot the venerable NYC Taxi dataset, after importing it
into a CrateDB Cloud database cluster.

🚧 _Please note this notebook is a work in progress._ 🚧

[![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkblue?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/amo/cloud-datashader/topic/timeseries/explore/cloud-datashader.ipynb) [![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/amo/cloud-datashader/topic/timeseries/explore/cloud-datashader.ipynb)


## Metabase

- [Using Metabase with CrateDB Cloud]
- [Real-time data analytics with Metabase and CrateDB]


## pandas

- [From data storage to data analysis\: Tutorial on CrateDB and pandas]


(plotly)=
## Plotly / Dash

- The `timeseries-queries-and-visualization.ipynb` notebook explores how to access
  time series data from CrateDB via SQL, load it into pandas DataFrames, and visualize
  it using Plotly.

  It includes advanced time series operations in SQL, like aggregations, window functions,
  interpolation of missing data, common table expressions, moving averages, JOINs, and
  the handling of JSON data.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkblue?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/timeseries-queries-and-visualization.ipynb) [![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/timeseries/timeseries-queries-and-visualization.ipynb)

- Alternatively, you are welcome to explore the canonical [Dash Examples].



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
[Datashader]: https://datashader.org/
[From data storage to data analysis\: Tutorial on CrateDB and pandas]: https://community.cratedb.com/t/from-data-storage-to-data-analysis-tutorial-on-cratedb-and-pandas/1440
[HoloViews]: https://www.holoviews.org/
[Introduction to Time Series Visualization in CrateDB and Explo]: https://cratedb.com/blog/introduction-to-time-series-visualization-in-cratedb-and-explo
[Introduction to time series visualization in CrateDB and Apache Superset (Blog)]: https://community.cratedb.com/t/introduction-to-time-series-visualization-in-cratedb-and-superset/1041
[Introduction to time series visualization in CrateDB and Apache Superset (Webinar)]: https://cratedb.com/resources/webinars/lp-wb-introduction-to-time-series-visualization-in-cratedb-apache-superset
[Introduction to time series Visualization in CrateDB and Apache Superset (Preset.io)]: https://preset.io/blog/timeseries-cratedb-superset/
[Real-time data analytics with Metabase and CrateDB]: https://www.metabase.com/community_posts/real-time-data-analytics-with-metabase-and-cratedb
[Set up Apache Superset with CrateDB]: https://community.cratedb.com/t/set-up-apache-superset-with-cratedb/1716
[Set up an Apache Superset development sandbox with CrateDB]: https://community.cratedb.com/t/set-up-an-apache-superset-development-sandbox-with-cratedb/1163
[Time Series with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/timeseries/explore
[Use CrateDB and Apache Superset for Open Source Data Warehousing and Visualization (Blog)]: https://cratedb.com/blog/use-cratedb-and-apache-superset-for-open-source-data-warehousing-and-visualization
[Using Grafana with CrateDB Cloud]: #integrations-grafana
[Using Metabase with CrateDB Cloud]: #integrations-metabase
[Verify Apache Superset with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/application/apache-superset
