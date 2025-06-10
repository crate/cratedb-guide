.. _performance-scaling:

##################
 Design for scale
##################

This article explores critical design considerations to successfully scale
CrateDB in large production environments to ensure performance and reliability
as workloads grow.

.. _mindful-of-memory:

*******************************
 Be mindful of memory capacity
*******************************

In CrateDB, operations requiring a working set like groupings, aggregations, and
sorting are performed fully in memory without spilling over to disk.

Sometimes you may have a query that leads to a sub-optimal execution plan
requiring lots of memory. If you are coming to CrateDB from other database
systems, your experience may be that these queries will proceed to run taking
longer than required and impacting other workloads in the meanwhile. Sometimes
this effect may be obvious if a query takes a lot of resources and runs for a
long time, other times it may go unnoticed if a query that could complete in say
100 milliseconds takes one hundred times longer, 10 seconds, but the users put
up with it without reporting to you.

If a query would require more heap memory than the interested nodes
have available the query will fail with a particular type of error message that
we call a ``CircuitBreakerException``. This is a fail-fast approach as we
quickly see there is an issue and can optimize the query to get the best
performance, without impacting other workloads.

Please take a look at :ref:`Query Optimization 101 <performance-optimization>`
for strategies to optimize your queries when you encounter this situation.

.. _reading-lots-of-records:

*************************
 Reading lots of records
*************************

When the HTTP endpoint is used CrateDB will prepare the entire response in
memory before sending it to the client.

When the PostgreSQL protocol is used CrateDB attempts to stream the results but
in many cases it still needs to bring all rows to the query handler node first.

So we should always limit how many rows we request at a time, see `Fetching
large result sets from CrateDB`_.

.. _number-of=shards:

******************
 Number of shards
******************

In CrateDB data in tables and partitions is distributed in storage units that we
call shards.

If we do not specify how many shards we want for a table/partition CrateDB will
derive a default from the number of nodes.

CrateDB also has replicas of data and this results in additional shards in the
cluster.

Having too many or too few shards has performance implications, so it is very
important to get familiar with the :ref:`Sharding Performance Guide
<sharding_guide>`.

In particular, there is a soft limit of 1000 shards per node; so table schemas,
partitioning strategy, and number of nodes need to be planned to stay well below
this limit, one strategy can be to aim for a configuration where even if one node
in the cluster is lost the remaining nodes would still have less than 1000 shards.

If this was not considered when initially defining the tables we have the
following considerations:

-  changing the partitioning strategy requires creating a new table and copying
   over the data
-  the easiest way to change the number of shards on a partitioned table is to
   do it for new shards only with the ``ALTER TABLE ONLY`` command
-  see also `Changing the number of shards`_

.. _amount-of-indexed-columns:

*************************************
 Number of indexed fields in OBJECTs
*************************************

``OBJECT`` columns are ``DYNAMIC`` by default and CrateDB indexes all their
fields, providing excellent query performance without requiring manual indexing.
However, excessive indexing can impact storage, write speed, and resource
utilization.

-  All fields in OBJECTs are automatically indexed when inserted.
-  CrateDB optimizes indexing using Lucene-based columnar storage.
-  A soft limit of 1,000 total indexed columns and OBJECT fields per table
   exists.
-  Going beyond this limit may impact performance.

In cases with many fields and columns, it is advised to determine if some
OBJECTs or nested parts of them need to be indexed, and use the `ignored column
policy`_ where applicable.

.. _section-joins:

*******
 JOINs
*******

CrateDB is a lot better at JOINs than many of our competitors and is getting
better at every release, but JOINs in distributed databases are tricky to
optimize, so in many cases queries involving JOINs may need a bit of tweaking.

See `Using common table expressions to speed up queries`_

.. _changing the number of shards: https://cratedb.com/docs/crate/reference/en/latest/general/ddl/alter-table.html#alter-shard-number

.. _fetching large result sets from cratedb: https://community.cratedb.com/t/fetching-large-result-sets-from-cratedb/1270

.. _ignored column policy: https://cratedb.com/docs/crate/reference/en/latest/general/ddl/data-types.html#ignored

.. _using common table expressions to speed up queries: https://community.cratedb.com/t/using-common-table-expressions-to-speed-up-queries/1719
