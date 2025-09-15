(etl)=
(io)=
(import-export)=
# Load and Export (ETL)

:::{include} /_include/links.md
:::

:::{div}
Options to integrate CrateDB with third‑party ETL applications, typically via
[CrateDB's PostgreSQL interface]. CrateDB also provides native adapter components
to leverage advanced features.

This section lists ETL applications and frameworks that work with CrateDB, and
outlines how to use them effectively. Additionally, see support for {ref}`cdc` solutions.
:::

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`storage;2em` Databases
- {ref}`dms`
- {ref}`dynamodb`
- {ref}`influxdb`
- {ref}`mongodb`
- {ref}`mysql`
- {ref}`oracle`
- {ref}`postgresql`
- {ref}`sql-server`
+++
Load data from database systems.
::::

::::{grid-item-card} {material-outlined}`fast_forward;2em` Streams
- {ref}`amqp`
- {ref}`kafka`
- {ref}`kinesis`
- {ref}`mqtt`
- {ref}`risingwave`
- {ref}`streamsets`
+++
Load data from streaming platforms.
::::

::::{grid-item-card} {material-outlined}`air;2em` Dataflow / Pipeline / Code-first
- {ref}`airflow`
- {ref}`dbt`
- {ref}`dlt`
- {ref}`flink`
- {ref}`ingestr`
- {ref}`kestra`
- {ref}`meltano`
- {ref}`nifi`
+++
Use data pipeline programming frameworks and platforms.
::::

::::{grid-item-card} {material-outlined}`all_inclusive;2em` Low-code / No-code / Visual
- {ref}`estuary`
- {ref}`hop`
- {ref}`n8n`
- {ref}`node-red`
+++
Use visual data flow and integration frameworks and platforms.
::::

::::{grid-item-card} {material-outlined}`add_to_queue;2em` Serverless Compute
- {ref}`aws-lambda`
- {ref}`azure-functions`
+++
Use serverless compute units for custom import tasks.
::::

::::{grid-item-card} {material-outlined}`dataset;2em` Datasets
- {ref}`iceberg`
+++
Load data from datasets and open table formats.
::::

:::::
