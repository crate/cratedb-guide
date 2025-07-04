.. highlight:: psql
.. _systables:

==============================
Diagnostics with System Tables
==============================

CrateDB maintains a set of diagnostic tables in the **sys** schema, which
provide insights into the cluster state.

If something is going wrong, and you initially don't know why, they help you to
analyze, identify the problem, and start mitigating it. While there is
:ref:`detailed information about all system tables <crate-reference:system-information>`,
this guide runs you through the most common situations.


Step 1: Inspect health checks
=============================

A good point to start is the table **sys.check** that maintains a number of
health checks. You may know it from the admin UI. Order them by severity::

    cr> SELECT description FROM sys.checks WHERE NOT passed ORDER BY severity DESC;
    +---------...-+
    | description |
    +---------...-+...
    +---------...-+
    SELECT ... in set (... sec)

If a check fails, the description offers some explanation on how to proceed.
This synthetic table reports checks that verify your cluster layout, gives recommendations
for configuration options, and warns you on incompatible software versions. More
checks will be added as we go.


Step 2: Check cluster activity
==============================

Statements that are currently executed on the server are tracked in the tables
**sys.jobs** and **sys.operations**. They give you the opportunity to view the
ongoing activity in the cluster.

If you're using an earlier version than CrateDB 3.0.0, you will have to enable
statistics using::

    cr> SET GLOBAL stats.enabled = true;
    SET OK, 1 row affected ( … sec)

When enabled, each syntactically correct request that got parsed and planned is
listed in the **sys.jobs** table while it's executed::

    cr> SELECT id as job_uuid, date_format(started) AS start, stmt FROM sys.jobs;
    +--------------------------------------+-----------------------------+-------------------------------------...----------------------------------+
    | job_uuid                             | start                       | stmt                                                                     |
    +--------------------------------------+-----------------------------+-------------------------------------...----------------------------------+
    ...
    +--------------------------------------+-----------------------------+-------------------------------------...----------------------------------+
    SELECT ... in set (... sec)

Once you identified the dedicated job UUID, you can kill that job with the
**KILL** command. A single job is split into several operations which run,
depending on the query, on distributed nodes of your cluster. The table has
also a system column **node** indicating on which node CrateDB actually
executes the operation::

    cr> SELECT node['name'], node['id'], * FROM sys.operations;
    +---------------+----------...+----+---------------...+---------+---------------+------------+
    | node['name'] | node['id']   | id | job_id           | name    |       started | used_bytes |
    +---------------+----------...+----+---------------...+---------+---------------+------------+
    ...
    +---------------+----------...+----+---------------...+---------+---------------+------------+
    SELECT ... in set (... sec)

Find out more about the **node** system column in the next sections. If there
are no current jobs nor operations that are causing problems, check the
recorded history of finished jobs and operations in the tables **sys.jobs_log**
and **sys.operations_log**, respectively.


Step 3: Analyze cluster resources
=================================

Sometimes it is not a single query that causes problems, but a component of your
distributed cluster. To find out more about it, check the table
**sys.cluster**, which holds a single row containing the name and ID of the
current master along with several other settings. To list all available data,
run::

    cr> SHOW COLUMNS IN cluster FROM sys;
    +--------------------------------------------------------------------------------...+-----------...+
    | column_name                                                                       | data_type    |
    +--------------------------------------------------------------------------------...+-----------...+
    ...
    +--------------------------------------------------------------------------------...+-----------...+
    SHOW 104 rows in set (... sec)

While **sys.cluster** contains information about the cluster as a whole,
**sys.nodes** maintains more detailed information about each CrateDB instance.
This can be useful to track down data nodes that misbehave because their CPU is
overloaded or because they have an outdated Java version::

    cr> SELECT name, load['1'], os_info['jvm']['version'] FROM sys.nodes;
    +-------+--------...+------------------------...+
    | name  | load['1'] | os_info['jvm']['version'] |
    +-------+--------...+------------------------...+
    ...
    +-------+--------...+------------------------...+
    SELECT ... in set (... sec)

To list all nodes using more than 98 per cent of system memory, invoke::

    cr> SELECT * FROM sys.nodes WHERE mem['used_percent'] > 98;
    +--...+---...+------...-+-...+---...+--...+---...+------...+-...+------...+---...+-----...-+-------...+----------...-+------...+
    | fs  | heap | hostname | id | load | mem | name | network | os | os_info | port | process | rest_url | thread_pools | version |
    +--...+---...+------...-+-...+---...+--...+---...+------...+-...+------...+---...+------...+-------...+----------...-+------...+
    ...
    SELECT ... in set (... sec)

