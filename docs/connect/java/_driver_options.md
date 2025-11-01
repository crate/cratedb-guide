---
orphan: true
---
Choose one of two JDBC drivers:

- {ref}`postgresql-jdbc` — `jdbc:postgresql://`
- {ref}`cratedb-jdbc` — `jdbc:crate://`

Prefer the PostgreSQL JDBC driver first, it is often already in your classpath
and works out of the box. If your application or framework emits
PostgreSQL‑specific SQL that CrateDB doesn’t support, switch to the CrateDB
JDBC driver for full CrateDB dialect support and smoother integration.

For example, the JDBC catalog integration with Apache Flink depends on CrateDB
JDBC, in this case we recommend to use that driver depending on your needs.

The {ref}`CrateDB JDBC internals <crate-jdbc:internals>` page includes more information
about compatibility and differences between the two driver variants,
and more details about the CrateDB JDBC Driver.
