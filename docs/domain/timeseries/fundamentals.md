(timeseries-basics)=
# Time Series Fundamentals with CrateDB

## Getting Started

- [](#connect)
- [](#timeseries-generate)
- [](#timeseries-normalize)
- [Financial data collection and processing using pandas]
- [](#timeseries-analysis)
- [Load and visualize time series data using CrateDB, SQL, pandas, and Plotly](#plotly)
- [](project:#timeseries-querying)
- [](project:#timeseries-with-metadata)

::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**Notebook: How to Build Time Series Applications with CrateDB**

This notebook illustrates how to import and work with time series data in CrateDB.
It uses Dask to import data into CrateDB.
Dask is a framework to parallelize operations on pandas data frames.
 
{{ '{}[dask-weather-data-github]'.format(nb_github) }} {{ '{}[dask-weather-data-colab]'.format(nb_colab) }}
:::

:::{grid-item}
:columns: 3
{tags-primary}`Data I/O`

{tags-secondary}`Python`
{tags-secondary}`Dask`
{tags-secondary}`SQL`
:::

::::


## Downsampling and Interpolation

- [](#downsampling-timestamp-binning)
- [](#downsampling-lttb)
- [](#ni-interpolate)
- [Interpolating missing time series values]
- [](inv:crate-reference#aggregation-percentile)

## Operations
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



[CrateDB partitioned table vs. TimescaleDB Hypertable]: https://community.cratedb.com/t/cratedb-partitioned-table-vs-timescaledb-hypertable/1713
[dask-weather-data-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/timeseries/dask-weather-data-import.ipynb
[dask-weather-data-github]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/dask-weather-data-import.ipynb
[Financial data collection and processing using pandas]: https://community.cratedb.com/t/automating-financial-data-collection-and-storage-in-cratedb-with-python-and-pandas-2-0-0/916
[Interpolating missing time series values]: https://community.cratedb.com/t/interpolating-missing-time-series-values/1010
