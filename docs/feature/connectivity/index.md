(connect)=
(connectivity)=

# Connectivity

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
off-the-shelve, 3rd-party, open-source, and proprietary applications.

:::{rubric} About
:::
CrateDB supports both the HTTP protocol and the PostgreSQL wire protocol,
which ensures that many clients that work with PostgreSQL, will also work with
CrateDB.

Through corresponding drivers, CrateDB is compatible with JDBC, ODBC,
and other database API specifications.
By supporting SQL, CrateDB is compatible with many standard database
environments out of the box.

:::{rubric} Details
:::

CrateDB provides plenty of connectivity options with database drivers,
applications, and frameworks, in order to get time series data in and
out of CrateDB, and to connect to other applications.

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

```{rubric} Protocols and API Standards
```
- [HTTP protocol]
- [PostgreSQL wire protocol]
- [JDBC]
- [ODBC]
- [SQL]
::::

:::::


## Synopsis

In order to provide a CrateDB instance for testing purposes, use, for
example, Docker.
```shell
docker run --rm -it --publish=4200:4200 --publish=5432:5432 crate/crate:nightly
```
:::{tip}
The [CrateDB Examples] repository also includes a collection of
clear and concise examples how to connect to and work with CrateDB,
using different environments, applications, or frameworks.
:::


## Learn

::::{grid} 2 3 3 3
:padding: 0

:::{grid-item-card} Ecosystem Catalog
:link: catalog
:link-type: ref
:link-alt: Ecosystem Catalog
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller
{material-outlined}`category;3.5em`
+++
Explore all open-source and partner applications and solutions.
:::

:::{grid-item-card} Driver Support
:link: crate-clients-tools:connect
:link-type: ref
:link-alt: Driver Support
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller
{material-outlined}`link;3.5em`
+++
List of HTTP and PostgreSQL client drivers, and tutorials.
:::

:::{grid-item-card} Integration Tutorials
:link: integrate
:link-type: ref
:link-alt: Integration Tutorials
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller
{material-outlined}`local_library;3.5em`
+++
Learn how to integrate CrateDB with applications and tools.
:::

::::



[CrateDB Examples]: https://github.com/crate/cratedb-examples
[Driver Support]: inv:crate-clients-tools:*:label#connect
[Ecosystem Catalog]: inv:crate-clients-tools:*:label#index
[HTTP interface]: inv:crate-reference:*:label#interface-http
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[SQL]: https://en.wikipedia.org/wiki/Sql
[SQL query syntax]: inv:crate-reference:*:label#sql


```{include} /_include/styles.html
```
