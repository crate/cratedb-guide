(rockset)=
# Welcome Rockset Developers

:::{include} /_include/links.md
:::

<style>
/* Cards with links */
.sd-hide-link-text {
  height: 0;
}
</style>

:::::{grid} 1 1 2 2
:padding: 0

::::{grid-item}
:columns: auto auto 8 8

:::{rubric} Introduction
:::
Because the [Rockset HTTP API is sunsetting on September 30th, 2024],
and CrateDB covers a reasonable amount of features, this page
presents its capabilities to support your analytical workloads
and data consolidation efforts.

Both Rockset and CrateDB use SQL, so there is no need for your teams to learn
a new query language or querying regime.

:::{rubric} Details
:::
When it comes to **real-time analytics and hybrid search**,
CrateDB is the only solution that offers a similar approach to converged indexing,
full-text search, vector search, and geospatial support in a single storage engine,
accessible via native SQL and HTTP endpoints.

Because CrateDB is [truly open-source software] with a [clear commitment],
you will no longer find yourself
in vendor lock-in situations and service shutdowns due to M&A procedures and
similar occasions, being forced to migrate to a different system once again.

As we work with more and more companies looking to migrate their workloads
from [Rockset] to [CrateDB], we have built expertise on the details of what
a [migration] entails. This page shares a few insights on this topic, and
why CrateDB is your go-to choice when selecting a cost-effective
replacement solution.
::::

::::{grid-item}
:columns: auto auto 4 4

:::{card}
:link: https://cratedb.com/resources/webinars/lp-wb-from-rockset-to-cratedb
:link-alt: "Webinar: From Rockset to CrateDB"
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: text-smaller
:class-footer: text-smaller
{material-outlined}`cast_for_education;3.7em`

Watch our Webinars
^^^
- Why CrateDB is a perfect \[Rockset\] replacement for real-time analytics and hybrid search. 
- How CrateDB compares to \[Rockset\] and Elasticsearch/OpenSearch for streaming ingest.
- Why CrateDB is a cost-effective alternative to \[Rockset\].
+++
Watch recordings of previous sessions from this webinar series.
:::

::::
:::::


## What's Inside

:::{rubric} Introduction and Comparison
:::
An overview about CrateDB, and a side-by-side comparison, tuned for Rockset users.

:::::{card}
:link: https://cratedb.com/blog/why-cratedb-is-a-perfect-rockset-replacement 
:link-alt: "Why CrateDB is a perfect Rockset replacement"
:margin: 3
:class-header: sd-font-weight-bold sd-fs-5
:class-title: sd-fs-5
{material-outlined}`swap_horiz;1.7em` Why CrateDB is a perfect Rockset replacement
^^^
::::{grid} 2
:::{grid-item}
:columns: 9
Learn about the top five reasons for choosing CrateDB as a Rockset replacement.
1. Converged index aka. automated indexing.
2. Fully-featured SQL and HTTP interface.
3. Support for structured, semi-structured, and unstructured data.
4. Support for real-time streaming and updates.
5. CrateDB is fully open source and deployment-agnostic.
:::
:::{grid-item}
:columns: 3
{tags-primary}`CrateDB vs. Rockset` \
{tags-info}`Features` \
{tags-secondary}`Blog`
:::
::::
+++
A detailed comparison to help you in selecting the right alternative and ensuring a
timely and seamless migration.
:::::

:::::{card}
:link: https://cratedb.com/blog/how-cratedb-compares-to-rockbench
:link-alt: "Performance Matters"
:margin: 3
:class-header: sd-font-weight-bold sd-fs-5
:class-title: sd-fs-5
{material-outlined}`stacked_line_chart;1.7em` Performance Matters
^^^
::::{grid} 2
:::{grid-item}
:columns: 9
Insights into how ingest performance compares between Rockset and CrateDB.

We used the Rockbench benchmark to evaluate ingestion performance on throughput
and data latency. The results are impressive.

