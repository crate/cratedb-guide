# Welcome Rockset Developers

::::{grid} 2
:padding: 0

:::{grid-item}
:columns: 8
Because the [Rockset HTTP API is sunsetting on September 30th, 2024],
and CrateDB covers a reasonable amount of features, we would like to
present its capabilities to support your analytical workloads and
data consolidation efforts.

Both Rockset and CrateDB use SQL, so there is no need for your team to learn
a new query language or querying regime.

Because CrateDB is [truly open-source software], you will no longer find yourself
in vendor lock-in situations and service shutdowns due to M&A procedures and
similar occasions, being forced to migrate to a different system once again.

As we work with more and more companies looking to migrate their workloads
from [Rockset] to [CrateDB], we have built expertise on the details of what
a [migration] entails. This page intends to share a few spots on this topic.
:::

:::{grid-item-card}
:columns: 4
:link: https://cratedb.com/resources/webinars/lp-wb-from-rockset-to-cratedb
:link-alt: "Webinar: From Rockset to CrateDB"
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: text-smaller
:class-footer: text-smaller
Join our Webinar on July 25th, 2024
^^^
- Why CrateDB is a perfect \[Rockset\] replacement for real-time analytics and hybrid search. 
- How CrateDB compares to \[Rockset\] and Elasticsearch/OpenSearch for streaming ingest.
- Why CrateDB is a cost-effective alternative to \[Rockset\].
+++
Learn about our migration services, and have a live Q&A session with our experts.
:::

::::


## What's Inside

An overview about CrateDB, and a side-by-side comparison, tuned for Rockset users.

:::{card}
:link: https://cratedb.com/blog/why-cratedb-is-a-perfect-rockset-replacement 
:link-alt: "Why CrateDB is a perfect Rockset replacement"
:class-header: sd-font-weight-bold
:class-footer: text-smaller
Why CrateDB is a perfect \[Rockset\] replacement 
^^^
When it comes to **real-time analytics and hybrid search**,
CrateDB is the only solution that offers a similar approach to converged indexing,
full-text search, vector search, and geospatial support in a single storage engine,
accessible via native SQL and HTTP endpoints.
+++
A detailed comparison to help you in selecting the right alternative and ensuring a
timely and seamless migration, also enumerating the top five reasons for choosing
CrateDB as a Rockset replacement.
:::

CrateDB's features and integration capabilities in a nutshell.

:::::{grid} 2
:gutter: 3

::::{grid-item-card}
:::{rubric} Fundamentals
:::
- [All features of CrateDB at a glance].
- [Operational freedom]:
  The two editions of CrateDB Cloud vs. Self-Deployed allow you to choose and
  balance between convenience and performance requirements.
- No vendor lock-in and service sunsetting woes.
- No capacity limits.
::::

::::{grid-item-card}
:::{rubric} SQL Analytics
:::
CrateDB's lingua franca is SQL, ready for big data, very similar like
Rockset's SQL dialect. Because CrateDB is also compatible with applications
in the PostgreSQL ecosystem, ...
::::

::::{grid-item-card}
:::{rubric} Integrations
:::
With Rockset, as a complete data warehouse system, integrating data from other
sources is a nobrainer, and offers exceptional UX/DX.

CrateDB offers a wide range of integration capabilities, is compatible
with the PostgreSQL wire protocol, and offers adapter components to
integrate with applications and frameworks.

- [Integration Tutorials I]
- [Integration Tutorials II]
::::

::::{grid-item-card}
:::{rubric} Anything else?
:::
Foo. Bar. Please share your ideas!
::::


:::::


## What's Next

Our teams are working on improving SQL support and integrating relevant
features into our managed solutions, based on popular requests from
Rockset customers.
Feel free to reach out to us any time, in order to share your use cases
and workload insights. We will be happy to take them into consideration.

::::{grid} 2
:padding: 0

:::{grid-item-card}
In order to overcome deviations and variations on SQL dialect matters,
our teams are working on closing the gaps in SQL function support,
and corresponding educational material. 
:::
 
:::{grid-item-card}
Accompanying managed services offered by [CrateDB Cloud], Rockset-like
convenience features will be added over the course of the next weeks.
:::

::::

Our teams are working on software components that yield immediate leverage
when aiming to migrate data integration pipelines.

::::{grid} 2
:padding: 0

:::{grid-item-card}
Zero-ETL DX/UX, to make data ingestion work on your fingertips.

- [MongoDB Atlas Change Streams]
- [Amazon DynamoDB Streams]
- [Amazon Kinesis Data Streams]
:::

:::{grid-item-card}
The [Rockset Adapter for CrateDB] is an experiment to provide CrateDB's features
through a HTTP API that is roughly compatible with the Rockset HTTP API,
so client programs and libraries can work unmodified.
:::

::::


[All features of CrateDB at a glance]: https://cratedb-guide--53.org.readthedocs.build/feature/
[Amazon DynamoDB Streams]: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html
[Amazon Kinesis Data Streams]: https://aws.amazon.com/kinesis/
[CrateDB]: https://cratedb.com/database
[CrateDB Cloud]: https://cratedb.com/docs/cloud/
[Integration Tutorials I]: inv:#integrate
[Integration Tutorials II]: https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015
[migration]: https://cratedb.com/migrations/rockset
[MongoDB Atlas Change Streams]: https://www.mongodb.com/docs/manual/changeStreams/
[Operational freedom]: https://cratedb.com/database/editions
[Rockset]: https://rockset.com/product/
[Rockset Adapter for CrateDB]: https://cratedb-toolkit.readthedocs.io/adapter/rockset.html
[Rockset HTTP API is sunsetting on September 30th, 2024]: https://docs.rockset.com/documentation/docs/faq
[truly open-source software]: https://cratedb.com/blog/cratedb-doubling-down-on-permissive-licensing-and-the-elasticsearch-lockdown
