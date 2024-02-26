(scaling-clusters)=

# Scaling Clusters Up and Down

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


[scaling CrateDB clusters up and down to cope with peaks in demand]: https://community.cratedb.com/t/scaling-cratedb-clusters-up-and-down-to-cope-with-peaks-in-demand/1314
[shard allocation filtering]: inv:crate-reference#ddl_shard_allocation
