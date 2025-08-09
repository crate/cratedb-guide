(timeseries-longterm)=
(timeseries-long-term-storage)=
# Time Series Long Term Storage

CrateDB stores large volumes of data, keeping it accessible for querying
and insightful analysis, even considering historic data records.
**Never retire data just because your database can't handle the cardinality.**


:::{rubric} Use Cases and Tutorials
:::


::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**Optimizing storage for historic time series data**

This tutorial illustrates how to reduce table storage size by 80%,
by using arrays for time-based bucketing, a historical table having
a dedicated layout, and querying using the UNNEST table function.

{{ '{}[Optimizing storage for historic time series data]'.format(tutorial) }}
:::

:::{grid-item}
:columns: 3
{tags-primary}`Rich Time Series`
{tags-primary}`Storage Efficiency`

{tags-secondary}`SQL`
:::

::::


:::{rubric} Related
:::

::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**CrateDB as metrics and log data store for the long term**

Store and analyze high volumes of system monitoring information.
Read more about using CrateDB as [](#metrics-store).
:::

:::{grid-item}
:columns: 3
{tags-primary}`Long Term Storage`
{tags-primary}`Metrics`
{tags-primary}`Logging`
:::

::::


::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**CrateDB provides real-time analytics on raw data stored for the long term**

Keep massive amounts of data ready in the hot zone for analytics purposes.
Read more about using CrateDB for [](#analytics).
:::

:::{grid-item}
:columns: 3
{tags-primary}`Long Term Storage`
{tags-primary}`Real-Time Analytics`
:::

::::


:::{rubric} Applications
:::

::::{info-card}

:::{grid-item}
:columns: auto 8 8 8
**Storing and analyzing massive amounts of synoptic weather data**

Wetterdienst uses CrateDB for mass storage of weather data, allowing you to
query it efficiently. It provides access to data at more than ten canonical
sources of raw weather data from domestic weather agencies.

[![Wetterdienst Documentation](https://img.shields.io/badge/Documentation-Data%20Export-darkgreen?logo=Markdown)](https://wetterdienst.readthedocs.io/en/latest/usage/python-api.html#export)
[![Wetterdienst Project](https://img.shields.io/badge/Repository-Wetterdienst-darkblue?logo=GitHub)](https://github.com/earthobservations/wetterdienst)
:::

:::{grid-item}
:columns: 4
{tags-primary}`Earth Observations`
{tags-primary}`Metadata`
{tags-primary}`Sensor Data`
{tags-primary}`Rich Time Series`

{tags-secondary}`pandas`
{tags-secondary}`Polars`
{tags-secondary}`SQL`
:::

::::



[Optimizing storage for historic time series data]: https://community.cratedb.com/t/optimizing-storage-for-historic-time-series-data/762
