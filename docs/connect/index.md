(connect)=
# Connect / Drivers

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
CrateDB connectivity options at a glance.
:::

Choose from a variety of options to connect to CrateDB, and to integrate it with
off-the-shelf, third-party, open-source, and proprietary applications, drivers,
and frameworks.

:::{rubric} Get started
:::

To get started,
please learn about typical connection URI formats for CrateDB and its
default client applications.

:::::{grid} 2 2 2 3
:padding: 0
:gutter: 4

::::{grid-item-card} {material-outlined}`link;2em` General information
:link: connect-configure
:link-type: ref
:link-alt: CrateDB connect URI
Database URI and connection properties for different drivers.
::::

::::{grid-item-card} {material-outlined}`apps;2em` Applications
:link: connect-applications
:link-type: ref
:link-alt: CrateDB standard client applications
Use CLI programs or database IDEs to connect to CrateDB.
::::

:::::


:::{rubric} Drivers by language
:::

CrateDB drivers and adapters for supported programming languages, frameworks, and environments.

:::::{grid} 2 2 2 4
:margin: 4 4 0 0
:padding: 0

::::{grid-item-card} Java
:link: connect-java
:link-type: ref
:link-alt: Connect to CrateDB using Java
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6
{fab}`java`
::::

::::{grid-item-card} JavaScript
:link: connect-javascript
:link-type: ref
:link-alt: Connect to CrateDB using JavaScript
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6
{material-regular}`javascript;2em`
::::

::::{grid-item-card} PHP
:link: connect-php
:link-type: ref
:link-alt: Connect to CrateDB using PHP
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6
{fab}`php`
::::

::::{grid-item-card} Python
:link: connect-python
:link-type: ref
:link-alt: Connect to CrateDB using Python
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6
{fab}`python`
::::

::::{grid-item-card} Ruby
:link: connect-ruby
:link-type: ref
:link-alt: Connect to CrateDB using Ruby
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6

```{image} /_assets/icon/ruby-logo.svg
:width: 40px
```

::::

:::::


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

:::{note}
While it is generally recommended to use the PostgreSQL interface (PG) for maximum
compatibility in PostgreSQL environments, the HTTP interface supports CrateDB
bulk operations and BLOBs, which are not supported by the PostgreSQL
protocol.
:::

:::{rubric} Further reading
:::

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`article;1.5em` Documentation
:columns: 3
- [HTTP interface]
- [PostgreSQL interface]
::::

::::{grid-item-card} {material-outlined}`link;1.5em` Related
:columns: 3
- [Authentication]
- [SQL query syntax]
- [Bulk operations]
- [BLOB support][CrateDB BLOBs]
::::

::::{grid-item-card} {material-outlined}`read_more;1.5em` Read more
:columns: 6
- {ref}`All drivers <connect-drivers>`
- {ref}`All integrations <integrate>`
- {ref}`Ingestion methods <ingest>`
- {ref}`connect-natural`
::::

:::::


```{toctree}
:maxdepth: 1
:hidden:

general
application
```

```{toctree}
:maxdepth: 1
:hidden:

java
javascript
php
python
ruby
natural
All drivers <drivers>
```


[Authentication]: inv:crate-reference:*:label#admin_auth
[Bulk operations]: inv:crate-reference:*:label#http-bulk-ops
[HTTP interface]: inv:crate-reference:*:label#interface-http
[PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[SQL query syntax]: inv:crate-reference:*:label#sql
