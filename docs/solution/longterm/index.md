(longterm-store)=
(timeseries-longterm)=
(timeseries-long-term-storage)=

# Long-term store

:::{div} sd-text-muted
Never retire data just because your other systems can't handle the cardinality.
:::

CrateDB stores large volumes of data, keeping it accessible for querying
and insightful analysis, even considering historic data records.

Many organizations need to retain data for years or decades to meet regulatory
requirements, support historical analysis, or preserve valuable insights for
future use. However, traditional storage systems force you to choose between
accessibility and affordability, often leading to data exports, archival
systems, or downsampling that sacrifice query capabilities.

CrateDB eliminates this trade-off by storing large volumes of data efficiently
while keeping it fully accessible for querying and analysis. Unlike systems
that struggle with high cardinality or require expensive tiered architectures,
CrateDB handles billions of unique records in a single platform, maintaining
fast query performance even on historic datasets spanning years.

By keeping all your data in one place, you avoid the complexity and costs of
exporting to specialized long-term storage systems, data lakes, or cold storage
tiers. Your historical data remains as queryable as your recent data, enabling
seamless analysis across any time range without data movement, ETL pipelines,
or rehydration processes.

With CrateDB, compatible to PostgreSQL, you can do all of that using plain SQL.
Other than integrating well with commodity systems using standard database
access interfaces like ODBC or JDBC, it provides a proprietary HTTP interface
on top.

## Use cases

:::{rubric} Metrics and monitoring
:::

::::{grid} 1 1 1 2
:gutter: 2
:padding: 0

:::{grid-item-card} Prometheus
:link: prometheus
:link-type: ref
Prometheus and similar monitoring systems excel at real-time alerting but face challenges
with long-term metric retention due to storage costs and query performance at scale. CrateDB
addresses these challenges by providing:
- **Scalable long-term storage**: Store years of metrics without compromising query performance.
- **High cardinality support**: Handle millions of unique label combinations that would overwhelm traditional TSDBs.
- **Rich SQL analytics**: Perform complex analytical queries on historic metrics using standard SQL.
- **Seamless integration**: Use CrateDB's Prometheus Adapter for transparent remote write/read operations.
+++
Set up CrateDB as a long-term metrics store for Prometheus.
:::

:::{grid-item-card} OpenTelemetry
:link: opentelemetry
:link-type: ref
OpenTelemetry and similar observability frameworks excel at generating rich telemetry data
but face challenges with long-term retention due to storage scale and query complexity.
CrateDB addresses these challenges by providing:
- **Scalable long-term storage**: Store large volumes of telemetry through CrateDB's distributed architecture.
- **Vendor-neutral ingestion**: Use OpenTelemetry SDKs/agents and Telegraf to send telemetry into your CrateDB observability pipeline.
- **Rich SQL analytics**: Run SQL/time-series queries, aggregations and joins on telemetry data for troubleshooting and analytics.
- **Flexible attribute mapping**: Customize which span/log/profile attributes become columns/tags for dimensional queries.
+++
Set up CrateDB as a long-term observability backend for OpenTelemetry.
:::

::::

## Tools

### Automatic retention and expiration

When operating a system storing and processing large amounts of data,
it is crucial to manage data flows and life-cycles well, which includes
handling concerns of data expiry, size reduction, and archival.

Optimally, corresponding tasks are automated rather than manually
performed. CrateDB provides relevant integrations and standalone
applications for automatic data retention purposes.

:::{rubric} Apache Airflow
:::

{ref}`Build a hot/cold storage data retention policy <airflow-data-retention-hot-cold>`
describes how to manage aging data by leveraging CrateDB cluster
features to mix nodes with different hardware setups, i.e. hot
nodes using the latest generation of NVMe drives for responding
to analytics queries quickly, and cold nodes that have access to
cheap mass storage for retaining historic data.

:::{rubric} CrateDB Toolkit
:::

[CrateDB Toolkit Retention and Expiration] is a data retention and
expiration policy management system for CrateDB, providing multiple
retention strategies.

:::{note}
The system derives its concepts from [InfluxDB data retention] ideas and
from the {ref}`Airflow-based data retention tasks for CrateDB <airflow-data-retention-policy>`,
but aims to be usable as a standalone system in different software environments.
Effectively, it is a Python library and CLI around a policy management
table defined per [retention-policy-ddl.sql].
:::

## Related sections

{ref}`metrics-store` includes information about how to
store and analyze high volumes of system monitoring information
like metrics and log data with CrateDB.

{ref}`analytics` describes how
CrateDB provides real-time analytics on raw data stored for the long term.
Keep massive amounts of data ready in the hot zone for analytics purposes.

[Optimizing storage efficiency for historic time series data]
illustrates how to reduce table storage size by 80%,
by using arrays for time-based bucketing, a historical table having
a dedicated layout, and querying using the UNNEST table function.

{ref}`weather-data-storage` provides information about how to
use CrateDB for mass storage of synoptic weather observations,
allowing you to query them efficiently.


[CrateDB Toolkit Retention and Expiration]: https://cratedb-toolkit.readthedocs.io/retention.html
[InfluxDB data retention]: https://docs.influxdata.com/influxdb/v1/guides/downsample_and_retain/
[Optimizing storage efficiency for historic time series data]: https://community.cratedb.com/t/optimizing-storage-for-historic-time-series-data/762
[retention-policy-ddl.sql]: https://github.com/crate/cratedb-toolkit/blob/main/cratedb_toolkit/retention/setup/schema.sql
