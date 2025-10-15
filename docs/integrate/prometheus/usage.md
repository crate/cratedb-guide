(prometheus-usage)=
# Store Prometheus long-term metrics into CrateDB

This usage guide shows how to use Docker Compose to run the services
CrateDB, Prometheus, and the [CrateDB Prometheus Adapter].

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`
- {download}`cratedb-prometheus-adapter.yaml`
- {download}`ddl.sql`
- {download}`prometheus.yml`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

## Explore data

CrateDB stores the metrics in the designated table, ready for inspection and analysis.
```shell
docker compose exec cratedb crash -c "SELECT * FROM testdrive.metrics ORDER BY timestamp LIMIT 5;"
```

## Screenshots

Navigate to `http://localhost:9090` to open the Prometheus UI. Go to **Status** → **Targets**.

![Prometheus Targets page showing the self-scrape target as UP](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/91223397b30bce2f7188617436ea12ceed83d83c.png)

Confirm that Prometheus monitors itself.

![Prometheus target details for the self-scrape job](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/57ccb5374b0ab524466de08feefbafde559dac87.png)

Return to the CrateDB Admin UI and select the `metrics` table you created.

After a few minutes, Prometheus will have gathered a few thousands of data points.

![CrateDB Admin UI showing the populated metrics table](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/22e8c7d5a90ec9240a4cb4269774e143759aa92e.jpeg)

Use CrateDB’s query engine to analyze and visualize this data with tools
like {ref}`grafana`, see also
[Monitoring a self-managed CrateDB cluster with Prometheus and Grafana].


[CrateDB]: https://cratedb.com/database
[CrateDB Prometheus Adapter]: https://github.com/crate/cratedb-prometheus-adapter
[Docker Compose]: https://docs.docker.com/compose/
[Docker containers]: https://www.docker.com/resources/what-container
[Docker installation guide]: https://docs.docker.com/get-docker/
[Monitoring a self-managed CrateDB cluster with Prometheus and Grafana]: https://community.cratedb.com/t/monitoring-a-self-managed-cratedb-cluster-with-prometheus-and-grafana/1236
[Prometheus]: https://prometheus.io/docs/introduction/overview/
[Prometheus documentation]: https://prometheus.io/docs/prometheus/latest/getting_started/
