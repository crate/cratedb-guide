(start-hybrid)=
# Hybrid search

:::{div} sd-text-muted
Combine vector similarity (kNN) and term-based full-text (BM25)
searches in a single SQL query.
:::

While **vector search** provides powerful semantic retrieval based on machine learning models, it's not always optimal, especially when models are not fine-tuned for a specific domain. On the other hand, **traditional full-text search** (e.g., BM25 scoring) offers high precision on exact or keyword-based queries, with strong performance out of the box. **Hybrid search** blends these approaches, combining semantic understanding with keyword relevance to deliver more accurate, robust, and context-aware search results.

Hybrid search is particularly effective for **knowledge bases, product or document search, multilingual content search, FAQ bots and semantic assistants**, and **AI-powered search experiences.** It allows applications to go beyond keyword matching, incorporating vector similarity while still respecting domain-specific terms.

CrateDB supports **hybrid search** by combining **vector similarity search** (kNN) and **term-based full-text search** (BM25) in a single SQL query. CrateDB lets you implement hybrid search natively in SQL using **common table expressions (CTEs)** and **scoring fusion techniques**, such as:

* **Convex combination** (weighted sum of scores)
* **Reciprocal rank fusion (RRF)**

## Supported Search Capabilities in CrateDB

| Search Type           | Function      | Description                                    |
| --------------------- | ------------- |------------------------------------------------|
| **Vector search**     | `KNN_MATCH()` | Finds vectors closest to a given vector        |
| **Full-text search**  | `MATCH()`     | Uses Lucene's BM25 scoring                     |
| **Geospatial search** | `MATCH()`     | For shapes and points (see: Geospatial search) |

CrateDB enables all three through **pure SQL**, allowing flexible combinations and advanced analytics.

## Example: Hybrid Search in SQL

Here’s a simple structure of a hybrid search query combining BM25 and vector results using a CTE:

```sql
WITH 
    vector_results AS (
        SELECT id, title, content, 
               _score AS vector_score
        FROM documents
        WHERE KNN_MATCH(embedding, [0.2, 0.1, ..., 0.3], 10)
    ),
    bm25_results AS (
        SELECT id, title, content, 
               _score AS bm25_score
        FROM documents
        WHERE MATCH(content, 'knn search')
    )

SELECT 
    v.id,
    v.title,
    bm25_score,
    vector_score,
    0.5 * bm25_score + 0.5 * vector_score AS hybrid_score
FROM 
    bm25_results b
JOIN 
    vector_results v ON v.id = b.id
ORDER BY 
    hybrid_score DESC
LIMIT 10;
```

You can adjust the weighting (`0.5`) depending on your desired balance between keyword precision and semantic similarity.

## Sample Results

### Hybrid Scoring (Convex Combination)

| hybrid\_score | bm25\_score | vector\_score | title                                         |
| ------------- | ----------- | ------------- | --------------------------------------------- |
| 0.7440        | 1.0000      | 0.5734        | knn\_match(float\_vector, float\_vector, int) |
| 0.4868        | 0.5512      | 0.4439        | Searching On Multiple Columns                 |
| 0.4716        | 0.5694      | 0.4064        | array\_position(...)                          |

### Reciprocal Rank Fusion (RRF)

| final\_rank | bm25\_rank | vector\_rank | title                                         |
| ----------- | ---------- | ------------ | --------------------------------------------- |
| 0.03278     | 1          | 1            | knn\_match(float\_vector, float\_vector, int) |
| 0.03105     | 7          | 2            | Searching On Multiple Columns                 |
| 0.03057     | 8          | 3            | Usage                                         |

:::{note}
RRF rewards documents that rank highly across multiple methods,
regardless of exact score values.
:::

## Further reading

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`article;1.5em` Reference
:columns: 3
- {ref}`crate-reference:sql_dql_fulltext_search`
- {ref}`crate-reference:fulltext-indices`
- {ref}`crate-reference:predicates_match`
- {ref}`crate-reference:scalar_knn_match`
- {ref}`crate-reference:scalar_vector_similarity`
- {ref}`crate-reference:type-float_vector`
::::

::::{grid-item-card} {material-outlined}`link;1.5em` Related
:columns: 3
- {ref}`start-fulltext`
- {ref}`start-geospatial`
- {ref}`start-vector`
::::

::::{grid-item-card} {material-outlined}`read_more;1.5em` Read more
:columns: 6
- [Doing Hybrid Search in CrateDB]
- {ref}`Hybrid search feature details <hybrid-search>`
::::

:::::


[Doing Hybrid Search in CrateDB]: https://cratedb.com/blog/hybrid-search-explained
