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


## Amazon DynamoDB
:::{div}
Tap into [Amazon DynamoDB Streams], to replicate CDC events from DynamoDB into CrateDB,
with support for CrateDB's container data types.
- {hyper-open}`Documentation <[DynamoDB CDC Relay]>`
- {hyper-read-more}`Blog <[Replicating CDC events from DynamoDB to CrateDB]>`
:::

## AWS DMS
[AWS Database Migration Service] (AWS DMS) is a managed migration and replication
service that helps move your database and analytics workloads quickly, securely,
and with minimal downtime and zero data loss.

AWS DMS supports migration between 20-plus database and analytics engines, either
on-premises, or per EC2 instance databases. Supported data migration sources are:
Amazon Aurora, Amazon DocumentDB, Amazon S3, IBM DB2, MariaDB, Azure SQL Database,
Microsoft SQL Server, MongoDB, MySQL, Oracle, PostgreSQL, SAP ASE.

CrateDB provides two variants how to conduct data migrations using AWS DMS.
Either use it standalone / on your own premises, or use it in a completely
managed environment with services of AWS and CrateDB Cloud.

- {hyper-navigate}`AWS DMS Kinesis Relay (standalone) <[AWS DMS Kinesis Relay]>`
- {hyper-navigate}`AWS DMS Kinesis Relay (managed) <[AWS DMS Kinesis Relay]>`

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



[AWS Database Migration Service]: https://aws.amazon.com/dms/
[How to replicate data from other databases to CrateDB with Debezium and Kafka]: https://cratedb.com/resources/webinars/lp-wb-debezium-kafka
[StreamSets Data Collector]: https://www.softwareag.com/en_corporate/platform/integration-apis/data-collector-engine.html
