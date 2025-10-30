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
:gutter: 3
:padding: 0

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


:::::{grid} 2 3 4 5
:gutter: 2
:padding: 0

::::{grid-item-card}
:link: connect-odbc
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold

```{image} /_assets/icon/odbc-logo.png
:height: 80px
```
+++
Any (ODBC)
::::

::::{grid-item-card}
:link: connect-elixir
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold

```{image} https://cdn.prod.website-files.com/6047a9e35e5dc54ac86ddd90/63064ea203056632171dfaa2_43c017db.png
:width: 40px
```
+++
Elixir
::::

::::{grid-item-card}
:link: connect-go
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold
{fab}`golang`
+++
Go
::::

::::{grid-item-card}
:link: connect-java
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold
{fab}`java`
+++
Java (JDBC)
::::

::::{grid-item-card}
:link: connect-javascript
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold
{material-regular}`javascript;1.5em`
+++
JavaScript
::::

::::{grid-item-card}
:link: connect-php
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold
{fab}`php`
+++
PHP
::::

::::{grid-item-card}
:link: connect-python
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold
{fab}`python`
+++
Python
::::

::::{grid-item-card}
:link: connect-r
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold
{fab}`r-project`
+++
R
::::

::::{grid-item-card}
:link: connect-ruby
:link-type: ref
:class-body: sd-fs-1 sd-text-center
:class-footer: sd-fs-5 sd-font-weight-bold

```{image} /_assets/icon/ruby-logo.svg
:height: 40px
```
+++
Ruby
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

:::{rubric} See also
:::

:::::{grid}
:gutter: 2
:padding: 0

::::{grid-item-card} {material-outlined}`article;1.5em` Documentation
:columns: 12 6 3 3
- [HTTP interface]
- [PostgreSQL interface]
::::

::::{grid-item-card} {material-outlined}`link;1.5em` Related
:columns: 12 6 3 3
- [Authentication]
- [SQL query syntax]
- [Bulk operations]
- [BLOB support][CrateDB BLOB support]
::::

::::{grid-item-card} {material-outlined}`read_more;1.5em` Read more
:columns: 12 12 6 6
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

elixir/index
go/index
java/index
javascript
php
python
r/index
ruby
odbc/index
natural
All drivers <drivers>
```


[Authentication]: inv:crate-reference:*:label#admin_auth
[Bulk operations]: inv:crate-reference:*:label#http-bulk-ops
[HTTP interface]: inv:crate-reference:*:label#interface-http
[PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[SQL query syntax]: inv:crate-reference:*:label#sql
