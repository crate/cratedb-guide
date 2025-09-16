(timeseries-basics)=
(timeseries-fundamentals)=
# Time Series Fundamentals with CrateDB

:::{div} sd-text-muted
Learn how to conduct fundamental data analysis on large time series datasets
with CrateDB.
:::

{tags-primary}`Metadata integration`
{tags-primary}`Advanced SQL for time series`

:::{include} /_include/links.md
:::

## Getting Started

After evaluating [connectivity options](#connect), you would like to get
hands-on with CrateDB. We prepared a few introductory tutorials, some of
them in executable forms, to demonstrate CrateDB's features to work with
time series data on the spot. You may want to use them as starting points
for your own explorations.

:::{include} /_include/card/timeseries-intro.md
:::

:::{include} /_include/card/timeseries-explore.md
:::

:::{include} /_include/card/timeseries-datashader.md
:::

:::{include} /_include/card/timeseries-dask.md
:::


## Special Features
Working with time series data needs special feature support to enable
fluent data workflows.

:::{rubric} Downsampling and Interpolation
:::
- [](#downsampling-timestamp-binning)
- [](#downsampling-lttb)
- [](#ni-interpolate)
- [Interpolating missing time series values]
- [](inv:crate-reference#aggregation-percentile)

## Operations
CrateDB provides operational support to store and query large time series data
efficiently.
- [](#sharding-partitioning)
- [CrateDB partitioned table vs. TimescaleDB Hypertable]


:::{tip}
For more in-depth information, please visit the documentation pages about
[](#timeseries-advanced). Alternatively, you
may prefer the [](#timeseries-video).
:::


:::{toctree}
:hidden:

generate/index
learn/normalize-pandas
learn/query
learn/with-metadata
:::

:::{todo}
Outdated: [](#timeseries-generate), [](#timeseries-normalize), [Financial data collection and processing using pandas]
:::


[CrateDB partitioned table vs. TimescaleDB Hypertable]: https://community.cratedb.com/t/cratedb-partitioned-table-vs-timescaledb-hypertable/1713
[Financial data collection and processing using pandas]: https://community.cratedb.com/t/automating-financial-data-collection-and-storage-in-cratedb-with-python-and-pandas-2-0-0/916
[Interpolating missing time series values]: https://community.cratedb.com/t/interpolating-missing-time-series-values/1010
