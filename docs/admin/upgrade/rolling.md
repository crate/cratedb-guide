(rolling-upgrade)=

# Rolling Upgrade

## Introduction

A rolling upgrade updates one CrateDB node at a time while the remaining nodes
continue serving requests. This minimizes service disruption and avoids
stopping the entire cluster.

For each node, decommission it gracefully, install the new version,
restart it, verify that it has rejoined the cluster, and then
continue with the next node.

To perform a rolling upgrade of a cluster, stop one node at a time using the
{ref}`graceful stop <crate-reference:conf_graceful_stop>` procedure
(see {ref}`Signal Handling <crate-reference:cli-crate-signals>`). This will allow
CrateDB to relocate shards away from the node being decommissioned.
Depending on the configured availability mode, replica shards may temporarily
be unavailable and the cluster may become yellow. The node being decommissioned
rejects new requests while allowing pending requests to finish.

:::{NOTE}
Due to the distributed execution of requests, some client requests might
fail during a rolling upgrade.

Please always have retry mechanisms in place for critical queries.
:::

## Version requirements

A rolling upgrade is possible in the following scenarios:

- Between patch-level releases of the same minor version
- From one minor version to the next within the same major version
- From one major version to the next major version

For example, you can do a rolling upgrade:

- From 6.1.2 to 6.1.3
- From 6.0.x to 6.1.y
- From 5.10.x to 6.0.0

You cannot do a rolling upgrade from x.y.z to x.(y + 3).z unless the release
notes explicitly mention support.

:::{WARNING}
Check the {ref}`release notes <crate-reference:release_notes>` for the
version you are upgrading to for any specific instructions that may override
this.
:::

## Graceful stop particularities

To initiate a graceful stop that behaves as described in the introduction
of this document, the {ref}`ALTER CLUSTER DECOMMISSION <crate-reference:alter_cluster_decommission>`
statement must be used.

Stopping a node via the `TERM` user signal (invoked via `Ctrl+C` or
`systemctl stop crate`) will cause a normal stop of CrateDB, **without**
going through the graceful stop procedure.

Depending on the size of your cluster, stopping a CrateDB node gracefully
might take a while. You might want to check your server logs to see if the
graceful stop process is progressing well. In case of an error or a timeout,
the node will stay up, signaling the error in its log files.

Using the default settings, the node will shut down by moving all primary shards
off the node first. This ensures that a primary copy of each shard remains
available before the node shuts down. However, the cluster health will most
likely turn yellow, because replicas that lived on that node will be missing.

Keep in mind that relocating shards might take some time depending on the
number of shards and their size. A timeout will occur after the duration configured as {ref}`cluster.graceful_stop.timeout <crate-reference:cluster.graceful_stop.timeout>`.
In case of a timeout, the stop process will abort and the cluster will
start distributing shards evenly again. If you want to force a stop after
the timeout, even if the relocation is not finished, you can set {ref}`cluster.graceful_stop.force <crate-reference:cluster.graceful_stop.force>`
to `true`.

:::{WARNING}
A forced stop does not ensure the minimum data availability defined in the
settings and may result in temporary or even permanent loss of data!
:::

By default, only the graceful stop process considers the cluster settings
described at {ref}`graceful stop <crate-reference:conf_graceful_stop>`.

## Upgrade process

To run the actual upgrade process, follow the steps outlined below in the designated order.

::::::{stepper}

### Ensure green health

We assume that the cluster is in good health before starting the upgrade.
This means all shards are allocated and there are no failed health checks,
such as breached disk space watermarks.

If you use the Admin UI, verify that the cluster health indicator is green
and that no node checks are failing.

You can also verify the status manually. All tables should be in a green state:

```psql
cr> SELECT *
... FROM sys.health
... WHERE health <> 'GREEN';
+--------+----------------+-----------------+----------+------------+--------------+------------------------+
| health | missing_shards | partition_ident | severity | table_name | table_schema | underreplicated_shards |
+--------+----------------+-----------------+----------+------------+--------------+------------------------+
+--------+----------------+-----------------+----------+------------+--------------+------------------------+
SELECT 0 rows in set (... sec)
```

There should be no failed node checks:

```psql
cr> SELECT *
... FROM sys.node_checks
... WHERE passed = FALSE;
+--------------+-------------+----+---------+--------+----------+
| acknowledged | description | id | node_id | passed | severity |
+--------------+-------------+----+---------+--------+----------+
+--------------+-------------+----+---------+--------+----------+
SELECT 0 rows in set (... sec)
```

### Backup

:::{WARNING}
Before upgrading, you should ensure you have {ref}`a current snapshot
<crate-reference:snapshot-restore>`.
:::

### Prevent reallocations

Prevent the cluster from unnecessarily reallocating shard replicas while nodes
are restarted. Configure the cluster to permit only the allocation of primary
shards for newly created tables or partitions.

Use the {ref}`SET <crate-reference:ref-set>` command to do so:

```psql
cr> SET GLOBAL TRANSIENT "cluster.routing.allocation.enable" = 'new_primaries';
SET OK, 1 row affected (... sec)
```

:::{NOTE}
This step may be omitted if you set the
`cluster.graceful_stop.min_availability` setting to `full` (see {ref}`rolling_data_availability` below).
:::

### Graceful stop

Issue an `ALTER CLUSTER DECOMMISSION` command:

```psql
cr> ALTER CLUSTER DECOMMISSION 'your_node_name';
ALTER OK, 1 row affected (... sec)
```

