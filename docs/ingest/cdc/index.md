(cdc)=
# Change Data Capture (CDC)

:::{include} /_include/links.md
:::

:::{div}
Options to integrate CrateDB with third‑party CDC applications, typically via
[CrateDB's PostgreSQL interface]. CrateDB also provides native adapter components
to leverage advanced features.

This section lists ETL applications and frameworks that work with CrateDB, and
outlines how to use them effectively. Additionally, see support for
{ref}`generic ETL <etl>` solutions.
:::


## Connectors

Native and specialized integration connectors for CrateDB, both managed and unmanaged.

:::::{grid} 3
:gutter: 2

::::{grid-item-card} Amazon DynamoDB
:link: dynamodb
:link-type: ref
Load data from DynamoDB, a fully managed NoSQL database service provided by
Amazon Web Services (AWS), which is designed for high-performance, scalable
applications and offers key-value and document data structures.
::::

::::{grid-item-card} Amazon Kinesis
:link: kinesis
:link-type: ref
Load data from Amazon Kinesis Data Streams, a serverless streaming data service
that simplifies the capture, processing, and storage of data streams at any scale.
::::

::::{grid-item-card} MongoDB
:link: mongodb
:link-type: ref
Load data from MongoDB or MongoDB Atlas, a document database, self-hosted
or multi-cloud.
::::

:::::


## Platforms

CrateDB supports popular third-party data integration frameworks and platforms,
both managed and unmanaged.

:::::{grid} 2
:gutter: 2

::::{grid-item-card} AWS DMS
:link: dms
:link-type: ref
Use AWS Database Migration Service (AWS DMS), a managed migration and replication
service that helps move your database and analytics workloads between different
kinds of databases.
::::

::::{grid-item-card} Debezium
:link: debezium
:link-type: ref
Use Debezium, an open source distributed platform for change data capture for
loading data into CrateDB.
It is used as a building block by a number of downstream third-party projects and products.
::::

::::{grid-item-card} Estuary
:link: estuary
:link-type: ref
Use Estuary Flow, a managed, real-time, reliable change data capture (CDC) solution,
to load data into CrateDB.
It combines agentless CDC, zero-code pipelines, and enterprise-grade governance to
simplify data integration.
::::

::::{grid-item-card} RisingWave
:link: risingwave
:link-type: ref
Use RisingWave, a stream processing and management platform, to load data into CrateDB.
It provides a Postgres-compatible SQL interface, like CrateDB, and a DataFrame-style
Python interface. It is available for on-premises and as a managed service.
::::

::::{grid-item-card} StreamSets
:link: streamsets
:link-type: ref
Use the StreamSets Data Collector Engine to ingest and transform data from many
sources into CrateDB. It runs on-premises or in any cloud.
::::

:::::