- CrateDB outperforms Rockset on the same hardware while saving between
  20% and 60% on costs.
- CrateDB achieves 6-9x lower latencies than Rockset for streaming ingest.
  When data volume increases, the latency increased
  linearly in Rockset, while remaining mostly flat in CrateDB.
:::
:::{grid-item}
:columns: 3
{tags-primary}`CrateDB vs. Rockset` \
{tags-info}`Performance` \
{tags-secondary}`Blog`
:::
::::
+++
A benchmark evaluation demonstrating CrateDB's ability to efficiently support
high-velocity data streams while it delivers more constant query latencies
than Rockset.
:::::


:::::{card}
:link: https://cratedb.com/blog/cost-efficient-rockset-alternative
:link-alt: "Cost Matters"
:margin: 3
:class-header: sd-font-weight-bold sd-fs-5
:class-title: sd-fs-5
{material-outlined}`add_card;1.7em` Cost Matters
^^^
::::{grid} 2
:::{grid-item}
:columns: 9

Based on [Rockset's pricing examples], we combined the experience of real-world
customer projects as well as Rockbench benchmark runs, to compare the costs for
multiple scenarios.

Examples: A geospatial search application for logistics tracking, a recommendation engine, a backend
for in-app search and analytics, a backend for real-time game telemetry,
and an anomaly detection application.
:::
:::{grid-item}
:columns: 3
{tags-primary}`CrateDB vs. Rockset` \
{tags-info}`Costs` \
{tags-secondary}`Blog`
:::
::::
+++
Results of comparing against Rockset's canonical example application scenarios
show that CrateDB Cloud is in a similar ballpark and oftentimes a bit cheaper
than solutions from other vendors.
:::::



:::{rubric} Features and Benefits
:::
CrateDB's benefits and principles in a nutshell.

:::::{grid} 1 1 2 2
:gutter: 3

::::{grid-item-card}
:::{rubric} Fundamentals
:::
CrateDB is a scalable and cost-effective real-time analytics database,
combining complex JSON handling, time series, geospatial data, full-text
search, and vector search in one single storage engine.

- [All features of CrateDB at a glance]
- [The CrateDB Documentation]

:::{rubric} Foundation
:::
Built on top of Apache Lucene and Elasticsearch, CrateDB [automatically
indexes all your data] in exactly the same way as Rockset's [Converged
Index™], in order to achieve millisecond response times for any kind
of query and aggregation workloads.

:::{rubric} Availability
:::
CrateDB is offered as a managed service available on AWS, Azure, and GCP,
and also as a fully open source edition.

- No vendor lock-in and service sunsetting woes.
- No capacity limits.

See [CrateDB Cloud] and [CrateDB Editions].
::::

::::{grid-item-card}
:::{rubric} Interoperability, Open Source, Open Standards
:::
Rockset is a proprietary solution available as a managed service in AWS only.

With CrateDB, you leverage open standards to avoid vendor lock-in and
future-proof your systems.

CrateDB's [open-source code base] accepts contributions from community
members and corporates, so you can easily add features you need, and
distribute them to downstream users in multiple ways, without any
licensing hassles.

:::{rubric} Development and Embedding
:::
The attributes enumerated above allow you to integrate CrateDB into your
products seamlessly, and supply your engineers and continuous integration
systems with dedicated instances of CrateDB, instead of needing to run
them against a cloud-only service, which is slowing down development,
mostly due to API rate-limiting measures.
::::

:::::


## Learn
Learn how to use CrateDB.

:::::{grid} 1 1 2 2
:gutter: 3

::::{grid-item-card}
:::{rubric} SQL Query Language
:::
CrateDB's lingua franca is SQL, ready for big data, very similar to
Rockset's SQL dialect.
- [CrateDB SQL]
- [Advanced Querying]
::::

::::{grid-item-card}
:::{rubric} Migrating queries from Rockset to CrateDB
:::
Because both Rockset and CrateDB use SQL, there is no need for your teams to
learn a new query language. There are a few differences in the SQL dialect,
where we provide relevant support information to make transitioning easier.
:::{toctree}
Migrate Queries <query>
::::

