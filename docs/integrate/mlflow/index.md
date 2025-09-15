(mlflow)=
# MLflow

```{div}
:style: "float: right; margin-left: 1em"
[![MLflow logo](https://github.com/crate/crate-clients-tools/assets/453543/d1d4f4ac-1b44-46b8-ba6f-4a82607c57d3){height=60px loading=lazy}][MLflow]
```
```{div}
:style: "clear: both"
```

:::{rubric} About
:::

[MLflow] is an open-source platform to manage the whole ML lifecycle, including
experimentation, reproducibility, deployment, and a central model registry.

The [MLflow adapter for CrateDB], available through the [mlflow-cratedb] package
on PyPI, provides support to use CrateDB as a storage database for the
[MLflow Tracking] subsystem, which is about recording and querying experiments,
across code, data, config, and results.

:::{rubric} Learn
:::
Tutorials and Notebooks about using [MLflow] together with CrateDB.

::::{info-card}
:::{grid-item}
:columns: 9
**Blog: Running Time Series Models in Production using CrateDB**

Part 1: Introduction to [Time Series Modeling using Machine Learning]

The article will introduce you to the concept of time series modeling,
discussing the main obstacles running it in production.
It will introduce you to CrateDB, highlighting its key features and
benefits, why it stands out in managing time series data, and why it is
an especially good fit for supporting machine learning models in production.
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Time Series Modeling`
:::
::::


::::{info-card}
:::{grid-item}
:columns: 9
**Notebook: Create a Time Series Anomaly Detection Model**

Guidelines and runnable code to get started with MLflow and
CrateDB, exercising time series anomaly detection and time series forecasting /
prediction using NumPy, Salesforce Merlion, and Matplotlib.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][MLflow and CrateDB]
[![Notebook on GitHub](https://img.shields.io/badge/Open-Notebook%20on%20GitHub-darkgreen?logo=GitHub)][tracking-merlion-github]
[![Notebook on Colab](https://img.shields.io/badge/Open-Notebook%20on%20Colab-blue?logo=Google%20Colab)][tracking-merlion-colab]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Time Series` \
{tags-secondary}`Anomaly Detection` \
{tags-secondary}`Prediction / Forecasting`
:::
::::


[MLflow]: https://mlflow.org/
[MLflow adapter for CrateDB]: https://github.com/crate/mlflow-cratedb
[MLflow and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/mlflow
[mlflow-cratedb]: https://pypi.org/project/mlflow-cratedb/
[MLflow Tracking]: https://mlflow.org/docs/latest/tracking.html
[Time Series Modeling using Machine Learning]: https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-machine-learning-time-series-data
[tracking-merlion-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/mlflow/tracking_merlion.ipynb
[tracking-merlion-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/mlflow/tracking_merlion.ipynb
