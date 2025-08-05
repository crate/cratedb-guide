(connect)=

# Connect

This documentation section is about connecting your applications to CrateDB
and CrateDB Cloud, using database drivers, compatibility adapters and dialects.

:::{include} /_include/links.md
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 9 9 9


:::{rubric} Overview
:::
CrateDB connectivity options at a glance.

You have a variety of options to connect to CrateDB, and to integrate it with
off-the-shelf, 3rd-party, open-source, and proprietary applications.

:::{rubric} Protocol Support
:::
CrateDB supports both the HTTP protocol and the PostgreSQL wire protocol,
which ensures that many clients that work with PostgreSQL, will also work with
CrateDB. Through corresponding drivers, CrateDB is compatible with ODBC,
JDBC, and other database API specifications. By supporting SQL, CrateDB is
compatible with many standard database environments out of the box.

While it is generally recommended to use the PostgreSQL interface (PG) for maximum
compatibility in PostgreSQL environments, the HTTP interface supports CrateDB
bulk operations and CrateDB BLOBs, which are not supported by the PostgreSQL
protocol.

The HTTP protocol can also be used to connect from environments where
PostgreSQL-based communication is not applicable.

:::{rubric} Details
:::

CrateDB provides popular connectivity options with database drivers,
applications, and frameworks.

To learn more, please refer to the documentation sections and hands-on
tutorials about supported client drivers, libraries, and frameworks,
and how to configure and use them with CrateDB optimally.
::::


::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

```{rubric} Reference Manual
```
- [HTTP interface]
- [PostgreSQL interface]
- [SQL query syntax]
- [Bulk operations]
- [BLOBs]

```{rubric} Protocols and API Standards
```
- [HTTP protocol]
- [PostgreSQL wire protocol]
- [JDBC]
- [ODBC]
- [SQL]
::::

:::::


::::{grid} 2 2 2 4
:padding: 0

:::{grid-item-card}
:columns: 12
:link: connect-configure
:link-type: ref
:link-alt: Configure CrateDB connection string
:padding: 3
:class-card: sd-pt-1
:class-footer: text-smaller

Configure database URI
+++
In order to connect to CrateDB, your application or driver needs to be configured
with corresponding connection properties. Please note that different applications
and drivers may obtain connection properties in different formats.
:::

:::{grid-item-card}
:columns: 12
:link: connect-drivers
:link-type: ref
:link-alt: All drivers suitable for CrateDB
:padding: 3
:class-card: sd-pt-1
:class-footer: text-smaller

All drivers
+++
Drivers and adapters for supported programming languages,
frameworks, and environments.
:::

:::{grid-item-card}
:link: connect-java
:link-type: ref
:link-alt: Connect using Java
:padding: 3
:text-align: center
:class-card: sd-pt-1

Java
:::

:::{grid-item-card}
:link: connect-javascript
:link-type: ref
:link-alt: Connect using JavaScript
:padding: 3
:text-align: center
:class-card: sd-pt-1

JavaScript
:::

:::{grid-item-card}
:link: connect-python
:link-type: ref
:link-alt: Connect using Python
:padding: 3
:text-align: center
:class-card: sd-pt-1

Python
:::

::::


```{toctree}
:maxdepth: 1
:hidden:

configure
Drivers <drivers>
CLI programs <cli>
Dataframe libraries <df/index>
ORM libraries <orm>
```

```{toctree}
:maxdepth: 1
:hidden:

java
javascript
php
python
ruby
```


[ADBC]: https://arrow.apache.org/docs/format/ADBC.html
[Authentication]: inv:crate-reference:*:label#admin_auth
[BLOBs]: inv:crate-reference:*:label#blob_support
[Bulk operations]: inv:crate-reference:*:label#http-bulk-ops
[CrateDB Examples]: https://github.com/crate/cratedb-examples
[CrateDB HTTP interface]: inv:crate-reference:*:label#interface-http
[CrateDB PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[HTTP interface]: inv:crate-reference:*:label#interface-http
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity 
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[python-dbapi-by-example]: inv:crate-python:*:label#by-example
[python-sqlalchemy-by-example]: inv:sqlalchemy-cratedb:*:label#by-example
[schema]: inv:crate-reference:*:label#ddl-create-table-schemas
[schemas]: inv:crate-reference:*:label#ddl-create-table-schemas
[SQL]: https://en.wikipedia.org/wiki/Sql
[SQL query syntax]: inv:crate-reference:*:label#sql
[superuser]: inv:crate-reference:*:label#administration_user_management
