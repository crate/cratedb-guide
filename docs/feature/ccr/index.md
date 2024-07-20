(replication)=
# Cross-Cluster Replication

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

:::{rubric} Overview
:::
Cross-cluster replication, also called logical replication, is a method of data
replication across multiple clusters.

:::{rubric} About
:::
CrateDB uses a "publish and subscribe" model where subscribers pull data from
the publications of the publisher they subscribed to.

:::{rubric} Details
:::
Logical replication is useful for different use cases.

- Consolidating data from multiple clusters into a single one
  for aggregated reports.
- Ensure high availability if one cluster becomes unavailable.
- Replicating between different compatible versions of CrateDB.
  Replicating tables created on a cluster with higher major/minor
  version to a cluster with lower major/minor version is not supported.
::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Reference Manual
:::
- {ref}`crate-reference:administration-logical-replication`
:::{rubric} SQL Functions
:::
- {ref}`crate-reference:sql-create-publication`
- {ref}`crate-reference:sql-alter-publication`
- {ref}`crate-reference:sql-drop-publication`
- {ref}`crate-reference:sql-create-subscription`
- {ref}`crate-reference:sql-drop-subscription`
:::{rubric} System Tables
:::
- {ref}`crate-reference:pg_publication`
- {ref}`crate-reference:pg_publication_tables`
- {ref}`crate-reference:pg_subscription`
- {ref}`crate-reference:pg_subscription_rel`

{tags-primary}`SQL`
{tags-primary}`Logical Replication`
::::

:::::


## Synopsis
Create a publication others can subscribe to.
```sql
CREATE PUBLICATION temperature_publication FOR TABLE doc.temperature_data;
```
Verify publication has been created.
```sql
SELECT * FROM pg_publication;
```
Create a subscription.
```sql
CREATE SUBSCRIPTION temperature_subscription
CONNECTION 'crate://cratedb.example.net:5432?user=crate&mode=pg_tunnel'
PUBLICATION temperature_publication;
```
Verify operational status of subscription.
```sql
SELECT subname, r.srrelid::TEXT, srsubstate, srsubstate_reason
FROM pg_subscription s
LEFT JOIN pg_subscription_rel r ON s.oid = r.srsubid;
```


## Learn

Learn how to set up logical replication between CrateDB clusters.

::::{grid} 2 2 2 2
:padding: 0

:::{grid-item-card}
:link: guide:logical_replication_setup
:link-type: ref
:link-alt: Logical replication setup between CrateDB clusters
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold
:class-body: sd-text-center2 sd-fs2-5
:class-footer: text-smaller
Logical replication using Docker
^^^
- Hands-on tutorial exercising publishing and subscribing end-to-end.
- Uses a workstation setup based on two instances running on Docker or Podman.
+++
How to configure logical replication on standalone clusters.
:::

:::{grid-item-card}
:link: cloud:logical-replication
:link-type: ref
:link-alt: Logical replication setup on CrateDB Cloud
:padding: 3
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold
:class-body: sd-text-center2 sd-fs2-5
:class-footer: text-smaller
Logical replication on CrateDB Cloud
^^^
- Notes about configuring the feature in the context of Cloud clusters.
- It mostly works out of the box.
+++
How to configure logical replication on CrateDB Cloud clusters.
:::

::::
