(etl)=
(io)=
(import-export)=
# Load and Export (ETL)

:::{include} /_include/links.md
:::

:::{div}
You have a variety of options to connect and integrate with 3rd-party
ETL applications, mostly using [CrateDB's PostgreSQL interface].
:::

This documentation section lists corresponding ETL applications and
frameworks which can be used together with CrateDB, and outlines how
to use them optimally.
Please also have a look at support for [](#cdc) solutions.


## Apache Airflow / Astronomer

- {ref}`apache-airflow`

## Apache Flink

- {ref}`apache-flink`

## Apache Hop

- {ref}`apache-hop`

## Apache Iceberg / RisingWave
:::{div}
- {ref}`iceberg-risingwave`
:::

```{toctree}
:hidden:

iceberg-risingwave
```

## Apache Kafka

- {ref}`apache-kafka`

## Apache NiFi

- {ref}`apache-nifi`

## AWS DMS

:::{div}
[AWS Database Migration Service (AWS DMS)] is a managed migration and replication
service that helps move your database and analytics workloads between different
kinds of databases quickly, securely, and with minimal downtime and zero data
loss. It supports migration between 20-plus database and analytics engines.

AWS DMS supports migration between 20-plus database and analytics engines, either
on-premises, or per EC2 instance databases. Supported data migration sources are:
Amazon Aurora, Amazon DocumentDB, Amazon S3, IBM DB2, MariaDB, Azure SQL Database,
Microsoft SQL Server, MongoDB, MySQL, Oracle, PostgreSQL, SAP ASE.

The [AWS DMS Integration with CrateDB] uses Amazon Kinesis Data Streams as
a DMS target, combined with a CrateDB-specific downstream processor element.

CrateDB provides two variants how to conduct data migrations using AWS DMS.
Either use it standalone / on your own premises, or use it in a completely
managed environment with services of AWS and CrateDB Cloud.
:::


## AWS Kinesis

Amazon Kinesis Data Streams is a serverless streaming data service that
simplifies the capture, processing, and storage of data streams at any
scale, such as application logs, website clickstreams, and IoT telemetry
data, for machine learning (ML), analytics, and other applications.
:::{div}
The [DynamoDB CDC Relay] pipeline uses Amazon Kinesis to relay a table
change stream from a DynamoDB table into a CrateDB table, see also
[DynamoDB CDC](#cdc-dynamodb).
:::


## Azure Functions

- {ref}`azure-functions`

```{toctree}
:hidden:

azure-functions
```


## dbt

- {ref}`dbt`

## DynamoDB
:::{div}
- [DynamoDB Table Loader]
- [DynamoDB CDC Relay]
:::


## Estuary

- {ref}`estuary`

## InfluxDB

- {ref}`integrate-influxdb`

## Kestra

- {ref}`kestra`

## Meltano

- {ref}`meltano`

## MongoDB
:::{div}
- Tutorial: {ref}`integrate-mongodb`
- Documentation: [MongoDB Table Loader]
- Documentation: [MongoDB CDC Relay]
:::
```{toctree}
:hidden:

mongodb
```


## MySQL

- {ref}`integrate-mysql`

```{toctree}
:hidden:

mysql
```

## Node-RED

- {ref}`node-red`

## RisingWave

- {ref}`risingwave`

## SQL Server Integration Services

- {ref}`sql-server`

## StreamSets

- {ref}`streamsets`

```{toctree}
:hidden:

streamsets
```
