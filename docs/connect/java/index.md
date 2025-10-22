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

Choose one of two JDBC drivers:

- {ref}`postgresql-jdbc` — `jdbc:postgresql://`
- {ref}`cratedb-jdbc` — `jdbc:crate://`

Prefer the PostgreSQL JDBC driver first—it’s often already on your classpath
and works out of the box. If your application or framework emits
PostgreSQL‑specific SQL that CrateDB doesn’t support, switch to the CrateDB
JDBC driver for full CrateDB dialect support and smoother integration.

The {ref}`crate-jdbc:internals` page includes more information
about compatibility and differences between the two driver variants,
and more details about the CrateDB JDBC Driver.

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
A Quarkus/Panache example using Hibernate.
::::

::::{grid-item-card} ![jOOQ logo][jOOQ logo]{height=40px} &nbsp; jOOQ
:link: jooq
:link-type: ref
:link-alt: jOOQ with CrateDB
A jOOQ example.
::::

::::{grid-item-card} ![JUnit logo][JUnit logo]{height=40px} &nbsp; Software testing
:link: java-testing
:link-type: ref
:link-alt: Software testing with CrateDB and Java
JUnit and Testcontainers for CrateDB.
::::

:::::

## HTTP

You can also talk to CrateDB using HTTP, using any HTTP library of your choice.
Below is a quick example using Apache Commons HTTP.

:::{todo}
Add example.
:::


:::{toctree}
:maxdepth: 1
:hidden:
postgresql-jdbc
cratedb-jdbc
hibernate
jooq
testing
:::
