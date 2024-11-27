(scaling-clusters)=
# Scale Clusters Up and Down

A significant feature in CrateDB is that it can scale horizontally, which means
that instead of adding more RAM, CPU, and disk resources to existing nodes, you
will add more individual nodes to your CrateDB cluster.

By running your database cluster on multiple nodes, you will gain two benefits.

- Store data volumes larger than being able to be handled on a single machine.
- Add resiliency to your distributed database cluster, by increasing the number
  of replica nodes.


(scaling-expand)=
## Expand Cluster

The article about [how to add new nodes to an existing cluster] walks you
through the process of scaling up your database cluster, and educates you
about the corresponding details to consider.


(scaling-ondemand)=
## Scale On-Demand

The article about [scaling CrateDB clusters up and down to cope with peaks in
demand] shares knowledge about the [shard allocation filtering] feature of
CrateDB.

Along the lines, it demonstrates how this functionality is applied in a real-
world data management scenario, which is about tuning your database cluster to
cope with high-demand situations.

Prepare adding extra nodes to the database cluster.
```sql
/* Apply routing setting to all existing partitions and new partitions. */
ALTER TABLE test SET ("routing.allocation.exclude.storage" = 'temporarynodes');

/* Configure the setting to be excluded / not applied to _new_ partitions. */
ALTER TABLE ONLY test RESET ("routing.allocation.exclude.storage");
```

Before the high-demand event, properly configure table routing accordingly.
```sql
ALTER TABLE ONLY test SET ("routing.allocation.total_shards_per_node" = 2);
```

To decommission extra database nodes, we need to move the data collected during
the days of the event.
```sql
-- Move the collected data off the extra nodes.
ALTER TABLE test SET ("routing.allocation.exclude.storage" = 'temporarynodes');
ALTER TABLE test RESET ("routing.allocation.total_shards_per_node");

-- Invoke the decommissioning.
ALTER CLUSTER DECOMMISSION 'nodename';
```


[how to add new nodes to an existing cluster]: https://community.cratedb.com/t/how-to-add-new-nodes-to-an-existing-cluster/1546
[scaling CrateDB clusters up and down to cope with peaks in demand]: https://community.cratedb.com/t/scaling-cratedb-clusters-up-and-down-to-cope-with-peaks-in-demand/1314
[shard allocation filtering]: inv:crate-reference#ddl_shard_allocation
