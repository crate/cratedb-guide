(clustering)=
# Clustering

:::{include} /_include/links.md
:::


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

**CrateDB provides scalability through partitioning, sharding, and replication.**

:::{rubric} Overview
:::
CrateDB uses a shared-nothing architecture to form high-availability, resilient
database clusters with minimal effort of configuration, effectively implementing
a distributed SQL database.

:::{rubric} About
:::
CrateDB relies on Lucene for storage and inherits components from Elasticsearch /
OpenSearch for cluster consensus. Fundamental concepts of CrateDB are familiar
to Elasticsearch users, because both are actually using the same implementation.

:::{rubric} Details
:::

Sharding and partitioning are techniques used to distribute data evenly across
multiple nodes in a cluster, ensuring data scalability, availability, and
performance.

Replication can be applied to increase redundancy, which reduces the chance of
data loss, and to improve read performance.

:Sharding:

    In CrateDB, tables are split into a configured number of shards. Then, the
    shards are distributed across multiple nodes of the database cluster.
    Each shard in CrateDB is stored in a dedicated Lucene index.

    You can think of shards as a self-contained part of a table, that includes
    both a subset of records and the corresponding indexing structures.

    Figuring out how many shards to use for your tables requires you to think about
    the type of data you are processing, the types of queries you are running, and
    the type of hardware you are using.

:Partitioning:

    CrateDB also supports splitting up data across another dimension with
    partitioning.
    Tables can be partitioned by defining partition columns.
    You can think of a partition as a set of shards.

    - Partitioned tables optimize access efficiency when querying data, because only
      a subset of data needs to be addressed and acquired.
    - Each partition can be backed up and restored individually, for efficient operations.
    - Tables allow to change the number of shards even after creation time for future
      partitions. This feature enables you to start out with few shards per partition,
      and scale up the number of shards for later partitions once traffic
      and ingest rates increase over the lifetime of your application or system.

:Replication:

    You can configure CrateDB to replicate tables. When you configure replication,
    CrateDB will ensure that every table shard has one or more copies available
    at all times.

    Replication can also improve read performance because any increase in the
    number of shards distributed across a cluster also increases the
    opportunities for CrateDB to parallelize query execution across multiple nodes.

::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Concepts
:::
- {ref}`crate-reference:concept-clustering`
- {ref}`crate-reference:concept-storage-consistency`
- {ref}`crate-reference:concept-resiliency`

:::{rubric} Reference Manual
:::
- {ref}`crate-reference:ddl-sharding`
- {ref}`crate-reference:partitioned-tables`
- {ref}`Partition columns <gloss-partition-column>`
- {ref}`crate-reference:ddl-replication`

:::{rubric} Guides
:::
- {ref}`guide:clustering`

{tags-primary}`Clustering`
{tags-primary}`Sharding`
{tags-primary}`Partitioning`
{tags-primary}`Replication`
::::

:::::


## Synopsis
With a monthly throughput of 300 GB, partitioning your table by month,
and using six shards, each shard will manage 50 GB of data, which is
within the recommended size range (10 - 50 GB).

Through replication, the table will store three copies of your data,
in order to reduce the chance of permanent data loss.
```sql
CREATE TABLE timeseries_table (
    ts TIMESTAMP,
    val DOUBLE PRECISION,
    part GENERATED ALWAYS AS date_trunc('month', ts)
)
CLUSTERED INTO 6 SHARDS
PARTITIONED BY (part)
WITH (number_of_replicas = 2);
```


## Learn
Individual characteristics and shapes of data need different sharding and
partitioning strategies. Learn about the details of shard allocation, that
will support you to choose the right strategy for your data and your most
prominent types of workloads.

::::{grid} 2 2 2 2
:padding: 0

:::{grid-item-card}
:link: sharding-partitioning
:link-type: ref
:link-alt: Sharding and Partitioning
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold
:class-body: sd-text-center2 sd-fs2-5
:class-footer: text-smaller
Sharding and Partitioning
^^^
- Introduction to the concepts of sharding and partitioning.
- Learn how to choose a strategy that fits your needs.
+++
{material-outlined}`lightbulb;1.8em`
An in-depth guide on how to configure sharding and partitioning,
presenting best practices and examples.
:::

:::{grid-item-card}
:link: sharding-performance
:link-type: ref
:link-alt: Sharding and Partitioning
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold
:class-body: sd-text-center2 sd-fs2-5
:class-footer: text-smaller
Sharding Performance Guide
^^^
- Optimising for query performance.
- Optimising for ingestion performance.
+++
{material-outlined}`lightbulb;1.8em`
Guidelines about balancing your strategy to yield the best performance for your workloads.
:::

:::{grid-item-card}
:link: https://community.cratedb.com/t/sharding-and-partitioning-guide-for-time-series-data/737
:link-alt: Sharding and partitioning guide for time series data
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold
:class-body: sd-text-center2 sd-fs2-5
:class-footer: text-smaller
Sharding and partitioning guide for time series data
^^^
A hands-on walkthrough to support you with building a sharding and partitioning
strategy for your time series data.
+++
{material-outlined}`lightbulb;1.8em`
Includes details about partitioning, sharding, and replication. Gives valuable
advises about relevant topic matters.
:::

::::
