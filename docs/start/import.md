(start-import)=
(start-ingest)=
# Importing data

:::{rubric} Features
:::

The platform supports loading data through native methods such as the
`COPY FROM` SQL statement, enabling import from local files or remote sources
including HTTP, FTP, and cloud storage providers like AWS S3 and Azure.

Supported formats for ingestion include CSV and JSON Lines, and CrateDB offers
features for both batch and incremental loads. Additionally, the Foreign Data
Wrapper feature allows you to access and query external databases as if they
were local tables, further expanding integration capabilities.

:::{rubric} Integrations
:::

The guide also highlights advanced options like using third-party tools and
connectors—such as ingestr—to migrate or synchronise data from a wide array
of traditional databases, cloud warehouses, message brokers, and file/object
storage systems.

These integrations help automate and streamline the ETL (extract, transform,
load) process, supporting use cases that range from one-time migrations to
continuous, real-time data pipelines. As a result, CrateDB is well-suited
for large-scale analytics, IoT, and time-series workloads that demand
seamless and flexible ingestion strategies.

:::{rubric} Next step
:::

:::{card}
:link: ingest
:link-type: ref
:width: 75%
:margin: auto
The data ingestion guide provides an overview of how to efficiently bring
data from various sources into CrateDB.
+++
```{button-ref} ingest
:color: primary
:expand:
All data ingestion methods for CrateDB at a glance
```
:::
