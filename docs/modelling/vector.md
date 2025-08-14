# Vector data

CrateDB natively supports **vector embeddings** for efficient **similarity search** using **approximate nearest neighbor (ANN)** algorithms. This makes it a powerful engine for building AI-powered applications involving semantic search, recommendations, anomaly detection, and multimodal analytics—all in the simplicity of SQL.

Whether you’re working with text, images, sensor data, or any domain represented as high-dimensional embeddings, CrateDB enables **real-time vector search at scale**, in combination with other data types like full-text, geospatial, and time-series.\


## 1. Data Type: VECTOR

CrateDB introduces a native `VECTOR` type with the following key characteristics:

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

## 2. Indexing: Enabling Vector Search

To use fast similarity search, define an **HNSW index** on the vector column:

```sql
CREATE INDEX embedding_hnsw
ON documents (embedding)
USING HNSW
WITH (
  m = 16,
  ef_construction = 128,
  ef_search = 64,
  similarity = 'cosine'
);
```

**Parameters:**

* `m`: controls the number of bi-directional links per node (default: 16)
* `ef_construction`: affects index build accuracy/speed (default: 128)
* `ef_search`: controls recall/latency trade-off at query time
* `similarity`: choose from `'cosine'`, `'l2'` (Euclidean), `'dot_product'`

> CrateDB automatically builds the ANN index in the background, allowing for real-time updates.

## 3. Querying Vectors with SQL

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

:::{note}
Combine vector similarity with full-text, metadata, or geospatial filters!
:::

## 4. Ingestion: Working with Embeddings

You can ingest vectors in several ways:

*   **Precomputed embeddings** from models like OpenAI, HuggingFace, or SentenceTransformers:

    ```sql
    INSERT INTO documents (id, title, embedding)
    VALUES ('uuid-123', 'AI and Databases', [0.12, 0.34, ..., 0.01]);
    ```
* **Batched imports** via `COPY FROM` using JSON or CSV
* CrateDB doesn't currently compute embeddings internally—you bring your own model or use pipelines that call CrateDB.

## 5. Use Cases

| Use Case                | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| Semantic Search         | Rank documents by meaning instead of keywords                      |
| Recommendation Systems  | Find similar products, users, or behaviors                         |
| Image / Audio Retrieval | Store and compare embeddings of images/audio                       |
| Fraud Detection         | Match behavioral patterns via vectors                              |
| Hybrid Search           | Combine vector similarity with full-text, geo, or temporal filters |

Example: Hybrid semantic product search

```sql
SELECT id, title, price, description
FROM products
WHERE MATCH(description_ft, 'running shoes') AND brand = 'Nike'
ORDER BY features <-> [vector] ASC
LIMIT 10;
```

## 6. Performance & Scaling

* Vector search uses **HNSW**: state-of-the-art ANN algorithm with logarithmic search complexity.
* CrateDB parallelizes ANN search across shards/nodes.
* Ideal for 100K to tens of millions of vectors; supports real-time ingestion and queries.

:::{note}
Note: vector dimensionality must be consistent for each column.
:::

## 7. Best Practices

| Area           | Recommendation                                                          |
| -------------- | ----------------------------------------------------------------------- |
| Vector length  | Use standard embedding sizes (e.g. 384, 512, 768, 1024)                 |
| Similarity     | Cosine for semantic/textual data; dot-product for ranking models        |
| Index tuning   | Tune `ef_search` for latency/recall trade-offs                          |
| Hybrid queries | Combine vector similarity with metadata filters (e.g. category, region) |
| Updates        | Re-inserting or updating vectors is fully supported                     |
| Data pipelines | Use external tools for vector generation; push to CrateDB via REST/SQL  |

## 8. Integrations

* **Python / pandas / LangChain**: CrateDB has native drivers and REST interface
* **Embedding models**: Use OpenAI, HuggingFace, Cohere, or in-house models
* **RAG architecture**: CrateDB stores vector + metadata + raw text in a unified store

## 9. Further Learning & Resources

* CrateDB Docs – Vector Search
* Blog: Using CrateDB for Hybrid Search (Vector + Full-Text)
* CrateDB Academy – Vector Data
* [Sample notebooks on GitHub](https://github.com/crate/cratedb-examples)

## 10. Summary

CrateDB gives you the power of **vector similarity search** with the **flexibility of SQL** and the **scalability of a distributed database**. It lets you unify structured, unstructured, and semantic data—enabling modern applications in AI, search, and recommendation without additional vector databases or pipelines.
