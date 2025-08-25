(ingestr)=
# ingestr

```{div} .float-right .text-right
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-ingestr.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-ingestr.yml?branch=main&label=ingestr" loading="lazy" alt="CI status: ingestr"></a>
```
```{div} .clearfix
```

[ingestr] is a command-line application that allows copying data from any
source into any destination database. It supports CrateDB on the source
and the destination side. ingestr uses {ref}`dlt`.

::::{grid}

:::{grid-item}
- **Single command**: ingestr allows copying & ingesting data from any source
  to any destination with a single command.

- **Many sources & destinations**: ingestr supports all common source and
  destination databases.

- **Incremental Loading**: ingestr supports both full-refresh and
  incremental loading modes.
:::

:::{grid-item}
![ingestr in a nutshell](https://github.com/bruin-data/ingestr/blob/main/resources/demo.gif?raw=true){loading=lazy}
:::

::::


## Synopsis

Invoke ingestr for exporting data from CrateDB.
```shell
ingestr ingest \
    --source-uri 'crate://crate@localhost:4200/' \
    --source-table 'sys.summits' \
    --dest-uri 'duckdb:///cratedb.duckdb' \
    --dest-table 'dest.summits'
```

Invoke ingestr for loading data into CrateDB.
```shell
ingestr ingest \
   --source-uri 'csv://input.csv' \
   --source-table 'sample' \
   --dest-uri 'cratedb://crate:@localhost:5432/?sslmode=disable' \
   --dest-table 'doc.sample'
```

:::{note}
Please note there a subtle differences in the CrateDB source vs. target URL.
While `--source-uri=crate://...` addresses CrateDB's SQLAlchemy dialect,
`--dest-uri=cratedb://...` is effectively a PostgreSQL connection URL
with a protocol schema designating CrateDB. The source adapter uses
CrateDB's HTTP protocol, while the destination adapter uses CrateDB's
PostgreSQL interface.
:::


## Coverage

ingestr supports migration from 20-plus databases, data platforms, analytics
engines, including all [databases supported by SQLAlchemy].

:::{rubric} Databases
:::
Actian Data Platform, Vector, Actian X, Ingres, Amazon Athena, Amazon Redshift,
Amazon S3, Apache Drill, Apache Druid, Apache Hive and Presto, Apache Solr, 
Clickhouse, CockroachDB, CrateDB, Databend, Databricks, Denodo, DuckDB, EXASOL DB,
Elasticsearch, Firebird, Firebolt, Google BigQuery, Google Sheets, Greenplum, 
HyperSQL (hsqldb), IBM DB2 and Informix, IBM Netezza Performance Server, Impala, InfluxDB, 
Kinetica, Microsoft Access, Microsoft SQL Server, MonetDB, MongoDB, MySQL and MariaDB, 
OpenGauss, OpenSearch, Oracle, PostgreSQL, Rockset, SAP ASE, SAP HANA,
SAP Sybase SQL Anywhere, Snowflake, SQLite, Teradata Vantage, TiDB, YDB, YugabyteDB.

:::{rubric} Brokers
:::
Amazon Kinesis, Apache Kafka (Amazon MSK, Confluent Kafka, Redpanda, RobustMQ)

:::{rubric} File formats
:::
CSV, JSONL/NDJSON, Parquet

:::{rubric} Object stores
:::
Amazon S3, Google Cloud Storage

:::{rubric} Services
:::
Airtable, Asana, GitHub, Google Ads, Google Analytics, Google Sheets, HubSpot,
Notion, Personio, Salesforce, Slack, Stripe, Zendesk, etc.


## Learn

::::{grid}

:::{grid-item-card} Documentation: ingestr CrateDB source
:link: https://bruin-data.github.io/ingestr/supported-sources/cratedb.html#source
:link-type: url
Documentation about the CrateDB source adapter for ingestr.
:::

:::{grid-item-card} Documentation: ingestr CrateDB destination
:link: https://bruin-data.github.io/ingestr/supported-sources/cratedb.html#destination
:link-type: url
Documentation about the CrateDB destination adapter for ingestr.
:::

:::{grid-item-card} Examples: Use ingestr with CrateDB
:link: https://github.com/crate/cratedb-examples/tree/main/application/ingestr
:link-type: url
Executable code examples / rig that demonstrates how to use ingestr to
load data from Kafka to CrateDB.
:::

::::



[databases supported by SQLAlchemy]: https://docs.sqlalchemy.org/en/20/dialects/
[ingestr]: https://bruin-data.github.io/ingestr/
[sources supported by ingestr]: https://bruin-data.github.io/ingestr/supported-sources/
