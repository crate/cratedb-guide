(ai-integration)=
# AI integration

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 9 9 9

:::{rubric} Introduction
:::

CrateDB is not just a real-time analytics database, it's a powerful platform to **feed and interact with machine learning models**, thanks to its ability to store, query, and transform **structured, unstructured, and vectorized data** at scale using standard **SQL**.

Whether you're training models, running batch or real-time inference, or integrating with AI pipelines, CrateDB offers:

- High ingestion performance for time-series or sensor data.
- SQL-powered transformations and filtering.
- Unified queries across structured and semi-structured data: \
  Full-text, vector, and JSON.
- Native support for embeddings via **FLOAT\_VECTOR** data type, \
  for conducting similarity searches in vector spaces (HNSW).

:::{rubric} Benefits of using CrateDB in ML pipelines
:::

| Use Case            | CrateDB Role                                          |
| ------------------- | ----------------------------------------------------- |
| Feature Store       | Store pre-computed features with SQL access           |
| Real-Time Inference | Serve vector-based results with `KNN_MATCH`           |
| Experimentation     | Use SQL for fast slicing, filtering, and aggregations |
| Monitoring          | Track model performance, drift, or input quality      |
| Data Collection     | Capture telemetry, events, logs, and raw user data    |

::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Related
:::
- {ref}`vector-search`
- {ref}`hybrid-search`
- {ref}`Machine Learning <ml>`

:::{rubric} Integrations
:::
- {ref}`langchain`
- {ref}`llamaindex`
- {ref}`mindsdb`
- {ref}`mlflow`
- {ref}`pycaret`

:::{rubric} See also
:::
- [Blog: Vector support and KNN search]
- {ref}`Synopsis: Text-to-SQL <llamaindex-synopsis>`
- {ref}`Tutorial: Text-to-SQL using Azure <llamaindex-usage-azure>`
- [Examples: ML]

::::

:::::

:::{rubric} Use cases
:::

## Similarity search
**Feature:** Store and query [word embeddings] using [HNSW] nearest neighbor
search through SQL. CrateDB supports high-dimensional vectors with `FLOAT_VECTOR`.
To query these vectors for similarity-based inference, see
{ref}`Vector Search <vector-search>` and the quick synopsis below.

::::{grid} 2
:padding: 0
:class-row: title-slim

:::{grid-item}
Create a table using the `FLOAT_VECTOR` data type.
:::
:::{grid-item}
```sql
CREATE TABLE word_embeddings (
  text STRING PRIMARY KEY,
  embedding FLOAT_VECTOR(4)
);
```
:::
:::{grid-item}
Insert a few vectors.
:::
:::{grid-item}
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
Query dataset for similarities.
:::
:::{grid-item}
```sql
SELECT *
FROM word_embeddings
WHERE KNN_MATCH(
    embedding, [0.3, 0.6, 0.0, 0.9], 2);
```
:::
::::


## ML engineering

::::{grid} 2
:padding: 0
:class-row: title-slim

:::{grid-item}
**Feature Engineering:** Use SQL to build features dynamically from raw data.
:::
:::{grid-item}
```sql
SELECT
  user_id,
  AVG(duration) AS avg_session,
  COUNT(DISTINCT page) AS page_diversity
FROM sessions
GROUP BY user_id;
```
:::
:::{grid-item}
**Feature Engineering:** Use CrateDB as a feature store.
Centralize your features and use them in production models.
:::
:::{grid-item}
```sql
SELECT *
FROM user_features
WHERE last_active > NOW() - INTERVAL '1 day';
```
:::
:::{grid-item}
**Training Dataset Extraction:**
Efficiently extract and filter relevant training data from large datasets using plain SQL.
:::
:::{grid-item}
```sql
SELECT *
FROM telemetry
WHERE temperature > 80
  AND error_code IS NOT NULL
  AND ts BETWEEN NOW() - INTERVAL '7 days' AND NOW();
```
:::

:::{grid-item}
**Model Training Pipeline:**
An example architecture for feature engineering and model training with CrateDB,
see also {ref}`mlflow` and {ref}`pycaret` for AutoML purposes.
:::
:::{grid-item}
```text
[ Sensors, APIs ] (ingest)
     ↓
[ CrateDB ] (real-time analytics store)
     ↓
[ Python ML* ] (model training)
     ↓
[ Model Registry ] (model serving)
```
```{div} text-small
\* ... using frameworks or platforms like Apache Spark, Databricks, MLflow, pandas,
PyCaret, scikit-learn.
```

:::

:::{grid-item}
**Real-Time Inference with Hybrid Queries:**
An example architecture for hybrid queries, see also {ref}`vector-search` and
{ref}`hybrid-search`.
:::
:::{grid-item}
```text
[ User ] (query expression)
   ↓
[ CrateDB ] (data source)
  - JSON filters
  - Full-text search (BM25)
  - FLOAT_VECTOR support (HNSW)
  - SQL + KNN_MATCH
   ↓
[ Application response ]
```
:::

::::


:::{note}
For advanced ML engineering tasks and use cases, based on industry-approved
frameworks and libraries, see CrateDB's support for MLflow and PyCaret at
{ref}`machine-learning`.
:::


## Text-to-SQL
Text‑to‑SQL lets you query data in natural language with contemporary
large language models, optionally offline.
:::{seealso}
{ref}`llamaindex-synopsis`
:::


## Related features

Learn more about how to combine ML features with other major features of CrateDB.

| Feature             | Description                                 | Documentation                          |
| ------------------- | ------------------------------------------- |----------------------------------------|
| FLOAT\_VECTOR       | High-dimensional embedding support          | {ref}`vector-search`                   |
| KNN\_MATCH          | Nearest neighbor search in SQL              | {ref}`vector-search`                   |
| JSON & full-text    | Store unstructured and semi-structured data | {ref}`document`, {ref}`fts`            |
| Joins & aggregates  | Combine data in real-time                   | {ref}`relational`, {ref}`aggregations` |
| Time-series support | Perfect for sensor-based training data      | {ref}`timeseries`                      |



[Blog: Vector support and KNN search]: https://cratedb.com/blog/unlocking-the-power-of-vector-support-and-knn-search-in-cratedb
[Examples: ML]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning
[HNSW]: https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world
[Tutorial: Text-to-SQL]: https://community.cratedb.com/t/text-to-sql-talk-to-your-data-using-cratedb-llamaindex-and-azure-openai/1612
[word embeddings]: https://en.wikipedia.org/wiki/Word_embedding
