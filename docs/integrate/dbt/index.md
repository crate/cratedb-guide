(dbt)=

# dbt

```{div}
:style: "float: right"
[![](https://www.getdbt.com/ui/img/logos/dbt-logo.svg){w=180px}](https://www.getdbt.com/)
```

[dbt] is an open source tool for transforming data in data warehouses using Python and
SQL. It is an SQL-first transformation workflow platform that lets teams quickly and
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

![](https://www.getdbt.com/ui/img/products/what-is-dbt-main-image.png){h=120px}
![](https://www.getdbt.com/ui/img/products/what-is-dbt-deploy.svg){h=120px}
![](https://www.getdbt.com/ui/img/products/what-is-dbt-eliminate-silos.svg){h=120px}

:::{dropdown} **Managed dbt**
```{div}
:style: "float: right"
[![](https://www.getdbt.com/ui/img/hero-dbt-cloud-features-2x5.png){w=180px}](https://www.getdbt.com/product/dbt-cloud/)
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


## Install
Install the most recent version of the [dbt-cratedb2] Python package.
```shell
pip install --upgrade 'dbt-cratedb2'
```


## Connect
**dbt Profile Configuration:** CrateDB targets should be set up using the
following configuration in your `profiles.yml` file.
```yaml
company-name:
  target: dev
  outputs:
    dev:
      type: cratedb
      host: [hostname]
      user: [username]
      password: [password]
      port: [port]   # Default is 5432.
      dbname: crate  # Fixed. Do not change.
      schema: doc    # `doc` is the default schema.
```
dbt-cratedb2 is based on dbt-postgres, which uses [psycopg2] to connect to
the database server.
Because CrateDB is compatible with PostgreSQL, the same connectivity
options apply like outlined on the [dbt Postgres Setup] documentation
page.


## Learn

:::{rubric} Tutorials
:::
- [Using dbt with CrateDB]

:::{rubric} Development
:::
- [dbt CrateDB examples]


:::{rubric} Webinars
:::

::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Intro to Data Build Tool (dbt)**

Learn how to get started using dbt (data-build-tool) by following along
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
[dbt-cratedb2]: https://pypi.org/project/dbt-cratedb2/
[dbt Cloud]: https://www.getdbt.com/product/dbt-cloud/
[dbt Postgres Setup]: https://docs.getdbt.com/docs/core/connect-data-platform/postgres-setup
[Using dbt with CrateDB]: https://community.cratedb.com/t/using-dbt-with-cratedb/1566
[dbt CrateDB examples]: https://github.com/crate/cratedb-examples/tree/main/framework/dbt/
[psycopg2]: https://pypi.org/project/psycopg2/
