(import)=
(ingest)=
(load)=
# Load data into CrateDB

:::{div} sd-text-muted
Data ingestion / loading / import methods for CrateDB at a glance.
:::

:::{toctree}
:maxdepth: 2
:hidden:

fdw
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

Additional data import methods provided by CrateDB Cloud.

:{ref}`Import files <cluster-import>`:

  Managed data loading from remote sources using CrateDB Cloud's ETL services.

  **Protocols:** HTTP, Blob Storage (AWS S3, Azure)
  <br>
  **Formats:** CSV, JSON Lines, Parquet

:{ref}`MongoDB CDC integration <integrations-mongo-cdc>`:

  CrateDB Cloud enables continuous data ingestion from MongoDB using Change Data Capture
  (CDC), providing seamless, real-time synchronization of your data.

## {material-outlined}`arrow_circle_up;1.5em` Using external systems

Supported industry-standard applications, frameworks, and systems
for one-shot and continuous / streaming data imports.

:{ref}`Extract Transform Load (ETL) <etl>`:

  Ingest data with polyglot data integration platforms or libraries
  and complete ETL solutions.

:{ref}`cdc`:

  Integrate with third-party change-data-capture (CDC) tools.

:{ref}`telemetry`:

  Ingest telemetry data—metrics, logs, and traces—from monitoring
  and sensor collector systems.

  Store metrics and telemetry data for the long term, with the benefits of
  using standard database interfaces, SQL query language, and horizontal
  scalability through clustering as you go.

  **What's inside:**
  Never retire old records to cold storage,
  always have them ready for historical analysis.
