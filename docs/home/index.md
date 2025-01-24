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

Welcome to the official CrateDB Documentation. Whether you are a developer,
database administrator, or just starting your journey with CrateDB, our
documentation provides the information and knowledge needed to build
real-time analytics and hybrid search applications that leverage CrateDB's
unique features.

:::{rubric} Benefits
:::
* In a unified data platform approach, CrateDB includes analyzing relational, JSON,
  time-series, geospatial, full-text, and vector data within a single system,
  eliminating the need for multiple databases.
* The fully distributed SQL query engine, built on top of Apache Lucene,
  and inheriting technologies from Elasticsearch/OpenSearch, provides performant
  aggregations and advanced SQL features like JOINs and CTEs on large datasets
  of semi-structured data.
* Real-time indexing automatically indexes all columns, including nested
  structures, as data is ingested, eliminating the need to worry about
  indexing strategy.
* The flexible data schema dynamically adapts based on the data you ingest,
  offering seamless integration and instant readiness for analysis.
* Columnar storage enables fast search query and aggregation performance.
* PostgreSQL wire protocol compatibility and a HTTP interface provide versatile
  integration capabilities.
* AI-ready: The vector store subsystem integrates well
  with an extensive 3rd party ecosystem of AI/ML frameworks for advanced data
  analysis and data-driven decisions.


::::::{grid} 1
:margin: 1
:padding: 2

:::{grid-item-card} {material-outlined}`rocket_launch;1.7em` CrateDB Cloud
:link: cloud-docs-index
:link-type: ref
:link-alt: CrateDB Cloud
:padding: 2
:class-title: sd-fs-5

Start with a fully managed CrateDB instance to accelerate and simplify working
with analytical data. CrateDB Cloud enables seamless deployment, monitoring,
backups, and scaling of CrateDB clusters on AWS, Azure or GCPs, eliminating
the need for direct database management.

With CrateDB Cloud, you can skip infrastructure setup and focus on delivering
value for your business with a query console, SQL Scheduler, table policies
and various connectors to import data.
+++
```{button-link} https://cratedb.com/docs/cloud/tutorials/quick-start.html
:color: primary
:expand:
**Start forever free cluster with 8 GB of storage**
```
:::

:::::{grid-item}
:margin: 0
:padding: 2

::::{grid} 2
:margin: 0
:padding: 0

:::{grid-item-card} {material-outlined}`lightbulb;1.7em` Database Features
:link: https://cratedb.com/docs/guide/feature/
:link-alt: Database Features
:class-title: sd-fs-5

Explore all functional, operational and advanced features of CrateDB at a glance.
:::

:::{grid-item-card} {material-outlined}`auto_stories;1.7em` Database Manual
:link: https://cratedb.com/docs/reference/
:link-alt: Database Manual
:class-title: sd-fs-5

Learn core CrateDB concepts, including data modeling, querying data,
aggregations, sharding, and more.
:::

::::
:::::

:::{grid-item-card} {material-outlined}`link;1.7em` Client Libraries
:link: https://cratedb.com/docs/crate/clients-tools/en/latest/connect/
:link-alt: CrateDB: Client Drivers and Libraries
:padding: 2
:class-title: sd-fs-5

Learn how to connect your applications using database drivers, libraries,
adapters, and connectors.

CrateDB supports both the [HTTP protocol] and the [PostgreSQL wire protocol],
ensuring compatibility with many PostgreSQL clients.

Through corresponding drivers and adapters, CrateDB is compatible with [ODBC],
[JDBC], and other database API specifications.
:::

::::::


## Learn

:::{rubric} Videos
:::
::::{card} Today's data challenges and a high level overview of CrateDB
:class-title: sd-fs-4
:class-body: sd-text-center
:class-footer: sd-fs-6

:::{youtube} cByAOsaYddQ
:::
+++
_Webinar: Turbocharge your aggregations, search & AI models & get real-time insights._

:::{div} text-smaller
Discover CrateDB, the leading real-time analytics database. It provides the
flexibility, speed, and scalability necessary to master today's data challenges.
Watch this video to learn how CrateDB empowers you with real-time insights
into your data to fuel advanced analytics, search, and AI models—enabling
informed decisions that drive meaningful impact.
:::
::::

::::{card} CrateDB Videos curated by Simon Prickett
:class-footer: sd-fs-6

Simon leads Developer Relations at CrateDB. Here, he is [sharing a playlist
of videos] he has been part of that will show you what CrateDB is and how
you can use it for a variety of projects.
Make sure you also do not miss relevant [CrateDB customer stories].
::::


:::{rubric} Introduction
:::
Learn about the fundamentals of CrateDB, guided and self-guided.

::::{grid} 2 2 4 4
:padding: 0

:::{grid-item-card}
:link: https://cratedb.com/docs/guide/getting-started.html
:link-alt: Getting started with CrateDB
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: sd-text-center sd-fs-5
:class-footer: text-smaller
Getting Started
^^^
{material-outlined}`not_started;3.5em`
+++
Learn how to interact with the database for the first time.
:::

:::{grid-item-card}
:link: https://cratedb.com/docs/guide/
:link-alt: The CrateDB Guide
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: sd-text-center sd-fs-5
:class-footer: text-smaller
The CrateDB Guide
^^^
{material-outlined}`hiking;3.5em`
+++
Guides and tutorials about how to use CrateDB in practice.
:::

:::{grid-item-card}
:link: https://learn.cratedb.com/
:link-alt: The CrateDB Academy
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: sd-text-center sd-fs-5
:class-footer: text-smaller
Academy Courses
^^^
{material-outlined}`school;3.5em`
+++
A learning hub dedicated to data enthusiasts.
:::

:::{grid-item-card}
:link: https://community.cratedb.com/
:link-alt: The CrateDB Community Portal
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: sd-text-center sd-fs-5
:class-footer: text-smaller
Community Portal
^^^
{material-outlined}`groups;3.5em`
+++
A hangout place for members of the CrateDB community.
:::

::::


:::{rubric} Database Clients and Tools
:::
Learn about the fundamental tools and utility programs that support working directly with CrateDB.

::::{grid} 2 3 3 3
:padding: 0

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
and integrations with 3rd-party applications and frameworks.

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
Discover integrations and solutions from the open-source community and CrateDB partners.
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
{material-outlined}`integration_instructions;3.5em`
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

**Resources:**
[Academy] • [Blog] • [Community] • [Customers] • [Examples] • 
[GitHub] • [Guide] • [Support]


[Academy]: https://learn.cratedb.com/
[Blog]: https://cratedb.com/blog
[Community]: https://community.cratedb.com/
[CrateDB customer stories]: https://www.youtube.com/playlist?list=PLDZqzXOGoWUJrAF_lVx9U6BzAGG9xYz_v
[Customers]: https://cratedb.com/customers
[Examples]: https://github.com/crate/cratedb-examples
[GitHub]: https://github.com/crate
[Guide]: https://cratedb.com/docs/guide/
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[Integrations]: #integrate
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity 
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[sharing a playlist of videos]: https://www.youtube.com/playlist?list=PL3cZtICBssphXl5rHgsgG9vTNAVTw_Veq
[Support]: https://cratedb.com/support/
