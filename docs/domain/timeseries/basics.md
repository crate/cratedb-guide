(timeseries-basics)=
# Time Series Basics with CrateDB

## Getting Started

- [](#timeseries-generate)
- [](#timeseries-normalize)
- [Financial data collection and processing using pandas]
- [](inv:cloud#time-series)
- [Load and visualize time series data using CrateDB, SQL, pandas, and Plotly](#plotly)
- [How to Build Time Series Applications with CrateDB]

## Downsampling and Interpolation

- [](#downsampling-timestamp-binning)
- [](#downsampling-lttb)
- [](#ni-interpolate)
- [Interpolating missing time series values]
- [](inv:crate-reference#aggregation-percentile)

## Machine Learning

- [](#timeseries-ml-primer)
- [Machine Learning Integrations](#integrate-machine-learning)

## Operations
- [](#sharding-partitioning)
- [CrateDB partitioned table vs. TimescaleDB Hypertable]


:::{tip}
For more in-depth information, please visit the documentation pages about
[](#timeseries-connect) and [](#timeseries-advanced). Alternatively, you
may prefer the [](#timeseries-video).
:::


:::{toctree}
:hidden:

generate/index
normalize-intervals
:::



[CrateDB partitioned table vs. TimescaleDB Hypertable]: https://community.cratedb.com/t/cratedb-partitioned-table-vs-timescaledb-hypertable/1713
[Financial data collection and processing using pandas]: https://community.cratedb.com/t/automating-financial-data-collection-and-storage-in-cratedb-with-python-and-pandas-2-0-0/916
[How to Build Time Series Applications with CrateDB]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/dask-weather-data-import.ipynb
[Interpolating missing time series values]: https://community.cratedb.com/t/interpolating-missing-time-series-values/1010