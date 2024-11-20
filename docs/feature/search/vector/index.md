(hnsw)=
(vector-store)=
(vector-search)=

# Vector Search

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::

**Vector search on machine learning embeddings: CrateDB is all you need.**

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9


:::{rubric} Overview
:::
CrateDB can be used as a [vector database] (VDBMS) for storing and retrieving
vector embeddings based on the FLOAT_VECTOR data type and its accompanying
KNN_MATCH and VECTOR_SIMILARITY functions, effectively conducting HNSW
semantic similarity searches on them, also known as vector search.

:::{rubric} About
:::
Vector search leverages machine learning (ML) to capture the meaning and
context of unstructured data, including text and images, transforming it
into a numeric representation.

Frequently used for semantic search, vector
search finds similar data using approximate nearest neighbor (ANN) algorithms.
Compared to traditional keyword search, vector search yields more relevant
results and executes faster.

:::{rubric} Details
:::
CrateDB uses Lucene as a storage layer, so it inherits the implementation
and concepts of Lucene Vector Search, in the same spirit as Elasticsearch.

To learn more details about what's inside, please refer to the [HNSW] graph
search algorithm, [how Lucene implemented it][making of Lucene vector search],
[how Elasticsearch now also builds on it][Vector search in Elasticsearch],
and why effectively [Lucene Is All You Need].

While Elasticsearch uses a [query DSL based on JSON], in CrateDB, you can work
with Lucene Vector Search using SQL.
::::


::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