The `crate` process will automatically terminate at the end of the decommissioning process.

:::{dropdown} **Optional: Observe the relocations**

If you want to observe the relocation process triggered by the graceful stop,
you can issue the following SQL queries regularly.

Get the number of shards remaining on the node being decommissioned:

```psql
cr> SELECT COUNT(*) AS remaining_shards
... FROM sys.shards
... WHERE node['name'] = 'your_node_name';
+------------------+
| remaining_shards |
+------------------+
|                0 |
+------------------+
SELECT 1 row in set (... sec)
```

Get some more details about which shards remain on your node:

```psql
cr> SELECT schema_name, table_name, partition_ident, id, primary, size / POWER(1024, 3) AS size_gb, state
... FROM sys.shards
... WHERE node['name'] = 'your_node_name'
... ORDER BY 1, 2, 3, 4, 5;
+-------------+------------+-----------------+----+---------+---------+-------+
| schema_name | table_name | partition_ident | id | primary | size_gb | state |
+-------------+------------+-----------------+----+---------+---------+-------+
...
SELECT ... rows in set (... sec)
```

:::

:::{NOTE}
If you observe the graceful stop process using the Admin UI, you might see
the cluster turning red for a small instant when a node finally shuts down.
This is due to the way the Admin UI determines the cluster state.

If a query fails due to a missing node, the Admin UI may falsely consider
the cluster to be in a critical state.
:::

### Upgrade CrateDB

After the node has stopped, you can safely upgrade your CrateDB installation.
Depending on your installation and operating system, you can upgrade using the
package manager.

Example for RHEL (DNF package manager):

```shell
dnf update -y crate
```

If you are in doubt how to upgrade an installed package, please refer to the
man pages of your operating system or package manager.

### Start CrateDB

Once the upgrade has completed, you can start the CrateDB process again.
Most commonly, this is done using your operating system's service manager, such as:

```shell
systemctl start crate
```

### Wait for the node to rejoin

Wait until the upgraded node has started and rejoined the cluster.

Once the node rejoined, it will appear in `sys.nodes` with the updated version number:

```psql
cr> SELECT version['number']
... FROM sys.nodes
... WHERE name = 'your_node_name';
+-------------------+
| version['number'] |
+-------------------+
...
SELECT ... rows in set (... sec)
```

Confirm that the query returns exactly one row containing the target version.

### Repeat

Repeat steps 4 - 7 for all other nodes.

### Enable allocations

Finally, when all nodes are updated you can restore the shard allocation
setting. If allocations were set to the default value before, run this query
to restore the setting:

```psql
cr> SET GLOBAL TRANSIENT "cluster.routing.allocation.enable" = 'all';
SET OK, 1 row affected (... sec)
```

### Wait for complete recovery

Before considering the upgrade done, verify that all shards have successfully
been recovered. This process can take some time, depending on your data volume.
The number of tables or partitions with non-green health should steadily
decrease as shards recover.

```psql
cr> SELECT *
... FROM sys.health
... WHERE health <> 'GREEN';
+--------+----------------+-----------------+----------+------------+--------------+------------------------+
| health | missing_shards | partition_ident | severity | table_name | table_schema | underreplicated_shards |
+--------+----------------+-----------------+----------+------------+--------------+------------------------+
...
SELECT 0 rows in set (... sec)
```

::::::

(rolling_data_availability)=

## Data availability options

There are different levels of data availability that can be achieved during the upgrade process.
This is controlled via the {ref}`cluster.graceful_stop.min_availability <crate-reference:cluster.graceful_stop.min_availability>`
parameter. It can be either `primaries`, `full`, or `none` and can be configured using the
{ref}`SET <crate-reference:ref-set>` statement.

- **primaries** *(default)*: Only primary shards will be moved to other nodes. Using
this setting means that the cluster will go into the `yellow` (underreplicated) warning state
if a node that has been stopped contained replicas that are then unavailable.
- **full**: All shards currently located on the node will be moved to the
other nodes in order to stop gracefully. Using this setting, the cluster will
stay `green` the whole time.
- **none**: There is no data-availability guarantee. The node will stop,
possibly leaving the cluster in the critical `red` state if the node
contained a primary shard that has no replicas that can take over.

The default `primaries` setting offers a good balance between relocating shards and data availability.
Choose `none` if you prefer a fast upgrade path and can tolerate intermittent data unavailability
(e.g. during a maintenance window), or `full` if you want to retain full availability at all times.

### Full minimum data availability

If the `full` minimum data availability is configured, the cluster needs to
contain enough nodes to hold the number of replicas that are configured, even if
one node is missing.

For example, if there are only two nodes in a cluster and a table has one
replica configured, the graceful stop procedure will not succeed and abort
as it won't be possible to relocate the replicas.

If a table has a range configured as number of replicas, the upper number of
replicas will be taken into account.
With two nodes and 0-1 replicas, the graceful stop procedure will abort.

:::{NOTE}
For the `full` graceful stop to work, the following has to be true:

**number_of_nodes > max_number_of_replicas + 1**
:::

### Primaries minimum data availability

If the `primaries` minimum data availability is used, take care that there
are still enough replicas in the cluster after a node has been stopped so that
writes can be processed.

:::{NOTE}
By default, write or delete operations succeed if the primary shard is available (see `CREATE TABLE` parameter {ref}`write.wait-for-active-shards <crate-reference:sql-create-table-write-wait-for-active-shards>`).
:::
