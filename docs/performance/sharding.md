(sharding-guide)=
(sharding-performance)=

# Sharding performance guide

:::{div} sd-text-muted
Applying sharding can drastically improve the performance on large datasets.
:::

This document is a sharding best practice guide for CrateDB.
A brief recap: CrateDB tables are split into a configured number of shards.
These shards are distributed across the cluster to optimize concurrent and
parallel data processing.

Whenever possible, CrateDB will parallelize query workloads and distribute them
across the whole cluster. The more CPUs this query workload can be distributed
across, the faster the query will run.

:::{seealso}
This guide assumes you know the basics.
If you are looking for an intro to sharding, see also the
{ref}`sharding-partitioning` and the
{ref}`sharding reference <crate-reference:ddl-sharding>` documentation.
:::


## General recommendations

To avoid running your clusters with too many shards or too large shards,
implement the following guidelines as a rule of thumb:

- Use shard sizes between 10 GB and 50 GB.

- Keep the number of records on each shard below 200 million.

Finding the right balance when it comes to sharding will vary on a lot of
things. While it is generally advisable to slightly over-allocate, we
recommend to benchmark your particular setup to find the sweet spot to
implement an appropriate sharding strategy.

Figuring out how many shards to use for your tables requires you to think about
the type of data you are processing, the types of queries you are running, and
the type of hardware you are using.

- Too many shards can degrade search performance and make the cluster unstable.
  This is referred to as _oversharding_.

- Very large shards can slow down cluster operations and prolong recovery times
  after failures.

## Sizing considerations

General principles require careful consideration of cluster
sizing and architecture.
Keep the following things in mind when building your sharding strategy.
Each shard incurs overhead in terms of open files, RAM allocation, and CPU cycles
for maintenance operations.

### Shard size vs. number of shards

The optimal approach balances shard count with shard size. Individual shards should
typically contain 10-50 GB of data, being the sweet spot for most
workloads. In large clusters, this often means fewer shards than total CPU cores,
as larger shards can still be processed efficiently by multiple CPU cores during
query execution.

### Shard-per-CPU ratio

If most nodes have more shards per table than they have CPUs, the cluster can
experience performance degradations.
For example, on clusters with substantial CPU resources (e.g., 8 nodes × 32 CPUs
= 256 total CPUs), creating 256+ shards per table often proves counterproductive.
If you don't manually set the number of shards per table, CrateDB will make a
best guess, based on the assumption that your nodes have two CPUs each.
The general advice is to calculate with 1 shard per CPU as a starting point.

### 1000 shards per node limit

To avoid _oversharding_, CrateDB by default limits the number of shards per node to
1_000 as a protection limit. Any operation that would exceed that limit
leads to an exception.
For an 8-node cluster, this allows up to 8_000 total shards across all tables.
Approaching this limit typically indicates a suboptimal sharding strategy rather
than optimal performance tuning. See also relevant documentation about
{ref}`table reconfiguration <number-of-shards>` wrt. sharding options.

### Partitions

If you are using {ref}`partitioned tables <crate-reference:partitioned-tables>`,
note that each partition is clustered into as many shards as you configure
for the table.

For example, a table with four shards and two partitions will have eight
shards that can be commonly queried across. But a query that only touches
one partition will only query across four shards.

How this factors into balancing your shard allocation will depend on the
types of queries you intend to run.

### Replicas

CrateDB uses replicas for both data durability and query performance. When a
node goes down, replicas ensure no data is lost. For read operations, CrateDB
randomly distributes queries across both primary and replica shards, improving
concurrent read throughput.

Each replica adds to the total shard count in the cluster. By default, CrateDB
uses the replica setting `0-1` on newly created tables, resulting in twice the
number of configured shards. The more replicas you add, the higher the
multiplier (x3, x4, etc.) for capacity planning

See the {ref}`replication reference <crate-reference:ddl-replication>`
documentation for more details.

### Segments

The number of segments within a shard affects query performance because more
segments have to be visited.

## Notes

:::{caution}
:class: hero
Balancing the number and size of your shards is important for the performance
and stability of your CrateDB clusters.
:::

(sharding-under-allocation)=
### Avoid under-allocation

:::{CAUTION}
If you have fewer shards than CPUs in the cluster, this is called
*under-allocation*, and it means you're not getting the best performance out
of CrateDB.
:::

To increase the chances that a query can be parallelized and distributed
maximally, there should be at least as many shards for a table than there are
CPUs in the cluster. This is because CrateDB will automatically balance shards
across the cluster so that each node contains as few shards as possible.

In summary: the smaller your shards are, the more of them you will have, and so
the more likely it is that they will be distributed across the whole cluster,
and hence across all of your CPUs, and hence the faster your queries will run.

(sharding-over-allocation)=
### Avoid extensive over-allocation

:::{CAUTION}
If you have more shards per table than CPUs, this is called *over-allocation*. A
little over-allocation is desirable. But if you significantly over-allocate
your shards per table, you will see performance degradation.
:::

When you have slightly more shards per table than CPUs, you ensure that query
workloads can be parallelized and distributed maximally, which in turn ensures
maximal query performance.

(sharding-ingestion)=
### Optimize for ingestion

When doing heavy ingestion, it is
good to cluster a table across as many nodes as possible. However, [we have
found][we have found] that ingestion throughput can often increase as the table shard per CPU
ratio on each node *decreases*.

Ingestion throughput typically varies on: data volume, individual payload
sizes, batch insert size, and the hardware. In particular: using solid-state
drives (SSDs) instead of hard-disk drives (HDDs) can massively increase
ingestion throughput.

We recommend to benchmark your particular ingest workload to find the sweet
spot.

[we have found]: https://cratedb.com/blog/big-cluster-insights-ingesting
