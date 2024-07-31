(feature)=
(features)=
(all-features)=
# All Features

:::{include} /_include/styles.html
:::

All features of CrateDB at a glance.

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`lightbulb;2em` Functional
:::{toctree}
:maxdepth: 1

sql/index
connectivity/index
document/index
relational/index
Search: FTS, Geo, Vector, Hybrid <search/index>
blob/index
:::
+++
CrateDB combines the power of Lucene with the advantages of
industry-standard SQL.
::::

::::{grid-item-card} {material-outlined}`group;2em` Operational
:::{toctree}
:maxdepth: 1

cluster/index
snapshot/index
cloud/index
storage/index
index/index
:::
+++
CrateDB scales horizontally using a shared-nothing
architecture, inherited from Elasticsearch.
::::

::::{grid-item-card} {material-outlined}`read_more;2em` Advanced
:::{toctree}
:maxdepth: 1

query/index
generated/index
cursor/index
fdw/index
udf/index
ccr/index
:::
+++
Advanced features supporting daily data
operations, all based on standard SQL.
::::

:::::


:::{rubric} Connect and Integrate
:::
Connect to CrateDB using traditional database drivers, and integrate CrateDB
with popular 3rd-party applications in open-source and proprietary software
landscapes.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

:::{grid-item-card} {material-outlined}`link;2em` Connectivity
:link: connectivity
:link-type: ref
:link-alt: About connection options with CrateDB

Connect to your CrateDB cluster using drivers, frameworks, and adapters.
+++
**What's inside:**
Connectivity and integration options with database drivers
and applications, libraries, and frameworks.
:::


:::{grid-item-card} {material-outlined}`sync;2em` Import and Export
:link: import-export
:link-type: ref
:link-alt: About time series data import and export

Import data into and export data from your CrateDB cluster.
+++
**What's inside:**
A variety of options to connect and integrate with 3rd-party
ETL applications.
:::

::::


:::{rubric} Highlights
:::

Important fundamental features of CrateDB, and how they are applied within software
solutions and application platforms in different scenarios and environments.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2


:::{grid-item-card} {material-outlined}`description;2em` Document Store
:link: document
:link-type: ref
:link-alt: About CrateDB's OBJECT data type

Learn about CrateDB's OBJECT data type, how to efficiently store JSON
or other structured data, also nested, and how to query this data with
ease, fully indexed thus performant from the start, optionally using
relational joins.
+++
**What's inside:**
CrateDB can do the same like Lotus Notes / Domino, CouchDB, MongoDB,
and PostgreSQL's JSON data type.
:::


:::{grid-item-card} {material-outlined}`manage_search;2em` Full-Text Search
:link: fulltext
:link-type: ref
:link-alt: About CrateDB's full-text search capabilities

Learn about CrateDB's Okapi BM25 implementation, how to set up your database
for full-text search, and how to query text data efficiently, to make sense
of large volumes of unstructured information.
+++
**What's inside:**
Like Elasticsearch and Solr, CrateDB is based on Lucene, the premier
industry-grade full-text search engine library.
:::

::::


:::{rubric} Quotes
:::

> When using CrateDB, a project that got started around the same time, it's like
you've stumbled into an alternative reality where Elastic is a proper database.
>
> <small>-– Henrik Ingo, Nyrkiö Oy, independent database consultant, MongoDB</small>

> CrateDB enables use cases we couldn't satisfy with other
database systems, also with databases which are even stronger
focused on the time series domain.
>
> CrateDB is not your normal database!
>
> <small>-- Daniel Hölbling-Inzko, Director of Engineering Analytics, Bitmovin</small>