The table also contains performance metrics like the load average, disk,
memory, heap, or network throughput.
The object has the same structure as the **node** system column of
**sys.operations** from the previous section.
This query lists all available attributes::

    cr> SHOW columns IN nodes FROM sys;
    +-------------------------------------------------...+-----------...+
    | column_name                                        | data_type    |
    +-------------------------------------------------...+-----------...+
    ...
    +-------------------------------------------------...+-----------...+
    SHOW ... rows in set (... sec)



Step 4: Insights about partitions, shards, and replication
==========================================================

CrateDB divides the rows of each table into shards that are distinctively
distributed to all nodes in your cluster. Replication uses the same mechanism
to add redundancy and thus resilience to your data.

While most of the time
CrateDB transparently takes care of distributing and replicating the shards,
it is useful in troubleshooting situations to learn more about these
data structures. The **sys.shards** table provides access to the status and
size of shards, their names, and IDs::

    cr> SHOW COLUMNS IN shards FROM sys;
    +--------------------------------+-----------+
    | column_name                    | data_type |
    +--------------------------------+-----------+
    | blob_path                      | string    |
    | id                             | integer   |
    | min_lucene_version             | string    |
    | num_docs                       | long      |
    | orphan_partition               | boolean   |
    | partition_ident                | string    |
    | path                           | string    |
    | primary                        | boolean   |
    | recovery                       | object    |
    | recovery['files']              | object    |
    | recovery['files']['percent']   | float     |
    | recovery['files']['recovered'] | integer   |
    | recovery['files']['reused']    | integer   |
    | recovery['files']['used']      | integer   |
    | recovery['size']               | object    |
    | recovery['size']['percent']    | float     |
    | recovery['size']['recovered']  | long      |
    | recovery['size']['reused']     | long      |
    | recovery['size']['used']       | long      |
    | recovery['stage']              | string    |
    | recovery['total_time']         | long      |
    | recovery['type']               | string    |
    | relocating_node                | string    |
    | routing_state                  | string    |
    | schema_name                    | string    |
    | size                           | long      |
    | state                          | string    |
    | table_name                     | string    |
    +--------------------------------+-----------+
    SHOW 28 rows in set (... sec)

The cluster state is somewhat delicate when nodes join or leave, since in those
situations shards have to be rearranged to ensure that each of them is
replicated to different nodes. As long as the **state** attribute is
``STARTED`` for all shards, the cluster is in a stable state; otherwise,
CrateDB is occupied with some background activity. The cluster state indicators
on the admin UI evaluate these values as well.

The **sys.shards** table contains even more information about the rebalancing
activities. Sometimes CrateDB needs to transfer a shard to another node, since
that may be necessary to ensure there are enough replicas of it distributed in
the cluster.

You can estimate the progress of that operation with the **recovery** object.
Run this query to monitor the progress of the shard transfer::

    cr> select node['name'], id, recovery['stage'], recovery['size']['percent'], routing_state, state from sys.shards
    ... where routing_state in ('RELOCATING','INITIALIZING') order by id;
    +--------------+----+-------------------+-----------------------------+---------------+-------+
    | node['name'] | id | recovery['stage'] | recovery['size']['percent'] | routing_state | state |
    +--------------+----+-------------------+-----------------------------+---------------+-------+
    +--------------+----+-------------------+-----------------------------+---------------+-------+
    SELECT ... in set (... sec)

It lists pairs of rows, in which the first row denotes the destination shard
and the second row the source shard.

Each row contains the shard's hostname, ID, and the recovery percentage of the
transferred shard. When the shard starts relocating, a new shard entry appears
in the  **sys.shards** table with a **routing_state** of ``INITIALIZING``. The
**state** of this row is ``RECOVERING``. Meanwhile, the value of
**routing_state** of the source row switches from ``STARTED`` to ``RELOCATING``
until the transfer is done. After that, the source row is deleted from
**sys.shards** automatically.

To find out on which specific node a shard is stored, also use the object in
the **node** system column that is available for this table. For example,
this query lists the hosts and tables with the highest number of rows inside
a single shard::

    cr> SELECT node['name'], table_name, num_docs FROM sys.shards ORDER BY num_docs DESC LIMIT 3;
    +--------------...+-----------...-+----------+
    | node['name']    | table_name    | num_docs |
    +--------------...+------------...+----------+
    ...
    +--------------...+------------...+----------+
    SELECT ... in set (... sec)

.. SEEALSO::

    :ref:`Bulk import: Shards and replicas <bulk-shards-replicas>`


Step 5: Analyze allocation problems
===================================

Related to the previous step about gaining insights about shards and
replication is the step about cluster-wide shard allocations.

In some circumstances, shard allocations might behave differently than you
expect. A typical example might be that a table remains under-replicated for no
apparent reason. You would probably want to find out what is causing the
cluster to not allocate the shards. For that, there is the ``sys.allocations``
table, which lists all shards in the cluster.

- If a shard is unassigned, the row will also include a reason why it cannot be
  allocated on any node.

