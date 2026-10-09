(start-vector)=
# Vector search

:::{div} sd-text-muted
Store, manage, and search vector embeddings at scale.
:::

Vector search retrieves the most semantically similar items to a query vector using **approximate nearest neighbor (ANN)** algorithms (e.g., HNSW via Lucene).&#x20;

CrateDB supports **native vector search**, enabling you to perform **similarity-based retrieval** directly in SQL, without needing a separate vector database or search engine.

Whether you're powering **semantic search**, **recommendation engines**, **anomaly detection**, or **AI-enhanced applications**, CrateDB lets you manage vector data **right alongside your structured, JSON, and full-text data.**

## Why CrateDB for Vector Search?

| Feature            | Benefit                                                      |
|--------------------|--------------------------------------------------------------|
| FLOAT_VECTOR       | Store embeddings up to 2048 dimensions                       |
| KNN_MATCH          | SQL-native k-nearest neighbor function with `_score` support |
| VECTOR_SIMILARITY  | Compute similarity scores between vectors in queries         |
| Real-time indexing | Fresh vectors are immediately searchable                     |
| Hybrid queries     | Combine vector search with filters, full-text, and JSON      |

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

### Anomaly Detection

```sql
SELECT *
FROM events
WHERE type = 'sensor'
  AND KNN_MATCH(vector_repr, [normal_pattern_emb], 1)
ORDER BY _score ASC
LIMIT 1;
```

## Further reading

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`article;1.5em` Reference
:columns: 3
- {ref}`crate-reference:type-float_vector`
- {ref}`crate-reference:scalar_knn_match`
- {ref}`crate-reference:scalar_vector_similarity`
::::

::::{grid-item-card} {material-outlined}`link;1.5em` Related
:columns: 3
- {ref}`start-fulltext`
- {ref}`start-geospatial`
- {ref}`start-hybrid`
::::

::::{grid-item-card} {material-outlined}`read_more;1.5em` Read more
:columns: 6
- [Intro Blog: Vector support & KNN search in CrateDB]
- {ref}`Vector search feature details <vector-search>`
- {ref}`Data modeling with vector data <model-vector>`
- {ref}`machine-learning`
- {ref}`Integration with LangChain <langchain>`
::::

:::::


[Intro Blog: Vector support & KNN search in CrateDB]: https://cratedb.com/blog/unlocking-the-power-of-vector-support-and-knn-search-in-cratedb
