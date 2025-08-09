(cdc)=
# Change Data Capture (CDC)

:::{include} /_include/links.md
:::

:::{div}
You have a variety of options to connect and integrate with 3rd-party
CDC applications, mostly using [CrateDB's PostgreSQL interface].

CrateDB also provides a few native adapter components that can be used
to leverage its advanced features. 

This documentation section lists corresponding CDC applications and
frameworks which can be used together with CrateDB, and outlines how
to use them optimally.
Please also have a look at support for [generic ETL](#etl) solutions.
:::

(cdc-dms)=
## AWS DMS

:::{div}
[AWS Database Migration Service (AWS DMS)] is a managed migration and replication
service that helps move your database and analytics workloads between different
kinds of databases quickly, securely, and with minimal downtime and zero data
loss.

AWS DMS supports migration between 20-plus database and analytics engines, either
on-premises, or per EC2 instance databases. Supported data migration sources are:
Amazon Aurora, Amazon DocumentDB, Amazon S3, IBM DB2, MariaDB, Azure SQL Database,
Microsoft SQL Server, MongoDB, MySQL, Oracle, PostgreSQL, SAP ASE.

The [AWS DMS Integration with CrateDB] uses Amazon Kinesis Data Streams as
a DMS target, combined with a CrateDB-specific downstream processor element.

CrateDB provides two variants how to conduct data migrations using AWS DMS.
Either use it standalone / on your own premises, or use it in a completely
managed environment with services of AWS and CrateDB Cloud.
AWS DMS supports both `full-load` and `cdc` operation modes, often used in
combination with each other (`full-load-and-cdc`).
:::

(cdc-kinesis)=
## AWS Kinesis
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

- {ref}`debezium`

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


[StreamSets Data Collector]: https://www.softwareag.com/en_corporate/platform/integration-apis/data-collector-engine.html
