(mongodb)=
# MongoDB

:::{include} /_include/links.md
:::

:::{rubric} About
:::

:::{div}
[MongoDB] is a document database designed for ease of application development and scaling.
[MongoDB Atlas] is a multi-cloud database service by the same people who build MongoDB.
Atlas simplifies deploying and managing your databases while offering the versatility
you need to build resilient and performant global applications on the cloud providers
of your choice.
:::

:::{rubric} Learn
:::

:::{div}
Explore support for loading [MongoDB collections and databases] into CrateDB (`full-load`),
and [MongoDB Change Streams], to relay CDC events from MongoDB into CrateDB (`cdc`).
:::

:::{list-table}
:header-rows: 1
:widths: auto

*   - Feature
    - CrateDB
    - CrateDB Cloud
    - Description 
*   - [MongoDB Table Loader]
    - ✅
    - ✅
    - CLI `ctk load table` for loading collections into CrateDB (`full-load`).
      Tutorial: {ref}`import-mongodb`
*   - [MongoDB CDC Relay]
    - ✅
    - ✅
    - CLI `ctk load table` for streaming changes of collections into CrateDB (`cdc`).
*   - {ref}`MongoDB CDC integration <cloud:integrations-mongo-cdc>`
    - ❌
    - ✅
    - Managed data loading from MongoDB and MongoDB Atlas into CrateDB Cloud
      (`full-load` and `cdc`), including advanced data translation and compensation
      strategies.
:::

:::{toctree}
:maxdepth: 1
:hidden:
learn
:::
