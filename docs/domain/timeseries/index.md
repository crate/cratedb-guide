(timeseries)=
# Time Series Data

Learn how to use CrateDB for time series use cases.

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


:::{grid-item-card} {material-outlined}`manage_history;2em` Long Term Storage
:link: timeseries-longterm
:link-type: ref
:link-alt: About storing time series data for the long term

Run efficient data operations for current and historical time series data.

+++
**What's inside:**
Time-based bucketing.
Import data using Dask.
Optimizing storage for historic time series data.
:::


:::{grid-item-card} {material-outlined}`smart_display;2em` Video Tutorials
:link: timeseries-video
:link-type: ref
:link-alt: Video tutorials about time series with CrateDB

Educational videos about time series data and CrateDB.
+++
**What's inside:**
Time series introduction. Importing, exporting,
and analyzing. Industrial applications.
:::

::::


:::{seealso}

**Features:**
[](#connect) •
[](#querying) •
[](#document) •
[](#fulltext) •
[](#geospatial)

**Domains:**
[](#metrics-store) •
[](#analytics) •
[](#industrial) •
[](#machine-learning)
:::


:::{toctree}
:hidden:

Fundamentals <fundamentals>
Advanced <advanced>
video
Long Term Store <longterm>
:::
