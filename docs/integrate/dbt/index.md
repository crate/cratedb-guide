(dbt)=
# dbt

:::{include} /_include/links.md
:::

## About
```{div}
:style: "float: right"
[![](https://www.getdbt.com/_next/image?url=%2Fimg%2Flogos%2Fdbt-labs-logo.svg&w=384&q=75){w=180px}](https://www.getdbt.com/)
```

[dbt] is a tool for transforming data in data warehouses using Python and SQL.

It is an SQL-first transformation workflow platform that lets teams quickly and
collaboratively deploy analytics code following software engineering best practices
like modularity, portability, CI/CD, and documentation.

> dbt enables data analysts and engineers to transform their data using the same
> practices that software engineers use to build applications.

With dbt, anyone on your data team can safely contribute to production-grade data
pipelines.

The idea is that data engineers make source data available to an environment where
dbt projects run, for example with [Debezium](#debezium) or with [Airflow](#apache-airflow).
Afterwards, data analysts can run their dbt projects against this data to produce models
(tables and views) that can be used with a number of [BI tools](#bi-tools).

![](https://www.getdbt.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fwl0ndo6t%2Fmain%2F6e98931b83c4b8bbe45751dced66bc80ea4ec9ac-1999x992.png%3Ffit%3Dmax%26auto%3Dformat&w=640&q=75){h=120px}
![](https://www.getdbt.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fwl0ndo6t%2Fmain%2Fcd8cba01b3f756a3a7ed194e6e2d6a4072fac194-1220x1200.png%3Ffit%3Dmax%26auto%3Dformat&w=640&q=75){h=120px}
![](https://www.getdbt.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fwl0ndo6t%2Fmain%2F58b87e47c2aed57fde9ccd49c927c3dff5b57d3c-1466x1130.png%3Ffit%3Dmax%26auto%3Dformat&w=640&q=75){h=120px}

:::{dropdown} **Managed dbt**
```{div}
:style: "float: right"
[![](https://www.getdbt.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fwl0ndo6t%2Fmain%2Fc24fbc41bfc3ddb7fcc64932be56f0836fd355c8-1771x780.png%3Ffit%3Dmax%26auto%3Dformat&w=640&q=75){w=180px}](https://www.getdbt.com/product/dbt-cloud/)
```

With [dbt Cloud], you can ditch time-consuming setup, and the struggles
of scaling your data production. dbt Cloud is a full-suite service that is built for
scale.

- Start building data products quickly using the dbt Cloud IDE with integrated security
  and governance controls.
- Schedule, deploy, and monitor your data products using the scalable and reliable dbt
  Cloud Scheduler.
- Help your data teams discover and reuse data products using hosted docs or integrations
  with the powerful Discovery API.
- Extend your workflow beyond dbt Cloud with 30+ seamless integrations covering a range
  of use cases across the Modern Data Stack, from observability and data quality to
  visualization, reverse ETL, and much more.
- Ship more high-quality data and scale your development like the 1000s of companies that
  use dbt Cloud. They’ve used its convenient and collaboration-friendly interface to
  eliminate the bottlenecks that keep growth limited.

```{div}
:style: "clear: both"
```
:::


### dbt's Features
The data abstraction layer provided by [dbt-core] allows the decoupling of
the models on which reports and dashboards rely from the source data. When
business rules or source systems change, you can still maintain the same models
as a stable interface.

Some of the things that dbt can do include:

* Import reference data from CSV files.
* Track changes in source data with different strategies so that downstream
  models do not need to be built every time from scratch.
* Run tests on data, to confirm assumptions remain valid, and to validate
  any changes made to the models' logic.

### CrateDB's Benefits
Due to its unique capabilities, CrateDB is an excellent warehouse choice for
data transformation projects. It offers automatic indexing, fast aggregations,
easy partitioning, and the ability to scale horizontally.


## Setup
Install the most recent version of the [dbt-cratedb2] Python package.
```shell
pip install --upgrade 'dbt-cratedb2'
```


## Configure
Because CrateDB is compatible with PostgreSQL, the same connectivity
options apply like outlined on the [dbt Postgres Setup] documentation
page.

The dbt connection profile settings for CrateDB stored in [`profiles.yml`]
are identical with PostgreSQL.
```yaml
cratedb_analytics:
  target: dev
  outputs:
    dev:
      type: cratedb
      host: [clustername].aks1.westeurope.azure.cratedb.net
      port: 5432
      user: [username]
      pass: [password]
      dbname: crate     # CrateDB's only catalog is `crate`.
      schema: doc       # Define schema. `doc` is the default.
      search_path: doc  # Use the same value like `schema` by default.
```


## Learn

Learn how to use CrateDB with dbt by exploring concise examples.

:::{rubric} Tutorials
:::

::::{grid} 2
:gutter: 5

:::{grid-item-card}
:link: dbt-usage
:link-type: ref
:link-alt: dbt usage guidelines
:padding: 3
:class-card: sd-text-center sd-pt-4
:class-header: sd-fs-4
{material-outlined}`integration_instructions;2.5em`
Usage Guidelines
^^^
```{toctree}
:maxdepth: 2
:hidden:

usage
```
+++
Usage guidelines, notes, and advanced configuration options.
:::

:::{grid-item-card}
:link: https://github.com/crate/cratedb-examples/tree/main/framework/dbt/
:link-type: url
:link-alt: dbt CrateDB Examples
:padding: 3
:class-card: sd-text-center sd-pt-4
:class-header: sd-fs-4
{material-outlined}`apps;2.5em`
Example Projects
^^^
+++
Explore a few dbt example projects using CrateDB.
:::

::::


:::{rubric} Webinars
:::

::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Introduction to dbt**

Learn how to get started using dbt by following along
with an easy step-by-step tutorial.

In this video, you will learn how to install dbt, initialize a new project
and then publish your project to a GitHub repository.
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/5rNquRnNb4E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Webinar`
{tags-secondary}`Fundamentals`
:::

::::


[dbt]: https://www.getdbt.com/
[dbt-core]: https://github.com/dbt-labs/dbt-core
[dbt-cratedb2]: https://pypi.org/project/dbt-cratedb2/
[dbt Cloud]: https://www.getdbt.com/product/dbt-cloud/
[dbt Postgres Setup]: https://docs.getdbt.com/docs/core/connect-data-platform/postgres-setup
[`profiles.yml`]: https://docs.getdbt.com/docs/core/connect-data-platform/profiles.yml
