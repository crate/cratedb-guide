(hybrid-search)=
# Hybrid Search

:::{rubric} Overview
:::
The capabilities of [](project:#vector-search) are impressive, but it isn't a
perfect technology. Without domain-specific datasets to fine-tune models
on, a traditional term-based search still has a few advantages.

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
- bm25 search, using `MATCH`
- geospatial search, using `MATCH`


## Synopsis
To give you an impression how a single-query hybrid search looks like.

The SQL expression uses common table expressions for a better structure,
and an inner-join to join results from both search methods into a single
result.

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

:::{tip}
The full example outlined below will also use a window function to assign a
rank to every row, using reciprocal rank fusion.
:::


## Learn

:::::{info-card}
::::{grid-item}
:columns: auto 9 9 9
**Hybrid Search in CrateDB**

{hyper-navigate}`Doing Hybrid Search in CrateDB <https://cratedb.com/blog/hybrid-search-explained>`

A common scenario is to combine semantic search (vector search) with lexical/term/keyword
search.

Semantic search excels at understanding the context of a phrase. Lexical search
is great at finding how many times a keyword or phrase appears in a document, taking
into account the length and the average length of your documents.

:::{rubric} What's Inside
:::
The article will go through both search methods bm25 and vector search. You will learn
about different re-ranking techniques, and how to apply them in CrateDB using pure SQL.

- Full-text search (BM25)
- Vector search (k-nearest neighbors)
- Convex combination
- Reciprocal rank fusion
- SQL: CTE, JOIN, RANK 

::::
::::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`Hybrid Search` \
{tags-secondary}`Pure SQL`
::::

:::::


:::{todo}
Bring page into the same shape like the others in this section.
:::
