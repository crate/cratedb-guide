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

:::{include} /_include/links.md
:::

(timeseries-anomaly-forecasting)=
## Anomaly Detection and Forecasting

To gain insights from your data in a one-shot or recurring way, based on
machine learning techniques, you may want to look into applying [anomaly]
detection and/or [forecasting] methods.

:::{rubric} Examples
:::

::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**Use MLflow for time series anomaly detection and time series forecasting**

Guidelines and runnable code to get started with [MLflow] and CrateDB, exercising
time series anomaly detection and time series forecasting / prediction using
NumPy, Merlion, and Matplotlib.

{{ '{}[MLflow and CrateDB]'.format(readme_github) }} {{ '{}[forecasting-merlion-github]'.format(nb_github) }} {{ '{}[forecasting-merlion-colab]'.format(nb_colab) }}
:::

:::{grid-item}
:columns: 3
{tags-primary}`Anomaly Detection`
{tags-primary}`Forecasting / Prediction`

{tags-secondary}`Python`
{tags-secondary}`MLflow`
:::

::::


::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**Use PyCaret to train time series forecasting models**

This notebook explores the [PyCaret] framework and shows how to use it
to train various time series forecasting models.

{{ '{}[MLflow and CrateDB]'.format(readme_github) }} {{ '{}[forecasting-pycaret-github]'.format(nb_github) }} {{ '{}[forecasting-pycaret-colab]'.format(nb_colab) }}
:::

:::{grid-item}
:columns: 3

{tags-primary}`Forecasting / Prediction`

{tags-secondary}`Python`
{tags-secondary}`PyCaret`
{tags-secondary}`MLflow`
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

:::{grid-item}
:columns: auto 9 9 9
**Analyze trend, seasonality, and fluctuations with PyCaret and CrateDB**

Learn how to extract data from CrateDB for analysis in PyCaret, how to
further preprocess it and how to use PyCaret to plot time series
decomposition by breaking it down into its basic components: trend,
seasonality, and residual (or irregular) fluctuations.

{{ '{}[timeseries-decomposition-github]'.format(nb_github) }} {{ '{}[timeseries-decomposition-colab]'.format(nb_colab) }}
:::

:::{grid-item}
:columns: 3
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

:::{grid-item}
:columns: auto 9 9 9
**Exploratory data analysis (EDA) with PyCaret and CrateDB**

Learn how to access time series data from CrateDB using SQL, and how to apply
exploratory data analysis (EDA) with PyCaret.

The notebook shows how to generate various plots and charts for EDA, helping
you to understand data distributions, relationships between variables, and to
identify patterns.

{{ '{}[timeseries-eda-github]'.format(nb_github) }} {{ '{}[timeseries-eda-colab]'.format(nb_colab) }}
:::

:::{grid-item}
:columns: 3
{tags-primary}`EDA on time series`

{tags-secondary}`Python`
{tags-secondary}`PyCaret`
:::

::::


(timeseries-analysis-metadata)=
## Metadata Integration

CrateDB is particularly effective when you need to combine time series data
with metadata, for instance, in scenarios where data like sensor readings
or log entries, need to be augmented with additional context for more
insightful analysis. See also [](#document).

CrateDB supports effective time series analysis with fast aggregations, a
rich set of built-in functions, and [JOIN](inv:crate-reference#sql_joins)
operations.

:::{rubric} Examples
:::

::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**Analyzing Device Readings with Metadata Integration**

This tutorial illustrates how to augment time series data with metadata, in
order to enable more comprehensive analysis. It uses a time series dataset that
captures various device readings, such as battery, CPU, and memory information.

{{ '{}(#timeseries-objects)'.format(tutorial) }}
:::

:::{grid-item}
:columns: 3

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

:::{grid-item}
:columns: 9
**Analyzing Weather Data**

Run aggregations with gap filling / interpolation, using common
table expressions (CTEs) and LAG / LEAD window functions.

Find maximum values using the MAX_BY aggregate function, returning
the value from one column based on the maximum or minimum value of another
column within a group.

{{ '{}(#timeseries-analysis-weather)'.format(tutorial) }}
:::

:::{grid-item}
:columns: 3

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

:::{include} /_include/card/timeseries-explore.md
:::

:::{include} /_include/card/timeseries-datashader.md
:::



[anomaly]: https://en.wikipedia.org/wiki/Anomaly_(natural_sciences)
[Data and information visualization]: https://en.wikipedia.org/wiki/Data_and_information_visualization
[Decomposition of time series]: https://en.wikipedia.org/wiki/Decomposition_of_time_series
[Exploratory data analysis (EDA)]: https://en.wikipedia.org/wiki/Exploratory_data_analysis
[forecasting]: https://en.wikipedia.org/wiki/Forecasting
[forecasting-merlion-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb
[forecasting-merlion-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb
[forecasting-pycaret-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb
[forecasting-pycaret-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb
[MLflow]: https://mlflow.org/
[MLflow and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/mlops-mlflow
[PyCaret]: https://www.pycaret.org
[Time series]: https://en.wikipedia.org/wiki/Time_series
[timeseries-decomposition-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/timeseries/time-series-decomposition.ipynb
[timeseries-decomposition-github]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/time-series-decomposition.ipynb
[timeseries-eda-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/timeseries/exploratory_data_analysis.ipynb
[timeseries-eda-github]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/exploratory_data_analysis.ipynb
