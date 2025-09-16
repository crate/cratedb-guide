(start-performance)=
# Performance considerations

:::{div} sd-text-muted
Follow these tips to use CrateDB optimally for maximum performance.
:::

| Optimization                   | Description                                                                                                       | Documentation                                                                                                                                                                                                      |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Leverage indexes               | Important for frequently grouped or filtered fields. <br> Fields are indexed by default.                          | {ref}`performance-optimization`                                                                                                                                                                                    |
| Avoid SELECT \*                | Select only the fields you need.                                                                                  | {ref}`performance-optimization`                                                                                                                                                                                    |
| Use targeted filters           | Narrow your search using `WHERE` clauses. <br> Use time filters especially on time series or partitioned tables.  | {ref}`crate-reference:sql_dql_where_clause` <br> {ref}`crate-reference:comparison-operators`                                                                                                                       |
| Pre-aggregate                  | Maintain rollup tables for common queries; use views as convenient wrappers (views are virtual, not precomputed). |                                                                                                                                                                                                                    |
| Use `DATE_BIN` or `DATE_TRUNC` | Apply time-based bucketing on time series data to reduce data volume.                                             | {ref}`DATE_BIN() <crate-reference:date-bin>` <br> {ref}`DATE_TRUNC() <crate-reference:scalar-date_trunc>` <br> [Optimizing storage for historic time series data] <br> [Resampling time series data with DATE_BIN] |
| Profile queries                | Use `EXPLAIN` and `ANALYZE` to inspect performance.                                                               | {ref}`EXPLAIN <crate-reference:ref-explain>` <br> {ref}`ANALYZE <crate-reference:analyze>`                                                                                                                         |
| Sizing & sharding              | Choose partitioning and shard size wisely (e.g., daily partitions for time-based data).                           | {ref}`sharding-partitioning` <br> {ref}`sharding-performance`                                                                                                                                                      |


:::{important}
For in-depth details about performance aspects, please head over to the {ref}`performance`.
:::


[Optimizing storage for historic time series data]: https://community.cratedb.com/t/optimizing-storage-for-historic-time-series-data/762
[Resampling time series data with DATE_BIN]: https://community.cratedb.com/t/resampling-time-series-data-with-date-bin/1009
