(airflow-data-retention-hot-cold)=
# Build a hot/cold storage data retention policy in CrateDB with Apache Airflow

:::{article-info}
---
avatar: https://sea2.discourse-cdn.com/flex020/user_avatar/community.cratedb.com/hammerhead/288/270_2.png
avatar-link: https://github.com/hammerhead
avatar-outline: muted
author: Niklas Schmidtmer
date: May 4, 2023
read-time: 20 min read
class-container: sd-p-2 sd-outline-muted sd-rounded-1
---
:::

This fourth article on automating recurring CrateDB queries with [Apache Airflow](https://airflow.apache.org/) presents a second data‑retention strategy. Previously, the {ref}`Data Retention Delete DAG <airflow-data-retention-policy>` dropped old partitions after a set period. This article adds a complementary hot/cold storage approach.

## What is a hot/cold storage strategy?

Hot/cold storage balances performance and cost. In CrateDB, recent data usually matters most for analytics. Fast disks (hot storage) meet performance requirements but are expensive. As data ages and becomes less critical, moving it to slower, cheaper disks (cold storage) improves the cost‑performance ratio.

CrateDB clusters can mix nodes with different hardware. Mark nodes as hot or cold using attributes; CrateDB then considers these attributes when allocating partitions.

## CrateDB setup

Use {ref}`docker-compose` to start a three‑node cluster—two hot nodes and one cold node. For simplicity, use separate Docker volumes instead of distinct disk hardware.

Set the node type by passing `-Cnode.attr.storage=hot|cold` to each node. The following `docker-compose.yml` starts two hot nodes and one cold node:

```yaml
services:
  cratedb01:
    image: crate:latest
    ports:
      - "4201:4200"
      - "5532:5432"
    volumes:
      - /tmp/crate/hot-01:/data
    command: ["crate",
              "-Ccluster.name=crate-docker-cluster",
              "-Cnode.name=cratedb01",
              "-Cnode.attr.storage=hot",
              "-Cnetwork.host=_site_",
              "-Cdiscovery.seed_hosts=cratedb02,cratedb03",
              "-Ccluster.initial_master_nodes=cratedb01,cratedb02,cratedb03",
              "-Cgateway.expected_data_nodes=3",
              "-Cgateway.recover_after_data_nodes=2"]
    environment:
      - CRATE_HEAP_SIZE=1g

  cratedb02:
    image: crate:latest
    ports:
      - "4202:4200"
      - "5632:5432"
    volumes:
      - /tmp/crate/hot-02:/data
    command: ["crate",
              "-Ccluster.name=crate-docker-cluster",
              "-Cnode.name=cratedb02",
              "-Cnode.attr.storage=hot",
              "-Cnetwork.host=_site_",
              "-Cdiscovery.seed_hosts=cratedb01,cratedb03",
              "-Ccluster.initial_master_nodes=cratedb01,cratedb02,cratedb03",
              "-Cgateway.expected_data_nodes=3",
              "-Cgateway.recover_after_data_nodes=2"]
    environment:
      - CRATE_HEAP_SIZE=1g

  cratedb03:
    image: crate:latest
    ports:
      - "4203:4200"
      - "5732:5432"
    volumes:
      - /tmp/crate/cold-03:/data
    command: ["crate",
              "-Ccluster.name=crate-docker-cluster",
              "-Cnode.name=cratedb03",
              "-Cnode.attr.storage=cold",
              "-Cnetwork.host=_site_",
              "-Cdiscovery.seed_hosts=cratedb01,cratedb02",
              "-Ccluster.initial_master_nodes=cratedb01,cratedb02,cratedb03",
              "-Cgateway.expected_data_nodes=3",
              "-Cgateway.recover_after_data_nodes=2"]
    environment:
      - CRATE_HEAP_SIZE=1g
```

Start the cluster with `docker compose up`. For details, see the linked documentation.

After the cluster starts, create a partitioned time‑series table. Set `"routing.allocation.require.storage" = 'hot'` in the `WITH` clause so CrateDB places new partitions on a hot node.

```sql
CREATE TABLE IF NOT EXISTS doc.raw_metrics (
   "variable" TEXT,
   "timestamp" TIMESTAMP WITH TIME ZONE,
   "ts_day" TIMESTAMP GENERATED ALWAYS AS DATE_TRUNC('day', "timestamp"),
   "value" REAL,
   "quality" INTEGER,
   PRIMARY KEY ("variable", "timestamp", "ts_day")
)
PARTITIONED BY (ts_day)
WITH ("routing.allocation.require.storage" = 'hot');
```

Insert a sample row to validate shard allocation:

```sql
INSERT INTO doc.raw_metrics (variable, timestamp, value, quality) VALUES ('water-flow', NOW() - '5 months'::INTERVAL, 12, 1);
```

The `INSERT` implicitly creates a new partition with the table’s configured number of shards.
Because `cratedb01` and `cratedb02` are hot nodes, CrateDB allocates shards only on those nodes, not on `cratedb03` (cold). Verify this in the Admin UI under “Shards”:

![CrateDB Admin UI “Shards” view showing primary and replica shards evenly distributed across hot nodes; no shards on the cold node](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ade3bbd61b56a642ee2493f2dca63a60cba7de1b.png){height=320px}

CrateDB distributes primary and replica shards evenly across the first two nodes and stores no shards on the third node.

Next, create a table that stores the retention policy to transition partitions from hot to cold nodes:

```sql
CREATE TABLE IF NOT EXISTS doc.retention_policies (
   "table_schema" TEXT,
   "table_name" TEXT,
   "partition_column" TEXT NOT NULL,
   "retention_period" INTEGER NOT NULL,
   "reallocation_attribute_name" TEXT,
   "reallocation_attribute_value" TEXT,
   "target_repository_name" TEXT,
   "strategy" TEXT NOT NULL,
   PRIMARY KEY ("table_schema", "table_name", "strategy")
)
CLUSTERED INTO 1 SHARDS;
```

This schema extends the first article’s {ref}`Data Retention Delete DAG <airflow-data-retention-policy>`. The `strategy` column switches between dropping partitions (`delete`) and reallocation (`reallocate`). For the `raw_metrics` table, add a policy that transitions partitions from hot to cold nodes after 60 days:

```sql
INSERT INTO doc.retention_policies VALUES ('doc', 'raw_metrics', 'ts_day', 60, 'storage', 'cold', NULL, 'reallocate');
```

Identify hot/cold nodes via `sys.nodes.attributes`. Determine whether a partition is reallocated by inspecting its routing setting or shard locations (for example, via `information_schema.table_partitions` and `sys.shards`).

## Airflow setup

Use a basic Astronomer/Airflow setup as described in the {ref}`first post <airflow-export-s3>`. The algorithm has three steps:

1. `get_policies`: A query on `doc.retention_policies` and `information_schema.table_partitions` identifies partitions affected by a retention policy.
2. `map_policy`: A helper method transforming the output of `get_policies` into a Python `dict` data structure for easier handling.
3. `reallocate_partitions`: Executes an SQL statement for each mapped policy: `ALTER TABLE "<schema>"."<table>" PARTITION ("<partition key>" = <partition value>) SET ("routing.allocation.require.storage" = 'cold');`

CrateDB then automatically initiates relocation of the affected partition to a node that fulfills the requirement (`cratedb03` in this setup).

The full implementation is available as [data_retention_reallocate_dag.py](https://github.com/crate/cratedb-airflow-tutorial/blob/main/dags/data_retention_reallocate_dag.py) on GitHub.

To validate the implementation, trigger the DAG once manually via the Airflow UI at `http://localhost:8081/`. After execution, the `reallocate_partitions` task logs confirm that the DAG triggered reallocation for the sample partition:

```text
[2021-12-08, 12:39:44 UTC] {data_retention_reallocate_dag.py:47} INFO - Reallocating partition ts_day = 1625702400000 for table doc.raw_metrics to storage = cold
[2021-12-08, 12:39:44 UTC] {dbapi.py:225} INFO - Running statement: ALTER TABLE doc.raw_metrics PARTITION (ts_day = 1625702400000) SET ("routing.allocation.require.storage" = 'cold');
```

The “Shards” section in the CrateDB Admin UI shows that CrateDB moved all shards to `cratedb03`.
With `number_of_replicas = '0-1'` and only one cold node in this setup, CrateDB does not allocate replicas on cold storage.

![CrateDB Admin UI “Shards” view showing all shards relocated to the cold node; replicas not allocated](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/9f56283dcb4457b1123e1a653d951fc78e52a612.png){height=320px}

## Combined hot/cold and deletion strategy

This hot/cold storage strategy integrates with the {ref}`Data Retention Delete DAG <airflow-data-retention-policy>`. Combine them:

1. Transition to cold nodes: Reallocates partitions from (expensive) hot nodes to (cheaper) cold nodes
2. Deletion from cold nodes: After another retention period on cold nodes, permanently delete partitions

Both DAGs use the same control table for retention policies. The example already adds an entry for the `reallocate` strategy after 60 days. To keep partitions on cold nodes for another 60 days and then delete them, add a `delete` policy. Note: the retention periods are not additive; specify the `delete` retention period as 120 days:

```sql
INSERT INTO doc.retention_policies (table_schema, table_name, partition_column, retention_period, strategy) VALUES ('doc', 'raw_metrics', 'ts_day', 120, 'delete');
```

## Summary

Reallocation builds on the earlier data‑retention policy and uses a single SQL statement.
CrateDB handles the movement automatically. A multi‑stage policy is straightforward: first reallocate, then delete.
