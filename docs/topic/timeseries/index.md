(timeseries)=
# Time Series Data

:::{div} sd-text-muted
Learn how to use CrateDB for time series use cases.
:::

CrateDB is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries. It is
PostgreSQL-compatible, and based on Lucene. 

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2


:::{grid-item-card} {material-outlined}`show_chart;2em` Fundamentals
:link: timeseries-fundamentals
:link-type: ref
:link-alt: Time series fundamentals with CrateDB

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


:::{grid-item-card} {material-outlined}`school;2em` Academy » Advanced Time Series
:link: https://cratedb.com/academy/time-series/
:link-type: url
:link-alt: Academy Resources: Advanced Time Series

CrateDB Academy is a learning hub dedicated to empowering data enthusiasts with
the tools and knowledge to harness the power of CrateDB.
+++

**What's inside:**
Data manipulation and visualization. Data Storage. Importing.
Machine Learning on Time Series Data: EDA, Decomposition, AutoML.
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


::::


:::{seealso}

**Domains:**
[](#metrics-store) •
[](#analytics) •
[](#industrial) •
[](#machine-learning)

**Features:**
[](#connect) •
[](#querying) •
[](#document) •
[](#fulltext) •
[](#geospatial)

**Product:**
[Time Series Data] •
[White Paper: Guide for Time Series Data Projects]
:::


:::{toctree}
:hidden:

Fundamentals <fundamentals>
video
Long Term Store <longterm>
:::



[Time Series Data]: https://cratedb.com/data-model/time-series
[White Paper: Guide for Time Series Data Projects]: https://cratedb.com/resources/white-papers/lp-wp-time-series-guide
