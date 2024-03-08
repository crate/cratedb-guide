(ml)=
(machine-learning)=

# Machine Learning

Integrate CrateDB with machine learning frameworks and
tools, for [MLOps] and [Vector database] operations.


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

MLOps is a paradigm that aims to deploy and maintain machine learning models
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

Vector databases can be used for similarity search, multi-modal search,
recommendation engines, large language models (LLMs), retrieval-augmented
generation (RAG), and other applications.
::::

:::::


## Anomaly Detection and Forecasting


(mlflow)=
### MLflow

Tutorials and Notebooks about using [MLflow] together with CrateDB.

::::{info-card}
:::{grid-item} **Blog: Running Time Series Models in Production using CrateDB**
:columns: 9

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
:::{grid-item} **Notebook: Create a Time Series Anomaly Detection Model**
:columns: 9

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
:::{grid-item} **Notebook: AutoML classification with PyCaret**
:columns: 9

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
:::{grid-item} **Notebook: Train time series forecasting models**
:columns: 9

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


(scikit-learn)=
### scikit-learn

Use [scikit-learn] with CrateDB.

::::{info-card}
:::{grid-item} **Regression analysis with pandas and scikit-learn**
:columns: 9

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
:::{grid-item} **Predictive Maintenance**
:columns: 9

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


(langchain)=
### LangChain

Tutorials and Notebooks about using [LangChain] together with CrateDB.
LangChain has a number of components designed to help build Q&A applications,
and RAG applications more generally.
This feature uses CrateDB's Vector Store implementation.

- What can you build with LangChain?

  - [LangChain: Retrieval augmented generation]
  - [LangChain: Analyzing structured data]
  - [LangChain: Chatbots]


::::{info-card}
:::{grid-item} **Tutorial: Set up LangChain with CrateDB**
:columns: 9

LangChain is a framework for developing applications powered by language models.
For this tutorial, we are going to use it to interact with CrateDB using only
natural language without writing any SQL.

To achieve that, you will need a CrateDB instance running, an OpenAI API key,
and some Python knowledge.

[![Navigate to Tutorial](https://img.shields.io/badge/Navigate%20to-Tutorial-darkblue?logo=Markdown)][How to set up LangChain with CrateDB]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`LLM` \
{tags-secondary}`RAG`
:::
::::


::::{info-card}
:::{grid-item} **Notebook: Vector Similarity Search**
:columns: 9

CrateDB's `FLOAT_VECTOR` type and its `KNN_MATCH` function can be used
for storing and retrieving embeddings, and for conducting similarity
searches.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][LangChain and CrateDB: Code Examples]
[![Notebook on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkgreen?logo=GitHub)][langchain-similarity-github]
[![Notebook on Colab](https://img.shields.io/badge/Open%20on-Colab-blue?logo=Google%20Colab)][langchain-similarity-colab]
[![Notebook on Binder](https://img.shields.io/badge/Open%20on-Binder-lightblue?logo=binder)][langchain-similarity-binder]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`LLM` \
{tags-secondary}`RAG`
:::
::::


::::{info-card}
:::{grid-item} **Notebook: SQLAlchemy Document Loader**
:columns: 9

Database tables in CrateDB can be used as a source provider for
LangChain documents.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][LangChain and CrateDB: Code Examples]
[![Notebook on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkgreen?logo=GitHub)][langchain-document-loader-github]
[![Notebook on Colab](https://img.shields.io/badge/Open%20on-Colab-blue?logo=Google%20Colab)][langchain-document-loader-colab]
[![Notebook on Binder](https://img.shields.io/badge/Open%20on-Binder-lightblue?logo=binder)][langchain-document-loader-binder]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`Data I/O`
:::
::::


::::{info-card}
:::{grid-item} **Notebook: Conversational History**
:columns: 9

CrateDB supports managing LangChain's conversation history.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][LangChain and CrateDB: Code Examples]
[![Notebook on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkgreen?logo=GitHub)][langchain-conversational-history-github]
[![Notebook on Colab](https://img.shields.io/badge/Open%20on-Colab-blue?logo=Google%20Colab)][langchain-conversational-history-colab]
[![Notebook on Binder](https://img.shields.io/badge/Open%20on-Binder-lightblue?logo=binder)][langchain-conversational-history-binder]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`History`
:::
::::


```{toctree}
:hidden:

tensorflow
```


[AutoML with PyCaret and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/automl
[automl-classify-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_classification_with_pycaret.ipynb
[automl-classify-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_classification_with_pycaret.ipynb
[automl-forecasting-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb
[automl-forecasting-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb
[How to set up LangChain with CrateDB]: https://community.cratedb.com/t/how-to-set-up-langchain-with-cratedb/1576
[Jupyter Notebook]: https://jupyter.org/
[LangChain]: https://python.langchain.com/
[LangChain: Analyzing structured data]: https://python.langchain.com/docs/use_cases/qa_structured/sql
[LangChain: Chatbots]: https://python.langchain.com/docs/use_cases/chatbots
[LangChain: Retrieval augmented generation]: https://python.langchain.com/docs/use_cases/question_answering/
[LangChain and CrateDB: Code Examples]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llm-langchain
[langchain-conversational-history-binder]: https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fconversational_memory.ipynb
[langchain-conversational-history-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/conversational_memory.ipynb
[langchain-conversational-history-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/conversational_memory.ipynb
[langchain-document-loader-binder]: https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fdocument_loader.ipynb
[langchain-document-loader-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/document_loader.ipynb
[langchain-document-loader-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/document_loader.ipynb
[langchain-similarity-binder]: https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fvector_search.ipynb
[langchain-similarity-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/vector_search.ipynb
[langchain-similarity-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/vector_search.ipynb
[Machine Learning and CrateDB: An introduction]: https://cratedb.com/blog/machine-learning-and-cratedb-part-one
[Machine Learning and CrateDB: Getting Started With Jupyter]: https://cratedb.com/blog/machine-learning-cratedb-jupyter
[Machine Learning and CrateDB: Experiment Design & Linear Regression]: https://cratedb.com/blog/machine-learning-and-cratedb-part-three-experiment-design-and-linear-regression
[MLflow]: https://mlflow.org/
[MLflow and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/mlops-mlflow
[MLOps]: https://en.wikipedia.org/wiki/MLOps
[pandas]: https://pandas.pydata.org/
[PyCaret]: https://www.pycaret.org
[scikit-learn]: https://scikit-learn.org/
[TensorFlow]: https://www.tensorflow.org/
[Time Series Modeling using Machine Learning]: https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-machine-learning-time-series-data
[tracking-merlion-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb
[tracking-merlion-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb
[Vector database]: https://en.wikipedia.org/wiki/Vector_database
