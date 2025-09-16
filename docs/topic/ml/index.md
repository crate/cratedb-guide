(ml)=
(ml-tools)=
(machine-learning)=
# Machine Learning with CrateDB

:::{include} /_include/links.md
:::

Machine learning applications and frameworks
which can be used together with CrateDB.

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


### MLflow
Use MLflow with CrateDB for experiment tracking and model registry.
:::{seealso}
See the dedicated page: {ref}`mlflow`.
:::


### PyCaret
:::{seealso}
See the dedicated page: {ref}`pycaret`.
:::


### R
:::{seealso}
Please navigate to the dedicated page about {ref}`r`.
:::



### scikit-learn
:::{seealso}
See the dedicated page: {ref}`scikit-learn`.
:::


### TensorFlow
:::{seealso}
Please navigate to the dedicated page about {ref}`tensorflow`.
:::


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


(ml-mindsdb)=
### MindsDB

:::{toctree}
:maxdepth: 1

../../integrate/mindsdb/index
:::



[End-to-End RAG with CrateDB and LangChain]: https://speakerdeck.com/cratedb/how-to-use-private-data-in-generative-ai-end-to-end-solution-for-rag-with-cratedb-and-langchain
[How to set up LangChain with CrateDB]: https://community.cratedb.com/t/how-to-set-up-langchain-with-cratedb/1576
[How to Use Private Data in Generative AI]: https://youtu.be/icquKckM4o0?feature=shared
