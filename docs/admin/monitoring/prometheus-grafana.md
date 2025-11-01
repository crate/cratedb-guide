(monitoring-prometheus-grafana)=
# Monitoring a self-managed CrateDB cluster with Prometheus and Grafana

## Introduction

In production, monitor CrateDB proactively to catch issues early and
collect statistics for capacity planning.

Pair two OSS tools: use [Prometheus] to collect and store metrics,
and [Grafana] to build dashboards.

For a CrateDB environment, we are interested in:
* CrateDB-specific metrics, such as the number of shards or number of failed queries
* and OS metrics, such as available disk space, memory usage, or CPU usage

For what concerns CrateDB-specific metrics we recommend making these available to Prometheus by using the [Crate JMX HTTP Exporter](https://cratedb.com/docs/crate/reference/en/5.1/admin/monitoring.html#exposing-jmx-via-http) and [Prometheus SQL Exporter](https://github.com/justwatchcom/sql_exporter). For what concerns OS metrics, in Linux environments, we recommend using the [Prometheus Node Exporter](https://prometheus.io/docs/guides/node-exporter/).

Containerized and [CrateDB Cloud] setups differ. This tutorial targets
standalone and on‑premises installations.

## Configure and start a CrateDB cluster

First things first, we will need a CrateDB cluster, you may have one already and
that is great, but if you do not we can get one up quickly.
{ref}`Multi-node setup instructions <multi-node-setup-example>` provides
a quick walkthrough for Ubuntu Linux.

## Setup of the Crate JMX HTTP Exporter

This is very simple, on each node run the following:

```shell
cd /usr/share/crate/lib
wget https://repo1.maven.org/maven2/io/crate/crate-jmx-exporter/1.2.0/crate-jmx-exporter-1.2.0.jar
nano /etc/default/crate
```

then uncomment the `CRATE_JAVA_OPTS` line and change its value to:

```shell
# Append to existing options (preserve other flags).
CRATE_JAVA_OPTS="${CRATE_JAVA_OPTS:-} -javaagent:/usr/share/crate/lib/crate-jmx-exporter-1.2.0.jar=8080"
```

and restart the crate daemon:

```bash
systemctl restart crate
```

## Prometheus Node Exporter

This can be set up with a one-liner:

```shell
apt install prometheus-node-exporter
```

## Prometheus SQL Exporter

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

## Prometheus setup

You would run this on a machine that is not part of the CrateDB cluster and it can be installed with:

```shell
apt install prometheus --no-install-recommends
```

By default, Prometheus binds to :9090 without authentication. Prevent
auto-start during install (e.g., with `policy-rcd-declarative`), then
configure web auth using a YAML file.

Create `/etc/prometheus/web.yml`:
```yaml
basic_auth_users:
  admin: <bcrypt hash>
```

Point Prometheus at it (e.g., `/etc/default/prometheus`):

```shell
ARGS="--web.config.file=/etc/prometheus/web.yml --web.enable-lifecycle"
```

Restart Prometheus after setting ownership and 0640 permissions on `web.yml`.

For a large deployment where you also use Prometheus to monitor other systems,
you may also want to use a CrateDB cluster as the storage for all Prometheus
metrics, you can read more about this at
[CrateDB Prometheus Adapter](https://github.com/crate/cratedb-prometheus-adapter).

Now we will configure Prometheus to scrape metrics from the node explorer from
the CrateDB machines and also metrics from our Crate JMX HTTP Exporter:
```shell
nano /etc/prometheus/prometheus.yml
```

Where it says:
```yaml
- job_name: 'node'
  static_configs:
    - targets: ['localhost:9100']
```

Replace it with the following jobs: port 9100 (Node Exporter),
port 8080 (Crate JMX Exporter), and port 9237 (SQL Exporter),
like outlined below.
```yaml
- job_name: 'node'
  static_configs:
    - targets: ['ubuntuvm1:9100', 'ubuntuvm2:9100']
- job_name: 'cratedb_jmx'
  static_configs:
    - targets: ['ubuntuvm1:8080', 'ubuntuvm2:8080']
- job_name: 'sql_exporter'
  static_configs:
    - targets: ['localhost:9237']
```

Restart the `prometheus` daemon if it was already started (`systemctl restart prometheus`).

## Grafana setup

Grafana can be installed on the same machine where you installed Prometheus.
To install Grafana on a Debian or Ubuntu machine, use those commands:
```shell
echo "deb https://packages.grafana.com/oss/deb stable main" | tee -a /etc/apt/sources.list.d/grafana.list
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
apt update
apt install grafana
```
Then, start Grafana.
```shell
systemctl start grafana-server
```
For other systems, please refer to the [Grafana installation documentation][grafana-debian].

Open `http://<grafana-host>:3000` to access the Grafana login screen.
The default credentials are `admin`/`admin`; change the password immediately.

Click on "Add your first data source", then click "Prometheus" and set the
URL to `http://<prometheus-host>:9090`.

If you had configured basic authentication for Prometheus this is where you would need to enter the credentials.

Click "Save & test".

An example dashboard based on the discussed setup is available for easy importing on [grafana.com](https://grafana.com/grafana/dashboards/17174-cratedb-monitoring/). In your Grafana installation, on the left-hand side, hover over the “Dashboards” icon and select “Import”. Specify the ID 17174 and load the dashboard. On the next screen, finalize the setup by selecting your previously created Prometheus data sources.

![CrateDB monitoring dashboard in Grafana|690x396](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/0e01a3f0b8fc61ae97250fdeb2fe741f34ac7422.png)

## Alternative implementations

If you decide to build your own dashboard or use an entirely different monitoring approach, we recommend still covering similar metrics as discussed in this article. The list below is a good starting point for troubleshooting most operational issues:

* CrateDB metrics (with example Prometheus queries based on the Crate JMX HTTP Exporter)
  * Thread pools rejected: `sum(rate(crate_threadpools{property="rejected"}[5m])) by (name)`
  * Thread pool queue size: `sum(crate_threadpools{property="queueSize"}) by (name)`
  * Thread pools active: `sum(crate_threadpools{property="active"}) by (name)`
  * Queries per second: `sum(rate(crate_query_total_count[5m])) by (query)`
  * Query error rate: `sum(rate(crate_query_failed_count[5m])) by (query)`
  * Average Query Duration over the last 5 minutes: `sum(rate(crate_query_sum_of_durations_millis[5m])) by (query) / sum(rate(crate_query_total_count[5m])) by (query)`
  * Circuit breaker memory in use: `sum(crate_circuitbreakers{property="used"}) by (name)`
  * Number of shards: `crate_node{name="shard_stats",property="total"}`
  * Garbage Collector rates: `sum(rate(jvm_gc_collection_seconds_count[5m])) by (gc)`
  * Thread pool rejected operations: `crate_threadpools{property="rejected"}`
* Operating system metrics
  * CPU utilization
  * Memory usage
  * Open file descriptors
  * Disk usage
  * Disk read/write operations and throughput
  * Received and transmitted network traffic

## Wrapping up

We got a Grafana dashboard that allows us to check live and historical data around performance and capacity metrics in our CrateDB cluster, this illustrates one possible setup. You could use different tools depending on your environment and preferences. Still, we recommend you use the interface of the Crate JMX HTTP Exporter to collect CrateDB-specific metrics and that you always also monitor the health of the environment at the OS level as we have done here with the Prometheus Node Exporter.


[CrateDB Cloud]: https://cratedb.com/products/cratedb-cloud
[Grafana]: https://grafana.com/
[grafana-debian]: https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/
[Prometheus]: https://prometheus.io/
