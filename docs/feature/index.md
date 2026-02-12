(feature)=
(features)=
(all-features)=
# All Features

:::{toctree}
:maxdepth: 1
:hidden:

Highlights <highlights>
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
:hidden:

query/index
generated/index
cursor/index
udf/index
ccr/index
:::

- {doc}`query/index`
- {doc}`generated/index`
- {doc}`cursor/index`
- {ref}`Foreign data wrappers <fdw>`
- {doc}`udf/index`
- {doc}`ccr/index`
+++
Advanced features supporting daily data
operations, all based on standard SQL.
::::

:::::


:::{rubric} Related sections
:::
Connect to CrateDB using traditional database drivers, and integrate CrateDB
with popular 3rd-party applications in open-source and proprietary software
landscapes.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

:::{grid-item-card} {material-outlined}`link;2em` Connectivity
:link: connect
:link-type: ref
:link-alt: About connectivity options with CrateDB

Connect to your CrateDB cluster using drivers, connectors,
adapters, and frameworks.
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
