(handbook)=

# Handbook

:::{div} sd-text-muted
Use CrateDB and CrateDB Cloud in practice.
:::

:::{rubric} Instructions, how-to guides, tutorials, and explanations
:::

:::::{grid} 2 3 3 3
:gutter: 2
:padding: 0

::::{grid-item-card}
:link: install
:link-type: ref
{material-outlined}`download_for_offline;2em` &nbsp; **Install CrateDB**
+++
Install CrateDB on different operating systems and environments.
::::

::::{grid-item-card}
:link: connect
:link-type: ref
{material-outlined}`settings_input_svideo;2em` &nbsp; **Connect to CrateDB**
+++
Database drivers, libraries, adapters, and connectors.
::::

:::::


:::::{grid} 2 3 3 3
:gutter: 2
:padding: 0

::::{grid-item-card}
:link: howtos
:link-type: ref
{material-outlined}`integration_instructions;2em` &nbsp; **How-to guides**
+++
Instructions how to get tasks done with CrateDB.
::::

::::{grid-item-card}
:link: tutorials
:link-type: ref
{material-outlined}`school;2em` &nbsp; **Tutorials**
+++
Acquire skills and knowledge about CrateDB.
::::

::::{grid-item-card}
:link: explanations
:link-type: ref
{material-outlined}`lightbulb;2em` &nbsp; **Explanations**
+++
Broaden and deepen your knowledge and understanding of CrateDB.
::::

:::::

:::{rubric} Best practice guides
:::

:::::{grid} 2 3 3 3
:gutter: 2
:padding: 0

::::{grid-item-card}
:link: administration
:link-type: ref
{material-outlined}`manage_accounts;2em` &nbsp; **Administration**
+++
Best practices for administering CrateDB database clusters.
::::

::::{grid-item-card}
:link: performance
:link-type: ref
{material-outlined}`speed;2em` &nbsp; **Performance guides**
+++
Best practices and tips for sharding, scaling, and performance tuning.
::::

:::::

:::{rubric} Data loading / import / ingestion
:::

Load data from many sources into CrateDB.

:::::{grid} 2 3 3 3
:gutter: 2
:padding: 0

::::{grid-item-card}
:link: etl
:link-type: ref
{material-outlined}`transform;2em` &nbsp; **ETL**
+++
Load and export data into/from CrateDB.
Integrate CrateDB with ETL and ELT applications and frameworks.
::::

::::{grid-item-card}
:link: cdc
:link-type: ref
{material-outlined}`double_arrow;2em` &nbsp; **CDC**
+++
Change Data Capture (CDC) into CrateDB.
Integrate CrateDB with CDC applications and frameworks.
::::

::::{grid-item-card}
:link: telemetry
:link-type: ref
{material-outlined}`query_stats;2em` &nbsp; **Telemetry**
+++
Collect telemtry data into CrateDB.
Use CrateDB with metrics collection agents, brokers, and stores.
::::

:::::

## See also

:::{rubric} Solutions and topics
:::

::::{grid} 1 2 2 2
:gutter: 2
:padding: 0

:::{grid-item-card} {material-outlined}`lightbulb;2em` Solutions and use cases
:link: solutions
:link-type: ref
:link-alt: Solutions built with CrateDB
Learn how to use CrateDB for time series use-cases,
about industry solutions built with CrateDB and
how others are using CrateDB successfully with
both standard software components and in
proprietary system landscapes.
+++
**What's inside:**
Time series data. Industrial big data.
Real-time raw-data analytics. Machine learning.
:::

:::{grid-item-card} {material-outlined}`numbers;2em` Categories / Topics
:link: topics
:link-type: ref
:link-alt: CrateDB topics overview
Learn how to apply CrateDB's features to optimally cover
different application categories and topic domains.
For example, connect CrateDB with third-party
software applications, libraries, and frameworks.
+++
**What's inside:**
Business intelligence, data lineage, data migrations, data visualization,
programming frameworks, software testing.
:::

::::

:::{rubric} Feature highlights
:::

:::::{grid} 2 3 3 3
:gutter: 2
:padding: 0

::::{grid-item-card}
:link: document
:link-type: ref
{material-outlined}`article;2em` &nbsp; **Document store**
+++
Store JSON documents or other structured data, also nested, using
CrateDB’s OBJECT and ARRAY container data types.
::::

::::{grid-item-card}
:link: search-overview
:link-type: ref
{material-outlined}`manage_search;2em` &nbsp; **Search**
+++
Based on Apache Lucene, CrateDB offers native BM25 term search
and vector search, all using SQL.
::::

::::{grid-item-card}
:link: advanced-querying
:link-type: ref
{material-outlined}`engineering;2em` &nbsp; **Advanced querying**
+++
Mix full-text search with time series aspects, and run powerful
aggregations or other kinds of complex queries on your data.
::::

:::::


```{toctree}
:hidden:

../install/index
../connect/index
../howto/index
../tutorial/index
../explain/index
../admin/index
../performance/index
../feature/index
Ingestion <../ingest/index>
../topic/index
Solutions <../solution/index>
../integrate/index
```
