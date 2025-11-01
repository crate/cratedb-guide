(java)=
(connect-java)=

# Java

:::{include} /_include/links.md
:::
:::{include} /_include/logos.md
:::

:::{div} sd-text-muted
Connect to CrateDB and CrateDB Cloud from Java.
:::

## JDBC

:::{div}
[JDBC] is the standard Java API that provides a common interface for accessing
databases in Java.
:::

:::{rubric} Driver options
:::

:::{include} _driver_options.md
:::

:::{rubric} Adapters and drivers
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} ![PostgreSQL logo][PostgreSQL logo]{height=40px} &nbsp; PostgreSQL JDBC
:link: postgresql-jdbc
:link-type: ref
:link-alt: PostgreSQL JDBC (pgJDBC)
The PostgreSQL JDBC driver.
::::

::::{grid-item-card} ![CrateDB logo][CrateDB logo]{height=40px} &nbsp; CrateDB JDBC
:link: cratedb-jdbc
:link-type: ref
:link-alt: CrateDB JDBC
The CrateDB JDBC driver.
::::

::::{grid-item-card} ![Hibernate logo][Hibernate logo]{height=40px} &nbsp; Hibernate
:link: hibernate
:link-type: ref
:link-alt: Hibernate with CrateDB
A Hibernate example using Quarkus/Panache.
::::

::::{grid-item-card} ![jOOQ logo][jOOQ logo]{height=40px} &nbsp; jOOQ
:link: jooq
:link-type: ref
:link-alt: jOOQ with CrateDB
A jOOQ example.
::::

::::{grid-item-card} {material-outlined}`verified;2em` &nbsp; Software testing
:link: java-testing
:link-type: ref
:link-alt: Software testing with CrateDB and Java
JUnit support and Testcontainers for CrateDB.
::::

:::::

:::{rubric} Frameworks
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} ![Flink logo][Flink logo]{height=40px} &nbsp; Apache Flink
:link: flink
:link-type: ref
:link-alt: Apache Flink and CrateDB
Use CrateDB with Apache Flink.
::::

::::{grid-item-card} ![Spark logo][Spark logo]{height=40px} &nbsp; Apache Spark
:link: spark
:link-type: ref
:link-alt: Apache Spark and CrateDB
Use CrateDB with Apache Spark.
::::

:::::


:::{toctree}
:maxdepth: 1
:hidden:
postgresql-jdbc
cratedb-jdbc
hibernate
jooq
testing
:::
