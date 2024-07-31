(hybrid-search)=

# Hybrid Search

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

**Combined BM25 term search and vector search based on Apache Lucene,
using SQL: CrateDB is all you need.**

:::{rubric} Overview
:::
The capabilities of [](project:#vector-search) are impressive, but it isn't a
perfect technology. Without domain-specific datasets to fine-tune models
on, a traditional term-based [](project:#fulltext-search) still has a few
advantages.

:::{rubric} About
:::
Vector search unlocks semantic search. Based on existing models, it provides
incredible and intelligent data retrieval, but struggles when it comes to
adapting to new domains.

Combining both approaches, in order to leverage the best from both worlds, is
called _hybrid search_, aiming to use the performance potential of vector
search, and the zero-shot adaptability of traditional search.

:::{rubric} Details
:::
Hybrid search as a technique enhances relevancy and accuracy by combining the
results of two or more search algorithms, achieving better accuracy and relevancy
than each algorithm would individually.

CrateDB supports three search functions:
- kNN search, using `KNN_MATCH`
- Okapi BM25 similarity scoring, using `MATCH`
- Geospatial search, using `MATCH`
::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Reference Manual
:::
- [](inv:crate-reference#sql_dql_fulltext_search)
- [](inv:crate-reference#fulltext-indices)
- [MATCH](inv:crate-reference#predicates_match)
- [KNN_MATCH](inv:crate-reference#scalar_knn_match)
- [FLOAT_VECTOR](inv:crate-reference#type-float_vector)

:::{rubric} Related
:::
- {ref}`sql`
- {ref}`fulltext-search`
- {ref}`vector-search`
- {ref}`query`

{tags-primary}`Full-Text Search`
{tags-primary}`Semantic Search`
{tags-primary}`Vector Search`

{tags-secondary}`SQL`
{tags-secondary}`BM25`
{tags-secondary}`kNN`
{tags-secondary}`HNSW`
::::

:::::


## Synopsis
A quick impression how a single-query hybrid search looks like.

:::::{grid}
:padding: 0

::::{grid-item}
:columns: auto 7 7 7
:padding: 1
```sql
WITH 
    vector_search as (vector_query),
    bm25_search as (bm25_query)

SELECT
    (CONVEX or RRF) as hybrid_score

FROM
    search_method_1, search_method_2

WHERE
    search_method_1.id = search_method_2.id;
```
::::

::::{grid-item}
:columns: auto 5 5 5
:padding: 3
The SQL expression uses common table expressions for a better structure,
and an inner-join to join results from both search methods into a single
unified result, based on the application requirements at hand.

:::{div} text-smaller
The blog article referenced below features a full example that explores
hybrid scoring using [convex combination], and in the final version 
assigns a rank to every row, using a window function and [reciprocal rank
fusion (RRF)].
:::
::::
:::::



:::{rubric} Example Results
:::

Example result for a search with convex combination scoring, yielding
individual scores for bm25 vs. vector, and a synthesized hybrid score.
The search expression was `MATCH("content", 'knn search')`.
```postgresql
+----------------------+-------------+--------------+----------------------------------------------------------------+
| hybrid_score         | bm25_score  | vector_score | title                                                          |
|----------------------|-------------|--------------|----------------------------------------------------------------|
| 0.7440367221832276   |  1          | 0.57339454   | knn_match(float_vector, float_vector, int)                     |
| 0.4868442595005036   |  0.5512639  | 0.4438978    | Searching On Multiple Columns                                  |
| 0.4716400563716888   |  0.56939983 | 0.40646687   | array_position(anycompatiblearray, anycompatible [, integer ] )|
| 0.4702456831932068   |  0.55290174 | 0.41514164   | Text search functions and operators                            |
| 0.4677474081516266   |  0.5523509  | 0.4113451    | Synopsis                                                       |
+----------------------+-------------+--------------+----------------------------------------------------------------+
```

Example result for a search with reciprocal rank fusion, assigning a rank to
every result row, also yielding ranks for individual components bm25 vs. vector,
and a synthesized final rank.
The search expression was `MATCH("content", 'knn search')`.
```postgresql
+------------+-----------+-------------+----------------------------------------------+
| final_rank | bm25_rank | vector_rank | title                                        |
|------------|-----------|-------------|----------------------------------------------|
| 0.032786   |  1        |     1       |   knn_match(float_vector, float_vector, int) |
| 0.031054   |  7        |     2       |   Searching On Multiple Columns              |
| 0.030578   |  8        |     3       |   Usage                                      |
| 0.028717   |  5        |     15      |   Text search functions and operators        |
| 0.02837    |  10       |     11      |   Synopsis                                   |
+------------+-----------+-------------+----------------------------------------------+
```


## Usage

Working with hybrid search in CrateDB.

:::{rubric} Pure SQL
:::
Querying both CrateDB's inverted index with BM25 scoring for FTS, and navigating
the vector space of machine learning embeddings, are available through SQL
and can be used by any application speaking it.


## Learn

Learn how to use hybrid search techniques in CrateDB, using pure SQL.

:::{rubric} Articles
:::

:::::{info-card}
::::{grid-item}
:columns: auto 9 9 9
**Blog: Hybrid Search in CrateDB**

A common scenario is to combine semantic search ([vector search][nearest neighbor
search]) with lexical/term/keyword search ([inverted index] + [BM25]).

Semantic search excels at understanding the context of a phrase. Lexical search
is great at finding how many times a keyword or phrase appears in a document, taking
into account the length and the average length of your documents ([TF–IDF]).

The article will go through both search methods. You will learn how to combine them,
and how to apply different scoring and re-ranking techniques, all using CrateDB and
pure SQL.

{hyper-navigate}`Doing Hybrid Search in CrateDB <https://cratedb.com/blog/hybrid-search-explained>`
::::

::::{grid-item}
:columns: auto 3 3 3
:class: rubric-slim

{tags-primary}`Introduction` \
{tags-secondary}`Hybrid Search` \
{tags-secondary}`Pure SQL`

:::{rubric} What's Inside
:::
:::{div} text-smaller
- Full-Text Search ([BM25])
- Vector Search ([kNN]/[HNSW])
- [Convex Combination]
- [Reciprocal Rank Fusion (RRF)]
- SQL: [CTE], [JOIN], [RANK]
:::
::::

:::::


[Convex Combination]: https://en.wikipedia.org/wiki/Convex_combination
[Reciprocal Rank Fusion (RRF)]: https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html
