(feature)=
(features)=

# All Features

All features of CrateDB at a glance.

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`lightbulb;2em` Fundamentals
:::{toctree}
:maxdepth: 1
sql/index
relational/index
document/index
search/index
geospatial/index
vector/index
blob/index
:::
+++
CrateDB combines the advantages of traditional SQL databases with the
best properties of NoSQL databases.
::::

::::{grid-item-card} {material-outlined}`group;2em` Operational
:::{toctree}
:maxdepth: 1
cluster/index
snapshot/index
connectivity/index
cloud/index
:::
+++
CrateDB scales horizontally using a shared-nothing
architecture, inherited from Elasticsearch.
::::

::::{grid-item-card} {material-outlined}`read_more;2em` More
:::{toctree}
:maxdepth: 1
query/index
generated/index
fdw/index
udf/index
replication/index
:::
+++
Advanced features supporting daily data
operations, all based on standard SQL.
::::

:::::


:::{rubric} Features and Use Cases
:::

Foundational features of CrateDB, and how they are applied within software
solutions and application platforms in different scenarios and environments.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2


:::{grid-item-card} {material-outlined}`description;2em` Document Store
:link: document
:link-type: ref
:link-alt: About CrateDB's OBJECT data type

Learn how to use CrateDB's OBJECT data type to efficiently store JSON or
other structured data, also nested, and how to query this data with ease.
+++
**What's inside:**
CrateDB can do the same like Lotus Notes / Domino, CouchDB, MongoDB,
and PostgreSQL's JSON data type.
:::


:::{grid-item-card} {material-outlined}`manage_search;2em` Full-Text Search
:link: fulltext
:link-type: ref
:link-alt: About CrateDB's full-text search capabilities

Learn how to set up your database for full-text search, and how to query
text data efficiently, to make sense of large volumes of unstructured
information.
+++
**What's inside:**
Like Elasticsearch, CrateDB is based on Lucene, the premier industry-grade
full-text search engine library.
:::


::::


```{include} /_include/styles.html
```
