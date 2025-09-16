(node-red)=
# Node-RED

```{div} .float-right
[![Node-RED logo](https://upload.wikimedia.org/wikipedia/commons/2/2b/Node-red-icon.png){height=60px loading=lazy}](https://nodered.org/)
```
```{div} .clearfix
```

:::{rubric} About
:::

[Node-RED] is a programming tool for wiring together hardware devices, APIs
and online services within a low-code programming environment for event-driven
applications. It allows orchestrating message flows and transformations through
an intuitive web interface.

It provides a browser-based editor that makes it easy to wire together flows
using the wide range of elements called "nodes" from the palette that can be
deployed to its runtime in a single-click.

:::{dropdown} **Managed Node-RED**
```{div}
:style: "float: right; margin: 0.5em"
[![FlowFuse logo](https://github.com/crate/crate-clients-tools/assets/453543/200d1a92-1e38-453a-89bf-d8b727451fab){width=180px}][FlowFuse]
```

With [FlowFuse], and [FlowFuse Cloud], essentially unmanaged and managed DevOps
for Node-RED, you can reliably deliver Node-RED applications in a continuous,
collaborative, and secure manner.

- **Collaborative Development:** FlowFuse adds team collaboration to Node-RED,
  allowing multiple developers to work together on a single instance. With
  FlowFuse, developers can easily share projects, collaborate in real-time and
  streamline workflow for faster development and deployment.
- **Manage Remote Deployments:** Many organizations deploy Node-RED instances to
  remote servers or edge devices. FlowFuse automates this process by creating
  snapshots on Node-RED instances that can be deployed to multiple remote targets.
  It also allows for rollback in cases where something might not have gone correctly.
- **Streamline Application Delivery:** FlowFuse simplifies the software development
  lifecycle of Node-RED applications. You can now set up DevOps delivery pipelines
  to support development, test and production environments for Node-RED application
  delivery, see [Introduction to FlowFuse].
- **Flexible FlowFuse Deployment:** We want to make it easy for you to use FlowFuse,
  so we offer FlowFuse Cloud, a managed cloud service, or a self-hosted solution.
  You have the freedom to choose the deployment method that works best for your
  organization.

```{div} .clearfix
```
:::


:::{rubric} Learn
:::

::::{grid} 2

:::{grid-item-card} Tutorial: Ingest MQTT
:link: node-red-tutorial
:link-type: ref
Ingesting MQTT messages into CrateDB using Node-RED.
:::

:::{grid-item-card} Tutorial: Recurrent queries
:link: https://community.cratedb.com/t/automating-recurrent-cratedb-queries/788
:link-type: url
Automating recurrent CrateDB queries using Node-RED.
:::

::::


```{seealso}
[CrateDB and Node-RED]
```

:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <mqtt-tutorial>
:::


[CrateDB and Node-RED]: https://cratedb.com/integrations/cratedb-and-node-red
[FlowFuse]: https://flowfuse.com/
[FlowFuse Cloud]: https://app.flowforge.com/
[Introduction to FlowFuse]: https://flowfuse.com/webinars/2023/introduction-to-flowforge/
[Node-RED]: https://nodered.org/
