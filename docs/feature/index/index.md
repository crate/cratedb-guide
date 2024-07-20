(convergent-index)=

# Convergent Index

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

**CrateDB indexes all columns by default,
for lightning-fast query responses on your fingertips.**

:::{rubric} Overview
:::
CrateDB, like Lucene, Elasticsearch, and Rockset, indexes all fields of stored
documents by default, yielding instant query performance on everything.

:::{rubric} About
:::
By default, CrateDB indexes all data in every field, and each indexed field has
a dedicated, optimized data structure. For example, text fields are stored in
inverted indices, and numeric and geo fields are stored in BKD trees.

The ability to use the per-field data structures to assemble and return search
results is what makes CrateDB so fast.

:::{rubric} Details
:::
For a quick refresh about the technologies behind the storage engine of CrateDB,
let us refer you to to a few upstream documentations and articles about Lucene
and Elasticsearch.

- [Searching and Indexing With Apache Lucene]
- [An Introduction to Elasticsearch]
- [Elasticsearch for Dummies]
- [Elasticsearch: Documents and Indices]

See also an article by Rockset, which refers to the same powerful indexing
regime, claiming that paradigm would be a unique invention.

- [Converged Index™: The Secret Sauce Behind Rockset's Fast Queries]

On disk, CrateDB stores data into Lucene indexes. By default, all fields are indexed,
nested or not, but the indexing can be turned off selectively.

- {ref}`storage-layer`
::::


::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Reference Manual
:::
- {ref}`crate-reference:fulltext-indices`
- {ref}`crate-reference:type-geo_shape-index`

{tags-primary}`Index Types`
{tags-primary}`Index Everything`
{tags-primary}`Fast Query Execution`
::::

:::::



## Usage

Handling data types in the most efficient way, for maximum usability, is built
into CrateDB. You automatically leverage its indexing data structures by
submitting SQL queries to the execution engine.


## Learn

Articles about CrateDB's uniqueness as an "index everything by default"
database, insights into the technologies behind, and also comparing it
with solutions from other vendors.



::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**Blog: Indexing and Storage in CrateDB**

{{ '{}[Indexing and Storage in CrateDB]'.format(blog) }}

Learn about the fundamentals of the CrateDB storage layer,
looking at the three main Lucene structures that are used within CrateDB:
Inverted Indexes for text values, BKD-trees for numeric values, and Doc Values.
:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Converged Indexing`
{tags-secondary}`Deep Dive`
:::
::::


::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**Blog: Time Series Benchmark on CrateDB and MongoDB**

{{ '{}[Time Series Benchmark on CrateDB and MongoDB]'.format(blog) }} {{ '{}[Independent comparison of CrateDB and MongoDB using Time Series Benchmark Suite]'.format(readmore) }}

> When using CrateDB – that got started as a project around those times [^es-advent] –
> it's like you've stumbled into an alternative reality where Elastic is a
> proper database.
> 
> -- Henrik Ingo, Nyrkiö Oy, independent database consultant, MongoDB

About the revolutionary idea to index all columns, in order to make all
queries equally fast, unlocking completely ad hoc exploratory querying.

> I knew that Rockset had developed a service where they would index every
> column by default, based on their innovative LSM indexing structure,
> making such a revolutionary idea even possible. CrateDB is now the
> second product I've heard of offering this feature – and now with
> Rockset being acquired and shutting down [...]

Also about benchmarking CrateDB against MongoDB using the [Distributed Systems
Infrastructure (DSI)] benchmark framework and the [TimescaleDB Time Series
Benchmark Suite (TSBS)].

[^es-advent]: In the advent of Elasticsearch, users dearly wanted to use it
as their primary and only database, but were educated not to.


:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Benchmark` \
{tags-secondary}`Converged Indexing`
{tags-secondary}`Query Performance`
:::
::::



:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
It only includes the most basic essentials, and needs expansion. For example,
the "Synopsis" section is missing completely, and the "Usage" section is a
bit thin.
:::


[An Introduction to Elasticsearch]: https://dzone.com/articles/an-introduction-to-elasticsearch
[Converged Index™: The Secret Sauce Behind Rockset's Fast Queries]: https://rockset.com/blog/converged-indexing-the-secret-sauce-behind-rocksets-fast-queries/
[Distributed Systems Infrastructure (DSI)]: https://github.com/nyrkio/dsi
[Elasticsearch for Dummies]: https://dzone.com/articles/elasticsearch-for-dummies
[Elasticsearch: Documents and Indices]: https://www.elastic.co/guide/en/elasticsearch/reference/current/documents-indices.html
[Independent comparison of CrateDB and MongoDB using Time Series Benchmark Suite]: https://blog.nyrkio.com/wp-content/uploads/2024/07/Nyrkio-comparison-of-CrateDB-and-MongoDB-with-TSBS-v2.pdf
[Indexing and Storage in CrateDB]: https://cratedb.com/blog/indexing-and-storage-in-cratedb
[Searching and Indexing With Apache Lucene]: https://dzone.com/articles/apache-lucene-a-high-performance-and-full-featured
[Time Series Benchmark on CrateDB and MongoDB]: https://blog.nyrkio.com/2024/07/11/timeseries-benchmark-on-cratedb-and-mongodb/
[TimescaleDB Time Series Benchmark Suite (TSBS)]: https://github.com/timescale/tsbs
