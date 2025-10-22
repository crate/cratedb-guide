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

:::{div}
You have two JDBC driver options: The {ref}`postgresql-jdbc` Driver
and the {ref}`cratedb-jdbc` Driver.
PostgreSQL JDBC uses the `jdbc:postgresql://` protocol identifier,
while CrateDB JDBC uses `jdbc:crate://`.
:::

You are encouraged to probe the PostgreSQL JDBC Driver first. This is the
most convenient option, specifically if the system you are connecting with
already includes the PostgreSQL driver JAR file, and you can't change it.

However, applications using the PostgreSQL JDBC Driver may emit PostgreSQL-specific
SQL that CrateDB does not understand, while the framework assumes the
database would understand the PostgreSQL dialect completely.
In this case, use the CrateDB JDBC Driver instead
to ensure compatibility and allow downstream components to handle
CrateDB-specific behavior, for example, by employing a CrateDB-specific
SQL dialect implementation for their purposes and realms.

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
