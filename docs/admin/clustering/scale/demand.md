(scale-demand)=

# Scale CrateDB clusters up and down to cope with peaks in demand

This tutorial demonstrates the [shard allocation filtering] functionality,
and how it is applied in a real-world data management scenario, specifically
about tuning your database cluster to cope with high-demand situations.


## Introduction

Many organizations size their database infrastructure to handle the maximum level of load they can anticipate, but very often load is seasonal, in some cases around specific events on certain days of the year. Compromises are often made where infrastructure sits idle most of the year and performance is not as good as desired when requests peak.

CrateDB allows clusters to be scaled both up and down by adding and removing nodes, this allows significant savings during quiet periods, and also the provisioning of extra capacity during particular periods of high activity to have optimal performance.

When nodes are added or removed CrateDB automatically rebalances shards, but in cases where we have very large volumes of historical data and new nodes are only added for a short period of time, we may want to avoid any of the historical data being relocated to the temporary nodes.

## About
The approach described below explains how to achieve this using [shard allocation filtering](https://crate.io/docs/crate/reference/en/5.1/general/ddl/shard-allocation.html) on a table that is partitioned by day, the idea is that the period of high activity can be foreseen, so the scaling up will take place the day before a big event, and the scaling down someday after the event has ended.

This same approach can be applied to multiple tables. It is particularly relevant for the larger tables, and smaller tables can be kept on the baseline nodes, but it is always good to consider the impact on querying performance if the small tables will be queried during the big event `JOIN`ed to the big tables that will have data on the temporary nodes.

## Preparing the test environment

In this example, we will imagine that the surge in demand we are preparing for is related to the 2022 FIFA Men’s World Cup running from 20/11/2022 to 18/12/2022.

We will start with a 3 nodes cluster, on which we will create a test table and populate it with some pre-World Cup data:

```sql
CREATE TABLE test (
  ts TIMESTAMP,
  recorddetails TEXT,
  "day" GENERATED ALWAYS AS date_trunc('day',ts)
)
PARTITIONED BY ("day")
CLUSTERED INTO 4 SHARDS
WITH (number_of_replicas = 1);

INSERT INTO test (ts) VALUES ('2022-11-18'), ('2022-11-19');
```

The shards will initially look like this:
![Image](https://github.com/user-attachments/assets/045f66fc-4134-4363-a37a-711a449c43d5)

## Before deploying extra nodes

We want to make sure that the addition of the temporary nodes does not result on data from the large tables getting rebalanced to use these nodes.

We will be able to identify the new nodes by using a custom attribute (`node.attr.storage=temporarynodes`) (see further down for details on how to configure this), so the first step is to configure the existing partitions so that they do not consider the new nodes as suitable targets for shard allocation.

In CrateDB 5.1.2 or higher, you can achieve this with:
```sql
/* this applies the setting to all existing partitions and new partitions */
ALTER TABLE test SET ("routing.allocation.exclude.storage" = 'temporarynodes');

/* then we run this other command so that the setting does not apply to new partitions */
ALTER TABLE ONLY test RESET ("routing.allocation.exclude.storage");
```
In CrateDB 5.9.0 or higher, you don't need to change shard allocations for each
individual table any longer. Instead, default allocation rules can be set on
the cluster level:
> [CrateDB 5.9.0] added support to override `routing.allocation.*` cluster
> settings with a `routing.allocation.*` table setting. This can be used to
> define the default routing behavior for all tables with a cluster setting
> and reroute individual tables by assigning the table setting using `ALTER
> TABLE SET`.

No data gets reallocated when running this, and there is no impact on querying or ingestion.

Starting in CrateDB 5.2 this setting is visible in `settings['routing']` in `information_schema.table_partitions`.

## Deploying the extra nodes

We want to deploy the new nodes setting a custom attribute.
If using containers add a line to `args` in your YAML file with:

```
- -Cnode.attr.storage=temporarynodes
```

Otherwise add this to `crate.yml` (typically on `/etc/crate`)

```
node.attr.storage=temporarynodes
```

Please note the word `storage` in this context does not have any special meaning for CrateDB, it is just a name that we have chosen in this case for the custom attribute.

Starting with CrateDB 5.2 these node attributes will be visible in `sys.nodes`.

We need to calculate how many shards will be created each day (that is on each partition) during the special event, since our test table is `CLUSTERED INTO 4 SHARDS` `WITH (number_of_replicas=1)` we would have 4 (shards per partition) x 2 (primary + copy) = 8

We then need to see what is the ceiling of the number we got (8) divided by the total number of nodes (baseline + temporary), if that is for instance 3+2=5 then we have ceiling(8/5)=2.

That means that if a maximum of 2 of the new shards created each day during the event goes to each node then the new data will be balanced across all nodes.

With the nodes ready, on the day before the event, we need to configure the special tables so that any new partitions follow this rule:

```sql
ALTER TABLE ONLY test SET ("routing.allocation.total_shards_per_node" = 2);
```

This setting (`total_shards_per_node`) is visible at partition level in `settings['routing']` in `information_schema.table_partitions`.

No data gets reallocated when running this and there is no impact on querying or ingestion.

This setting can be checked by using:

```sql
SHOW CREATE TABLE test;
```

## During the event

Let’s now simulate the arrival of data during the event:

```sql
INSERT INTO test (ts) VALUES 
('2022-11-20'), ('2022-11-21'), ('2022-11-22'), ('2022-11-23'),
('2022-11-24'), ('2022-11-25'), ('2022-11-26'), ('2022-11-27'),
('2022-11-28'), ('2022-11-29'), ('2022-11-30'), ('2022-12-01'),
('2022-12-02'), ('2022-12-03'), ('2022-12-04'), ('2022-12-05'),
('2022-12-06'), ('2022-12-07'), ('2022-12-08'), ('2022-12-09'),
('2022-12-10'), ('2022-12-11'), ('2022-12-12'), ('2022-12-13'),
('2022-12-14'), ('2022-12-15'), ('2022-12-16'), ('2022-12-17'),
('2022-12-18')
```

We can see that data from before the event stays on the baseline nodes while data for the days of the event gets distributed over all nodes:

![Image](https://github.com/user-attachments/assets/b0f294a4-ff2b-4b84-8a34-aa782cb5a300)

The same can be checked programmatically with this query:

```sql
SELECT table_partitions.table_schema,
       table_partitions.table_name,
       table_partitions.values['day']::TIMESTAMP,
       shards.primary,
       shards.node['name']
FROM sys.shards
JOIN information_schema.table_partitions
  ON shards.partition_ident = table_partitions.partition_ident
ORDER BY 1, 2, 3, 4, 5;
```

## The day the event ends

On the last day of the event, we need to configure the table so that the next partition goes to the baseline nodes:

```sql
ALTER TABLE ONLY test SET ("routing.allocation.exclude.storage" = 'temporarynodes');

ALTER TABLE ONLY test RESET ("routing.allocation.total_shards_per_node");
```

## A day after the event has ended

New data should now again go the baseline nodes only.

Let’s confirm it:

```sql
INSERT INTO test (ts) VALUES ('2022-12-19'), ('2022-12-20');
```

![image|690x73]

When we are ready to decommission the temporary nodes, we need to move the data collected during the days of the event.

In CrateDB 5.1.2 or higher, you can achieve this with:
```sql
ALTER TABLE test SET ("routing.allocation.exclude.storage" = 'temporarynodes');
ALTER TABLE test RESET ("routing.allocation.total_shards_per_node");
```

The data movement takes place one replica at a time and there is no impact on querying of the event’s data while it is being moved, new data also continues to flow to the baseline nodes and its ingestion and querying are also not impacted.

We can monitor the progress of the data relocation querying `sys.shards` and `sys.allocations`.

Once all shards have moved away from the temporary nodes, we can decommission them gracefully:

```sql
ALTER CLUSTER DECOMMISSION 'nodename';
```

Once this is done, the machines can safely be shutdown.

## When the time comes for the next event

If desired, new nodes can be deployed reusing the same names that were used for the temporary nodes before.


[CrateDB 5.9.0]: inv:crate-reference#version_5.9.0
[shard allocation filtering]: inv:crate-reference#ddl_shard_allocation
