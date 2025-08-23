# Vector search

CrateDB supports **native vector search**, enabling you to perform **similarity-based retrieval** directly in SQL, without needing a separate vector database or search engine.

Whether you're powering **semantic search**, **recommendation engines**, **anomaly detection**, or **AI-enhanced applications**, CrateDB lets you store, manage, and search vector embeddings at scale **right alongside your structured, JSON, and full-text data.**

## What Is Vector Search?

Vector search retrieves the most semantically similar items to a query vector using **Approximate Nearest Neighbor (ANN)** algorithms (e.g., HNSW via Lucene). CrateDB provides unified SQL support for this via `KNN_MATCH`.

## Why CrateDB for Vector Search?

| FLOAT\_VECTOR       | Store embeddings up to 2048 dimensions                       |
| ------------------- | ------------------------------------------------------------ |
| KNN\_MATCH          | SQL-native k-nearest neighbor function with `_score` support |
| VECTOR\_SIMILARITY  | Compute similarity scores between vectors in queries         |
| Real-time indexing  | Fresh vectors are immediately searchable                     |
| Hybrid queries      | Combine vector search with filters, full-text, and JSON      |

## Common Query Patterns

### K-Nearest Neighbors (KNN) Search

```sql
SELECT text, _score
FROM word_embeddings
WHERE KNN_MATCH(embedding, [0.3, 0.6, 0.0, 0.9], 3)
ORDER BY _score DESC;
```

Returns top 3 most similar embeddings.

### Combine with Filters

```sql
SELECT product_name, _score
FROM products
WHERE category = 'shoes'
  AND KNN_MATCH(features, [0.2, 0.1, 0.3], 5)
ORDER BY _score DESC;
```

### Compute Similarity Score

```sql
SELECT id, VECTOR_SIMILARITY(emb, [q_vector]) AS score
FROM items
WHERE KNN_MATCH(emb, [q_vector], 10)
ORDER BY score DESC;
```

Useful if combining scoring logic manually.

## Real-World Examples

### Semantic Document Search

```sql
SELECT id, title
FROM documents
WHERE KNN_MATCH(embedding, [query_emb], 5)
ORDER BY _score DESC;
```

### E-commerce Recommendations

```sql
SELECT id, name
FROM product_vecs
WHERE in_stock
  AND KNN_MATCH(feature_vec, [user_emb], 4)
ORDER BY _score DESC;
```

### Chat Memory Recall

```sql
SELECT message
FROM chat_history
WHERE KNN_MATCH(vec, [query_emb], 3)
ORDER BY _score DESC;
```

Anomaly Detection

```sql
SELECT *
FROM events
WHERE type = 'sensor'
  AND KNN_MATCH(vector_repr, [normal_pattern_emb], 1)
ORDER BY _score ASC
LIMIT 1;
```

## Performance & Indexing Tips

| Tip                                | Benefit                                                 |
| ---------------------------------- | ------------------------------------------------------- |
| Use `FLOAT_VECTOR`                 | Efficiency with fixed-size arrays up to 2048 dimensions |
| Create HNSW index when supported   | Enables fast ANN queries via Lucene                     |
| Consistent vector length           | All embeddings must match column definition             |
| Pre-filter with structured filters | Reduces scanning overhead                               |
| Tune `KNN_MATCH`                   | Adjust neighbor count per shard or globally             |

## When to Use CrateDB for Vector Search

Use CrateDB when you need to:

* Execute **semantic search** within your primary database
* Avoid managing an external vector database
* Build **hybrid queries** combining embeddings and metadata
* Scale to real-time pipelines with **millions of vectors**
* Keep everything accessible through SQL

## Related Features

| Feature            | Description                                     |
| ------------------ | ----------------------------------------------- |
| FLOAT\_VECTOR      | Native support for high-dimensional arrays      |
| KNN\_MATCH         | Core SQL predicate for vector similarity search |
| VECTOR\_SIMILARITY | Compute proximity scores in SQL                 |
| Lucene HNSW ANN    | Efficient graph-based search engine             |
| Hybrid search      | Combine ANN search with full-text, geo, JSON    |

## Learn More

* [Vector Search Guide](https://cratedb.com/docs/guide/feature/search/vector/index.html)&#x20;
* `KNN_MATCH` & `VECTOR_SIMILARITY` reference
* [Intro Blog: Vector support & KNN search in CrateDB](https://cratedb.com/blog/unlocking-the-power-of-vector-support-and-knn-search-in-cratedb)
* [LangChain & Vector Store integration](https://cratedb.com/docs/guide/domain/ml/index.html)

## Summary

CrateDB’s **vector search** empowers developers to build **AI-driven applications** without the complexity of separate infrastructure. Use `KNN_MATCH` for fast retrieval, combine it with filters, metadata, or textual logic, and stay entirely within SQL while scaling across your cluster seamlessly.
