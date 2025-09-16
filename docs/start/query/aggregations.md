(aggregation)=
(aggregations)=
# Aggregations

:::{div} sd-text-muted
High-performance aggregations on massive volumes of data using SQL.
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 9 9 9

:::{rubric} Introduction
:::

Whether you are monitoring sensor networks, analyzing customer behavior, or powering dashboards, CrateDB’s distributed engine, columnar storage, and native support for structured and semi-structured data make aggregations blazingly fast, even across billions of rows.

:::{rubric} Use CrateDB when you need to
:::

- Aggregate over **high-ingestion** datasets (millions of records per hour)
- Analyze **real-time** metrics across structured, JSON, or time series fields
- Build **dynamic dashboards** and run **interactive ad-hoc analytics**
- Combine aggregations with **full-text**, **geospatial**, or **vector** filters

:::{rubric} Benefits of using CrateDB for aggregations
:::

| Feature                       | Benefit                                                                  |
| ----------------------------- |--------------------------------------------------------------------------|
| Distributed SQL engine        | Parallel execution across nodes ensures linear scalability               |
| Columnar storage              | Reads only relevant columns for faster aggregations                      |
| Real-time ingestion           | Query freshly ingested data without delay                                |
| Aggregations on any data type | Structured, JSON, full-text, geospatial, or vector                       |
| Smart indexing                | Built-in indexing and configuration options that can boost performance   |

::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Documentation
:::
- {ref}`crate-reference:aggregation`
- {ref}`performance-select`

:::{rubric} Integrations
:::
- {ref}`grafana`
- {ref}`metabase`
- {ref}`powerbi`
- {ref}`superset`
- {ref}`tableau`

:::{rubric} See also
:::
- {ref}`analytics`
- [Hands-on: Aggregating and Grouping Data]
- [Real-Time Analytics Primer]
::::

:::::


## Supported Aggregation Functions

CrateDB supports a rich set of **SQL-92-compliant** and extended functions for aggregation, including:

- `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
- `STDDEV()`, `PERCENTILE()`, `VARIANCE()`, `TOPK()`
- `HYPERLOGLOG_DISTINCT()`
- Windowed and conditional aggregations via `OVER(...)` and `FILTER (WHERE ...)` clauses

To learn about the full set of functions, please visit the reference
documentation at {ref}`crate-reference:aggregation-functions`.
See also {ref}`crate-reference:window-functions`.


## Common Aggregation Patterns

::::{grid} 2
:padding: 0
:class-row: title-slim

:::{grid-item}
Count & Grouping
:::
:::{grid-item}
```sql
SELECT city, COUNT(*) AS trip_count
FROM trips
GROUP BY city
ORDER BY trip_count DESC
LIMIT 10;
```
:::

:::{grid-item}
Time-Based Aggregation
:::
:::{grid-item}
```sql
SELECT DATE_TRUNC('day', timestamp) AS day, AVG(temperature) AS avg_temp
FROM sensor_data
GROUP BY day
ORDER BY day ASC;
```
:::

:::{grid-item}
Statistical Summaries
:::
:::{grid-item}
```sql
SELECT
  MIN(response_time),
  MAX(response_time),
  AVG(response_time),
  STDDEV_POP(response_time)
FROM logs
WHERE timestamp >= now() - INTERVAL '1 day';
```
:::

:::{grid-item}
Nested / Object Field Aggregation
:::
:::{grid-item}
```sql
SELECT payload['device']['os'], COUNT(*) AS count
FROM events
GROUP BY payload['device']['os'];
```
:::

:::{grid-item}
**Statistics:**
Example using PERCENTILE for tail latency.
:::
:::{grid-item}
```sql
SELECT PERCENTILE(response_time, 0.95) AS p95
FROM api_logs
WHERE endpoint = '/checkout';
```
:::

::::


## Real-World Examples

::::{grid} 2
:padding: 0
:class-row: title-slim

:::{grid-item}
**Industrial IoT:**
Monitor and aggregate sensor readings from thousands of devices in real time.
:::
:::{grid-item}
```sql
SELECT device_id, MAX(temperature) AS max_temp
FROM readings
WHERE timestamp >= now() - INTERVAL '1 hour'
GROUP BY device_id;
```
:::

:::{grid-item}
**E-Commerce Analytics:**
Aggregate customer orders across dimensions like product, region, or time.
:::
:::{grid-item}
```sql
SELECT product_id, SUM(quantity) AS units_sold
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY product_id
ORDER BY units_sold DESC
LIMIT 20;
```
:::

:::{grid-item}
**Fleet Monitoring:**
Aggregate location and status data of vehicles in motion.
:::
:::{grid-item}
```sql
SELECT status, COUNT(*)
FROM vehicle_tracking
WHERE updated_at >= now() - INTERVAL '10 minutes'
GROUP BY status;
```

:::

::::


## Visualization & BI Tools

CrateDB integrates seamlessly with:

:Grafana: Build real-time dashboards with time-series aggregations
:Apache Superset: Explore multidimensional data visually
:Tableau, Power BI, Metabase: Connect via PostgreSQL wire protocol

These tools submit SQL queries to CrateDB, which returns pre-aggregated
or real-time data efficiently.
To learn about the full set of integrations, please visit the
documentation at {ref}`bi` and {ref}`visualization`.


[Hands-on: Aggregating and Grouping Data]: https://cratedb.com/academy/fundamentals/working-with-data-in-cratedb/hands-on-aggregating-and-grouping-data
[Real-Time Analytics Primer]: https://cratedb.com/real-time-analytics/definition
