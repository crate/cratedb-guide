(timeseries-basics)=
(timeseries-fundamentals)=
# Time series fundamentals with CrateDB

:::{div} sd-text-muted
Learn how to conduct fundamental data analysis on large time series datasets
with CrateDB.
:::

{tags-primary}`Metadata integration`
{tags-primary}`Advanced SQL for time series`

:::{include} /_include/links.md
:::

## Getting started

After evaluating {ref}`connectivity options <connect>`, you would like to get
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


## Special features
Working with time series data often requires special feature support to enable
fluent data workflows.

- {ref}`downsampling-timestamp-binning`
- {ref}`downsampling-lttb`
- {ref}`ni-interpolate`
- [Interpolating missing time series values]
- {ref}`crate-reference:aggregation-percentile`


(timeseries-analysis-ml)=
## Time series analysis

Analyze time series data with statistical and machine learning techniques,
for time series anomaly detection and forecasting.

::::{grid} 2
:gutter: 3

:::{grid-item-card} Statistical analysis and visualization on huge datasets
:link: r-tutorial
:link-type: ref
Learn how to create a machine learning pipeline using R and CrateDB.
:::

:::{grid-item-card} Regression analysis with pandas and scikit-learn
:link: scikit-learn
:link-type: ref
Use pandas and scikit-learn to run a regression analysis within a Jupyter Notebook.
:::

:::{grid-item-card} Build model for predictive maintenance with TensorFlow
:link: tensorflow-tutorial
:link-type: ref
Learn how to build a machine learning model that will predict whether
a machine will fail within a specified time window in the future.
:::

:::{grid-item-card} Advanced time series analysis
:link: ml-timeseries
:link-type: ref
Learn how to conduct advanced data analysis on large time series datasets
with CrateDB, MLflow, and PyCaret:
Anomaly detection and forecasting, time series decomposition,
Exploratory data analysis (EDA).
:::

::::

## Big data operations

CrateDB clusters can elastically scale to store and query large time
series data efficiently. CrateDB provides corresponding operational support.
- {ref}`sharding-partitioning`
- [CrateDB partitioned table vs. TimescaleDB Hypertable]

## See also

- {ref}`timeseries-analysis-advanced`
- {ref}`timeseries-video`


:::{toctree}
:hidden:
generate/index
learn/normalize-pandas
learn/query
learn/with-metadata
:::


[CrateDB partitioned table vs. TimescaleDB Hypertable]: https://community.cratedb.com/t/cratedb-partitioned-table-vs-timescaledb-hypertable/1713
[Interpolating missing time series values]: https://community.cratedb.com/t/interpolating-missing-time-series-values/1010
