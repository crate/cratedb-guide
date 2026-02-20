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

etl/index
cdc/index
telemetry/index
:::

## {material-outlined}`file_upload;1.5em` CrateDB Server

CrateDB natively supports data import using its {ref}`COPY FROM <sql-copy-from>`
SQL statement. It can load data in CSV and JSONL (NDJSON) formats from the local
filesystem or from remote sources (HTTP, FTP, Blob Storage).

CrateDB's {ref}`fdw` subsystem makes data in remote database servers available
as tables within CrateDB. You can then query these foreign tables like regular
user tables.

## {material-outlined}`cloud_upload;1.5em` CrateDB Cloud

CrateDB Cloud provides managed data loading from remote sources.

- Supports {ref}`file import <cluster-import>` in CSV, JSONL (NDJSON), and
  Parquet formats from HTTP and Blob Storage (AWS S3, Azure Storage, Google GCS).

- The {ref}`MongoDB CDC integration <integrations-mongo-cdc>`
  continuously ingests from MongoDB using Change Data Capture (CDC),
  providing near real-time synchronization of your data.

## {material-outlined}`arrow_circle_up;1.5em` Integrations

CrateDB integrates with a range of applications and frameworks
for one-shot and continuous / streaming data imports.

:{ref}`Extract Transform Load (ETL) <etl>`:

  Ingest data from many sources.

:{ref}`cdc`:

  Integrate with change-data-capture (CDC) systems.

:{ref}`telemetry`:

  Ingest telemetry data—metrics, logs, and traces—from monitoring
  and sensor collector systems.
