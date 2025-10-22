(handbook)=

# Handbook

:::{div} sd-text-muted
About using CrateDB and CrateDB Cloud in practice.
:::


::::{grid} 2 2 4 4
:gutter: 2
:padding: 0

:::{grid-item-card} Getting Started
:link: getting-started
:link-type: ref
:link-alt: Getting started with CrateDB
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`rocket_launch;1.3em`
:::

:::{grid-item-card} Installation
:link: install
:link-type: ref
:link-alt: Installing CrateDB
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`download_for_offline;1.3em`
:::

:::{grid-item-card} Connect
:link: connect
:link-type: ref
:link-alt: Connecting to CrateDB
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`settings_input_svideo;1.3em`
:::

::::


## Learn

How-to guides, tutorials, and explanations.

::::{grid} 2 2 4 4
:gutter: 2
:padding: 0

:::{grid-item-card} How-to guides
:link: howtos
:link-type: ref
:link-alt: How-to guides about CrateDB
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`assistant_direction;1.3em`
:::

:::{grid-item-card} Tutorials
:link: tutorials
:link-type: ref
:link-alt: Tutorials about CrateDB
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`school;1.3em`
:::

:::{grid-item-card} Administration
:link: administration
:link-type: ref
:link-alt: CrateDB Administration
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`manage_accounts;1.3em`
:::

:::{grid-item-card} Performance guides
:link: performance
:link-type: ref
:link-alt: CrateDB Performance guides
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`speed;1.3em`
:::

::::


## Features

:::{rubric} Highlights
:::

::::{grid} 2 2 3 3
:gutter: 2
:padding: 0

:::{grid-item-card} Document Store
:link: document
:link-type: ref
:link-alt: Storing JSON documents using CrateDB's `OBJECT` data type
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`article;1.3em`
:::

:::{grid-item-card} Search
:link: search-overview
:link-type: ref
:link-alt: About CrateDB's search capabilities
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`manage_search;1.3em`
:::

:::{grid-item-card} Advanced Querying
:link: advanced-querying
:link-type: ref
:link-alt: About CrateDB's advanced querying capabilities
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`engineering;1.3em`
:::

::::

:::{card} All features
:link: all-features
:link-type: ref

CrateDB is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries. It is
based on Lucene, combines a unique set of features, and is PostgreSQL-compatible.

![CrateDB feature overview diagram](https://cratedb.com/hs-fs/hubfs/nativesql.png?width=800&name=nativesql.png)
+++
Read about all features of CrateDB at a glance.
:::


## Data ingestion

Load data from many sources into CrateDB.

::::{grid} 2 2 3 3
:gutter: 2
:padding: 0

:::{grid-item-card} ETL
:link: etl
:link-type: ref
:link-alt: Load and export data into/from CrateDB
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`transform;1.3em`
:::

:::{grid-item-card} CDC
:link: cdc
:link-type: ref
:link-alt: Change Data Capture (CDC) into CrateDB
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`double_arrow;1.3em`
:::

:::{grid-item-card} Telemetry
:link: telemetry
:link-type: ref
:link-alt: Use CrateDB with metrics collection agents, brokers, and stores
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5
{material-outlined}`query_stats;1.3em`
:::

::::


## Solutions and topics

::::{grid} 1 2 2 2
:gutter: 2
:padding: 0

:::{grid-item-card} {material-outlined}`lightbulb;2em` Solutions and use cases
:link: solutions
:link-type: ref
:link-alt: Solutions built with CrateDB
Learn about solutions built with CrateDB and
how others are using CrateDB successfully.
+++
**What's inside:**
Full-text and semantic search, real-time raw-data analytics,
industrial data, machine learning, data migrations.
:::

:::{grid-item-card} {material-outlined}`numbers;2em` Topics
:link: topics
:link-type: ref
:link-alt: CrateDB topics overview
Learn how to apply CrateDB's features to optimally cover use-cases
across different application and topic domains.
For example, connect CrateDB with third-party
software applications, libraries, and frameworks.
+++
**What's inside:**
Business intelligence, data lineage, data visualization,
programming frameworks, software testing, time series data.
:::

::::



```{toctree}
:hidden:

../install/index
../connect/index
../howto/index
../tutorial/index
../admin/index
../performance/index
../feature/index
Ingestion <../ingest/index>
../topic/index
Solutions <../solution/index>
../integrate/index
```
