(airflow)=
(astronomer)=
# Airflow / Astronomer

:::{include} /_include/links.md
:::

```{div} .float-right
[![Apache Airflow logo](https://19927462.fs1.hubspotusercontent-na1.net/hub/19927462/hubfs/Partner%20Logos/392x140/Apache-Airflow-Logo-392x140.png?width=784&height=280&name=Apache-Airflow-Logo-392x140.png){height=60px loading=lazy}][Apache Airflow]
```
```{div} .clearfix
```

:::{rubric} About
:::

:::{div}
[Apache Airflow] is an open source software platform to programmatically author,
schedule, and monitor workflows, written in Python.
[Astronomer] offers managed Airflow services on the cloud of your choice, to
run Airflow with less overhead.
:::

:::{dropdown} **Details**
Airflow has a modular architecture and uses a message queue to orchestrate an
arbitrary number of workers. Pipelines are defined in Python, allowing for
dynamic pipeline generation and on-demand, code-driven pipeline invocation.

Airflow parameterizes pipelines with the Jinja templating engine.
To extend the system, you can define your own operators and extend libraries
to fit the level of abstraction that suits your environment.
:::

:::{dropdown} **Managed Airflow**

```{div}
:style: "float: right"
[![Astronomer logo](https://logowik.com/content/uploads/images/astronomer2824.jpg){w=180px}](https://www.astronomer.io/)
```

[Astro][Astronomer] is a managed Airflow service.

- Astro runs on the cloud of your choice. Astro manages Airflow and gives you all the
  features you need to focus on what really matters – your data. All while connecting
  securely to any service in your network.
- Create Airflow environments quickly.
- Protect production DAGs with easy Airflow upgrades and custom high-availability configs.
- Get visibility into what’s running with analytics views and easy interfaces for logs
  and alerts. Across environments.
- Adopt Airflow best practices with support and timely upgrades.

```{div} .clearfix
```

:::

(airflow-tutorials)=

:::{rubric} Learn: Starter Tutorials
:::

::::{grid} 2

:::{grid-item-card} Getting started with Apache Airflow
:columns: 12
:link: airflow-getting-started
:link-type: ref
Define an Airflow DAG that downloads, processes, and stores data in CrateDB.
:::

:::{grid-item-card} Tutorial: Import Parquet files
:link: airflow-import-parquet
:link-type: ref
Define an Airflow DAG to import a Parquet file from S3 into CrateDB.
:::

:::{grid-item-card} Tutorial: Load stock market data
:link: airflow-import-stock-market-data
:link-type: ref
Define an Airflow DAG to download, process, and store stock market data
into CrateDB.
:::

::::


:::{rubric} Learn: Advanced Tutorials
:::

::::{grid} 3

:::{grid-item-card} Tutorial: Export to S3
:link: airflow-export-s3
:link-type: ref
Export data from CrateDB to S3 on a schedule.
:::

:::{grid-item-card} Tutorial: Implement a data retention policy
:link: airflow-data-retention-policy
:link-type: ref
An effective retention policy for time-series data, relating to the practice of
storing and managing data for a designated period of time.
:::

:::{grid-item-card} Tutorial: Implement a hot and cold storage data retention policy
:link: airflow-data-retention-hot-cold
:link-type: ref
A hot/cold storage strategy is often motivated by a tradeoff between performance
and cost-effectiveness.
:::

::::



```{seealso}
**Repository:** <https://github.com/crate/cratedb-airflow-tutorial>
<br>
**Product:** [CrateDB and Apache Airflow]
<br>
**Web:**
[ETL with Astro and CrateDB Cloud in 30min - fully up in the cloud] |
[ETL pipeline using Apache Airflow with CrateDB (Source)] |
[Run an ETL pipeline with CrateDB and data quality checks]
```


:::{toctree}
:maxdepth: 1
:hidden:
Getting started <getting-started>
Import Parquet files <import-parquet>
Import stock market data <import-stock-market-data>
Export to S3 <export-s3>
Data retention policy <data-retention-policy>
Hot/cold data retention <data-retention-hot-cold>
:::


[CrateDB and Apache Airflow]: https://cratedb.com/integrations/cratedb-and-apache-airflow
[ETL pipeline using Apache Airflow with CrateDB (Source)]: https://github.com/astronomer/astro-cratedb-blogpost
[ETL with Astro and CrateDB Cloud in 30min - fully up in the cloud]: https://www.astronomer.io/blog/run-etlelt-with-airflow-and-cratedb/
[Run an ETL pipeline with CrateDB and data quality checks]: https://registry.astronomer.io/dags/etl_pipeline/
