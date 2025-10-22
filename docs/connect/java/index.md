(java)=
(connect-java)=

# Java

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Java applications mostly use JDBC to connect to CrateDB.
:::

## Protocols

### JDBC

:::{div}
[JDBC] is a standard Java API that provides a common interface for accessing
databases in Java.
:::

:::{rubric} Driver options
:::

:::{div}
You have two JDBC driver options: The [PostgreSQL
JDBC Driver] and the {ref}`crate-jdbc:index`.
PostgreSQL JDBC uses the `jdbc:postgresql://` protocol identifier,
while CrateDB JDBC uses `jdbc:crate://`.
:::

You are encouraged to probe the PostgreSQL JDBC Driver first. This is the
most convenient option, specifically if the system you are connecting with
already includes the driver jar.

However, applications using the PostgreSQL JDBC Driver may emit PostgreSQL-specific
SQL that CrateDB does not understand. Use the CrateDB JDBC Driver instead
to ensure compatibility and allow downstream components to handle
CrateDB-specific behavior, for example, by employing a CrateDB-specific
SQL dialect implementation.

The {ref}`crate-jdbc:internals` page includes more information
about compatibility and differences between the two driver variants,
and more details about the CrateDB JDBC Driver.

### HTTP

You can also talk to CrateDB using HTTP, using any HTTP library of your choice.
Below is a quick example using Apache Commons HTTP.


## Driver list

:::::{grid} 2 2 2 3
:gutter: 3
:padding: 0

::::{grid-item-card} {fab}`java;fa-xl` PostgreSQL JDBC
:link: postgresql-jdbc
:link-type: ref
:link-alt: PostgreSQL JDBC (pgJDBC)
The PostgreSQL JDBC driver.
::::

::::{grid-item-card} {fab}`java;fa-xl` CrateDB JDBC
:link: cratedb-jdbc
:link-type: ref
:link-alt: CrateDB JDBC
The CrateDB JDBC driver.
::::

::::{grid-item-card} {fab}`hibernate` Hibernate
:link: hibernate
:link-type: ref
:link-alt: Hibernate with CrateDB
A Quarkus/Panache example using Hibernate.
::::

::::{grid-item-card} {fab}`jooq` jOOQ
:link: hibernate
:link-type: ref
:link-alt: jOOQ with CrateDB
A jOOQ example.
::::

::::{grid-item-card} {fab}`junit` Software testing
:link: java-testing
:link-type: ref
:link-alt: Software testing with CrateDB and Java
JUnit and Testcontainers for CrateDB.
::::

:::::

{material-outlined}`apps;2em`

:::{toctree}
:maxdepth: 1
:hidden:
postgresql-jdbc
cratedb-jdbc
hibernate
jooq
testing
:::
