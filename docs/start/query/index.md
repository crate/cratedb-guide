(start-query)=
(query-capabilities)=
# Query capabilities

:::{div} sd-text-muted
SQL is all you need.
:::

SQL is the most widely used language for querying data and is the natural
choice for people in many roles working with data in databases.

CrateDB extends industry-standard SQL with features to support its
data types, data I/O procedures, and cluster management.


::::{grid} 2
:gutter: 2

:::{grid-item-card} Aggregations
:link: aggregations
:link-type: ref
CrateDB is designed to deliver high-performance aggregations on massive volumes of data—in real time and using familiar SQL syntax.
:::

:::{grid-item-card} Ad-hoc queries
:link: ad-hoc-queries
:link-type: ref
CrateDB is built to support highly dynamic, ad-hoc querying, even on large-scale, real-time datasets.
:::

:::{grid-item-card} Search
:link: search-overview
:link-type: ref
Based on Apache Lucene, CrateDB offers native BM25 term search and vector search, all using SQL. Combine both—still using SQL—to implement powerful single‑query hybrid search.
:::

:::{grid-item-card} AI integration
:link: ai-integration
:link-type: ref
CrateDB is not just a real-time analytics database, it’s a powerful platform to feed and interact with machine learning models, thanks to its ability to store, query, and transform structured, unstructured, and vectorized data at scale using standard SQL.
:::

::::

```{toctree}
:maxdepth: 1
:hidden:

aggregations
ad-hoc
../../feature/search/index
ai-integration
```

:::{seealso}
To learn more, check out the {ref}`SQL introduction <sql>`, {ref}`advanced-querying`
tutorials, and the {ref}`SQL syntax reference manual <crate-reference:sql>`.
:::
