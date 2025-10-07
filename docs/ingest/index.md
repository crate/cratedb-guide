(ingest)=
# CrateDB data ingestion

:::{div} sd-text-muted
Data ingestion methods for CrateDB at a glance.
:::

:::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2
:class-container: ul-li-wide

::::{grid-item-card} {material-outlined}`file_upload;2em` Load data using CrateDB
- {ref}`Import files <crate-reference:sql-copy-from>`

  Load data from the local filesystem or from remote sources using CrateDB's
  native `COPY FROM` SQL statement.

  **Protocols:** HTTP, FTP, Blob Storage (AWS S3, Azure)
  <br>
  **Formats:** CSV, JSON Lines

- {ref}`fdw`

  Make data in remote database servers available as tables within CrateDB.
  You can then query these foreign tables like regular user tables.
+++
Data import methods supported by CrateDB natively.
::::

::::{grid-item-card} {material-outlined}`cloud_upload;2em` Load data using CrateDB Cloud
- {ref}`Import files <cloud:cluster-import>`

  Managed data loading from remote sources using CrateDB Cloud's ETL subsystem.

  **Protocols:** HTTP, Blob Storage (AWS S3, Azure)
  <br>
  **Formats:** CSV, JSON Lines, Parquet

- {ref}`MongoDB CDC integration <cloud:integrations-mongo-cdc>`

  CrateDB Cloud enables continuous data ingestion from MongoDB using Change Data Capture
  (CDC), providing seamless, real-time synchronization of your data.
+++
Data import methods provided by CrateDB Cloud.
::::

::::{grid-item-card} {material-outlined}`arrow_circle_up;2em` Load data using external systems
- {ref}`Extract Transform Load (ETL) <etl>`

  Ingest data with polyglot data integration platforms or libraries
  and complete ETL solutions.

- {ref}`cdc`

  Integrate with third-party change-data-capture (CDC) tools.

- {ref}`telemetry`

  Ingest telemetry data—metrics, logs, and traces—from monitoring
  and sensor collector systems.

+++
Supported industry-standard frameworks and paradigms.
::::

:::::


```{toctree}
:maxdepth: 2
:hidden:

etl/index
cdc/index
telemetry/index
```
