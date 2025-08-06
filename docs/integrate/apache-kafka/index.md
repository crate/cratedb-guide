(apache-kafka)=
# Apache Kafka

:::{include} /_include/links.md
:::

:::{rubric} About
:::

```{div}
:style: "float: right; margin-left: 2em"
[![](https://kafka.apache.org/logos/kafka_logo--simple.png){w=180px}](https://kafka.apache.org/)
```

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

:::{div}
- {ref}`kafka-connect`
- [Replicating data to CrateDB with Debezium and Kafka]
- [Executable stack with Apache Kafka, Apache Flink, and CrateDB]
:::

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
