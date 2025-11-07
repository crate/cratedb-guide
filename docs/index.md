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

:::{rubric} Start
:::

::::{grid} 2
:gutter: 3

:::{grid-item-card} {material-outlined}`arrow_circle_right;1.7em` CrateDB Cloud
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

:::{rubric} Quick links
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {material-outlined}`not_started;2em` &nbsp; Getting started
:link: getting-started
:link-type: ref
Learn how to interact with the database for the first time.
::::

::::{grid-item-card} {material-outlined}`link;2em` &nbsp; Connect
:link: connect
:link-type: ref
Database drivers, libraries, adapters, and connectors.
::::

::::{grid-item-card} {material-outlined}`auto_stories;2em` &nbsp; Handbook
:link: handbook
:link-type: ref
Use CrateDB and CrateDB Cloud in practice.
::::

:::::

:::{rubric} Learn
:::

:::{card} All features
:link: all-features
:link-type: ref

CrateDB is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries. It is
based on Lucene, combines a unique set of features, and is PostgreSQL-compatible.

![CrateDB feature overview diagram](https://cratedb.com/hs-fs/hubfs/nativesql.png?width=800&name=nativesql.png)
+++
Read about all features of CrateDB at a glance.
:::



[Product overview]: https://cratedb.com/database
