(cdc)=
# Change Data Capture (CDC)

:::{include} /_include/links.md
:::

:::{div}
You have a variety of options to connect and integrate with 3rd-party
CDC applications, mostly using [CrateDB's PostgreSQL interface].

CrateDB also provides a few native adapter components, that can be used
to leverage its advanced features. 

This documentation section lists corresponding CDC applications and
frameworks which can be used together with CrateDB, and outlines how
to use them optimally.
Please also have a look at support for [generic ETL](#etl) solutions.
:::

## Debezium
Debezium is an open source distributed platform for change data capture (CDC).
It is built on top of Apache Kafka, a distributed streaming platform. It allows
to capture changes on a source database system, mostly OLTP, and replicate them
to another system, mostly to run OLAP workloads on the data.

Debezium provides connectors for MySQL/MariaDB, MongoDB, PostgreSQL, Oracle,
SQL Server, IBM DB2, Cassandra, Vitess, Spanner, JDBC, and Informix.

- [Tutorial: Replicating data to CrateDB with Debezium and Kafka]
- [Webinar: How to replicate data from other databases to CrateDB with Debezium and Kafka]

## DynamoDB
:::{div}
Tap into [Amazon DynamoDB Streams], to replicate CDC events from DynamoDB into CrateDB,
with support for CrateDB's container data types.
- {hyper-open}`Documentation <[DynamoDB CDC Relay]>`
- {hyper-read-more}`Blog <[Replicating CDC events from DynamoDB to CrateDB]>`
:::

## MongoDB
:::{div}
Tap into [MongoDB Change Streams], to relay CDC events from MongoDB into CrateDB,
with support for CrateDB's container data types.
- {hyper-open}`Documentation <[MongoDB CDC Relay]>`
:::

## StreamSets

The [StreamSets Data Collector] is a lightweight and powerful engine that
allows you to build streaming, batch and change-data-capture (CDC) pipelines
that can ingest and transform data from a variety of different sources.

StreamSets Data Collector Engine makes it easy to run data pipelines from Kafka,
Oracle, Salesforce, JDBC, Hive, and more to Snowflake, Databricks, S3, ADLS, Kafka
and more. Data Collector Engine runs on-premises or any cloud, wherever your data
lives.

- {ref}`streamsets`



[Tutorial: Replicating data to CrateDB with Debezium and Kafka]: https://community.cratedb.com/t/replicating-data-to-cratedb-with-debezium-and-kafka/1388
[Webinar: How to replicate data from other databases to CrateDB with Debezium and Kafka]: https://cratedb.com/resources/webinars/lp-wb-debezium-kafka
[StreamSets Data Collector]: https://www.softwareag.com/en_corporate/platform/integration-apis/data-collector-engine.html
