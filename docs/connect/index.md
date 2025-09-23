(connect)=
# Connect

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
off-the-shelf, 3rd-party, open-source, and proprietary applications or frameworks.

:::{rubric} Protocol Support
:::
CrateDB supports both the HTTP protocol and the PostgreSQL wire protocol,
which ensures that many clients that work with PostgreSQL, will also work with
CrateDB.

Through corresponding drivers, CrateDB is compatible with ODBC,
JDBC, and other database API specifications. By supporting SQL, CrateDB is
compatible with many standard database environments out of the box.

The HTTP protocol can be used to connect from environments where
PostgreSQL-based communication is not applicable.

:::{rubric} Notes
:::
While it is generally recommended to use the PostgreSQL interface (PG) for maximum
compatibility in PostgreSQL environments, the HTTP interface supports CrateDB
bulk operations and BLOBs, which are not supported by the PostgreSQL
protocol.
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
- [BLOB support][CrateDB BLOBs]

```{rubric} Protocols and API Standards
```
- [HTTP protocol]
- [PostgreSQL wire protocol]
- [JDBC]
- [ODBC]
- [SQL]
::::

:::::


:::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`link;2em` How to connect
:class-body: ul-li-wide
- {ref}`connect-configure`

  To connect to CrateDB, your application or driver needs to be configured
  with corresponding database URI and connection properties.

- {ref}`CLI programs <connect-cli>`

  Use CLI programs to connect to CrateDB.

- {ref}`Database IDEs <connect-ide>`

  Use IDEs to connect to CrateDB.
+++
Database connectivity options and tools.
::::

::::{grid-item-card} {material-outlined}`link;2em` How to connect
- {ref}`connect-java`
- {ref}`connect-javascript`
- {ref}`connect-php`
- {ref}`connect-python`
- {ref}`connect-ruby`
- Overview: {ref}`connect-drivers`

  All available CrateDB drivers and adapters for supported programming languages,
  frameworks, and environments.
+++
Database driver connection examples.
::::

:::::

```{toctree}
:maxdepth: 1
:hidden:

configure
connect
CLI programs <cli>
ide
Drivers <drivers>
DataFrame libraries <df/index>
mcp/index
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
[Bulk operations]: inv:crate-reference:*:label#http-bulk-ops
[CrateDB Examples]: https://github.com/crate/cratedb-examples
[HTTP interface]: inv:crate-reference:*:label#interface-http
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[schema]: inv:crate-reference:*:label#ddl-create-table-schemas
[schemas]: inv:crate-reference:*:label#ddl-create-table-schemas
[SQL]: https://en.wikipedia.org/wiki/Sql
[SQL query syntax]: inv:crate-reference:*:label#sql
[superuser]: inv:crate-reference:*:label#administration_user_management
