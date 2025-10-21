(model-vector)=
# Vector data

CrateDB natively supports **vector embeddings** for efficient **similarity
search** using **k-nearest neighbour (kNN)** algorithms. This makes it a
powerful engine for building AI-powered applications involving semantic search,
recommendations, anomaly detection, and multimodal analytics, all in the
simplicity of SQL.

Whether you’re working with text, images, sensor data, or any domain represented
as high-dimensional embeddings, CrateDB enables **real-time vector search at
scale**, in combination with other data types like full-text, geospatial, and
time-series.

## Data Type: FLOAT_VECTOR

CrateDB has a native {ref}`FLOAT_VECTOR type <crate-reference:type-float_vector>`
type with the following key characteristics:

* Fixed-length float arrays (1-2048 dimensions)
* Backed by Lucene’s HNSW approximate nearest neighbor (ANN) search
* Similarity and scoring exposed via {ref}`KNN_MATCH <crate-reference:scalar_knn_match>`
and {ref}`VECTOR_SIMILARITY <crate-reference:scalar_vector_similarity>`.

**Example: Define a Table with Vector Embeddings**

```sql
CREATE TABLE documents (
  title TEXT,
  content TEXT,
  embedding FLOAT_VECTOR(3)
);
```

* `FLOAT_VECTOR(3)` declares a vector column with 3 floats.

## Ingestion: Working with Embeddings

You can ingest vectors in several ways:

*   **Precomputed embeddings** from models:
    ```sql
    INSERT INTO documents (title, embedding)
    VALUES ('AI and Databases', [0.12, 0.34, 0.01]);
    ```
    You must insert the exact number of floats defined in the table or an error
    will be thrown.

* **Batched imports** via {ref}`COPY FROM <crate-reference:dml-importing-data>`
using JSON or CSV.
* CrateDB doesn't currently compute embeddings internally — you bring your own
model or use pipelines that call CrateDB.

## Querying Vectors with SQL

Use {ref}`KNN_MATCH <crate-reference:scalar_knn_match>` to perform similarity
search:

```sql
SELECT title, content, _score
FROM documents
WHERE knn_match(embedding, [3.14, 5.1, 8.2], 2)
ORDER BY _score DESC;
```

This ranks results by **vector similarity** to the vector supplied by searching
top 2 nearest neighbours.

## See also

* {ref}`Vector Search <vector-search>`: More details about searching with
  vectors
Reference manual:
  * {ref}`FLOAT_VECTOR type <crate-reference:type-float_vector>`
  * {ref}`KNN_MATCH <crate-reference:scalar_knn_match>`
  * {ref}`VECTOR_SIMILARITY <crate-reference:scalar_vector_similarity>`
* Blog: [Vector support and KNN search](https://cratedb.com/blog/unlocking-the-power-of-vector-support-and-knn-search-in-cratedb)
* CrateDB Academy: [Vector similarity
  search](https://learn.cratedb.com/cratedb-fundamentals?lesson=vector-similarity-search)
