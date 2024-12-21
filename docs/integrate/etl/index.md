(etl)=
(io)=
(import-export)=
# Load and Export

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


(airflow)=
(apache-airflow)=
## Apache Airflow / Astronomer

A set of starter tutorials.

- [Automating the import of Parquet files with Apache Airflow]
- [Updating stock market data automatically with CrateDB and Apache Airflow]
- [Automating stock data collection and storage with CrateDB and Apache Airflow]

A set of elaborated tutorials, including blueprint implementations.

- [Automating export of CrateDB data to S3 using Apache Airflow]
- [Implementing a data retention policy in CrateDB using Apache Airflow]
- [CrateDB and Apache Airflow: Building a data ingestion pipeline]
- [Building a hot and cold storage data retention policy in CrateDB with Apache Airflow]

Tutorials and resources about configuring the managed variants, Astro and CrateDB Cloud.

- [ETL with Astro and CrateDB Cloud in 30min - fully up in the cloud]
- [ETL pipeline using Apache Airflow with CrateDB (Source)]
- [Run an ETL pipeline with CrateDB and data quality checks]


## Apache Flink

:::{toctree}
:maxdepth: 1

../apache-flink/index
:::


## Apache Hop

- [Using Apache Hop with CrateDB]
- [CrateDB dialect for Apache Hop]
- [CrateDB Apache Hop Bulk Loader transform]


## Apache Kafka
:::{div}
- {ref}`kafka-connect`
- [Replicating data to CrateDB with Debezium and Kafka]
- [Executable stack with Apache Kafka, Apache Flink, and CrateDB]
:::

```{toctree}
:hidden:

kafka-connect
```

## Apache NiFi

- [Connecting to CrateDB from Apache NiFi]


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

:::{toctree}
:maxdepth: 1

../dbt/index
:::


## DynamoDB
:::{div}
- [DynamoDB Table Loader]
- [DynamoDB CDC Relay]
:::


## InfluxDB

- {ref}`integrate-influxdb`

```{toctree}
:hidden:

../influxdb/index
```


## Kestra

- [Setting up data pipelines with CrateDB and Kestra]

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

- [Ingesting MQTT messages into CrateDB using Node-RED]
- [Automating recurrent CrateDB queries using Node-RED]


## Singer / Meltano

- [meltano-target-cratedb]
- [meltano-tap-cratedb]
- [Examples about working with CrateDB and Meltano]

🚧 _Please note these adapters are a work in progress._ 🚧


## SQL Server Integration Services

A demo project which uses SSIS and ODBC to read and write data from CrateDB:

- [Using SQL Server Integration Services with CrateDB]


## StreamSets

- {ref}`streamsets`

```{toctree}
:hidden:

streamsets
```



[Automating recurrent CrateDB queries using Node-RED]: https://community.cratedb.com/t/automating-recurrent-cratedb-queries/788
[Automating export of CrateDB data to S3 using Apache Airflow]: https://community.cratedb.com/t/cratedb-and-apache-airflow-automating-data-export-to-s3/901
[Automating stock data collection and storage with CrateDB and Apache Airflow]: https://community.cratedb.com/t/automating-stock-data-collection-and-storage-with-cratedb-and-apache-airflow/990
[Automating the import of Parquet files with Apache Airflow]: https://community.cratedb.com/t/automating-the-import-of-parquet-files-with-apache-airflow/1247
[Building a hot and cold storage data retention policy in CrateDB with Apache Airflow]: https://community.cratedb.com/t/cratedb-and-apache-airflow-building-a-hot-cold-storage-data-retention-policy/934
[Connecting to CrateDB from Apache NiFi]: https://community.cratedb.com/t/connecting-to-cratedb-from-apache-nifi/647
[CrateDB and Apache Airflow: Building a data ingestion pipeline]: https://community.cratedb.com/t/cratedb-and-apache-airflow-building-a-data-ingestion-pipeline/926 
[CrateDB Apache Hop Bulk Loader transform]: https://hop.apache.org/manual/latest/pipeline/transforms/cratedb-bulkloader.html
[CrateDB dialect for Apache Hop]: https://hop.apache.org/manual/latest/database/databases/cratedb.html
[ETL pipeline using Apache Airflow with CrateDB (Source)]: https://github.com/astronomer/astro-cratedb-blogpost
[ETL with Astro and CrateDB Cloud in 30min - fully up in the cloud]: https://www.astronomer.io/blog/run-etlelt-with-airflow-and-cratedb/
[Examples about working with CrateDB and Meltano]: https://github.com/crate/cratedb-examples/tree/amo/meltano/framework/singer-meltano
[Executable stack with Apache Kafka, Apache Flink, and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/framework/flink/kafka-jdbcsink-java
[Implementing a data retention policy in CrateDB using Apache Airflow]: https://community.cratedb.com/t/implementing-a-data-retention-policy-in-cratedb-using-apache-airflow/913 
[Ingesting MQTT messages into CrateDB using Node-RED]: https://community.cratedb.com/t/ingesting-mqtt-messages-into-cratedb-using-node-red/803
[meltano-tap-cratedb]: https://github.com/crate-workbench/meltano-tap-cratedb
[meltano-target-cratedb]: https://github.com/crate-workbench/meltano-target-cratedb
[Run an ETL pipeline with CrateDB and data quality checks]: https://registry.astronomer.io/dags/etl_pipeline/
[Setting up data pipelines with CrateDB and Kestra]: https://community.cratedb.com/t/setting-up-data-pipelines-with-cratedb-and-kestra-io/1400
[Updating stock market data automatically with CrateDB and Apache Airflow]: https://community.cratedb.com/t/updating-stock-market-data-automatically-with-cratedb-and-apache-airflow/1304
[Using Apache Hop with CrateDB]: https://community.cratedb.com/t/using-apache-hop-with-cratedb/1754
[Using SQL Server Integration Services with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/application/microsoft-ssis
