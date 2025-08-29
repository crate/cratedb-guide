(model-vector)=
# Vector data

CrateDB natively supports **vector embeddings** for efficient **similarity search** using **k-nearest neighbour (kNN)** algorithms. This makes it a powerful engine for building AI-powered applications involving semantic search, recommendations, anomaly detection, and multimodal analytics, all in the simplicity of SQL.

Whether you’re working with text, images, sensor data, or any domain represented as high-dimensional embeddings, CrateDB enables **real-time vector search at scale**, in combination with other data types like full-text, geospatial, and time-series.

***

## Data Type: VECTOR

CrateDB has a native `VECTOR` type with the following key characteristics:

* Fixed-length float arrays (e.g. 768, 1024, 2048 dimensions)
* Supports **HNSW (Hierarchical Navigable Small World)** indexing for fast approximate search
* Optimized for cosine, Euclidean, and dot-product similarity

**Example: Define a Table with Vector Embeddings**

```sql
CREATE TABLE documents (
  id UUID PRIMARY KEY,
  title TEXT,
  content TEXT,
  embedding VECTOR(FLOAT[768])
);
```

* `VECTOR(FLOAT[768])` declares a fixed-size vector column.
* You can ingest vectors directly or compute them externally and store them via SQL

***

## Querying Vectors with SQL

Use the `nearest_neighbors` predicate to perform similarity search:

```sql
SELECT id, title, content
FROM documents
ORDER BY embedding <-> [0.12, 0.73, ..., 0.01]
LIMIT 5;
```

This ranks results by **vector similarity** using the index.

Or, filter and rank by proximity:

```sql
SELECT id, title, content, embedding <-> [0.12, ..., 0.01] AS score
FROM documents
WHERE MATCH(content_ft, 'machine learning') AND author = 'Alice'
ORDER BY score
LIMIT 10;
```

```{note}
Combine vector similarity with full-text, metadata, or geospatial filters!
```

***

## Ingestion: Working with Embeddings

You can ingest vectors in several ways:

*   **Precomputed embeddings** from models like OpenAI, HuggingFace, or SentenceTransformers:

    ```sql
    INSERT INTO documents (id, title, embedding)
    VALUES ('uuid-123', 'AI and Databases', [0.12, 0.34, ..., 0.01]);
    ```
* **Batched imports** via `COPY FROM` using JSON or CSV
* CrateDB doesn't currently compute embeddings internally—you bring your own model or use pipelines that call CrateDB.

***

## Performance & Scaling

* Vector search uses **HNSW**: state-of-the-art ANN algorithm with logarithmic search complexity.
* CrateDB parallelizes ANN search across shards/nodes.
* Ideal for 100K to tens of millions of vectors; supports real-time ingestion and queries.

```{note}
Vector dimensionality must be consistent for each column.
```

***

## Integrations

* **Python / pandas / LangChain**: CrateDB has native drivers and REST interface
* **Embedding models**: Use OpenAI, HuggingFace, Cohere, or in-house models
* **RAG architecture**: CrateDB stores vector + metadata + raw text in a unified store

***

## Further Learning & Resources

* [Vector Search](project:#vector-search): More details about searching with vectors
* Blog: [Using CrateDB for Hybrid Search (Vector + Full-Text)](https://cratedb.com/blog/hybrid-search-explained)
* CrateDB Academy: [Vector similarity search](https://learn.cratedb.com/cratedb-fundamentals?lesson=vector-similarity-search)
