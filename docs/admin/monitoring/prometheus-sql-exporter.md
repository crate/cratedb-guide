(prometheus-sql-exporter)=

# Prometheus SQL Exporter

The SQL Exporter allows running arbitrary SQL statements against a CrateDB cluster to retrieve additional information. As the cluster contains information from each node, we do not need to install the SQL Exporter on every node. Instead, we install it centrally on the same machine that also hosts Prometheus.

Please note that it is not the same to set up a data source in Grafana pointing to CrateDB to display the output from queries in real-time as to use Prometheus to collect these values over time.

Installing the package is straight-forward:
```shell
apt install prometheus-sql-exporter
```

For the SQL exporter to connect to the cluster, we need to create a new user `sql_exporter`. We grant the user reading access to the `sys` schema. Run the below commands on any CrateDB node:
```shell
curl -H 'Content-Type: application/json' -X POST 'http://localhost:4200/_sql' -d '{"stmt":"CREATE USER sql_exporter WITH (password = '\''insert_password'\'');"}'
curl -H 'Content-Type: application/json' -X POST 'http://localhost:4200/_sql' -d '{"stmt":"GRANT DQL ON SCHEMA sys TO sql_exporter;"}'
```

We then create a configuration file in `/etc/prometheus-sql-exporter.yml` with a sample query that retrieves the number of shards per node:

```yaml
jobs:
- name: "global"
  interval: '5m'
  connections: ['postgres://sql_exporter:insert_password@ubuntuvm1:5433?sslmode=disable']
  queries:
  - name: "shard_distribution"
    help: "Number of shards per node"
    labels: ["node_name"]
    values: ["shards"]
    query: |
      SELECT node['name'] AS node_name, COUNT(*) AS shards
      FROM sys.shards
      GROUP BY 1;
    allow_zero_rows: true

  - name: "heap_usage"
    help: "Used heap space per node"
    labels: ["node_name"]
    values: ["heap_used"]
    query: |
      SELECT name AS node_name, heap['used'] / heap['max']::DOUBLE AS heap_used
      FROM sys.nodes;

  - name: "global_translog"
    help: "Global translog statistics"
    values: ["translog_uncommitted_size"]
    query: |
      SELECT COALESCE(SUM(translog_stats['uncommitted_size']), 0) AS translog_uncommitted_size
      FROM sys.shards;

  - name: "checkpoints"
    help: "Maximum global/local checkpoint delta"
    values: ["max_checkpoint_delta"]
    query: |
      SELECT COALESCE(MAX(seq_no_stats['local_checkpoint'] - seq_no_stats['global_checkpoint']), 0) AS max_checkpoint_delta
      FROM sys.shards;

  - name: "shard_allocation_issues"
    help: "Shard allocation issues"
    labels: ["shard_type"]
    values: ["shards"]
    query: |
        SELECT IF(s.primary = TRUE, 'primary', 'replica') AS shard_type, COALESCE(shards, 0) AS shards
        FROM UNNEST([true, false]) s(primary)
        LEFT JOIN (
          SELECT primary, COUNT(*) AS shards
          FROM sys.allocations
          WHERE current_state <> 'STARTED'
          GROUP BY 1
        ) a ON s.primary = a.primary;
```

*Please note: There exist two implementations of the SQL Exporter: [burningalchemist/sql_exporter](https://github.com/burningalchemist/sql_exporter) and [justwatchcom/sql_exporter](https://github.com/justwatchcom/sql_exporter). They don't share the same configuration options.
Our example is based on the implementation that is shipped with the Ubuntu package, which is justwatchcom/sql_exporter.*

To apply the new configuration, we restart the service:

```shell
systemctl restart prometheus-sql-exporter
```

The SQL Exporter can also be used to monitor any business metrics as well, but be careful with regularly running expensive queries. Below are two more advanced monitoring queries of CrateDB that may be useful:

```sql
/* Time since the last successful snapshot (backup) */
SELECT (NOW() - MAX(started)) / 60000 AS MinutesSinceLastSuccessfulSnapshot
FROM sys.snapshots
WHERE "state" = 'SUCCESS';
```
