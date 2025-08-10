(etl)=
(io)=
(import-export)=
# Load and Export (ETL)

:::{include} /_include/links.md
:::

:::{div}
Options to connect and integrate CrateDB with third-party
ETL applications, mostly using [CrateDB's PostgreSQL interface].
CrateDB also provides native adapter components to leverage advanced
features.

This documentation section lists ETL applications and
frameworks which can be used together with CrateDB, and outlines how
to use them optimally.
Additionally, see support for {ref}`cdc` solutions.
:::


:::{rubric} Grouped by category
:::

:::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2
:class-container: ul-li-wide


::::{grid-item-card} {material-outlined}`air;2em` Dataflow / Pipeline / Code-first
- {ref}`apache-airflow`

  Apache Airflow is an open-source software platform to programmatically author,
  schedule, and monitor workflows. Pipelines are defined in Python, allowing for
  dynamic pipeline generation and on-demand, code-driven pipeline invocation.

- {ref}`apache-flink`

  Apache Flink is a programming framework and distributed processing engine for
  stateful computations over unbounded and bounded data streams, written in Java.

- {ref}`apache-nifi`

  Apache NiFi is a dataflow system based on the concepts of flow-based programming.
  It supports powerful and scalable directed graphs of data routing, transformation,
  and system mediation logic.

- {ref}`dbt`

  dbt is an SQL-first platform for transforming data in data warehouses using
  Python and SQL. The data abstraction layer provided by dbt-core allows the
  decoupling of the models on which reports and dashboards rely from the source data.

- {ref}`kestra`

  Kestra is an open-source workflow automation and orchestration toolkit with a rich
  plugin ecosystem. It enables users to automate and manage complex workflows in a
  streamlined and efficient manner, defining them both declaratively, or imperatively
  using any scripting language like Python, Bash, or JavaScript.

- {ref}`meltano`

  Meltano is a declarative code-first polyglot data integration engine adhering to
  the Singer specification. Singer is a composable open-source ETL framework and
  specification, including powerful data extraction and consolidation elements.

+++
Data pipeline programming frameworks and platforms.
::::


::::{grid-item-card} {material-outlined}`all_inclusive;2em` Low-code / No-code / Visual
- {ref}`apache-hop`

  Apache Hop aims to be the future of data integration. Visual development enables
  developers to be more productive than they can be through code.

- {ref}`estuary`

  Estuary provides real-time data integration and modern ETL and ELT data pipelines
  as a fully managed solution. Estuary Flow is a real-time, reliable change data
  capture (CDC) solution.

- {ref}`n8n`

  n8n is a workflow automation tool that helps you to connect any app with an API with
  any other, and manipulate its data with little or no code.

- {ref}`node-red`

  Node-RED is an open-source programming tool for wiring together hardware devices,
  APIs and online services within a low-code programming environment for event-driven
  applications.

+++
Visual data flow and integration frameworks and platforms.
::::


::::{grid-item-card} {material-outlined}`storage;2em` Databases
- {ref}`aws-dms`

  AWS DMS is a managed migration and replication service that helps move your
  database and analytics workloads between different kinds of databases quickly,
  securely, and with minimal downtime and zero data loss.

- {ref}`aws-dynamodb`

  DynamoDB is a fully managed NoSQL database service provided by Amazon Web Services (AWS).

- {ref}`influxdb`

  InfluxDB is a scalable datastore for metrics, events, and real-time analytics to
  collect, process, transform, and store event and time series data.

- {ref}`mongodb`

  MongoDB is a document database designed for ease of application development and scaling.

- {ref}`mysql`

  MySQL and MariaDB are well-known free and open-source relational database management
  systems (RDBMS), available as standalone and managed variants.

- {ref}`sql-server`

  Microsoft SQL Server Integration Services (SSIS) is a component of the Microsoft SQL
  Server database software that can be used to perform a broad range of data migration tasks.

+++
Load data from database systems.
::::


::::{grid-item-card} {material-outlined}`fast_forward;2em` Streams
- {ref}`apache-kafka`

  Apache Kafka is an open-source distributed event streaming platform
  for high-performance data pipelines, streaming analytics, data integration,
  and mission-critical applications.

- {ref}`aws-kinesis`

  Amazon Kinesis Data Streams is a serverless streaming data service that simplifies
  the capture, processing, and storage of data streams at any scale, such as
  application logs, website clickstreams, and IoT telemetry data, for machine
  learning (ML), analytics, and other applications.

- {ref}`risingwave`

  RisingWave is a stream processing and management platform that allows configuring
  data sources, views on that data, and destinations where results are materialized.
  It provides both a Postgres-compatible SQL interface, like CrateDB, and a
  DataFrame-style Python interface.
  It delivers low-latency insights from real-time streams, database CDC, and
  time-series data, bringing streaming and batch together.

- {ref}`streamsets`

  The StreamSets Data Collector is a lightweight and powerful engine that allows you
  to build streaming, batch, and change-data-capture (CDC) pipelines that can ingest
  and transform data from many sources.

+++
Load data from streaming platforms.
::::


::::{grid-item-card} {material-outlined}`add_to_queue;2em` Serverless Compute
- {ref}`aws-lambda`

  AWS Lambda is a serverless compute service that runs your code in response to
  events and automatically manages the underlying compute resources for you. These
  events may include changes in state or an update.

- {ref}`azure-functions`

  An Azure Function is a short-lived, serverless computation that is triggered by
  external events. The trigger produces an input payload, which is delivered to
  the Azure Function. The Azure Function then does computation with this payload
  and subsequently outputs its result to other Azure Functions, computation
  services, or storage services.
+++
Use serverless compute units for custom import tasks.
::::


::::{grid-item-card} {material-outlined}`dataset;2em` Datasets

- {ref}`apache-iceberg`

  Apache Iceberg is an open table format for analytic datasets.

+++
Load data from datasets and open table formats.
::::


:::::


:::{rubric} Alphabetically sorted
:::

:::{div}
- {ref}`apache-airflow`
- {ref}`apache-flink`
- {ref}`apache-hop`
- {ref}`apache-iceberg`
- {ref}`apache-kafka`
- {ref}`apache-nifi`
- {ref}`aws-dynamodb`
- {ref}`aws-kinesis`
- {ref}`aws-dms`
- {ref}`aws-lambda`
- {ref}`azure-functions`
- {ref}`dbt`
- {ref}`estuary`
- {ref}`influxdb`
- {ref}`kestra`
- {ref}`meltano`
- {ref}`mongodb`
- {ref}`mysql`
- {ref}`n8n`
- {ref}`node-red`
- {ref}`risingwave`
- {ref}`sql-server`
- {ref}`streamsets`
:::
