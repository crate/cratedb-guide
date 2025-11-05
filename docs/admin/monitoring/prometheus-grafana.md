(monitoring-prometheus-grafana)=
# Monitoring a CrateDB cluster with Prometheus and Grafana

:::{div} sd-text-muted
:::

:::{rubric} Introduction
:::

We recommend [^standalone] pairing two standard observability tools:
Use [Prometheus] to collect and store metrics,
and [Grafana] to build dashboards.

This guide describes how to set up a Grafana dashboard that allows you
to check live and historical data around performance and capacity
metrics in your CrateDB cluster. It uses instructions suitable for
Debian or Ubuntu Linux, but can be adapted for other Linux distributions.

[^standalone]: {ref}`Containerized <install-container>` and [CrateDB Cloud] setups differ.
  This tutorial targets standalone and on‑premises installations.

:::{rubric} Overview
:::

For a CrateDB environment, you are interested in CrateDB-specific metrics,
such as the number of shards or number of failed queries, and OS metrics,
such as available disk space, memory usage, or CPU usage.
Based on Prometheus, the monitoring stack uses the following exporters
to fulfill those requirements.

:Node Exporter:

  Exposes a wide variety of hardware and kernel related metrics.

:JMX Exporter:

  Consumes metrics information from CrateDB's
  JMX collectors and exposes them via HTTP so they can be scraped by Prometheus.

:SQL Exporter:

  Allows running arbitrary SQL
  statements against a CrateDB cluster to retrieve additional
  information from CrateDB's system tables.

## Set up CrateDB cluster

First things first, you will need a CrateDB cluster.
{ref}`Multi-node setup instructions <multi-node-setup-example>` provides
a quick walkthrough for Ubuntu Linux.

## Set up Prometheus Exporters

The Node Exporter and the JMX Exporter need to be installed on all
machines that are running CrateDB nodes.

1. Install the Prometheus Node Exporter.
   ```shell
   apt install prometheus-node-exporter
   ```

2. Install the {ref}`prometheus-jmx-exporter`.

## Set up Prometheus

You would typically run this on a machine that is not part of the
CrateDB cluster.
The {ref}`prometheus-sql-exporter` also does not need to be installed
on each machine.

```shell
apt install prometheus prometheus-sql-exporter --no-install-recommends
```

For advanced configuration options, see {ref}`prometheus-auth` and
{ref}`prometheus-storage`.

Now, configure Prometheus to scrape metrics from Node Exporters and
JMX Exporters on all CrateDB nodes, and also metrics from the SQL
Exporter.
```shell
nano /etc/prometheus/prometheus.yml
```

:Node Exporter: Port 9100
:JMX Exporter: Port 8080
:SQL Exporter: Port 9237

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

Restart the Prometheus daemon if it was already started.
```shell
systemctl restart prometheus
```

## Set up Grafana

Install Grafana on the same machine where you installed Prometheus.
On a Debian or Ubuntu machine, run the following:
```shell
apt install --yes wget gpg
wget -q -O - https://packages.grafana.com/gpg.key | gpg --dearmor | tee /usr/share/keyrings/grafana.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/grafana.gpg] https://packages.grafana.com/oss/deb stable main" | tee /etc/apt/sources.list.d/grafana.list
apt update
apt install --yes grafana
```
Then, start Grafana.
```shell
systemctl start grafana-server
```
For other systems, please refer to the [Grafana installation documentation][grafana-debian].

:::{rubric} Data source
:::

Navigate to `http://<grafana-host>:3000/` to access the Grafana login screen.
The default credentials are `admin`/`admin`; change the password immediately.
Navigate to "Add your first data source", then select "Prometheus" and set the
URL to `http://<prometheus-host>:9090/`.
If you configured basic authentication for Prometheus, this is where you
would need to enter the credentials.
Confirm using "Save & test".

:::{rubric} Dashboard
:::

An example dashboard based on the discussed setup is available for easy importing
from [Grafana » CrateDB Monitoring Dashboard].
In your Grafana installation, on the left-hand side, hover over the “Dashboards”
icon and select “Import”. Specify the dashboard ID **17174** and load the dashboard.
On the next screen, finalize the setup by selecting the previously created
Prometheus data source.

![CrateDB monitoring dashboard in Grafana|690x396](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/0e01a3f0b8fc61ae97250fdeb2fe741f34ac7422.png){width=690px}

## Alternative implementations

If you decide to build your own dashboard or use an entirely different monitoring
approach, we recommend still covering similar metrics as discussed in this article.
The list below is a good starting point for troubleshooting most operational issues.

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

## Appendix

(prometheus-auth)=
:::{rubric} Prometheus authentication
:::

By default, Prometheus binds to port 9090 without authentication. Prevent
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

(prometheus-storage)=
:::{rubric} CrateDB as Prometheus storage
:::

For a large deployment where you also use Prometheus to monitor other systems,
you may also want to use a CrateDB cluster as the storage for all Prometheus
metrics. The {ref}`CrateDB Prometheus Adapter <prometheus>` achieves that.


[CrateDB Cloud]: https://cratedb.com/products/cratedb-cloud
[Grafana]: https://grafana.com/
[grafana-debian]: https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/
[Grafana » CrateDB Monitoring Dashboard]: https://grafana.com/grafana/dashboards/17174-cratedb-monitoring/
[Prometheus]: https://prometheus.io/
[Prometheus Node Exporter]: https://prometheus.io/docs/guides/node-exporter/
