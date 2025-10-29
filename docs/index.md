(index)=

# Welcome to CrateDB

<!--
NOTE: When adding or removing top-level entries in this toctree, you must also
update the corresponding hardcoded links in the theme's sidebartoc.html file:
https://github.com/crate/crate-docs-theme/blob/main/src/crate/theme/rtd/crate/sidebartoc.html

Look for the "Section A: Guide" section in the {% else %} branch.
-->

```{toctree}
:hidden:

start/index
handbook/index
```

CrateDB is a **distributed SQL database** designed for **real-time analytics,
search and AI** at scale. Whether you are working with time series data, full-text
search, or large volumes of structured and semi-structured data, CrateDB gives
you the **power of SQL**, the **scalability of NoSQL**, and the **flexibility
of a modern data platform**.

See our [product overview] and {ref}`features overview <features>` to learn
more about high-level features and use cases.

This documentation is about helping you get started, explore in practice, and
operate in details.

::::{grid} 2 2 2 3
:gutter: 3

:::{grid-item-card}
:link: getting-started
:link-type: ref
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: sd-text-center sd-fs-5
:class-footer: text-smaller
Getting started
^^^
{material-outlined}`not_started;3.5em`
+++
Learn how to interact with the database for the first time.
:::

:::{grid-item-card}
:link: connect
:link-type: ref
:link-alt: CrateDB: Client Drivers and Libraries
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: sd-text-center sd-fs-5
:class-footer: text-smaller
Connect
^^^
{material-outlined}`link;3.5em`
+++
Database drivers, libraries, adapters, and connectors.
:::

:::{grid-item-card}
:link: integrate
:link-type: ref
:link-alt: Integrations
:class-header: sd-text-center sd-fs-5 sd-align-minor-center sd-font-weight-bold sd-text-capitalize
:class-body: sd-text-center sd-fs-5
:class-footer: text-smaller
Integrate
^^^
{material-outlined}`integration_instructions;3.5em`
+++
Integrate with third-party applications and frameworks.
:::

::::


:::{rubric} Start
:::

::::{grid} 2
:gutter: 3

:::{grid-item-card} {material-outlined}`not_started;1.7em` CrateDB Cloud
:link: https://console.cratedb.cloud/
:link-type: url
:link-alt: Getting started with CrateDB Cloud
:class-title: sd-fs-5

Start with a fully managed FREE FOREVER CrateDB instance to quickly explore
features through guided tutorials or on your own with custom data.
+++
```{button-ref} first-steps
:color: primary
:expand:
**Start with CrateDB Cloud**
```
:::

:::{grid-item-card} {material-outlined}`download_for_offline;1.7em` Install CrateDB
:link: install
:link-type: ref
:link-alt: Install CrateDB
:class-title: sd-fs-5

Install CrateDB on different operating systems and environments,
for on-premises operations and development purposes.
:::

::::



[Product overview]: https://cratedb.com/database
