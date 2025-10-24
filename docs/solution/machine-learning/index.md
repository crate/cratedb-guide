(ml)=
(ml-tools)=
(machine-learning)=
# Machine learning

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
CrateDB provides a vector type natively, and adapters for integrating
with machine learning frameworks.
:::

:::{todo}
**Instructions:**
Elaborate a bit longer about the topic domain and the ingredients of this section
in an abstract way, concisely highlighting and summarizing relevant benefits,
like the `../analytics/index`, `../industrial/index`, and `../longterm/index`
pages are doing it already.
Use concise language, active voice, and avoid yapping.
:::

## Vector store

:::{div}
[Vector databases][Vector Database] can be used for similarity search,
multi-modal search, recommendation engines, large language models (LLMs),
and other applications.

These applications can answer questions about specific sources of information,
for example using techniques like Retrieval Augmented Generation (RAG).
RAG is a technique for augmenting LLM knowledge with additional data,
often private or real-time.

CrateDB supports high-dimensional vectors with `FLOAT_VECTOR`, e.g. to
store and query word embeddings using [HNSW]-based nearest neighbor search
through SQL.
:::

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} Documentation: Vector search
:link: vector-search
:link-type: ref
CrateDB's FLOAT_VECTOR data type implements a vector store and the k‑nearest
neighbors (k‑NN) search algorithm to find vectors that are similar to a query
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
It supports retrieval-augmented generation (RAG).
+++
The LangChain adapter lets you use CrateDB as a vector store database, load
documents via document loaders, and use LangChain’s conversational memory.
:::

::::


(text-to-sql)=
## Text-to-SQL

:::{div} sd-text-muted
Integrate CrateDB with Text-to-SQL solutions,
and provide MCP and AI enterprise data integrations.
:::

::::{grid} 2
:gutter: 3

:::{grid-item-card} Text-to-SQL with LlamaIndex
:link: llamaindex
:link-type: ref
Text-to-SQL is a technique that converts natural language queries into SQL
queries that can be executed by a database.
:::

:::{grid-item-card} All about MCP
:link: mcp
:link-type: ref
The Model Context Protocol (MCP) is an open protocol that enables seamless
integration between LLM applications and external data sources and tools.
:::

:::{grid-item-card} MindsDB
:link: mindsdb
:link-type: ref
MindsDB is the platform for customizing AI from enterprise data.
:::

::::


## Time series analysis

:::{div} sd-text-muted
Load and analyze data from database systems for
time series anomaly detection and forecasting.
:::

:::{card} Time series analysis using ML
:link: timeseries-analysis-ml
:link-type: ref
- **End-to-end:** Statistical analysis and visualization on huge datasets.
- **Traditional:** Regression analysis within a Jupyter Notebook.
- **Predictive maintenance:** Build a machine learning model to predict machine failures.
- **Advanced time series analysis:** Conduct advanced data analysis on large time series datasets.
:::


## MLOps and model training

:::{div} sd-text-muted
CrateDB supports MLOps procedures through adapters to best-of-breed software
frameworks.
:::

:::{div}
Training a machine learning model, running it in production, and maintaining
it, requires a significant amount of data processing and bookkeeping
operations.

Machine Learning Operations [MLOps] is a paradigm that aims to deploy and
maintain machine learning models in production reliably and efficiently,
including experiment tracking, and in the spirit of continuous development
and DevOps.
:::

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} MLflow
:link: mlflow
:link-type: ref
MLflow is an open-source platform to manage the whole ML lifecycle,
including experimentation, reproducibility, deployment, and a central
model registry.
+++
CrateDB can be used as a storage database for the MLflow Tracking subsystem.
:::

:::{grid-item-card} PyCaret
:link: pycaret
:link-type: ref
PyCaret is an open-source, low-code machine learning library for Python
that automates machine learning workflows (AutoML).
+++
CrateDB can be used as a storage database for training and production datasets.
:::

:::{grid-item-card} Advanced time series analysis with MLflow and PyCaret
:link: ml-timeseries
:link-type: ref
:columns: 12
Learn how to conduct advanced data analysis on large time series datasets
with CrateDB, MLflow, and PyCaret.
+++
**What's inside:** Anomaly detection and forecasting, time series decomposition,
exploratory data analysis (EDA).
:::

::::
