(etl)=

# Load and Export

You have a variety of options to connect and integrate with 3rd-party
ETL applications, mostly using [CrateDB's PostgreSQL interface].

This documentation section lists corresponding ETL applications and
frameworks which can be used together with CrateDB, and outlines how
to use them optimally.


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

- {ref}`kafka-connect`
- [Build a data ingestion pipeline using Kafka, Flink, and CrateDB]
- [Community Day: Stream processing with Apache Flink and CrateDB]
- [Executable stack: Apache Kafka, Apache Flink, and CrateDB]


## Apache Kafka

- [Data Ingestion using Kafka and Kafka Connect]
- [Executable stack: Apache Kafka, Apache Flink, and CrateDB]
- [Tutorial: Replicating data to CrateDB with Debezium and Kafka]


## Azure Functions

- {ref}`azure-functions`


## dbt

- [Using dbt with CrateDB]


## Debezium

- [Tutorial: Replicating data to CrateDB with Debezium and Kafka]
- [Webinar: How to replicate data from other databases to CrateDB with Debezium and Kafka]


## Kestra

- [Setting up data pipelines with CrateDB and Kestra]


## MongoDB

- {ref}`integrate-mongodb`


## MySQL

- {ref}`integrate-mysql`


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


[Automating recurrent CrateDB queries using Node-RED]: https://community.cratedb.com/t/automating-recurrent-cratedb-queries/788
[Automating export of CrateDB data to S3 using Apache Airflow]: https://community.cratedb.com/t/cratedb-and-apache-airflow-automating-data-export-to-s3/901
[Automating stock data collection and storage with CrateDB and Apache Airflow]: https://community.cratedb.com/t/automating-stock-data-collection-and-storage-with-cratedb-and-apache-airflow/990
[Automating the import of Parquet files with Apache Airflow]: https://community.cratedb.com/t/automating-the-import-of-parquet-files-with-apache-airflow/1247
[Build a data ingestion pipeline using Kafka, Flink, and CrateDB]: https://dev.to/crate/build-a-data-ingestion-pipeline-using-kafka-flink-and-cratedb-1h5o
[Building a hot and cold storage data retention policy in CrateDB with Apache Airflow]: https://community.cratedb.com/t/cratedb-and-apache-airflow-building-a-hot-cold-storage-data-retention-policy/934
[Community Day: Stream processing with Apache Flink and CrateDB]: https://cratedb.com/blog/cratedb-community-day-2nd-edition-summary-and-highlights
[CrateDB and Apache Airflow: Building a data ingestion pipeline]: https://community.cratedb.com/t/cratedb-and-apache-airflow-building-a-data-ingestion-pipeline/926 
[CrateDB's PostgreSQL interface]: inv:crate-reference#interface-postgresql
[Data Ingestion using Kafka and Kafka Connect]: https://cratedb.com/docs/crate/howtos/en/latest/integrations/kafka-connect.html
[ETL pipeline using Apache Airflow with CrateDB (Source)]: https://github.com/astronomer/astro-cratedb-blogpost
[ETL with Astro and CrateDB Cloud in 30min - fully up in the cloud]: https://www.astronomer.io/blog/run-etlelt-with-airflow-and-cratedb/
[Examples about working with CrateDB and Meltano]: https://github.com/crate/cratedb-examples/tree/amo/meltano/framework/singer-meltano
[Executable stack: Apache Kafka, Apache Flink, and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/application/apache-kafka-flink
[Implementing a data retention policy in CrateDB using Apache Airflow]: https://community.cratedb.com/t/implementing-a-data-retention-policy-in-cratedb-using-apache-airflow/913 
[Ingesting MQTT messages into CrateDB using Node-RED]: https://community.cratedb.com/t/ingesting-mqtt-messages-into-cratedb-using-node-red/803
[meltano-tap-cratedb]: https://github.com/crate-workbench/meltano-tap-cratedb
[meltano-target-cratedb]: https://github.com/crate-workbench/meltano-target-cratedb
[Run an ETL pipeline with CrateDB and data quality checks]: https://registry.astronomer.io/dags/etl_pipeline/
[Setting up data pipelines with CrateDB and Kestra]: https://community.cratedb.com/t/setting-up-data-pipelines-with-cratedb-and-kestra-io/1400
[Tutorial: Replicating data to CrateDB with Debezium and Kafka]: https://community.cratedb.com/t/replicating-data-to-cratedb-with-debezium-and-kafka/1388
[Updating stock market data automatically with CrateDB and Apache Airflow]: https://community.cratedb.com/t/updating-stock-market-data-automatically-with-cratedb-and-apache-airflow/1304
[Using dbt with CrateDB]: https://community.cratedb.com/t/using-dbt-with-cratedb/1566
[Using SQL Server Integration Services with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/application/microsoft-ssis
[Webinar: How to replicate data from other databases to CrateDB with Debezium and Kafka]: https://cratedb.com/resources/webinars/lp-wb-debezium-kafka



```{toctree}
:hidden:

mongodb
mysql
```

```{toctree}
:hidden:

kafka-connect
azure-functions
streamsets
```
