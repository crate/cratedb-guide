(mongodb)=
# MongoDB

:::{include} /_include/links.md
:::

```{div} .float-right .text-right
[![MongoDB logo](https://upload.wikimedia.org/wikipedia/commons/9/93/MongoDB_Logo.svg){height=60px loading=lazy}][MongoDB]
<br>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/mongodb.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/mongodb.yml?branch=main&label=CTK%2BMongoDB" loading="lazy"></a>
```
```{div} .clearfix
```

:::::{grid}
:padding: 0

::::{grid-item}
:columns: auto 9 9 9

:::{rubric} About
:::

:::{div}
[MongoDB] is a document database designed for ease of application development and scaling.
[MongoDB Atlas] is a multi-cloud database service by the same people who build MongoDB.
Atlas simplifies deploying and managing your databases while offering the versatility
you need to build resilient and performant global applications on the cloud providers
of your choice.
:::

::::

::::{grid-item}
:columns: auto 3 3 3

:::{rubric} Related
:::
- [MongoDB collections and databases]
- [MongoDB Change Streams]

::::

:::::


:::{rubric} Managed
:::
MongoDB CDC is available as a managed service on CrateDB Cloud.

::::{grid}

:::{grid-item-card} MongoDB CDC integration
:link: cloud:integrations-mongo-cdc
:link-type: ref
Managed data loading from MongoDB and MongoDB Atlas into CrateDB Cloud
(`full-load` and `cdc`), including advanced data migration, translation
and compensation strategies.
:::

::::

:::{rubric} Standalone
:::
Data from MongoDB can also be loaded by other means.

::::{grid}

:::{grid-item-card} Tutorial: Import data from MongoDB
:link: mongodb-tutorial
:link-type: ref
How to load data from MongoDB Server and MongoDB Atlas into CrateDB.
:::

:::{grid-item-card} MongoDB Table Loader
:link: ctk:mongodb-loader
:link-type: ref
Standalone CLI `ctk load table` for loading MongoDB collections into CrateDB
(`full-load`), optionally using transformations.
:::

:::{grid-item-card} MongoDB CDC Relay
:link: ctk:mongodb-cdc-relay
:link-type: ref
Standalone CLI `ctk load table` for streaming changes of MongoDB collections
into CrateDB (`cdc`), optionally using transformations.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
cloud
model
:::


:::{seealso}
**Blog:** [Announcing MongoDB CDC Integration (Public Preview) in CrateDB Cloud]
:::

:::{note}
The MongoDB I/O component is based on the [migr8] migration utility package. Consult its
documentation for advanced capabilities when working with MongoDB.
:::


[Announcing MongoDB CDC Integration (Public Preview) in CrateDB Cloud]: https://cratedb.com/blog/announcing-mongodb-cdc-integration-public-preview-in-cratedb-cloud
[migr8]: https://cratedb-toolkit.readthedocs.io/io/mongodb/migr8.html
