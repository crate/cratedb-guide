(use)=
(getting-started)=
# Getting Started

:::{div} sd-text-muted
Get up and running with CrateDB: Install, connect, run your first queries,
and explore key features.
:::

:::{rubric} Warm up
:::

:::::{grid} 2 2 2 4
:padding: 0
:class-container: installation-grid

::::{grid-item-card} First steps with CrateDB
:link: first-steps
:link-type: ref
:link-alt: First steps with CrateDB
:columns: 6 3 3 3
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`play`
::::

::::{grid-item-card} Connect to CrateDB
:link: connect
:link-type: ref
:link-alt: Connect to CrateDB
:columns: 6 3 3 3
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`link`
::::

::::{grid-item-card} Query Capabilities
:link: query-capabilities
:link-type: ref
:link-alt: Query Capabilities
:columns: 6 3 3 3
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`magnifying-glass`
::::

::::{grid-item-card} Ingesting Data
:link: ingest
:link-type: ref
:link-alt: Ingesting Data
:columns: 6 3 3 3
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`file-import`
::::
:::::

(start-going-further)=

:::{rubric} Learn more
:::

To learn more about CrateDB, we invite you to explore the other sections
of the documentation.

:::::{card}

::::{sd-table}
:widths: 4 8
:row-class: top-border

:::{sd-row}
```{sd-item} **Topic**
```
```{sd-item} **Description**
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
{ref}`Data modelling <data-modelling>`
```
```{sd-item}
Learn the different types of structured, semi-structured, and unstructured data.
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
{ref}`Query capabilities <query-capabilities>`
```
```{sd-item}
Explore CrateDB’s key query capabilities, such as aggregations, ad-hoc queries,
search and AI integration on large datasets at scale.
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
{ref}`Drivers <connect>`
```
```{sd-item}
Connect CrateDB to your applications using official drivers. Also explore CrateDB CLI tools.
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
{ref}`Integrations <integrate>`
```
```{sd-item}
Use CrateDB with third-party adapters, connectors, data sources, and integrations.
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
{ref}`Reference manual <crate-reference:index>`
```
```{sd-item}
Access the complete technical reference manual for CrateDB, and learn about
its concepts and details.
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
{ref}`Sample applications <example-applications>`
```
```{sd-item}
Explore ready-to-run sample projects that demonstrate how to build real-world solutions using CrateDB.
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
{ref}`Database management <administration>`
```
```{sd-item}
Learn to manage your cluster: configuration, sizing,
production deployment, migration and upgrade procedures,
sharding and partitioning, troubleshooting, user creation,
and cost optimization. Explore monitoring, alerting, and automation.
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
{ref}`performance`
```
```{sd-item}
Learn about best practices and recommendations to ensure optimal
system efficiency. Key points include performance tuning details around
selecting your sharding strategy, storage advice, and query optimization guidelines.
```
:::

:::{sd-row}
```{sd-item}
:class: sd-font-weight-bolder
[Support and learning ↗](https://learn.cratedb.com/)
```
```{sd-item}
Get access to more resources to continue learning.
```
:::

::::

:::::



```{toctree}
:maxdepth: 1
:hidden:

first-steps
modelling/index
query/index
Ingesting data <../ingest/index>
application/index
```


:::{note}
To learn more about all the details of CrateDB features, operations, and
its SQL dialect, please also visit the [All Features] page and the
[CrateDB Reference Manual].
:::


[All Features]: project:#features
[CrateDB Reference Manual]: inv:crate-reference:*:label#index