- If a shard is assigned but cannot be moved or rebalanced, the row includes a
  reason why it remains on the current node.

- For a full list of available columns, see the :ref:`reference documentation
  about the sys.allocations table <crate-reference:sys-allocations>`.

- To find out about the different states of shards of a specific table, you can
  simply filter by ``table_schema`` and ``table_name``, e.g.::

    cr> SELECT table_name, shard_id, node_id, explanation
    ... FROM sys.allocations
    ... WHERE table_schema = 'doc' AND table_name = 'my_table'
    ... ORDER BY current_state, shard_id;
    +------------+----------+---------+-------------+
    | table_name | shard_id | node_id | explanation |
    +------------+----------+---------+-------------+
    | doc        | my_table | ...     | ...         |
    +------------+----------+---------+-------------+
    ...
    +------------+----------+---------+-------------+
    SELECT ... in set (... sec)


Step 6: Analyze queries
=======================

To understand the load on the cluster, analyzing resource consumption of
queries issued against the cluster can give good indications.

CrateDB exposes currently running and already running queries through some
system table, namely:

- :ref:`sys.jobs <crate-reference:sys-jobs>`
  This exposes information about a complete, still running, query.
- :ref:`sys.jobs_log <crate-reference:sys-logs>`
  Same as :ref:`sys.jobs <crate-reference:sys-jobs>`, but contains only finished
  queries.
- :ref:`sys.operations <crate-reference:sys-operations>`
  This exposes information about concrete execution operations of each query.
- :ref:`sys.operations_log <crate-reference:sys-logs>`
  Same as :ref:`sys.operations <crate-reference:sys-operations>`, but contains
  only finished operations.

See also :ref:`crate-reference:jobs_operations_logs` for more detailed information
about these tables.

To figure out the runtime of a currently running query and how much memory it
used, these table must be joined together as the memory is accounted per
*operation*. On an idling cluster with no other query running, this will just
show our own diagnostic query::


    cr> SELECT
    ...   j.id,
    ...   now() - j.started as runtime,
    ...   sum(used_bytes) as used_bytes,
    ...   count(*) as ops,
    ...   j.stmt
    ... FROM sys.jobs j
    ... JOIN sys.operations o ON j.id = o.job_id
    ... GROUP BY j.id, j.stmt, runtime;
    +--...-+---...----+------------+-----+----------------------...------------------------+
    | id   | runtime  | used_bytes | ops | stmt                                            |
    +--...-+---...----+------------+-----+----------------------...------------------------+
    | ...  | ...      |    ...     |  13 | select j.id, now() - j.started as runtime, ...; |
    +--...-+---...----+------------+-----+----------------------...------------------------+
    SELECT 1 row in set (... sec)

To get the same information about already ran queries, the ``sys.jobs_log`` and
``sys.operations_log`` must be used, otherwise the query is almost the same::


    cr> SELECT
    ...   j.id,
    ...   j.ended - j.started as runtime,
    ...   sum(used_bytes) as used_bytes,
    ...   count(*) as ops,
    ...   j.stmt
    ... FROM sys.jobs_log j
    ... JOIN sys.operations_log o ON j.id = o.job_id
    ... GROUP BY j.id, j.stmt, runtime;
    +--...-+---...----+------------+-----+----------------------...------------------------+
    | id   | runtime  | used_bytes | ops | stmt                                            |
    +--...-+---...----+------------+-----+----------------------...------------------------+
    | ...  | ...      |    ...     |  13 | select j.id, now() - j.started as runtime, ...; |
    +--...-+---...----+------------+-----+----------------------...------------------------+
    SELECT 1 row in set (... sec)


Step 7: Manage snapshots
========================

Finally: if your repair efforts did not succeed, and your application or users
accidentally deleted some data, recover one of the previously taken snapshots
of your cluster. The tables **sys.snapshots** and **sys.repositories** assist
you in managing your backups.

Remember, one or more backups are stored in
repositories outside the CrateDB cluster initialized with the **CREATE
REPOSITORY** request. An actual copy of a current database state is made with
the **CREATE SNAPSHOT** command. If you forgot where you store your snapshots::

    cr> SELECT * FROM sys.repositories;
    +------+----------+------+
    | name | settings | type |
    +------+----------+------+
    +------+----------+------+
    SELECT ... in set (... sec)

might come in handy. To actually recover data, first determine which snapshot
to restore. Suppose you make nightly backups, this command displays last week's
snapshots along with their name, the stored indices, and how long they took::

    cr> SELECT * FROM sys.snapshots ORDER BY started DESC LIMIT 7;
    +------------------+----------+------+------------+---------+-------+---------+
    | concrete_indices | finished | name | repository | started | state | version |
    +------------------+----------+------+------------+---------+-------+---------+
    +------------------+----------+------+------------+---------+-------+---------+
    SELECT ... in set (... sec)
