(scaling-clusters)=
# Scale Clusters Up and Down

A significant feature in CrateDB is that it can scale horizontally, which means
that instead of adding more RAM, CPU, and disk resources to existing nodes, you
will add more individual nodes to your CrateDB cluster.

By running your database cluster on multiple nodes, you will gain two benefits.

- Store data volumes larger than being able to be handled on a single machine.
- Add resiliency to your distributed database cluster, by increasing the number
  of replica nodes.


:::{toctree}
:maxdepth: 1
:hidden:

Expand <expand>
On-Demand <demand>
Autoscale <auto>
On Kubernetes <kubernetes>
:::


## Learn

:::::{grid}

::::{grid-item-card}
:link: scale-expand
:link-type: ref
(scaling-expand)=
:::{rubric} Expand Cluster
:::
Learn how to add new nodes to an existing CrateDB database cluster
running on your premises, in order to expand its capacity using
horizontal scaling.
+++
{hyper-tutorial}`scale-expand`
::::

::::{grid-item-card}
:link: scale-demand
:link-type: ref
(scaling-ondemand)=
:::{rubric} On-Demand Scaling
:::
Learn how to use CrateDB's [shard allocation filtering] feature in
practice, in order to scale CrateDB clusters up and down to cope
with peaks in high-demand situations. 
+++
{hyper-tutorial}`scale-demand`
::::

::::{grid-item-card}
:link: scale-auto
:link-type: ref
(scaling-autoscale)=
:::{rubric} Automatic Scaling
:::
Learn how to automatically scale your CrateDB Cloud Cluster based on a
threshold on the number of shards in a cluster, using the
CrateDB Cloud REST API.
+++
{hyper-tutorial}`scale-auto`
::::
:::::


## Synopsis

A rough walkthrough how resource management works in CrateDB, to manage
high-demand / peak situations.

:::{rubric} Provision Resources
:::
Prepare by adding extra nodes to the database cluster.
```sql
/* Apply routing setting to all existing partitions and new partitions. */
ALTER TABLE test SET ("routing.allocation.exclude.storage" = 'temporarynodes');

/* Configure the setting to be excluded / not applied to _new_ partitions. */
ALTER TABLE ONLY test RESET ("routing.allocation.exclude.storage");
```

:::{rubric} Scale Up
:::
Right before the high-demand event, adjust the table routing,
so the cluster will use additional resources.
```sql
ALTER TABLE ONLY test SET ("routing.allocation.total_shards_per_node" = 2);
```

:::{rubric} Scale Down
:::
To decommission excess database nodes, move the data collected during
the days of the event away.
```sql
-- Move the collected data off the extra nodes.
ALTER TABLE test SET ("routing.allocation.exclude.storage" = 'temporarynodes');
ALTER TABLE test RESET ("routing.allocation.total_shards_per_node");

-- Invoke the decommissioning.
ALTER CLUSTER DECOMMISSION 'nodename';
```


## Advices

Please apply best-practice operation guidelines when managing your database
cluster.

:::{tip}
:class: hero font-large

For safely adding or decommissioning nodes, it is a good idea to
add and remove only one node at a time.
:::

:::{caution}
:class: hero font-large

When restarting, shutting down, or when removing nodes from a cluster, using
the `DECOMMISSION` command, you must be conscious about maintaining a quorum
of nodes up and connected to the cluster as a whole, even if some nodes would
no longer have any data.
:::



<style>
.font-large {
  font-size: large !important;
}
</style>


[how to add new nodes to an existing cluster]: https://community.cratedb.com/t/how-to-add-new-nodes-to-an-existing-cluster/1546
[how to scale CrateDB clusters up and down to cope with peaks in demand]: https://community.cratedb.com/t/scaling-cratedb-clusters-up-and-down-to-cope-with-peaks-in-demand/1314
[shard allocation filtering]: inv:crate-reference#ddl_shard_allocation
