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

## Amazon Kinesis
You can use Amazon Kinesis Data Streams to collect and process large streams of data
records in real time. A typical Kinesis Data Streams application reads data from a
data stream as data records.

As such, a common application is to relay DynamoDB table change stream events to a
Kinesis Stream, and consume that from an adapter to a consolidation database.
:::{div}
- About: [Amazon Kinesis Data Streams]
- See: [](#cdc-dynamodb)
:::

## Debezium
Debezium is an open source distributed platform for change data capture (CDC).
It is built on top of Apache Kafka, a distributed streaming platform. It allows
to capture changes on a source database system, mostly OLTP, and replicate them
to another system, mostly to run OLAP workloads on the data.

Debezium provides connectors for MySQL/MariaDB, MongoDB, PostgreSQL, Oracle,
SQL Server, IBM DB2, Cassandra, Vitess, Spanner, JDBC, and Informix.
:::{div}
- Tutorial: [Replicating data to CrateDB with Debezium and Kafka]
- Webinar: [How to replicate data from other databases to CrateDB with Debezium and Kafka]
:::

(cdc-dynamodb)=
## DynamoDB
:::{div}
Support for loading DynamoDB tables into CrateDB (full-load), as well as
[Amazon DynamoDB Streams] and [Amazon Kinesis Data Streams],
to relay CDC events from DynamoDB into CrateDB.

- [DynamoDB Table Loader]
- [DynamoDB CDC Relay]

If you are looking into serverless replication using AWS Lambda:
- [DynamoDB CDC Relay with AWS Lambda]
- Blog: [Replicating CDC events from DynamoDB to CrateDB]
:::

## MongoDB
:::{div}
Support for loading MongoDB collections and databases into CrateDB (full-load),
and [MongoDB Change Streams], to relay CDC events from MongoDB into CrateDB.

- [MongoDB Table Loader]
- [MongoDB CDC Relay]
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



[How to replicate data from other databases to CrateDB with Debezium and Kafka]: https://cratedb.com/resources/webinars/lp-wb-debezium-kafka
[StreamSets Data Collector]: https://www.softwareag.com/en_corporate/platform/integration-apis/data-collector-engine.html
