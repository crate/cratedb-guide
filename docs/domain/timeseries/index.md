(timeseries)=
# Time Series Data

Learn how to optimally use CrateDB for time series use-cases.

CrateDB is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries. It is
PostgreSQL-compatible, and based on Lucene. 


```{include} /_include/styles.html
```

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2


:::{grid-item-card} {material-outlined}`show_chart;2em` Basics
:link: timeseries-basics
:link-type: ref
:link-alt: Time series basics with CrateDB

Basic introductory tutorials about using CrateDB with time series data.
+++
**What's inside:**
Getting Started, Downsampling and Interpolation,
Operations: Sharding and Partitioning.
:::


:::{grid-item-card} {material-outlined}`analytics;2em` Advanced
:link: timeseries-analysis
:link-type: ref
:link-alt: About time series analysis

Advanced time series data analysis with CrateDB.
+++
**What's inside:**
Exploratory data analysis (EDA), time series decomposition,
anomaly detection, forecasting.
:::


:::{grid-item-card} {material-outlined}`sync;2em` Import and Export
:link: timeseries-io
:link-type: ref
:link-alt: About time series data import and export

Import data into and export data from your CrateDB cluster.
+++
**What's inside:**
Connectivity and integration options with database drivers
and applications, libraries, and frameworks.
:::


:::{grid-item-card} {material-outlined}`smart_display;2em` Video
:link: timeseries-video
:link-type: ref
:link-alt: Video tutorials about time series with CrateDB

Video tutorials about time series data and CrateDB.
+++
**What's inside:**
Time series introduction. Importing, exporting,
and analyzing. Industrial applications.
:::

::::


:::{toctree}
:hidden:

Basics <basics>
Advanced <advanced>
Connectivity <connect>
video
:::
