---
orphan: true
---


<style>
/* Cards with links */
.sd-hide-link-text {
  height: 0;
}
</style>



# CrateDB Documentation

Documentation overview for CrateDB and CrateDB Cloud.
<br>
Reference manuals, tutorials, example code, and more.

::::{grid} 1 1 2 2
:margin: 1
:padding: 2

:::{grid-item-card} {material-outlined}`rocket_launch;1.7em` CrateDB Cloud
:link: cloud-docs-index
:link-type: ref
:link-alt: CrateDB Cloud
:padding: 2
:class-title: sd-fs-5

CrateDB Cloud is a fully managed, terabyte-scale, and cost-effective analytics
database that lets you run analytics over vast amounts of data in near real time,
even with complex queries.

CrateDB Cloud is an SQL database service for enterprise data warehouse workloads,
that works across clouds and scales with your data.
:::

:::{grid-item-card} {material-outlined}`auto_stories;1.7em` Database Manual
:link: cloud-docs-index
:link-type: ref
:link-alt: CrateDB Cloud
:padding: 2
:class-title: sd-fs-5

CrateDB is a distributed and scalable SQL database for storing and
analyzing massive amounts of data in near real-time, even with complex queries.
It is PostgreSQL-compatible, and based on Lucene. 

CrateDB is an open source multi-model database for time series, documents
and vectors, combining the simplicity of SQL with the scalability of a
distributed architecture.
:::

::::


::::{grid} 1
:margin: 1
:padding: 2

:::{grid-item-card} {material-outlined}`link;1.7em` Client Libraries
:link: https://cratedb.com/docs/crate/clients-tools/en/latest/connect/
:link-alt: CrateDB Client Drivers and Libraries
:padding: 2
:class-title: sd-fs-5

Connect your applications to CrateDB and CrateDB Cloud, using database
drivers, libraries, adapters, connectors, and dialects.

CrateDB supports both the [HTTP protocol] and the [PostgreSQL wire protocol],
which ensures that many clients that work with PostgreSQL, will also work with
CrateDB. Through corresponding drivers, CrateDB is compatible with [ODBC],
[JDBC], and other database API specifications.

:::

::::


## Guides and Tutorials 


:::{rubric} Introduction
:::
Learn about the fundamentals of CrateDB and its utility applications.

::::{grid} 2 3 3 3
:padding: 0

:::{grid-item-card} Getting Started
:link: https://cratedb.com/docs/guide/getting-started.html
:link-alt: Getting started with CrateDB
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller

{material-outlined}`lightbulb;3.5em`
+++
Learn how to interact with the database for the first time.
:::


:::{grid-item-card} Admin UI
:link: https://cratedb.com/docs/crate/admin-ui/
:link-alt: The CrateDB Admin UI
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller

{material-outlined}`admin_panel_settings;3.5em`
+++
Learn about CrateDB's included web administration interface.
:::


:::{grid-item-card} Crash CLI
:link: https://cratedb.com/docs/crate/crash/
:link-alt: The Crash CLI
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller

{material-outlined}`terminal;3.5em`
+++
A command-line interface (CLI) tool for working with CrateDB.
:::

::::


:::{rubric} Drivers and Integrations
:::

Learn about database client libraries, drivers, adapters, connectors,
and integrations with 3rd-party applications.

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
Discover integrations and solutions from the open source community and CrateDB partners.
:::


:::{grid-item-card} Integration Tutorials I
:link: integrate
:link-type: ref
:link-alt: Integration Tutorials I
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller

{material-outlined}`school;3.5em`
+++
Learn about the variety of options to connect and integrate with 3rd-party applications.
:::


:::{grid-item-card} Integration Tutorials II
:link: https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015
:link-alt: Integration Tutorials II
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller

{material-outlined}`local_library;3.5em`
+++
Integration-focused tutorials to help you use CrateDB together with other tools and libraries.
:::


::::


## Examples

Learn how to use CrateDB by digesting concise examples.

::::{grid} 2 3 3 3
:padding: 0

:::{grid-item-card} CrateDB Examples 
:link: https://github.com/crate/cratedb-examples
:link-alt: CrateDB Examples
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller

{material-outlined}`play_circle;3.5em`
+++
A collection of clear and concise examples how to work with CrateDB.
:::

:::{grid-item-card} Sample Apps 
:link: https://github.com/crate/crate-sample-apps/
:link-alt: CrateDB Sample Apps
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller

{material-outlined}`apps;3.5em`
+++
Different client libraries used by canonical guestbook demo web applications. 
:::

::::


<br>

----

**Resources:** [Academy] • [Blog] • [Community] • [Customers] • [GitHub] • [Support]


[Academy]: https://learn.cratedb.com/
[Blog]: https://cratedb.com/blog
[Community]: https://community.cratedb.com/
[Customers]: https://cratedb.com/customers
[GitHub]: https://github.com/crate
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity 
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[Support]: https://cratedb.com/support/
