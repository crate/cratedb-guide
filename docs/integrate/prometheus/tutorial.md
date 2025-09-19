(prometheus-tutorial)=
# Storing long-term metrics with Prometheus in CrateDB

This tutorial shows how to:

* Set up Docker Compose to run CrateDB, Prometheus, and the CrateDB Prometheus Adapter
* Run the applications with Docker Compose

:::{note}
These examples use CrateDB 4.7.0, Prometheus 2.33.3, and the CrateDB Prometheus Adapter 0.5.8.
:::

## Motivation

[Prometheus] is a monitoring system that collects metrics from applications and
infrastructure. It focuses on ingesting large volumes of concise time‑series
events—timestamped points with key‑value labels.

This data helps you track a system’s state and trajectory. Many Prometheus users
want to retain it long term.

[CrateDB] helps here. With the [CrateDB Prometheus Adapter], you can store metrics
in CrateDB and use its fast ingestion and query performance to scale Prometheus.

## Set up Docker Compose

Run CrateDB, Prometheus, and the CrateDB Prometheus Adapter as [Docker containers].
Use [Docker Compose] to centralize container management so you can build and run
all containers with one command and define their connections in a YAML file.

Install Docker by following the [Docker installation guide].

Create a directory on your machine to host the configuration files.
Create three YAML files with your preferred editor and save them with the `.yml` extension.

### Create `docker-compose.yml`

Create `docker-compose.yml` to configure the three containers.
Define services for CrateDB, Prometheus, and the adapter. Mount `config.yml`
and `prometheus.yml` into the adapter and Prometheus containers, respectively.
You will create these files in the following steps.
```yaml
services:
  cratedb:
    image: "crate:4.7.0"
    ports:
      - "4200:4200"
      - "5432:5432"
    volumes:
      - cratedb-data:/data
    restart: unless-stopped
  prometheus:
    image: "prom/prometheus:v2.33.3"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
    restart: unless-stopped
  cratedb-prometheus-adapter:
    image: "ghcr.io/crate/cratedb-prometheus-adapter:0.5.8"
    volumes:
      - ./config.yml:/etc/cratedb-prometheus-adapter/config.yml
    ports:
      - "9268:9268"
    depends_on:
      - cratedb
      - prometheus
    restart: unless-stopped
volumes:
  cratedb-data:
```

### Create `prometheus.yml`

Next, create `prometheus.yml` following the [Prometheus documentation].
This file defines the services that Prometheus scrapes.

To keep it simple, monitor Prometheus itself.

To forward samples to CrateDB, set `remote_write` and `remote_read` to the adapter URL (see the [CrateDB Prometheus Adapter setup](https://github.com/crate/cratedb-prometheus-adapter)).

Because the adapter runs in Docker, use the adapter service name from `docker-compose.yml` (`cratedb-prometheus-adapter`) instead of `localhost` in the URLs.

Use the following `prometheus.yml`:
```yaml
global:
  scrape_interval:     15s # By default, scrape targets every 15 seconds.

  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
    monitor: 'codelab-monitor'

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any time-series scraped from this config.
  - job_name: 'prometheus'

    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 5s

    static_configs:
      - targets: ['prometheus:9090']

remote_write:
  - url: http://cratedb-prometheus-adapter:9268/write
remote_read:
  - url: http://cratedb-prometheus-adapter:9268/read
```
### Create `config.yml`

Finally, create `config.yml` following the [CrateDB Prometheus Adapter].
This file defines the CrateDB endpoints that the adapter writes to.

Set the host to `cratedb` (the service name in `docker-compose.yml`) instead of `localhost`. Keep the remaining variables at their defaults.
```yaml
cratedb_endpoints:
- host: "cratedb"           # Host to connect to (default: "localhost")
  port: 5432                # Port to connect to (default: 5432).
  user: "crate"             # Username to use (default: "crate")
  password: ""              # Password to use (default: "").
  schema: ""                # Schema to use (default: "").
  connect_timeout: 10       # TCP connect timeout (seconds) (default: 10).
  max_connections: 5        # The maximum number of concurrent connections (default: 5).
  enable_tls: false         # Whether to connect using TLS (default: false).
  allow_insecure_tls: false # Whether to allow insecure / invalid TLS certificates (default: false).
```
Place `docker-compose.yml`, `config.yml`, and `prometheus.yml` in the same directory on your machine.

## Start the services

Finally, navigate to your CrateDB–Prometheus directory and start Docker Compose:
```shell
cd /Users/Path/To/Directory/CrateDB-Prometheus
docker-compose up
```

After Docker Compose starts, open the CrateDB Admin UI at `http://localhost:4200`
and create a `metrics` table to store metrics gathered by Prometheus.
```sql
CREATE TABLE "metrics" (
    "timestamp" TIMESTAMP,
    "labels_hash" STRING,
    "labels" OBJECT(DYNAMIC),
    "value" DOUBLE,
    "valueRaw" LONG,
    "day__generated" TIMESTAMP GENERATED ALWAYS AS date_trunc('day', "timestamp"),
    PRIMARY KEY ("timestamp", "labels_hash", "day__generated")
  ) PARTITIONED BY ("day__generated")
```

Navigate to `http://localhost:9090` to open the Prometheus UI. Go to **Status** → **Targets**.

![Prometheus Targets page showing the self-scrape target as UP](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/91223397b30bce2f7188617436ea12ceed83d83c.png)

Confirm that Prometheus monitors itself.

![Prometheus target details for the self-scrape job](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/57ccb5374b0ab524466de08feefbafde559dac87.png)

Return to the CrateDB Admin UI and select the `metrics` table you created.

After a few minutes, Prometheus will have gathered hundreds of thousands of data points.

![CrateDB Admin UI showing the populated metrics table](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/22e8c7d5a90ec9240a4cb4269774e143759aa92e.jpeg)

Use CrateDB’s query engine to analyze and visualize this data with tools
like {ref}`grafana`.

Explore these related tutorials:

* [Visualizing time‑series data with Grafana and CrateDB](https://cratedb.com/blog/visualizing-time-series-data-with-grafana-and-cratedb)
* [Monitoring CrateDB with Prometheus and Grafana](https://cratedb.com/blog/monitoring-cratedb-with-prometheus-and-grafana)


[CrateDB]: https://cratedb.com/database
[CrateDB Prometheus Adapter]: https://github.com/crate/cratedb-prometheus-adapter
[Docker Compose]: https://docs.docker.com/compose/
[Docker containers]: https://www.docker.com/resources/what-container
[Docker installation guide]: https://docs.docker.com/get-docker/
[Prometheus]: https://prometheus.io/docs/introduction/overview/
[Prometheus documentation]: https://prometheus.io/docs/prometheus/latest/getting_started/
