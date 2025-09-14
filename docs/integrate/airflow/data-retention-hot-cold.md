(airflow-data-retention-hot-cold)=
# Building a hot and cold storage data retention policy in CrateDB with Apache Airflow

In this fourth article on automating recurrent CrateDB queries with [Apache Airflow](https://airflow.apache.org/), we will present a second strategy for implementing a data retention policy. Previously, we shared the {ref}`Data Retention Delete DAG <airflow-data-retention-policy>`, which dropped old partitions after a certain period of time. In that article, we introduce the complementary strategy of a hot/cold storage approach.

## What is a hot/cold storage strategy?

A hot/cold storage strategy is often motivated by a tradeoff between performance and cost-effectiveness. In a database such as CrateDB, more recent data tends to have a higher significance for analytical queries. Well-performing disks (hot storage) play a key role on the infrastructure side to support performance requirements but can come at a high cost. As data ages and gets less business-critical for near-real-time analysis, transitioning it to slower/cheaper disks (cold storage) helps to improve the cost-performance ratio.

In a CrateDB cluster, nodes can have different hardware specifications. Hence, a cluster can consist of a combination of hot and cold storage nodes, each with respective disks. By assigning corresponding attributes to nodes, CrateDB can be made aware of such node types and consider if when allocating partitions.

## CrateDB setup

To create a multi-node setup, we make use of {ref}`docker-compose` to spin up three nodes – two hot nodes, and one cold node. For the scope of this article, we will not actually use different hardware specifications for disks, but each disk is represented as a separate Docker volume.

The designation of a node type is done by passing the `-Cnode.attr.storage` parameter to each node with the value hot or cold. The resulting `docker-compose.yml` file with two hot nodes and one cold node is as follows:

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
      - CRATE_HEAP_SIZE=2g

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
      - CRATE_HEAP_SIZE=2g

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
      - CRATE_HEAP_SIZE=2g
```

The cluster is started via `docker-compose up`. For more details, please see the above-linked documentation.

Once the cluster is up and running, we create our partitioned time-series table. By specifying `"routing.allocation.require.storage" = 'hot'` in the `WITH` clause, we configure new partitions to be placed on a hot node.

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

To validate the allocation of shards we insert a sample row:

```sql
INSERT INTO doc.raw_metrics (variable, timestamp, value, quality) VALUES ('water-flow', NOW() - '5 months'::INTERVAL, 12, 1);
```

The `INSERT` statement will implicitly trigger the creation of a new partition consisting of six shards. Since we configured `cratedb01` and `cratedb02` as hot nodes, we expect shards to be allocated only on those two nodes, and not on `cratedb03` (which is a cold node). The allocation can be validated by navigating to the “Shards” section in the Admin UI:

![Screenshot 2021-12-08 at 11.03.44|273x250](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ade3bbd61b56a642ee2493f2dca63a60cba7de1b.png){height=320px}

As expected, primary shards, as well as replicas, are evenly distributed between the first two nodes, while no shards are stored on the third node.

Next, we will create a table storing the retention policy used to transition partitions from hot to cold nodes:

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

The schema is an extension of what was introduced in the first article on the {ref}`Data Retention Delete DAG <airflow-data-retention-policy>`. The `strategy` column allows switching between the previously introduced dropping of partitions (`delete`) and the now added reallocation (`reallocate`). For our `raw_metrics` table, we add a policy of transitioning from hot to cold nodes after 60 days:

```sql
INSERT INTO doc.retention_policies VALUES ('doc', 'raw_metrics', 'ts_day', 60, 'storage', 'cold', NULL, 'reallocate');
```

To remember which partitions have already been reallocated, we can make use of the `attributes` column in `sys.nodes` which reflects the hot/cold storage attribute we configured in the Docker Compose setup.

## Airflow setup

We assume that a basic Astronomer/Airflow setup is already in place, as described in our {ref}`first post <airflow-export-s3>`. Let’s quickly go through the three steps of the algorithm:

1. `get_policies`: A query on `doc.retention_policies` and `information_schema.table_partitions` identifies partitions affected by a retention policy.
2. `map_policy`: A helper method transforming the output of `get_policies` into a Python `dict` data structure for easier handling.
4. `reallocate_partitions`: Executes an SQL statement for each mapped policy: `ALTER TABLE <table> PARTITION (<partition key> = <partition value>) SET ("routing.allocation.require.storage" = 'cold');`
The CrateDB cluster will then automatically initiate the relocation of the affected partition to a node that fulfills the requirement (`cratedb03` in our case).

The full implementation is available as [data_retention_reallocate_dag.py](https://github.com/crate/crate-airflow-tutorial/blob/main/dags/data_retention_reallocate_dag.py) on GitHub.

To validate our implementation, we trigger the DAG once manually via the Airflow UI at `http://localhost:8081/`. Once executed, log messages of the `reallocate_partitions` task confirm the reallocation was triggered for the partition with the sample data set up earlier:

```text
[2021-12-08, 12:39:44 UTC] {data_cleanup_dag.py:47} INFO - Reallocating partition ts_day = 1625702400000 for table doc.raw_metrics to storage = cold
[2021-12-08, 12:39:44 UTC] {dbapi.py:225} INFO - Running statement: ALTER TABLE doc.raw_metrics PARTITION (ts_day = 1625702400000) SET ("routing.allocation.require.storage" = 'cold');
, parameters: None
```


Revisiting the “Shards” section in the CrateDB Admin UI confirms that all shards have been moved to `cratedb03`. Since the default replication setting is `0-1` and there is only one cold node in this setup, replicas have been discarded.

![Screenshot 2021-12-08 at 13.48.22|288x250](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/9f56283dcb4457b1123e1a653d951fc78e52a612.png){height=320px}

## Combined hot/cold and deletion strategy

The presented hot/cold storage strategy also integrates seamlessly with the previously introduced {ref}`Data Retention Delete DAG <airflow-data-retention-policy>`. Both strategies can be combined:

1. Transition to cold nodes: Reallocates partitions from (expensive) hot nodes to (cheaper) cold nodes
2. Deletion from cold nodes: After another retention period on cold nodes, permanently delete partitions

Both DAGs use the same control table for retention policies. In our example, we already added an entry for the reallocate strategy after 60 days. If we want to keep partitions on cold nodes for another 60 days and then discard them, we add an additional `delete` policy. Note that the retention periods are not additive, i.e. we need to specify the `delete` retention period as 120 days:

```sql
INSERT INTO doc.retention_policies (table_schema, table_name, partition_column, retention_period, strategy) VALUES ('doc', 'raw_metrics', 'ts_day', 120, 'delete');
```

## Summary

Building upon the previously discussed data retention policy implementation, we showed that reallocating partitions integrates seemingly and consists only of a single SQL statement.
CrateDB’s self-organization capabilities take care of all low-level operations and the actual moving of partitions. Furthermore, we showed that a multi-staged approach to data retention policies can be achieved by first reallocating and eventually deleting partitions permanently.
