(index)=

<!--
NOTE: When adding or removing top-level entries in this toctree, you must also
update the corresponding hardcoded links in the theme's sidebartoc.html file:
https://github.com/crate/crate-docs-theme/blob/main/src/crate/theme/rtd/crate/sidebartoc.html

Look for the "Section A: Guide" section in the {% else %} branch.
-->

```{toctree}
:hidden:

start/index
handbook/index
```

# Welcome to CrateDB

CrateDB is a **distributed SQL database** designed for **real-time analytics
and search** at scale. Whether you are working with time series data, full-text
search, or large volumes of structured and semi-structured data, CrateDB gives
you the **power of SQL**, the **scalability of NoSQL**, and the **flexibility
of a modern data platform**.

:::::{grid}
:padding: 4
:gutter: 2

::::{grid-item}
:class: rubric-slimmer
:columns: 6

:::{rubric} Why CrateDB?
:::
CrateDB was built for speed, scale, and simplicity:

* **Real-time performance:** Query millions of records per second with sub-second response times.
* **AI/ML-ready:** Store and serve data for modern AI pipelines.
* **Search + SQL**: Combine full-text search with rich SQL queries.
* **Geospatial & time series**: Native support for IoT, sensor data, and location-based use cases.
* **Horizontal scalability**: Add nodes effortlessly to handle more data and users.
* **Resilient and fault-tolerant**: Built-in replication and recovery.
::::

::::{grid-item}
:class: rubric-slimmer
:columns: 6

:::{rubric} What Can You Build?
:::
CrateDB is used across industries to power:

* Real-time **dashboards and analytics**
* Hybrid **search and retrieval experiences**
* Large-scale **IoT telemetry and analytics**
* Complex **geospatial applications**
* **AI-powered features** embedded in your apps
* **Industrial IoT** data backends
::::

:::::


:::{rubric} Benefits and Features
:::

Whether you are a developer,
database administrator, or just starting your journey with CrateDB, our
documentation provides the information and knowledge needed to build
real-time analytics and hybrid search applications that leverage CrateDB's
unique features.

* In a unified data platform, CrateDB lets you analyze relational, JSON,
  time series, geospatial, full-text, and vector data in a single system,
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
* Columnar storage enables fast query and aggregation performance.
* PostgreSQL wire protocol compatibility and an HTTP interface provide versatile
  integration capabilities.
* AI-ready: The vector store subsystem integrates well
  with an extensive third-party ecosystem of AI/ML frameworks for advanced data
  analysis and data-driven decisions.


## Get Started

:::{card} {material-outlined}`not_started;1.7em` CrateDB Cloud
:link: first-steps
:link-type: ref
:link-alt: Getting started with CrateDB Cloud
:class-title: sd-fs-5

Start with a fully managed FREE FOREVER CrateDB instance to quickly explore
features through guided tutorials or on your own with custom data.
+++
```{button-ref} first-steps
:color: primary
:expand:
**Get started with CrateDB Cloud**
```
:::


## Learn

:::{rubric} Introduction
:::
Learn about the fundamentals of CrateDB, guided and self-guided.

::::{grid} 2 2 4 4
:padding: 0

:::{grid-item-card}
:link: getting-started
:link-type: ref
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
:link: index
:link-type: ref
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


:::{rubric} Admin Tools
:::
Learn about the fundamental tools that support working directly with CrateDB.

::::{grid} 2 3 3 3
:padding: 0

:::{grid-item-card} Admin UI
:link: crate-admin-ui:index
:link-type: ref
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
:link: crate-crash:index
:link-type: ref
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


:::{rubric} Resources
:::

::::::{grid} 1
:margin: 1
:padding: 2

:::::{grid-item}
:margin: 0
:padding: 2

::::{grid} 2
:margin: 0
:padding: 0

:::{grid-item-card} {material-outlined}`lightbulb;1.7em` Database Features
:link: features
:link-type: ref
:link-alt: Database Features
:class-title: sd-fs-5

Explore all functional, operational and advanced features of CrateDB at a glance.
:::

:::{grid-item-card} {material-outlined}`auto_stories;1.7em` Database Manual
:link: crate-reference:index
:link-type: ref
:link-alt: Database Manual
:class-title: sd-fs-5

Learn core CrateDB concepts, including data modeling, querying data,
aggregations, sharding, and more.
:::

::::
:::::

:::{grid-item-card} {material-outlined}`link;1.7em` Connectivity Options
:link: connect
:link-type: ref
:link-alt: CrateDB: Client Drivers and Libraries
:padding: 2
:class-title: sd-fs-5

Learn how to connect your applications using database drivers, libraries,
adapters, and connectors.

CrateDB supports both the [HTTP protocol] and the [PostgreSQL wire protocol],
ensuring compatibility with many PostgreSQL clients.

Through corresponding drivers, adapters, and client libraries, CrateDB is
compatible with [ODBC], [JDBC], and other database API specifications.
:::

:::{grid-item-card} {material-outlined}`integration_instructions;1.7em` Integrations
:link: integrate
:link-type: ref
:link-alt: Integrations
:padding: 2
:class-title: sd-fs-5

Explore the many options for integrating with third-party applications and
frameworks.
:::

::::::

:::{rubric} Examples
:::

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
A collection of clear, concise examples of how to work with CrateDB.
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
Canonical guestbook demo applications implemented with different client libraries.
:::

::::


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

::::{card} CrateDB curated videos
:class-footer: sd-fs-6

In [this video playlist] Simon Prickett shares videos he has been part of that
show what CrateDB is and how you can use it for a variety of projects.
Don't miss the relevant [CrateDB customer stories].
::::


[CrateDB customer stories]: https://www.youtube.com/playlist?list=PLDZqzXOGoWUJrAF_lVx9U6BzAGG9xYz_v
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[this video playlist]: https://www.youtube.com/playlist?list=PL3cZtICBssphXl5rHgsgG9vTNAVTw_Veq
