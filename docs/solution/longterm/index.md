(longterm)=
(longterm-store)=
(timeseries-longterm)=
(timeseries-long-term-storage)=

# Long-term store

:::{toctree}
:hidden:
retention
:::

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

With CrateDB, compatible with PostgreSQL, you can do all of that using plain SQL.
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

## Related sections

{ref}`metrics-store` includes information about how to
store and analyze high volumes of system monitoring information
like metrics and log data with CrateDB.

{ref}`analytics` describes how
CrateDB provides real-time analytics on raw data stored for the long term.
Keep massive amounts of data ready in the hot zone for analytics purposes.

{ref}`retention` illustrates how to optimally implement data retention
procedures, to manage the life-cycle of data stored in CrateDB, handling
concerns of data expiry, size reduction, and archival.

[Optimizing storage efficiency for historic time series data]
illustrates how to reduce table storage size by 80%,
by using arrays for time-based bucketing, a historical table having
a dedicated layout, and querying using the UNNEST table function.

{ref}`weather-data-storage` provides information about how to
use CrateDB for mass storage of synoptic weather observations,
allowing you to query them efficiently.


[Optimizing storage efficiency for historic time series data]: https://community.cratedb.com/t/optimizing-storage-for-historic-time-series-data/762
