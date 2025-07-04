.. _sharding_guide:
.. _sharding-performance:

==========================
Sharding Performance Guide
==========================

This document is a sharding best practice guide for CrateDB.

A brief recap: CrateDB tables are split into a configured number of shards, and
then these shards are distributed across the cluster.

Figuring out how many shards to use for your tables requires you to think about
the type of data you're processing, the types of queries you're running, and
the type of hardware you're using.

.. NOTE::

   This guide assumes you know the basics.

   If you are looking for an intro to sharding, see :ref:`sharding
   <crate-reference:ddl-sharding>`.

Optimising for query performance
================================

.. _sharding-under-allocation:

Under-allocation is bad
-----------------------

.. CAUTION::

   If you have fewer shards than CPUs in the cluster, this is called
   *under-allocation*, and it means you're not getting the best performance out
   of CrateDB.

Whenever possible, CrateDB will parallelize query workloads and distribute them
across the whole cluster. The more CPUs this query workload can be distributed
across, the faster the query will run.

To increase the chances that a query can be parallelized and distributed
maximally, there should be at least as many shards for a table than there are
CPUs in the cluster. This is because CrateDB will automatically balance shards
across the cluster so that each node contains as few shards as possible.

In summary: the smaller your shards are, the more of them you will have, and so
the more likely it is that they will be distributed across the whole cluster,
and hence across all of your CPUs, and hence the faster your queries will run.

Significant over-allocation is bad
----------------------------------

.. CAUTION::

   If you have more shards per table than CPUs, this is called *over-allocation*. A
   little over-allocation is desirable. But if you significantly over-allocate
   your shards per table, you will see performance degradation.

When you have slightly more shards per table than CPUs, you ensure that query
workloads can be parallelized and distributed maximally, which in turn ensures
maximal query performance.

However, if most nodes have more shards per table than they have CPUs, you
could actually see performance degradation. Each shard comes with a cost in
terms of open files, RAM, and CPU cycles. Smaller shards also means small shard
indexes, which can adversely affect computed search term relevance.

For performance reasons, one thousand shards per table per node is considered
the highest recommended configuration. If you exceed this you will experience a
failing cluster check.

Balancing allocation
--------------------

Finding the right balance when it comes to sharding will vary on a lot of
things. And while it's generally advisable to slightly over-allocate, it's also
a good idea to benchmark your particular setup so as to find the sweet spot.

If you don't manually set the number of shards per table, CrateDB will make a best guess,
based on the assumption that your nodes have two CPUs each.

.. TIP::

   For the purposes of calculating how many shards a table should be clustered
   into, you can typically ignore replica partitions as these are not usually
   queried across for reads.

.. CAUTION::

   If you are using :ref:`partitioned tables <crate-reference:partitioned-tables>`,
   note that each partition is
   clustered into as many shards as you configure for the table.

   For example, a table with four shards and two partitions will have eight
   shards that can be commonly queried across. But a query that only touches
   one partition will only query across four shards.

   How this factors into balancing your shard allocation will depend on the
   types of queries you intend to run.

.. _sharding_ingestion:

Optimising for ingestion performance
====================================

As with `Optimising for query performance`_, when doing heavy ingestion, it is
good to cluster a table across as many nodes as possible. However, `we have
found`_ that ingestion throughput can often increase as the table shard per CPU
ratio on each node *decreases*.

Ingestion throughput typically varies on: data volume, individual payload
sizes, batch insert size, and the hardware. In particular: using solid-state
drives (SSDs) instead of hard-disk drives (HDDs) can massively increase
ingestion throughput.

It's a good idea to benchmark your particular setup so as to find the sweet
spot.


.. _we have found: https://cratedb.com/blog/big-cluster-insights-ingesting
