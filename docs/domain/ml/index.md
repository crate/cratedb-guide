(ml)=
(machine-learning)=

# Machine Learning

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::

Integrate CrateDB with machine learning frameworks and
tools, for MLOps and vector database operations.

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: 6

:::{rubric} Machine Learning Operations
:::
Training a machine learning model, running it in production, and maintaining
it, requires a significant amount of data processing and bookkeeping
operations.

CrateDB, as a universal SQL database, supports this process through
adapters to best-of-breed software components for MLOps procedures.

[MLOps] is a paradigm that aims to deploy and maintain machine learning models
in production reliably and efficiently, including experiment tracking, and in
the spirit of continuous development and DevOps.
::::

::::{grid-item}
:class: rubric-slimmer
:columns: 6

:::{rubric} Vector Store
:::
CrateDB's FLOAT_VECTOR data type implements a vector store and the k-nearest
neighbour (kNN) search algorithm to find vectors that are similar to a query
vector.

These feature vectors may be computed from raw data using machine learning
methods such as feature extraction algorithms, word embeddings, or deep
learning networks. 

[Vector databases][Vector Database] can be used for similarity search, multi-modal search,
recommendation engines, large language models (LLMs), retrieval-augmented
generation (RAG), and other applications.
::::

:::::


## Anomaly Detection and Forecasting


(mlflow)=
### MLflow

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


(pycaret)=
### PyCaret

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
{tags-secondary}`Time Series` \
{tags-secondary}`Anomaly Detection` \
{tags-secondary}`Prediction / Forecasting`
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
{tags-secondary}`Training` \
{tags-secondary}`Classification` \
{tags-secondary}`Forecasting`
:::
::::


(iris-r)=
### R

Use R with CrateDB.

:::::{info-card}
::::{grid-item}
:columns: 9
**Statistical analysis and visualization on huge datasets**

Details about how to create a machine learning pipeline
using R and CrateDB.

:::{toctree}
:maxdepth: 1

r
:::

::::
::::{grid-item}
:columns: 3
{tags-primary}`Fundamentals`
::::
:::::


(scikit-learn)=
### scikit-learn

Use [scikit-learn] with CrateDB.

::::{info-card}
:::{grid-item}
:columns: 9
**Regression analysis with pandas and scikit-learn**

Use [pandas] and [scikit-learn] to run a regression analysis within a
[Jupyter Notebook].

- [Machine Learning and CrateDB: An introduction]
- [Machine Learning and CrateDB: Getting Started With Jupyter]
- [Machine Learning and CrateDB: Experiment Design & Linear Regression]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Regression Analysis`
:::
::::


(tensorflow)=
### TensorFlow

Use [TensorFlow] with CrateDB.

::::{info-card}
:::{grid-item}
:columns: 9
**Predictive Maintenance**

Build a machine learning model that will predict whether a machine will
fail within a specified time window in the future.

- {doc}`./tensorflow`
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Prediction`
:::
::::


## LLMs / RAG

One of the most powerful applications enabled by LLMs is sophisticated
question-answering (Q&A) chatbots.
These are applications that can answer questions about specific sources
of information, using a technique known as Retrieval Augmented Generation,
or RAG. RAG is a technique for augmenting LLM knowledge with additional data.


:::{rubric} Video Tutorials
:::

::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**How to Use Private Data in Generative AI**

In this video recorded at FOSDEM 2024, we explain how to leverage private data
in generative AI on behalf of an end-to-end Retrieval Augmented Generation (RAG)
solution.

- [How to Use Private Data in Generative AI] (Video)
- [End-to-End RAG with CrateDB and LangChain] (Slides)
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/icquKckM4o0?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Fundamentals` \
{tags-secondary}`Generative AI`
{tags-secondary}`RAG`
:::

::::


(ml-langchain)=
### LangChain

:::{toctree}
:maxdepth: 1

../../integrate/langchain/index
:::


(ml-llamaindex)=
### LlamaIndex

:::{toctree}
:maxdepth: 1

../../integrate/llamaindex/index
:::



```{toctree}
:hidden:

tensorflow
```


[AutoML with PyCaret and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/pycaret
[automl-classify-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/pycaret/automl_classification_with_pycaret.py
[automl-classify-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/pycaret/automl_classification_with_pycaret.ipynb
[automl-forecasting-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/pycaret/automl_timeseries_forecasting_with_pycaret.ipynb
[automl-forecasting-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/pycaret/automl_timeseries_forecasting_with_pycaret.ipynb
[End-to-End RAG with CrateDB and LangChain]: https://speakerdeck.com/cratedb/how-to-use-private-data-in-generative-ai-end-to-end-solution-for-rag-with-cratedb-and-langchain
[How to set up LangChain with CrateDB]: https://community.cratedb.com/t/how-to-set-up-langchain-with-cratedb/1576
[How to Use Private Data in Generative AI]: https://youtu.be/icquKckM4o0?feature=shared
[Jupyter Notebook]: https://jupyter.org/
[Machine Learning and CrateDB: An introduction]: https://cratedb.com/blog/machine-learning-and-cratedb-part-one
[Machine Learning and CrateDB: Getting Started With Jupyter]: https://cratedb.com/blog/machine-learning-cratedb-jupyter
[Machine Learning and CrateDB: Experiment Design & Linear Regression]: https://cratedb.com/blog/machine-learning-and-cratedb-part-three-experiment-design-and-linear-regression
[MLflow]: https://mlflow.org/
[MLflow and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/mlflow
[MLOps]: https://en.wikipedia.org/wiki/MLOps
[pandas]: https://pandas.pydata.org/
[PyCaret]: https://www.pycaret.org
[scikit-learn]: https://scikit-learn.org/
[TensorFlow]: https://www.tensorflow.org/
[Time Series Modeling using Machine Learning]: https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-machine-learning-time-series-data
[tracking-merlion-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/mlflow/tracking_merlion.ipynb
[tracking-merlion-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/mlflow/tracking_merlion.ipynb
