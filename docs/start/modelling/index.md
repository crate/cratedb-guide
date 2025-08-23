(modelling)=
(data-modelling)=
# Data modelling

:::{div} sd-text-muted
CrateDB provides a unified storage engine that supports different data types.
:::

:::::{grid} 2 3 3 3
:padding: 0
:class-container: installation-grid

::::{grid-item-card} Relational data
:link: model-relational
:link-type: ref
:link-alt: Relational data
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`table-list`
::::

::::{grid-item-card} JSON data
:link: model-json
:link-type: ref
:link-alt: JSON data
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`file-lines`
::::

::::{grid-item-card} Timeseries data
:link: model-timeseries
:link-type: ref
:link-alt: Timeseries data
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`timeline`
::::

::::{grid-item-card} Geospatial data
:link: model-geospatial
:link-type: ref
:link-alt: Geospatial data
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`globe`
::::

::::{grid-item-card} Fulltext data
:link: model-fulltext
:link-type: ref
:link-alt: Fulltext data
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`font`
::::

::::{grid-item-card} Vector data
:link: model-vector
:link-type: ref
:link-alt: Vector data
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

{fas}`lightbulb`
::::

:::::


```{toctree}
:maxdepth: 1
:hidden:

relational
json
timeseries
geospatial
fulltext
vector
```

:::{rubric} Implementation notes
:::

Because CrateDB is a distributed analytical database (OLAP) designed to store
large volumes of data, users need to consider certain details compared to
traditional RDBMS.


:::{card} Primary key strategies
:link: model-primary-key
:link-type: ref
CrateDB is built for horizontal scalability and high ingestion throughput.
+++
To achieve this, operations must complete independently on each node—without
central coordination. This design choice means CrateDB does not support
traditional auto-incrementing primary key types like `SERIAL` in PostgreSQL
or MySQL by default.
:::

```{toctree}
:maxdepth: 1
:hidden:

primary-key
```
