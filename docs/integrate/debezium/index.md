(debezium)=
# Debezium

```{div} .float-right
[![Debezium logo](https://debezium.io/assets/images/color_black_debezium_type_600px.svg){height=60px loading=lazy}][Debezium]
```
```{div} .clearfix
```

:::{rubric} About
:::

[Debezium] is an open source distributed platform for change data capture (CDC).
After pointing it at your databases, you can subscribe to the event stream of
all database update operations.

It is built on top of Apache Kafka, a distributed streaming platform.
It allows capturing changes on a source database system (typically OLTP) and
replicating them to another system, for example to run OLAP workloads on the data.

Debezium provides connectors for MySQL/MariaDB, MongoDB, PostgreSQL, Oracle,
SQL Server, IBM DB2, Cassandra, Vitess, Spanner, JDBC, and Informix.

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Replicate data from MSSQL
:link: debezium-tutorial
:link-type: ref
Replicate data from MSSQL to CrateDB with Debezium and Kafka.
:::

:::{grid-item-card} Webinar: Replicate data from other databases
:link: https://cratedb.com/resources/webinars/lp-wb-debezium-kafka
:link-type: url
How to replicate data from other databases to CrateDB with Debezium and Kafka.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
:::


[Debezium]: https://debezium.io/
