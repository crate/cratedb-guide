(search-overview)=
# Search

:::{include} /_include/styles.html
:::

Based on Apache Lucene, CrateDB offers native BM25 term search and vector
search, all using SQL. By combining it, also using SQL, you can implement
powerful single-query hybrid search.

:::{rubric} All search features of CrateDB at a glance.
:::

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`search;2em` Full-Text Search
:link: fts
:link-type: ref
Inverted index and Okapi BM25 search ranking based on Apache Lucene
at scale, using SQL as lingua franca.
+++
BM25 term search using SQL: CrateDB is all you need.
::::

::::{grid-item-card} {material-outlined}`psychology_alt;2em` Vector Search
:link: vector-search
:link-type: ref
HNSW data retrieval on ML vector embeddings
enables semantic search on your fingertips,
using standard SQL.
+++
Vector search on machine learning embeddings: CrateDB is all you need.
::::

::::{grid-item-card} {material-outlined}`lightbulb;2em` Hybrid Search
:link: hybrid-search
:link-type: ref
Combines FTS and HNSW technologies, and unlocks the best of both worlds
in term-based and semantic search.
+++
Enhance relevancy and accuracy by combining multiple search algorithms.
::::

:::::


:::{toctree}
:maxdepth: 2
:hidden:

fts
vector
hybrid
:::
