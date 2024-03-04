(timeseries-advanced)=
(timeseries-analysis)=

# Advanced Time Series Analysis

Learn how to conduct advanced data analysis on large time series datasets
with CrateDB.

{tags-primary}`Anomaly detection`
{tags-primary}`Forecasting / Prediction`
{tags-primary}`Time series decomposition`
{tags-primary}`Exploratory data analysis`
{tags-primary}`Metadata integration`


<style>
.wrapper-content-right img {
  margin-bottom: 0 !important;
}
</style>


:::{contents}
:local:
:depth: 2
:::


(timeseries-anomaly-forecasting)=
## Anomaly Detection and Forecasting

To gain insights from your data in a one-shot or recurring way, based on
machine learning techniques, you may want to look into applying [anomaly]
detection and/or [forecasting] methods.

:::{rubric} Examples
:::

::::{info-card}

:::{grid-item} **Use MLflow for time series anomaly detection and timeseries forecasting**
:columns: 9

Guidelines and runnable code to get started with [MLflow] and CrateDB, exercising
time series anomaly detection and timeseries forecasting / prediction using
NumPy, Merlion, and Matplotlib.
:::

:::{grid-item}
:columns: 3

[![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkblue?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb)
[![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb)

{tags-primary}`Anomaly Detection`
{tags-primary}`Forecasting / Prediction`

{tags-secondary}`Python`
{tags-secondary}`MLflow`
:::

::::


::::{info-card}

:::{grid-item} **Use PyCaret to train time series forecasting models**
:columns: 9

This notebook explores the [PyCaret] framework and shows how to use it
to train various timeseries forecasting models.
:::

:::{grid-item}
:columns: 3

[![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkblue?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb)
[![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb)

{tags-primary}`Forecasting / Prediction`

{tags-secondary}`Python`
{tags-secondary}`PyCaret`
:::

::::


(timeseries-decomposition)=
## Time Series Decomposition

[Decomposition of time series] is a statistical task that deconstructs a [time
series] into several components, each representing one of the underlying
categories of patterns.

There are two principal types of decomposition, one based on rates of change,
the other based on predictability.

You can use this method to dissect a time series into multiple components,
typically including trend, seasonal, and random (or irregular) components.

This process helps in understanding the underlying patterns of the time series
data, such as identifying any long term direction (trend), recurring patterns
at fixed intervals (seasonality), and randomness (irregular fluctuations) in
the data.

Decomposition is crucial for analyzing how these components change over time,
improving forecasts, and developing strategies for addressing each element
effectively.

:::{rubric} Examples
:::

::::{info-card}

:::{grid-item} **Analyze trend, seasonality, and fluctuations with PyCaret and CrateDB**
:columns: 9

Learn how to extract data from CrateDB for analysis in PyCaret, how to
further preprocess it and how to use PyCaret to plot time series
decomposition by breaking it down into its basic components: trend,
seasonality, and residual (or irregular) fluctuations.
:::

:::{grid-item}
:columns: 3

[![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkblue?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/time-series-decomposition.ipynb)
[![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/timeseries/time-series-decomposition.ipynb)

{tags-primary}`Time series decomposition`

{tags-secondary}`Python`
{tags-secondary}`PyCaret`
:::

::::


(timeseries-eda)=
## Exploratory data analysis (EDA)

[Exploratory data analysis (EDA)] is an approach of analyzing data sets to
summarize their main characteristics, often using statistical graphics and
other data visualization methods.

EDA involves visualizing, summarizing, and analyzing data, to uncover
patterns, anomalies, or relationships within the dataset.

The objective of this step is to gain an understanding and intuition of the
data, identify potential issues, and, in machine learning, guide feature
engineering and model building.

:::{rubric} Examples
:::

::::{info-card}

:::{grid-item} **Exploratory data analysis (EDA) with PyCaret and CrateDB**
:columns: 9

Learn how to access time series data from CrateDB using SQL, and how to apply
exploratory data analysis (EDA) with PyCaret.

The notebook shows how to generate various plots and charts for EDA, helping
you to understand data distributions, relationships between variables, and to
identify patterns.
:::

:::{grid-item}
:columns: 3

[![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkblue?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/exploratory_data_analysis.ipynb)
[![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/timeseries/exploratory_data_analysis.ipynb)

{tags-primary}`EDA on time series`

{tags-secondary}`Python`
{tags-secondary}`PyCaret`
:::

::::


(timeseries-long-term-storage)=
## Long Term Storage

CrateDB stores large volumes of data, keeping it accessible for querying
and insightful analysis, even considering historic data records.
**Never retire data just because your database can't handle the cardinality.**

:::{rubric} Applications
:::

::::{info-card}

:::{grid-item} **Storing and analyzing massive amounts of synoptic weather data**
:columns: 8

Wetterdienst uses CrateDB for mass storage of weather data, allowing you to
query it efficiently. It provides access to data at more than ten canonical
sources of raw weather data from domestic weather agencies.
:::

:::{grid-item}
:columns: 4

[![Wetterdienst Documentation](https://img.shields.io/badge/Documentation-Wetterdienst%20Export-darkyellow?logo=Markdown)](https://wetterdienst.readthedocs.io/en/latest/usage/python-api.html#export)
[![Wetterdienst Project](https://img.shields.io/badge/Repository-Wetterdienst-darkblue?logo=GitHub)](https://github.com/earthobservations/wetterdienst)

{tags-primary}`Earth Observations`
{tags-primary}`Metadata`
{tags-primary}`Sensor Data`
{tags-primary}`Rich Time Series`

{tags-secondary}`pandas`
{tags-secondary}`Polars`
{tags-secondary}`SQL`
:::

::::


:::{rubric} Use Cases
:::


::::{info-card}

:::{grid-item} **CrateDB as metrics and log data store for the long term**
:columns: 8

Store and analyze high volumes of system monitoring information.
:::

:::{grid-item}
:columns: 4

[](#metrics-store)

{tags-primary}`Long Term Storage`
{tags-primary}`Metrics`
{tags-primary}`Logging`
:::

::::


::::{info-card}

:::{grid-item} **CrateDB provides real-time analytics on raw data stored for the long term**
:columns: 8

Keep massive amounts of data ready in the hot zone for analytics purposes.
:::

:::{grid-item}
:columns: 4

[](#analytics)

{tags-primary}`Long Term Storage`
{tags-primary}`Real-Time Analytics`
:::

::::


(timeseries-analysis-metadata)=
## Metadata Integration

CrateDB is particularly effective when you need to combine time-series data
with metadata, for instance, in scenarios where data like sensor readings
or log entries, need to be augmented with additional context for more
insightful analysis. See also [](#document).

CrateDB supports effective time-series analysis with fast aggregations, a
rich set of built-in functions, and [JOIN](inv:crate-reference#sql_joins)
operations.

:::{rubric} Examples
:::

::::{info-card}

:::{grid-item} **Analyzing Device Readings with Metadata Integration**
:columns: 9

This tutorial illustrates how to augment time-series data with metadata, in
order to enable more comprehensive analysis. It uses a time-series dataset that
captures various device readings, such as battery, CPU, and memory information. 
:::

:::{grid-item}
:columns: 3

[![Navigate to Tutorial](https://img.shields.io/badge/Navigate%20to-Tutorial-lightgray?logo=Markdown)](#timeseries-objects)

{tags-primary}`Rich Time Series`
{tags-primary}`Metadata`

{tags-secondary}`SQL`
:::

::::


(timeseries-analysis-sql)=
## SQL Analysis

CrateDB offers enhanced features for analysing time series data.

**Examples**

::::{info-card}

:::{grid-item} **Analyzing Weather Data**
:columns: 9

Run aggregations with gap filling / interpolation, using common
table expressions (CTEs) and LAG / LEAD window functions.

Find maximum values using the MAX_BY aggregate function, returning
the value from one column based on the maximum or minimum value of another
column within a group.
:::

:::{grid-item}
:columns: 3

[![Navigate to Tutorial](https://img.shields.io/badge/Navigate%20to-Tutorial-lightgray?logo=Markdown)](#timeseries-analysis-weather)

{tags-primary}`Aggregations`
{tags-primary}`Time series`

{tags-secondary}`SQL`
:::

::::


(timeseries-visualization)=
## Visualization

Similar to EDA, just applying [data and information visualization] can yield
significant insights into the characteristics of your data. By using
best-of-breed data visualization tools, initial data exploration is
mostly your first encounter with the data.

:::{rubric} Examples
:::

::::{info-card}

:::{grid-item} **Display millions of data points using hvPlot, Datashader, and CrateDB**
:columns: 9

[HoloViews] and [Datashader] frameworks enable channeling millions of data
points from your backend systems to the browser's glass.

This notebook plots the venerable NYC Taxi dataset after importing it
into a CrateDB Cloud database cluster.

🚧 _Please note this notebook is a work in progress._ 🚧
:::

:::{grid-item}
:columns: 3

[![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkblue?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/amo/cloud-datashader/topic/timeseries/explore/cloud-datashader.ipynb)
[![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/amo/cloud-datashader/topic/timeseries/explore/cloud-datashader.ipynb)

{tags-primary}`Time series visualization`

{tags-secondary}`Python`
{tags-secondary}`HoloViews`
{tags-secondary}`hvPlot`
{tags-secondary}`Datashader`
:::

::::



[anomaly]: https://en.wikipedia.org/wiki/Anomaly_(natural_sciences)
[Data and information visualization]: https://en.wikipedia.org/wiki/Data_and_information_visualization
[Datashader]: https://datashader.org/
[Decomposition of time series]: https://en.wikipedia.org/wiki/Decomposition_of_time_series
[Exploratory data analysis (EDA)]: https://en.wikipedia.org/wiki/Exploratory_data_analysis
[forecasting]: https://en.wikipedia.org/wiki/Forecasting
[HoloViews]: https://www.holoviews.org/
[MLflow]: https://mlflow.org/
[PyCaret]: https://www.pycaret.org
[Time series]: https://en.wikipedia.org/wiki/Time_series
