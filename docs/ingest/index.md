(ingest)=
# CrateDB data ingestion

:::{div} sd-text-muted
Data ingestion / loading / import methods for CrateDB at a glance.
:::

:::{toctree}
:maxdepth: 2
:hidden:

etl/index
cdc/index
telemetry/index
:::

## {material-outlined}`file_upload;1.5em` Using CrateDB

Data import methods supported by CrateDB natively.

:{ref}`Import files <sql-copy-from>`:

  Load data from the local filesystem or from remote sources using CrateDB's
  native `COPY FROM` SQL statement.

  **Protocols:** HTTP, FTP, Blob Storage (AWS S3, Azure)
  <br>
  **Formats:** CSV, JSON Lines

:{ref}`fdw`:

  Make data in remote database servers available as tables within CrateDB.
  You can then query these foreign tables like regular user tables.

## {material-outlined}`cloud_upload;1.5em` Using CrateDB Cloud

Data import methods provided by CrateDB Cloud.

:{ref}`Import files <cluster-import>`:

  Managed data loading from remote sources using CrateDB Cloud's ETL services.

  **Protocols:** HTTP, Blob Storage (AWS S3, Azure)
  <br>
  **Formats:** CSV, JSON Lines, Parquet

:{ref}`MongoDB CDC integration <integrations-mongo-cdc>`:

  CrateDB Cloud enables continuous data ingestion from MongoDB using Change Data Capture
  (CDC), providing seamless, real-time synchronization of your data.

## {material-outlined}`arrow_circle_up;1.5em` Using external systems

Supported industry-standard systems and frameworks.

:{ref}`Extract Transform Load (ETL) <etl>`:

  Ingest data with polyglot data integration platforms or libraries
  and complete ETL solutions.

:{ref}`cdc`:

  Integrate with third-party change-data-capture (CDC) tools.

:{ref}`telemetry`:

  Ingest telemetry data—metrics, logs, and traces—from monitoring
  and sensor collector systems.
