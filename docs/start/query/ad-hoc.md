(ad-hoc-queries)=
# Ad-hoc queries

:::{div} sd-text-muted
Support highly dynamic ad-hoc querying even on large-scale, real-time datasets.
:::

:::{rubric} Introduction
:::

Whether you're a developer, data analyst, or operator, CrateDB lets you **ask new questions** on the fly without waiting for data pipelines, ETL, or pre-aggregated views. Thanks to its distributed SQL engine, flexible data modeling, and support for semi-structured data, CrateDB is ideal for **interactive exploration** and **live analytics**.

CrateDB is your go-to database for **fast, flexible, and reliable ad-hoc querying**. Whether you’re debugging systems, answering tough questions, or uncovering hidden insights, CrateDB empowers you to work at the **speed of thought** on **real-time data**, at any scale.

:::{rubric} What are ad-hoc queries?
:::

Ad-hoc queries are **spontaneous, often one-off SQL queries** used for:

- Troubleshooting
- Exploratory analysis
- Debugging systems
- Investigating anomalies
- Supporting customer questions
- Generating quick reports

They are unpredictable by nature—and CrateDB is designed to handle exactly that.

---

:::{rubric} Benefits of using CrateDB for ad-hoc queries
:::

| Feature                | Benefit                                                |
| ---------------------- |--------------------------------------------------------|
| Distributed SQL engine | Fast performance, even on complex queries              |
| Real-time ingestion    | Query new data moments after it arrives                |
| Flexible schemas       | Combine structured, JSON, text, and geospatial data    |
| Full SQL support       | Use familiar SQL for joins, filters, sorting, and more |
| Easy integrations      | Query from CLI, notebooks, BI tools, or HTTP API       |

---

:::{rubric} When to use CrateDB for ad-hoc queries
:::
- Explore **new patterns** in operational or business data
- Run **troubleshooting queries** across complex systems
- **Query fresh data instantly**, without waiting for batch jobs
- Combine structured + JSON + full-text + spatial + vector data
- Avoid maintaining rigid ETL pipelines or OLAP cubes


## Common Query Patterns

::::{grid} 2
:padding: 0
:class-row: title-slim

:::{grid-item}
Quick Filters
:::
:::{grid-item}
```sql
SELECT timestamp, message, host
FROM logs
WHERE service = 'auth' AND log_level = 'error'
ORDER BY timestamp DESC
LIMIT 50;
```
:::

:::{grid-item}
Explore Nested JSON
:::
:::{grid-item}
```sql
SELECT
  payload['device']['os'],
  COUNT(*) AS count
FROM events
GROUP BY payload['device']['os'];
```
:::

:::{grid-item}
Geospatial Debugging
:::
:::{grid-item}
```sql
SELECT id, latitude, longitude
FROM vehicles
WHERE within(
  location,
  'POLYGON ((-73.97 40.78, -73.95 40.78, -73.95 40.76, -73.97 40.76, -73.97 40.78))'
);
```
:::

:::{grid-item}
Time-bound Query
:::
:::{grid-item}
```sql
SELECT timestamp, device_id, value
FROM sensor_data
WHERE timestamp > now() - INTERVAL '15 minutes';
```
:::

:::{grid-item}
Join Across Tables
:::
:::{grid-item}
```sql
SELECT o.order_id, c.name, o.total
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '7 days';
```
:::

::::


## Real-World Examples

::::{grid} 2
:padding: 0
:class-row: title-slim

:::{grid-item}
**DevOps & Observability:**
Investigate production issues by filtering logs or telemetry on the fly.
:::
:::{grid-item}
```sql
SELECT message
FROM logs
WHERE log_level = 'warn' AND host = 'api-01'
ORDER BY timestamp DESC;
```
:::

:::{grid-item}
**Data Exploration:**
Test hypotheses by slicing data in new ways without waiting for prebuilt reports.
:::
:::{grid-item}
```sql
SELECT city, AVG(duration)
FROM rides
GROUP BY city
HAVING AVG(duration) > 10;
```
:::

:::{grid-item}
**Product Analytics:**
Check how often a new product was bought after launch.
:::
:::{grid-item}
```sql
SELECT COUNT(*)
FROM orders
WHERE product_id = 'xyz123'
AND order_date >= '2025-07-01';
```
:::

:::{grid-item}
:::
:::{grid-item}
:::

::::


## Tools & Interfaces

CrateDB offers several interfaces for ad-hoc queries:

- **{ref}`Admin UI Console <crate-admin-ui:index>`** – Web-based SQL editor with result viewer
- **PostgreSQL Clients** – psql, DBeaver, DataGrip, etc.
- **HTTP Client** – Send ad-hoc queries over HTTP
- **{ref}`CrateDB Python Client <crate-python:index>`** – Ideal for notebooks and automation
- **Grafana / Superset** – Query builder UI and live dashboards

Example via HTTP:

```bash
curl -sSf -u USERNAME:PASSWORD -X POST https://your.cratedb.cloud:4200/_sql \
  -H "Content-Type: application/json" \
  -d '{"stmt": "SELECT timestamp, message, host FROM logs WHERE log_level = ? LIMIT 10", "args": ["error"]}'
```


## Related features

Learn more about how to use ad-hoc queries effectively.

| Feature                               | Description                                                                          | Documentation                                                |
|---------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Dynamic schemas & <br> object columns | Flexible modeling of semi-structured JSON data <br> No need to predefine every field | {ref}`object` <br> {ref}`crate-reference:data-types-objects` |
| Time series support                   | Perfect for time-bound diagnostics                                                   | {ref}`timeseries`                                            |
| Intelligent indexing                  | Works out of the box for ad-hoc querying                                             | {ref}`search-overview`                                                |
| Full-text & filter                    | Combine keyword search with structured queries                                       | {ref}`fts` <br> {ref}`crate-reference:fulltext-indices`      |


## Further reading

:::::{grid}
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`article;1.5em` Documentation
:columns: 12 6 3 3
- {ref}`SQL reference <crate-reference:sql>`
- {ref}`crate-reference:data-types-objects`
- {ref}`crate-reference:fulltext-indices`
::::

::::{grid-item-card} {material-outlined}`link;1.5em` Related
:columns: 12 6 3 3
- {ref}`object`
- {ref}`fts`
- {ref}`timeseries`
- {ref}`CrateDB Console <crate-crash:index>`
::::

::::{grid-item-card} {material-outlined}`read_more;1.5em` Read more
:columns: 12 12 6 6
- [Exploratory Time Series Data Analysis]
- [Academy: Time Series Query Optimization]
- [CrateDB Scalability Benchmark: Query Throughput]
::::

:::::


[Academy: Time Series Query Optimization]: https://cratedb.com/academy/time-series/time-series-data-manipulation-and-visualization/time-series-query-optimization
[CrateDB Scalability Benchmark: Query Throughput]: https://cratedb.com/blog/cratedb-scalability-benchmark-query-throughput
[Exploratory Time Series Data Analysis]: https://cratedb.com/data-model/time-series/exploratory-data-analysis
