(telegraf)=
# Telegraf

```{div} .float-right
[![Telegraf logo](https://github.com/crate/crate-clients-tools/assets/453543/3f0b4525-5344-42fe-bae6-1b0970fa0540){width=180px loading=lazy}][Telegraf]
```
```{div} .clearfix
```

:::{rubric} About
:::

[Telegraf] is a leading open source server agent to help you collect metrics
from your stacks, sensors, and systems. More than 200 adapters to connect
to other systems leaves nothing to be desired.

Telegraf is a server-based agent for collecting and sending all metrics and
events from databases, systems, and IoT sensors. Telegraf is written in Go
and compiles into a single binary with no external dependencies, and requires
a very minimal memory footprint.

:::{rubric} Overview
:::

::::{grid}

:::{grid-item}
- **IoT sensors**: Collect critical stateful data (pressure levels, temperature
  levels, etc.) with popular protocols like MQTT, ModBus, OPC-UA, and Kafka.

- **DevOps Tools and frameworks**: Gather metrics from cloud platforms,
  containers, and orchestrators like GitHub, Kubernetes, CloudWatch, Prometheus,
  and more.

- **System telemetry**: Metrics from system telemetry like iptables, Netstat,
  NGINX, and HAProxy help provide a full stack view of your apps.
:::

:::{grid-item}
![Telegraf architecture overview](https://www.influxdata.com/wp-content/uploads/Main-Diagram_06.01.2022v1.png){loading=lazy}
:::

::::


:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Tutorial: Use Telegraf with CrateDB
:link: telegraf-tutorial
:link-type: ref
How to configure Telegraf to submit metrics to CrateDB.
:::

:::{grid-item-card} Blog: Use CrateDB With Telegraf, an Agent for Collecting & Reporting Metrics
:link: https://cratedb.com/blog/use-cratedb-with-telegraf-an-agent-for-collecting-reporting-metrics
:link-type: url
Learn how to set up Telegraf, have Telegraf send metrics data to CrateDB,
and visualize the collected data with Grafana.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
:::

```{seealso}
[CrateDB and Telegraf]
```



[CrateDB and Telegraf]: https://cratedb.com/integrations/cratedb-and-telegraf
[Telegraf]: https://www.influxdata.com/time-series-platform/telegraf/
[Use CrateDB With Telegraf, an Agent for Collecting & Reporting Metrics]: https://cratedb.com/blog/use-cratedb-with-telegraf-an-agent-for-collecting-reporting-metrics
