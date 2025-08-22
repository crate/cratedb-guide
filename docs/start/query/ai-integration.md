# AI integration

CrateDB is not just a real-time analytics database, it's a powerful platform to **feed and interact with machine learning models**, thanks to its ability to store, query, and transform **structured, unstructured, and vectorized data** at scale using standard **SQL**.

Whether you're training models, running batch or real-time inference, or integrating with AI pipelines, CrateDB offers:

* High-ingestion performance for time-series or sensor data
* Real-time queries across structured and semi-structured data
* SQL-powered transformations and filtering
* Native support for embeddings via **FLOAT\_VECTOR** data type

:::{note}
For more details on how CrateDB handles similarity search and embeddings, see the [Vector Search](project:#vector-search) use case.
:::

## 1. Why CrateDB for ML Use Cases?

| Feature                    | Benefit                                                                |
| -------------------------- | ---------------------------------------------------------------------- |
| Real-time ingestion        | Ingest millions of records per second from IoT, logs, or user behavior |
| Unified data               | Mix structured, full-text, vector, and JSON data                       |
| FLOAT\_VECTOR              | Store and query high-dimensional embeddings                            |
| SQL transforms             | Use SQL for preprocessing, feature extraction, and filtering           |
| ML integration             | Use CrateDB as a feature store or inference backend                    |
| Python & LangChain support | Easily connect to training and inference pipelines                     |

## 2. Common Machine Learning Patterns

### Feature Engineering

Use SQL to build features dynamically from raw data.

```sql
SELECT
  user_id,
  AVG(duration) AS avg_session,
  COUNT(DISTINCT page) AS page_diversity
FROM sessions
GROUP BY user_id;
```

### Training Dataset Extraction

Efficiently extract and filter relevant training data.

```sql
SELECT *
FROM telemetry
WHERE temperature > 80
  AND error_code IS NOT NULL
  AND ts BETWEEN NOW() - INTERVAL '7 days' AND NOW();
```

### Store Embeddings

Save vector representations for documents or entities.

```sql
CREATE TABLE article_embeddings (
  id UUID PRIMARY KEY,
  content TEXT,
  embedding FLOAT_VECTOR(384)
);
```

:::{note}
CrateDB supports high-dimensional vectors with `FLOAT_VECTOR`. To query these vectors for similarity-based inference, see [Vector Search](project:#vector-search).
:::

### Use CrateDB as a Feature Store

Centralize your features and use them in production models.

```sql
SELECT *
FROM user_features
WHERE last_active > NOW() - INTERVAL '1 day';
```

## 3. When to Use CrateDB in ML Pipelines

| Use Case            | CrateDB Role                                          |
| ------------------- | ----------------------------------------------------- |
| Feature Store       | Store pre-computed features with SQL access           |
| Real-Time Inference | Serve vector-based results with `KNN_MATCH`           |
| Experimentation     | Use SQL for fast slicing, filtering, and aggregations |
| Monitoring          | Track model performance, drift, or input quality      |
| Data Collection     | Capture telemetry, events, logs, and raw user data    |

## 4. Architecture Examples

### Model Training Pipeline

```text
[ Ingestion (sensors, APIs) ]
           ↓
     [ CrateDB ]
  (Real-time data lake)
           ↓
[ Python / Spark / Pandas ]
  (Feature engineering, training)
           ↓
[ Model Registry / Serving ]
```

### Real-Time Inference with Hybrid Queries

```text
[ CrateDB ]
 - JSON filters
 - Full-text search
 - FLOAT_VECTOR support
         ↓
  [ SQL + KNN_MATCH ]
         ↓
[ Application Response ]
```

## 5. Performance Tips for ML Scenarios

| Tip                                | Benefit                                                     |
| ---------------------------------- | ----------------------------------------------------------- |
| Use `FLOAT_VECTOR` for embeddings  | Store and access high-dimensional vectors efficiently       |
| Normalize vectors before inference | Improves ANN accuracy                                       |
| Index only what you need           | Reduces overhead                                            |
| Use hybrid filters + vector search | Improves performance and precision                          |
| Train offline, infer online        | CrateDB is ideal for live inference from pre-trained models |

## 6. Ecosystem & Integration

| Tool                 | Integration                                    |
| -------------------- | ---------------------------------------------- |
| Python               | `crate-python` for pandas, scikit-learn        |
| LangChain            | Native CrateDB vector store                    |
| Jupyter              | Ideal for experimentation, model development   |
| OpenAI, Cohere, etc. | Store and search their embeddings via SQL      |
| Kafka                | Connect for real-time ingestion and prediction |

## 7. Related Features

| Feature             | Description                                 |
| ------------------- | ------------------------------------------- |
| FLOAT\_VECTOR       | High-dimensional embedding support          |
| KNN\_MATCH          | Nearest neighbor search in SQL              |
| JSON & full-text    | Store unstructured and semi-structured data |
| Joins & aggregates  | Combine data in real-time                   |
| Time-series support | Perfect for sensor-based training data      |

## 8. **Further Reading & Resources**

* [Vector Search use case](project:#vector-search)
* [LangChain Integration with CrateDB](https://python.langchain.com/docs/integrations/providers/cratedb/)
* [CrateDB ML Guide](https://cratedb.com/docs/guide/domain/ml/index.html)
* [CrateDB + Embeddings Blog](https://cratedb.com/blog/unlocking-the-power-of-vector-support-and-knn-search-in-cratedb)
* [CrateDB Examples – ML](https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning)
