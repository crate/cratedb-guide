(ingest)=
# CrateDB data ingestion

:::{include} /_include/styles.html
:::

All data ingest methods for CrateDB at a glance.

:::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`lightbulb;2em` Loading data from external sources

- {ref}`ingest-file`
  
  Load data from CSV, JSON, and Parquet files.

- {ref}`Extract Transform Load (ETL) <etl>`
  
  Ingest data with polyglot data integration platforms or libraries
  and complete ETL solutions.

- {ref}`cdc`
  
  Use a variety of options to connect and integrate with 3rd-party
  change-data-capture (CDC) applications.

- {ref}`telemetry`
  
  Ingest telemetry data, i.e. metrics, logs, and traces originating from
  monitoring- or sensor collector systems.

- {ref}`fdw`
  
  Make data in remote database servers
  available as tables within CrateDB. You can then query these foreign
  tables like regular user tables.

+++
Suported data source types when importing data into CrateDB.
::::

:::::
