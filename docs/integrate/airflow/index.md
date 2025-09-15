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

Pipeline parameterization is using the powerful Jinja templating engine.
To extend the system, you can define your own operators and extend libraries
to fit the level of abstraction that suits your environment.
:::

:::{dropdown} **Managed Airflow**

```{div}
:style: "float: right"
[![Astronomer logo](https://logowik.com/content/uploads/images/astronomer2824.jpg){w=180px}](https://www.astronomer.io/)
```

[Astro][Astronomer] is the best managed service in the market for teams on any step of their data
journey. Spend time where it counts.

- Astro runs on the cloud of your choice. Astro manages Airflow and gives you all the
  features you need to focus on what really matters – your data. All while connecting
  securely to any service in your network.
- Create Airflow environments with a click of a button.
- Protect production DAGs with easy Airflow upgrades and custom high-availability configs.
- Get visibility into what’s running with analytics views and easy interfaces for logs
  and alerts. Across environments.
- Take down tech-debt and learn how to drive Airflow best practices from the experts
  behind the project. Get world-class support, fast-tracked bug fixes, and same-day
  access to new Airflow versions.

```{div} .clearfix
```

:::


:::{rubric} Learn: Starter Tutorials
:::

::::{grid} 2

:::{grid-item-card} Tutorial: Import Parquet files
:link: https://community.cratedb.com/t/automating-the-import-of-parquet-files-with-apache-airflow/1247
:link-type: url
Define an Airflow DAG to import a Parquet file from S3 into CrateDB.
:::

:::{grid-item-card} Tutorial: Load stock market data
:link: https://community.cratedb.com/t/updating-stock-market-data-automatically-with-cratedb-and-apache-airflow/1304
:link-type: url
Define an Airflow DAG to download, process, and store stock market data
into CrateDB.
:::

::::


:::{rubric} Learn: Advanced Tutorials
:::

::::{grid} 3

:::{grid-item-card} Tutorial: Export to S3
:link: https://community.cratedb.com/t/cratedb-and-apache-airflow-automating-data-export-to-s3/901
:link-type: url
Recurrently export data from CrateDB to S3.
:::

:::{grid-item-card} Tutorial: Implement a data retention policy
:link: https://community.cratedb.com/t/implementing-a-data-retention-policy-in-cratedb-using-apache-airflow/913
:link-type: url
An effective retention policy for time-series data, relating to the practice of
storing and managing data for a designated period of time.
:::

:::{grid-item-card} Tutorial: Implement a hot and cold storage data retention policy
:link: https://community.cratedb.com/t/cratedb-and-apache-airflow-building-a-hot-cold-storage-data-retention-policy/934
:link-type: url
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


[CrateDB and Apache Airflow]: https://cratedb.com/integrations/cratedb-and-apache-airflow
[ETL pipeline using Apache Airflow with CrateDB (Source)]: https://github.com/astronomer/astro-cratedb-blogpost
[ETL with Astro and CrateDB Cloud in 30min - fully up in the cloud]: https://www.astronomer.io/blog/run-etlelt-with-airflow-and-cratedb/
[Run an ETL pipeline with CrateDB and data quality checks]: https://registry.astronomer.io/dags/etl_pipeline/
