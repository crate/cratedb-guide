(ml)=
(ml-tools)=
(machine-learning)=
# Machine learning with CrateDB

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
CrateDB provides a vector store natively, and adapters for integrating
with machine learning frameworks.
:::

## Vector store

:::{div}
[Vector databases][Vector Database] can be used for similarity search,
multi-modal search, recommendation engines, large language models (LLMs),
and other applications.

These applications can answer questions about specific sources of information,
for example using techniques like Retrieval Augmented Generation (RAG).
RAG is a technique for augmenting LLM knowledge with additional data.
:::

::::{grid} 2
:gutter: 4

:::{grid-item-card} Documentation: Vector search
:link: vector-search
:link-type: ref
CrateDB's FLOAT_VECTOR data type implements a vector store and the k-nearest
neighbour (kNN) search algorithm to find vectors that are similar to a query
vector.
+++
Vector search on machine learning embeddings: CrateDB is all you need.
:::

:::{grid-item-card} Documentation: Hybrid search
:link: hybrid-search
:link-type: ref
Hybrid search is a technique to enhance relevancy and accuracy by combining
traditional full-text with semantic search algorithms, for achieving better
accuracy and relevancy than each algorithm would individually.
+++
Combined BM25 term search and vector search based on Apache Lucene,
using SQL: CrateDB is all you need.
:::

:::{grid-item-card} Integration: LangChain
:link: langchain
:link-type: ref
LangChain is a framework for developing applications powered by language models,
written in Python, and with a strong focus on composability.
+++
The LangChain adapter for CrateDB provides support to use CrateDB as a vector
store database, to load documents using LangChain’s DocumentLoader, and also
supports LangChain’s conversational memory subsystem.
:::

::::


## Text-to-SQL and MCP

The adapters enumerated below integrate CrateDB for Text-to-SQL purposes,
and provide MCP and AI enterprise data integrations.

::::{grid} 2
:gutter: 4

:::{grid-item-card} Text-to-SQL with LlamaIndex
:link: llamaindex
:link-type: ref
Text-to-SQL is a technique that converts natural language queries into SQL
queries that can be executed by a database.
:::

:::{grid-item-card} MCP
:link: mcp
:link-type: ref
The Model Context Protocol (MCP), is an open protocol that enables seamless
integration between LLM applications and external data sources and tools.
:::

:::{grid-item-card} MindsDB
:link: mindsdb
:link-type: ref
MindsDB is the platform for customizing AI from enterprise data.
:::

::::


## MLOps and model training

:::{div}
Training a machine learning model, running it in production, and maintaining
it, requires a significant amount of data processing and bookkeeping
operations.

Machine Learning Operations [MLOps] is a paradigm that aims to deploy and
maintain machine learning models in production reliably and efficiently,
including experiment tracking, and in the spirit of continuous development
and DevOps.

CrateDB supports MLOps procedures through adapters to best-of-breed software
frameworks.
:::

::::{grid} 2
:gutter: 4

:::{grid-item-card} MLflow
:link: mlflow
MLflow is an open-source platform to manage the whole ML lifecycle,
including experimentation, reproducibility, deployment, and a central
model registry.
+++
CrateDB can be used as a storage database for the MLflow Tracking subsystem.
:::

:::{grid-item-card} PyCaret
:link: pycaret
PyCaret is an open-source, low-code machine learning library for Python
that automates machine learning workflows (AutoML).
+++
CrateDB can be used as a storage database for training and production datasets.
:::

::::


## Time-series anomaly detection and forecasting

Load and analyze data from database systems.

::::{grid} 2
:gutter: 4

:::{grid-item-card} Statistical analysis and visualization on huge datasets
:link: r-tutorial
Learn how to create a Machine Learning pipeline using R and CrateDB.
:::

:::{grid-item-card} Regression analysis with pandas and scikit-learn
:link: scikit-learn-tutorial
Use pandas and scikit-learn to run a regression analysis within a Jupyter Notebook.
:::

:::{grid-item-card} Use TensorFlow and CrateDB for predictive maintenance
:link: tensorflow-tutorial
Learn how to build a machine learning model that will predict whether
a machine will fail within a specified time window in the future.
:::

::::
