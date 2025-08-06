(debezium)=
# Debezium

:::{include} /_include/links.md
:::

:::{rubric} About
:::

```{div}
:style: "float: right; margin-left: 2em"
[![](https://debezium.io/assets/images/color_white_debezium_type_600px.svg){w=180px}](https://debezium.io/)
```

[Debezium] is an open source distributed platform for change data capture. After
pointing it at your databases, you can subscribe to the event stream of
all database update operations.

Debezium is an open source distributed platform for change data capture (CDC).
It is built on top of Apache Kafka, a distributed streaming platform. It allows
to capture changes on a source database system, mostly OLTP, and replicate them
to another system, mostly to run OLAP workloads on the data.

Debezium provides connectors for MySQL/MariaDB, MongoDB, PostgreSQL, Oracle,
SQL Server, IBM DB2, Cassandra, Vitess, Spanner, JDBC, and Informix.

:::{rubric} Learn
:::

:::{div}
- Tutorial: [Replicating data to CrateDB with Debezium and Kafka]
- Webinar: [How to replicate data from other databases to CrateDB with Debezium and Kafka]
:::


[Debezium]: https://debezium.io/
[How to replicate data from other databases to CrateDB with Debezium and Kafka]: https://cratedb.com/resources/webinars/lp-wb-debezium-kafka
