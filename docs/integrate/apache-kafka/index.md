(apache-kafka)=
# Apache Kafka

```{div} .float-right .text-right
[![Apache Kafka logo](https://kafka.apache.org/logos/kafka_logo--simple.png){height=60px loading=lazy}][Apache Kafka]
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-flink-kafka-java.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-flink-kafka-java.yml?branch=main&label=Apache%20Kafka,%20Apache%20Flink" loading="lazy" alt="CI status: Apache Kafka, Apache Flink"></a>
```
```{div} .clearfix
```

:::{include} /_include/links.md
:::

:::{rubric} About
:::

[Apache Kafka] is an open-source distributed event streaming platform used by
thousands of companies for high-performance data pipelines, streaming analytics,
data integration, and mission-critical applications. 

:::{dropdown} **Managed Kafka**
Several companies provide managed Kafka services (see the [overview of managed Kafka offerings]
for a more complete list).

- [Aiven for Apache Kafka]
- [Amazon Managed Streaming for Apache Kafka (MSK)]
- [Apache Kafka on Azure]
- [Azure Event Hubs for Apache Kafka]
- [Confluent Cloud]
- [DoubleCloud Managed Service for Apache Kafka]
:::


:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Tutorial: Build a data ingestion pipeline
:link: kafka-connect
:link-type: ref
The tutorial explains how to build a data ingestion pipeline using Apache
Kafka, CrateDB, and the Confluent Kafka Connect JDBC connector.
:::

:::{grid-item-card} Tutorial: Connect Debezium, Kafka, and CrateDB
:link: https://community.cratedb.com/t/replicating-data-to-cratedb-with-debezium-and-kafka/1388
:link-type: url
Replicating data to CrateDB with Debezium and Kafka.
:::

:::{grid-item-card} Source: Executable Stack (Java)
:link: https://github.com/crate/cratedb-examples/tree/main/framework/flink/kafka-jdbcsink-java
:link-type: url
An executable stack with Apache Kafka, Apache Flink, and CrateDB. Uses Java.
:::

::::

```{toctree}
:hidden:
kafka-connect
```

```{seealso}
[CrateDB and Apache Kafka]
```


[Aiven for Apache Kafka]: https://aiven.io/kafka
[Amazon Managed Streaming for Apache Kafka (MSK)]: https://aws.amazon.com/msk/
[Apache Kafka]: https://kafka.apache.org/
[Apache Kafka on Azure]: https://azuremarketplace.microsoft.com/marketplace/consulting-services/canonical.0001-com-ubuntu-managed-kafka
[Azure Event Hubs for Apache Kafka]: https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-kafka-overview
[Confluent Cloud]: https://www.confluent.io/confluent-cloud/
[CrateDB and Apache Kafka]: https://cratedb.com/integrations/cratedb-and-kafka
[DoubleCloud Managed Service for Apache Kafka]: https://double.cloud/services/managed-kafka/
[overview of managed Kafka offerings]: https://keen.io/blog/managed-apache-kafka-vs-diy/
