(search-overview)=
# Search

Based on Apache Lucene, CrateDB offers native BM25 term search and vector
search, all using SQL. By combining it, also using SQL, you can implement
powerful single-query hybrid search.

:::{rubric} All search features of CrateDB at a glance.
:::

:::::{grid} auto 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`search;2em` Full-Text Search
:link: fulltext-search
:link-type: ref
Inverted index and Okapi BM25 search ranking based on Apache Lucene
at scale, using SQL as lingua franca.
+++
BM25 term search using SQL: CrateDB is all you need.
::::

::::{grid-item-card} {material-outlined}`travel_explore;2em` Geo Search
:link: geo-search
:link-type: ref
Supports location data for efficiently storing and querying geographic
and spatial/geospatial data.
+++
Geospatial search is based on BKD tree index structures.
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
:columns: auto
Combines FTS and HNSW technologies, unlocking the best of both worlds
in term-based and semantic search.
+++
Enhance relevancy and accuracy by combining multiple search algorithms.
::::

:::::


:::{toctree}
:maxdepth: 2
:hidden:

fts/index
geo/index
vector/index
hybrid/index
:::