```{rubric} Reference Manual
```
- [FLOAT_VECTOR](inv:crate-reference#type-float_vector)
- [KNN_MATCH](inv:crate-reference#scalar_knn_match)
- [VECTOR_SIMILARITY](inv:crate-reference#scalar_vector_similarity)

```{rubric} Related
```
- {ref}`sql`
- {ref}`fulltext-search`
- {ref}`geo-search`
- {ref}`hybrid-search`
- {ref}`machine-learning`
- {ref}`query`

{tags-primary}`SQL`
{tags-primary}`Semantic Search`
{tags-primary}`Machine Learning`
{tags-primary}`ML Embeddings`
{tags-primary}`Vector Store`
::::

:::::


## Synopsis

Store and query word embeddings using similarity search based on Euclidean
distance.

::::{grid}
:padding: 0
:class-row: title-slim

:::{grid-item}
:columns: auto 6 6 6
**DDL**

```sql
CREATE TABLE word_embeddings (
  text STRING PRIMARY KEY,
  embedding FLOAT_VECTOR(4)
);
```
:::

:::{grid-item}
:columns: auto 6 6 6
**DML**

```sql
INSERT INTO word_embeddings (text, embedding)
VALUES
  ('Exploring the cosmos', [0.1, 0.5, -0.2, 0.8]),
  ('Discovering moon', [0.2, 0.4, 0.1, 0.7]),
  ('Discovering galaxies', [0.2, 0.4, 0.2, 0.9]),
  ('Sending the mission', [0.5, 0.9, -0.1, -0.7])
;
```
:::

:::{grid-item}
:columns: auto 6 6 6
**DQL**

```sql
WITH param AS
  (SELECT [0.3, 0.6, 0.0, 0.9] AS sv)
SELECT
  text,
  VECTOR_SIMILARITY(embedding,
    (SELECT sv FROM param)) AS score
FROM word_embeddings
WHERE KNN_MATCH(
  embedding, (SELECT sv FROM param), 2)
ORDER BY score DESC;
```
:::

:::{grid-item}
:columns: auto 6 6 6
**Result**

```text
+----------------------+-----------+
| text                 |     score |
+----------------------+-----------+
| Discovering galaxies | 0.9174312 |
| Exploring the cosmos | 0.9090909 |
| Discovering moon     | 0.9090909 |
| Sending the mission  | 0.2702703 |
+----------------------+-----------+
SELECT 4 rows in set (0.078 sec)
```
:::

::::


## Usage

Working with vector data in CrateDB.

:::{rubric} Pure SQL
:::
CrateDB's vector store features are available through SQL and can be used
by any application speaking it. The fundamental data type of FLOAT_VECTOR
is a plain array of floating point numbers, as such it will be communicated
through CrateDB's HTTP and PostgreSQL interfaces.

:::{rubric} Framework Integrations
:::
CrateDB supports applications using the vector data type through corresponding
framework adapters. The page about [](#machine-learning) illustrates all of them,
covering both topics about machine learning operations (MLOps), and vector
database operations (similarity search).


## Learn

Learn how to set up your database for vector search, how to create the relevant
indices, and how to semantically query your data efficiently. A few must-reads
for anyone looking to make sense of large volumes of unstructured text data.

:::{rubric} Tutorials
:::

::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**Vector Support and KNN Search through SQL**

The addition of vector support and KNN search makes CrateDB the optimal
multi-model database for all types of data. Whether it is structured,
semi-structured, or unstructured data, CrateDB stands as the all-in-one
solution, capable of handling diverse data types with ease.

In this feature-focused blog post, we will introduce how CrateDB can be
used as a vector database and how the vector store is implemented.
We will also explore the possibilities of the K-Nearest Neighbors (KNN)
search, and demonstrate vector capabilities with easy-to-follow examples.

{{ '{}[Vector support and KNN search in CrateDB]'.format(blog) }}
:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`Vector Store` \
{tags-secondary}`SQL`
:::
::::


::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**Retrieval Augmented Generation (RAG) with CrateDB and SQL**

This notebook illustrates CrateDB's vector store using pure SQL on behalf
of an example exercising a RAG workflow.

It uses the white-paper [Time series data in manufacturing] as input data,
generates embeddings using OpenAI's ChatGPT, stores them into a table
using `FLOAT_VECTOR(1536)`, and queries it using the `KNN_MATCH` and
`VECTOR_SIMILARITY` functions.

{{ '{}[langchain-rag-sql-github]'.format(nb_github) }} {{ '{}[langchain-rag-sql-colab]'.format(nb_colab) }} {{ '{}[langchain-rag-sql-binder]'.format(nb_binder) }}
:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`LangChain` \
{tags-secondary}`pandas` \
{tags-secondary}`SQL`
:::
::::


:::{rubric} Technologies
:::

::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Support for Vector Search in Apache Lucene**

Uwe Schindler talks at Berlin Buzzwords 2023 about the new vector search
features of Lucene 9, and about the journey of implementing HNSW from
2016 to 2021.

- [Uwe Schindler - What's coming next with Apache Lucene?]
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/EHJjSYWjIF0?start=330&si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Fundamentals`
{tags-secondary}`Lucene`
{tags-secondary}`Vector Search`
:::

::::


:::{seealso}
**Features:**
[](#querying) •
[](#fulltext)

**Domains:**
[](#industrial) •
[](#machine-learning) •
[](#timeseries)

**Product:**
[Relational Database] •
[Vector Database][Vector Database (Product)]
:::



[Lucene Is All You Need]: https://arxiv.org/pdf/2308.14963
[making of Lucene vector search]: https://www.apachecon.com/acna2022/slides/04_lucene_vector_search_sokolov.pdf
[Time series data in manufacturing]: https://github.com/crate/cratedb-datasets/raw/main/machine-learning/fulltext/White%20paper%20-%20Time-series%20data%20in%20manufacturing.pdf
[Uwe Schindler - What's coming next with Apache Lucene?]: https://youtu.be/EHJjSYWjIF0?t=330s&feature=shared
[Vector search in Elasticsearch]: https://www.elastic.co/search-labs/blog/articles/vector-search-elasticsearch-rationale
[Vector support and KNN search in CrateDB]: https://cratedb.com/blog/unlocking-the-power-of-vector-support-and-knn-search-in-cratedb
