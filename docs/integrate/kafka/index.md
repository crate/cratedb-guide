---
description: >-
  Apache Kafka is a widely used open-source distributed event-store and
  streaming platform.
---
(kafka)=
# Kafka

```{div} .float-right .text-right
[![Apache Kafka logo](https://kafka.apache.org/logos/kafka_logo--simple.png){height=60px loading=lazy}][Apache Kafka]
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-flink-kafka-java.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-flink-kafka-java.yml?branch=main&label=Apache%20Kafka,%20Apache%20Flink" loading="lazy" alt="CI status: Apache Kafka, Apache Flink"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-ingestr.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-ingestr.yml?branch=main&label=Ingestr%2BKafka" loading="lazy" alt="CI status: Apache Kafka, Apache Flink"></a>
```
```{div} .clearfix
```

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Apache Kafka is a widely used open-source distributed event-store and streaming platform.
:::


## Overview

[Apache Kafka] is a distributed event log for high-throughput, durable, and scalable data streams. CrateDB is a distributed SQL database optimized for time-series, IoT, and analytics at scale. Together, they form a robust pipeline for moving operational events from producers into a queryable store with SQL and real-time analytics.

## Benefits of CrateDB + Apache Kafka

* **Buffering & decoupling** – Kafka absorbs bursty writes and isolates producers from database load. This is particularly useful when it comes to heavy-load ingestion scenarios.
* **Scalability end-to-end** – Partitioned topics and a sharded cluster let you scale producers, brokers, consumers, and CrateDB independently.
* **Near-real-time analytics** – New events are available in CrateDB seconds (or even milliseconds) after production, exposed via SQL to standard BI tools.
* **Operational resilience** – Use Kafka as a durable buffer between CrateDB and data producers. Idempotent upserts (exactly-once semantics) reduce data-loss and duplication risks.

## Common Ingestion Options

:::{important}
The Apache Kafka PostgreSQL connector is 99% compatible with CrateDB. CrateDB does not support transactions, but this only becomes notable when either ingestion to CrateDB is failing or there is some other connection issue.&#x20;
:::

### Kafka Connect → CrateDB (recommended for most)

Use a sink connector to map Kafka topics directly to CrateDB tables, with built-in support for batching, upserts, and retries.&#x20;

This approach also lets you leverage the rich ecosystem of Kafka Connect and Flink connectors — not just for other databases, but also for ERP, CRM, social media platforms, and many other systems.

### Custom consumer application

Instead of using Kafka Connect, you can write your own Kafka consumer in Java, Python, Rust, or another language. The client reads records from Kafka and writes them into CrateDB using standard SQL (over the PostgreSQL wire protocol) or via the HTTP API.

This option gives you full control: you can transform data on the fly, filter out unwanted events, or route records into different CrateDB tables based on business logic. It’s usually chosen when you need flexibility beyond what a connector offers, but it does mean you’re responsible for batching, retries, and error handling yourself.

### Stream processors (Flink/Kafka Streams/Spark)

For more advanced pipelines, you can process events while they’re still in Kafka before they ever reach CrateDB. Frameworks like Flink, Kafka Streams, or Spark let you enrich records, join multiple streams together, run aggregations, or apply windowing functions in real time.

The processed results are then written into CrateDB, where they’re immediately available for SQL queries and dashboards. This approach is powerful when raw events need to be cleaned, combined, or summarised before storage, though it adds more moving parts compared to a simple connector.

## Typical use cases

*   **Time-series pipelines (sensors, logs, metrics, events)**

    Stream high-volume data from IoT devices, application logs, or monitoring systems into Kafka, then land it in CrateDB for storage and real-time querying. Ideal for scenarios where you need to keep years of historical data but still run live analytics on the latest events.
*   **CDC / operational data feeds (Debezium → Kafka → CrateDB)**

    Capture data changes from operational databases using Debezium and push them into Kafka. CrateDB acts as the analytics layer, letting you query an always-up-to-date view of your transactional data without putting load on the source systems.
*   **Real-time dashboards, anomaly detection, and alerting**

    Combine Kafka’s streaming capabilities with CrateDB’s fast SQL engine to power dashboards that update in near real time. Detect unusual patterns (e.g. equipment failure, fraud, traffic spikes) and trigger alerts directly from queries over live data.
*   **ETL / ELT landing zone for downstream analytics**

    Use Kafka as the ingestion backbone and CrateDB as a staging or analytics store. Raw events can be enriched or aggregated in-flight, written to CrateDB for exploration, and later exported to long-term storage or data warehouses for deeper batch analytics.

## Deployment options

How you run Kafka and CrateDB depends a lot on your environment and preferences. The most common approaches are:

* **Containerised on-premise** – Run both Kafka and CrateDB on Docker or Kubernetes in your own data centre or private cloud. This gives you the most control, but also means you manage scaling, upgrades, and monitoring.
* **Managed Kafka services** – Use a provider such as Confluent Cloud or AWS MSK to offload the operational heavy lifting of Kafka. You can still connect these managed clusters directly to a CrateDB deployment that you operate. CrateDB is also available on the major cloud providers as well.
* **Managed CrateDB** – Crate\.io offers CrateDB Cloud, which can pair with either self-managed Kafka or managed Kafka services. This option reduces database operations to a minimum.
* **Hybrid setups** – A common pattern is managed Kafka + self-managed CrateDB, or vice versa, depending on where you want to keep operational control.

In practice, teams usually start containerised (for dev/test or early projects) and move to managed services as scale or reliability requirements grow.

## Key design considerations

* **Topic & partition strategy** – Align Kafka partitions with expected throughput and consumer parallelism - aim for stable keys (e.g., device\_id) to keep ordering where needed.
* **Table modelling in CrateDB** – Choose primary keys and partitioning (e.g., by month on a timestamp column) to balance write speed and query performance - define shard count per table.
* **Upserts & deduplication** – Include a stable event key (id, source+timestamp) to make writes idempotent when possible.
* **Batching & back-pressure** – Tune sink batch size and retries to match CrateDB ingest capacity while keeping latency low.
* **Schema & types** – Keep payloads consistent, map Avro/JSON types carefully to CrateDB types (timestamps/time zones, numerics, arrays).
* **Retention & replay** – Kafka retention defines how far back you can reprocess, plan storage and compaction accordingly.
* **Observability** – Monitor producer lag, consumer lag, sink error rates, CrateDB shard health, and query latency.

## Learn more

::::{grid} 2
:gutter: 2

:::{grid-item-card} Tutorial: Use Docker and Python
:link: kafka-docker-python
:link-type: ref
This walkthrough demonstrates how to load data from a Kafka topic into a
CrateDB table, using a Python consumer and CrateDB's HTTP interface.
:::

:::{grid-item-card} Tutorial: Use Confluent Kafka Connect
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
docker-python
kafka-connect
```

```{seealso}
[CrateDB and Apache Kafka]
```


[Apache Kafka]: https://kafka.apache.org/
[CrateDB and Apache Kafka]: https://cratedb.com/integrations/cratedb-and-kafka
