(apache-flink)=
(flink)=
# Apache Flink

:::{include} /_include/links.md
:::

```{div} .float-right .text-right
[![Apache Flink logo](https://flink.apache.org/flink-header-logo.svg){height=60px loading=lazy}][Apache Flink]
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-flink-kafka-java.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-flink-kafka-java.yml?branch=main&label=Apache%20Kafka,%20Apache%20Flink" loading="lazy" alt="CI status: Apache Kafka, Apache Flink"></a>
```
```{div} .clearfix
```

[Apache Flink] is a programming framework and distributed processing engine
for stateful computations over unbounded and bounded data streams, written
in Java. It is a battle-hardened stream processor widely used for demanding
real-time applications.

:::{dropdown} **Details**

Flink has been designed to run in all common cluster environments, perform
computations at in-memory speed and at any scale. It received the [2023 SIGMOD
Systems Award].

> Apache Flink greatly expanded the use of stream data-processing.
> Data Pipelines Done Right.

![](https://flink.apache.org/img/flink-home-graphic.png){h=200px}

:::{dropdown} **Managed Flink**
A few companies are specializing in offering managed Flink services.

- [Aiven] offers their managed [Aiven for Apache Flink] solution.
- [Immerok Cloud]'s offering is being converged into [Flink managed by Confluent],
  see [Confluent Streaming Data Pipelines].
:::


## Connect
Flink's [JdbcSink] is a streaming connector that writes data to a JDBC database,
for example using the [PostgreSQL JDBC Driver] that also works with CrateDB.
When configuring the data sink, use:
:url:
  `jdbc:postgresql://localhost:5432/crate`
:driver:
  `org.postgresql.Driver`


## Synopsis
```python
from pyflink.common import Types
from pyflink.datastream.connectors.jdbc import JdbcConnectionOptions, JdbcExecutionOptions, JdbcSink

JdbcSink.sink(
    "INSERT INTO doc.weather_flink_sink (location, current) VALUES (?, ?)",
    Types.ROW_NAMED(["location", "current"], [Types.STRING(), Types.STRING()]),
    JdbcConnectionOptions.JdbcConnectionOptionsBuilder()
    .with_url("jdbc:postgresql://localhost:5432/crate")
    .with_driver_name("org.postgresql.Driver")
    .with_user_name("crate")
    .with_password("")
    .build())
```
:::::{dropdown} More Examples
::::{tab-set}

:::{tab-item} Java

```java
import org.apache.flink.connector.jdbc.JdbcConnectionOptions;
import org.apache.flink.connector.jdbc.JdbcExecutionOptions;
import org.apache.flink.connector.jdbc.JdbcSink;

JdbcSink.sink(
    "INSERT INTO my_schema.books (id, title, authors, year) VALUES (?, ?, ?, ?)",
    (statement, book) -> {
        statement.setLong(1, book.id);
        statement.setString(2, book.title);
        statement.setString(3, book.authors);
        statement.setInt(4, book.year);
    },
    JdbcExecutionOptions.builder()
        .withBatchSize(1000)
        .withBatchIntervalMs(200)
        .withMaxRetries(5)
        .build(),
    new JdbcConnectionOptions.JdbcConnectionOptionsBuilder()
        .withUrl("jdbc:postgresql://localhost:5432/crate")
        .withDriverName("org.postgresql.Driver")
        .withUsername("crate")
        .withPassword("")
        .build()
));
```
:::

:::{tab-item} Python
```python
from pyflink.common import Types
from pyflink.datastream.connectors.jdbc import JdbcConnectionOptions, JdbcExecutionOptions, JdbcSink

JdbcSink.sink(
    "INSERT INTO doc.weather_flink_sink (location, current) VALUES (?, ?)",
    Types.ROW_NAMED(["location", "current"], [Types.STRING(), Types.STRING()]),
    JdbcConnectionOptions.JdbcConnectionOptionsBuilder()
    .with_url("jdbc:postgresql://localhost:5432/crate")
    .with_driver_name("org.postgresql.Driver")
    .with_user_name("crate")
    .with_password("")
    .build(),
    JdbcExecutionOptions.builder()
    .with_batch_interval_ms(1000)
    .with_batch_size(200)
    .with_max_retries(5)
    .build()
)
```
:::
::::
:::::


## Learn

:::{rubric} Tutorials
:::

::::{grid}
:gutter: 2

:::{grid-item-card} Tutorial: Build a data ingestion pipeline
:link: https://dev.to/crate/build-a-data-ingestion-pipeline-using-kafka-flink-and-cratedb-1h5o
:link-type: url
:columns: 12
The tutorial explains how to build a data ingestion pipeline using three
open-source tools: Apache Kafka, Flink, and CrateDB.
+++
Example: Kafka receives telemetry messages from IoT sensors and devices. Flink
consumes the data stream and stores it into CrateDB. All tools are distributed
systems that provide elastic scaling, fault tolerance, high-throughput, and
low-latency performance via parallel processing.
:::

:::{grid-item-card} Source: Executable Stack (Java)
:link: https://github.com/crate/cratedb-examples/tree/main/framework/flink/kafka-jdbcsink-java
:link-type: url
An executable stack with Apache Kafka, Apache Flink, and CrateDB. Uses Java.
:::

:::{grid-item-card} Source: Executable Stack (Python)
:link: https://github.com/crate/cratedb-examples/tree/main/framework/flink/kafka-jdbcsink-python
:link-type: url
An executable stack with Apache Kafka, Apache Flink, and CrateDB. Uses Python.
:::

::::


:::{rubric} Webinars
:::

::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Apache Flink 101**

Why Flink is interesting for building real-time streaming applications,
and how it works.

Flink's performance and robustness are the results of a handful of core design
principles, including a shared-nothing architecture with local state, event-time
processing, and state snapshots (for recovery). This course introduces you to
these core concepts.
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/3cg5dABA6mo?list=PLa7VYi0yPIH1UdmQcnUr8lvjbUV8JriK0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Webinar`
{tags-secondary}`Fundamentals`
:::

::::


::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**CrateDB Community Day: Maximizing your data potential with CrateDB integrations**

Flink connects different messaging systems, file systems, and database key/value
stores for multiple purposes. For data integrations, it can serve as a data hub
between systems and much more like event-driven applications, and it's very flexible. 

The webinar includes a live demo of Apache Flink with CrateDB as source or sink.

- [CrateDB Community Day 2nd Edition: Summary and Highlights]
- [Community Day: Stream processing with Apache Flink and CrateDB]
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/R4UxMdrR5os?t=2207" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Webinar`
{tags-secondary}`Integrations`
:::

::::



[2023 SIGMOD Systems Award]: https://sigmod.org/2023-sigmod-systems-award/
[Aiven]: https://aiven.io/
[Aiven for Apache Flink]: https://aiven.io/flink
[Apache Flink]: https://flink.apache.org/
[Build a data ingestion pipeline using Kafka, Flink, and CrateDB]: https://dev.to/crate/build-a-data-ingestion-pipeline-using-kafka-flink-and-cratedb-1h5o
[Community Day: Stream processing with Apache Flink and CrateDB]: https://cratedb.com/event/cratedb-community-day-2023
[Confluent Streaming Data Pipelines]: https://www.confluent.io/streaming-data-pipelines/
[CrateDB Community Day 2nd Edition: Summary and Highlights]: https://cratedb.com/blog/cratedb-community-day-2nd-edition-summary-and-highlights
[Flink managed by Confluent]: https://www.datanami.com/2023/05/17/confluents-new-cloud-capabilities-address-data-streaming-hurdles/
[Immerok Cloud]: https://web.archive.org/web/20230602085618/https://www.immerok.io/product
[JdbcSink]: https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/datastream/jdbc/
[Streaming data with Apache Kafka, Apache Flink and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/framework/flink/kafka-jdbcsink-python
