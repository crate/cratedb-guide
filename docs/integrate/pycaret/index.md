(pycaret)=
# PyCaret

```{div}
:style: "float: right; margin-left: 1em"
[![PyCaret logo](https://github.com/crate/crate-clients-tools/assets/453543/b17a59e2-6801-4f53-892f-ff472491095f){w=180px}](https://pycaret.org/)
```
```{div}
:style: "clear: both"
```

:::{rubric} About
:::

[PyCaret] is an open-source, low-code machine learning library for Python that
automates machine learning workflows.

It is a high-level interface and AutoML wrapper on top of your loved machine learning
libraries like scikit-learn, XGBoost, Ray, LightGBM, and many more. PyCaret provides a
universal interface to utilize these libraries without needing to know the details
of the underlying model architectures and parameters.

:::{rubric} Concept
:::

The general concept of PyCaret—and, in fact, of AutoML in general—is straightforward:
take raw data, split it into training and test sets, train multiple models on the
training set, evaluate on the test set, and select the best‑performing model.

:::{rubric} Hyperparameter tuning
:::

This process gets repeated for tuning the hyperparameters of the best models.
Again, this process is highly empirical. The parameters are changed, the model is
retrained and evaluated again. This process is repeated until the best performing
parameters are found.

Common approaches include Grid Search, Random Search, and Bayesian Optimization.
For a quick introduction to these methods, see [Introduction to hyperparameter tuning].

:::{rubric} Benefits
:::

In the past, all these trial-and-error experiments had to be done manually,
which is a tedious and time-consuming task. PyCaret automates this process
and provides a simple interface to execute all these experiments in a
straightforward way. The notebooks referenced below demonstrate how this works.

:::{rubric} Learn
:::

Tutorials and Notebooks about using [PyCaret] together with CrateDB.

::::{info-card}
:::{grid-item}
:columns: 9
**Notebook: AutoML classification with PyCaret**

Explore the PyCaret framework and show how to use it to train different
classification models.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][AutoML with PyCaret and CrateDB]
[![Notebook on GitHub](https://img.shields.io/badge/Open-Notebook%20on%20GitHub-darkgreen?logo=GitHub)][automl-classify-github]
[![Notebook on Colab](https://img.shields.io/badge/Open-Notebook%20on%20Colab-blue?logo=Google%20Colab)][automl-classify-colab]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Classification`
:::
::::

::::{info-card}
:::{grid-item}
:columns: 9
**Notebook: Train time series forecasting models**

How to train time series forecasting models using PyCaret and CrateDB.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][AutoML with PyCaret and CrateDB]
[![Notebook on GitHub](https://img.shields.io/badge/Open-Notebook%20on%20GitHub-darkgreen?logo=GitHub)][automl-forecasting-github]
[![Notebook on Colab](https://img.shields.io/badge/Open-Notebook%20on%20Colab-blue?logo=Google%20Colab)][automl-forecasting-colab]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Time Series` \
{tags-secondary}`Prediction / Forecasting`
:::
::::


[AutoML with PyCaret and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/pycaret
[automl-classify-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/pycaret/automl_classification_with_pycaret.ipynb
[automl-classify-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/pycaret/automl_classification_with_pycaret.ipynb
[automl-forecasting-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/pycaret/automl_timeseries_forecasting_with_pycaret.ipynb
[automl-forecasting-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/pycaret/automl_timeseries_forecasting_with_pycaret.ipynb
[Introduction to hyperparameter tuning]: https://medium.com/analytics-vidhya/comparison-of-hyperparameter-tuning-algorithms-grid-search-random-search-bayesian-optimization-5326aaef1bd1
[PyCaret]: https://www.pycaret.org
