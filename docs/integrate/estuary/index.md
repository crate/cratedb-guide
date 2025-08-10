(estuary)=

# Estuary

```{div}
:style: "float: right"
[![Estuary logo](https://estuary.dev/static/estuary-430cce9313e0df82d11e40d8285f38b4.png){h=60px}][Estuary]
```
```{div}
:style: "clear: both"
```

:::{rubric} About
:::

[Estuary] provides real-time data integration and modern ETL and ELT data pipelines.
Build scalable, fault-tolerant streaming data pipelines that seamlessly connect
to virtually any data source for data warehouses, real-time analytics, operations,
machine learning, and AI.

:::{dropdown} **Details**
Estuary Flow is a real-time, reliable change data capture
(CDC) solution. It combines agentless CDC, zero-code pipelines,
and enterprise-grade governance to simplify data integration,
and drive business agility at a fraction of the cost of other
vendors, bearing a few excellent features:

- Move and transform data across 200+ systems
- Sub-100ms end-to-end latency
- Reliable delivery via exactly-once guarantees
- Flexible pipelines that run at your speed of choice
- Fully automated schema evolution
- Ability to maintain a current view or all change history in the destination
- Truly elastic scaling pipelines for maximum throughput
- Batch-load for analytics, and stream for ops and AI

![Estuary connectors](https://estuary.dev/static/f6d26b4e4c7ed825e241372f4c3d8804/9b7d3/real-time-graphic.webp){h=200px}

> Build low-latency ETL and ELT pipelines using connectors for any database
> or data warehouse, leveraging Change Data Capture (CDC) to power your
> analytics, operations, and AI.
:::

:::{dropdown} **Managed Estuary**
Estuary offers its solution as a [managed product][Estuary managed], available
per [three main deployment options][Estuary Deployment] to cater to various
organizational needs and security requirements: Public Deployment,
Private Deployment, and BYOC options.
:::


:::{rubric} Start
:::

::::{grid} 2
:gutter: 2

:::{grid-item-card}
:link: https://estuary.dev/destination/cratedb/
:link-type: url
:link-alt: "CrateDB destination connector for Estuary"
:padding: 3
:class-card: sd-text-center sd-pt-4
:class-header: sd-fs-6
:class-footer: text-smaller
CrateDB destination connector for Estuary
^^^
{material-outlined}`link;4.5em`
+++
Continuously ingest and deliver both streaming and batch change data from
100s of sources using Estuary's custom no-code connectors into CrateDB.
:::

::::


:::{rubric} Learn
:::

::::{grid} 2
:gutter: 2

:::{grid-item-card}
:link: https://estuary.dev/blog/the-complete-introduction-to-change-data-capture-cdc/
:link-type: url
:link-alt: "Change Data Capture (CDC): The Complete Guide"
:padding: 3
:class-card: sd-text-center sd-pt-4
:class-header: sd-fs-6
:class-footer: text-smaller
CDC: The Complete Guide
^^^
{material-outlined}`integration_instructions;4.5em`
+++
Understand what Change Data Capture (CDC) is, how it works, and when to use it.
Compare top CDC tools like Estuary, Debezium, Fivetran & more.
:::

:::{grid-item-card}
:link: https://github.com/crate/cratedb-estuary
:link-type: url
:link-alt: "Connector Repository"
:padding: 3
:class-card: sd-text-center sd-pt-4
:class-header: sd-fs-6
:class-footer: text-smaller
Connector Repository
^^^
{material-outlined}`source;4.5em`
+++
Issue tracker repository.
:::

::::

:::{note}
We are tracking interoperability issues per [Tool: Estuary] and appreciate
any contributions and reports.
:::


[Estuary]: https://estuary.dev/
[Estuary Managed]: https://estuary.dev/product/
[Estuary Deployment]: https://estuary.dev/deployment-options/
[Tool: Estuary]: https://github.com/crate/crate/labels/tool%3A%20Estuary
