(rill)=
# Rill

```{div}
:style: "float: right;"
[![Rill logo](https://github.com/rilldata/rill/raw/main/docs/static/img/rill-logo-light.svg){h=60px}][Rill]
```
```{div}
:style: "clear: both"
```

:::{rubric} About
:::

[Rill] is an open-source operational BI framework for effortlessly transforming
data sets into powerful, opinionated dashboards using SQL.

Unlike most BI tools, Rill comes with its own embedded in-memory database. Data
and compute are co-located, and queries return in milliseconds. So you can pivot,
slice, and drill-down into your data instantly.

::::{dropdown} **Details**

Rill takes a modern approach to Business Intelligence (BI), which is starting to
leverage software engineering principles by implementing the concept of BI as
code.

This methodology allows for versioning and tracking, thus improving collaboration
on BI projects using code, which is more efficient and scalable than traditional
BI tools, also breaking down information and knowledge barriers.

:::{rubric} Rill's design principles
:::

- **Feels good to use** – powered by Sveltekit & DuckDB = conversation-fast, not
  wait-ten-seconds-for-result-set fast
- **Works with your local and remote datasets** – imports and exports Parquet and
  CSV (s3, gcs, https, local)
- **No more data analysis "side-quests"** – helps you build intuition about your
  dataset through automatic profiling
- **No "run query" button required** – responds to each keystroke by re-profiling
  the resulting dataset
- **Radically simple interactive dashboards** – thoughtful, opinionated, interactive
  dashboard defaults to help you quickly derive insights from your data
- **Dashboards as code** – each step from data to dashboard has versioning, Git
  sharing, and easy project rehydration

![](https://cdn.prod.website-files.com/659ddac460dbacbdc813b204/65b83308971b2f12202ae0fa_b2a470f529fc0f7d9b66de4d75742674.gif){h=200px}
![](https://cdn.prod.website-files.com/659ddac460dbacbdc813b204/65b835371c75806184829601_BI-as-code%20(1)-p-3200.webp){h=200px}

::::

:::{rubric} Learn
:::

::::{grid} 2

:::{grid-item-card} Rill and CrateDB
:link: https://community.cratedb.com/t/introducing-rill-and-bi-as-code-with-cratedb-cloud/1718
:link-type: url
Introducing Rill and BI as Code with CrateDB Cloud.
:::

::::


[Rill]: https://www.rilldata.com/