:::::


## Integrate
Learn how to migrate your database use cases and workloads from Rockset to CrateDB.

:::::{grid} 1 1 2 2
:gutter: 3

::::{grid-item-card}
:::
:::{rubric} Migrating data using AWS DMS
:::
- [AWS DMS Integration with CrateDB]
:::{rubric} Migrating data from DynamoDB to CrateDB
:::
- [DynamoDB Table Loader]
- [DynamoDB CDC Relay]
- [DynamoDB CDC Relay with AWS Lambda]
- Blog: [Replicating CDC events from DynamoDB to CrateDB]
:::{rubric} Migrating data from MongoDB to CrateDB
:::
- [MongoDB Table Loader]
- [MongoDB CDC Relay]
:::{rubric} General I/O
:::
- [Data loading](#etl) with CrateDB.
- [](#cdc) with CrateDB.
::::

::::{grid-item-card}
:::{rubric} Integrating data from other sources into CrateDB
:::
With Rockset, as a complete data warehouse system, integrating data from other
sources is a nobrainer, and provides exceptional UX/DX.

CrateDB offers a wide range of integration capabilities, is compatible
with the PostgreSQL wire protocol, and offers adapter components to
integrate with applications and frameworks.

- [Ecosystem Catalog]
- [Integration Tutorials I]
- [Integration Tutorials II]
- [Software Development Kit]

:::{rubric} Integrating CrateDB technologies into Rockset-based infrastructure
:::
The [Rockset HTTP API Adapter for CrateDB] is an experiment to provide
CrateDB's features through an API that is compatible with the Rockset HTTP
API, so client programs and libraries can work unmodified.

It has been verified to work for the most basic API calls with plain
HTTP requests using curl or HTTPie, the Rockset CLI, and Java, JavaScript,
and Python example programs.
::::

:::::


[Advanced Querying]: project:#advanced-querying
[All features of CrateDB at a glance]: project:#all-features
[Apache/Confluent Kafka Streams]: https://kafka.apache.org/documentation/streams/
[automatically indexes all your data]: project:#hybrid-index
[clear commitment]: https://cratedb.com/blog/opensource-licensing-founder
[Converged Index™]: https://rockset.com/blog/converged-indexing-the-secret-sauce-behind-rocksets-fast-queries/
[CrateDB]: https://cratedb.com/database
[CrateDB Cloud]: https://cratedb.com/docs/cloud/
[CrateDB Editions]: https://cratedb.com/database/editions
[CrateDB SQL]: project:#sql
[DX]: https://en.wikipedia.org/wiki/User_experience#Developer_experience
[Ecosystem Catalog]: https://cratedb.com/docs/crate/clients-tools/
[Integration Tutorials I]: inv:#integrate
[Integration Tutorials II]: https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015
[migration]: https://cratedb.com/migrations/rockset
[MongoDB Atlas Change Streams]: https://www.mongodb.com/docs/manual/changeStreams/
[open-source code base]: https://github.com/crate/crate
[Rockset]: https://rockset.com/product/
[Rockset's pricing examples]: https://docs.rockset.com/documentation/docs/billing#pricing-examples
[Rockset HTTP API Adapter for CrateDB]: https://cratedb-toolkit.readthedocs.io/adapter/rockset.html
[Rockset HTTP API is sunsetting on September 30th, 2024]: https://docs.rockset.com/documentation/docs/faq
[Software Development Kit]: https://cratedb-toolkit.readthedocs.io/
[The CrateDB Documentation]: https://cratedb.com/docs/
[truly open-source software]: https://cratedb.com/blog/cratedb-doubling-down-on-permissive-licensing-and-the-elasticsearch-lockdown
[UX]: https://en.wikipedia.org/wiki/User_experience
[Zero-ETL]: https://www.datacamp.com/blog/what-is-zero-etl
