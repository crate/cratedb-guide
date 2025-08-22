# Aggregations

CrateDB is designed to deliver **high-performance aggregations** on massive volumes of data—**in real time** and using familiar SQL syntax.

Whether you’re monitoring sensor networks, analyzing customer behavior, or powering dashboards, CrateDB’s distributed engine, columnar storage, and native support for structured and semi-structured data make aggregations blazingly fast, even across billions of rows.



## Why Use CrateDB for Aggregations?

| Feature                       | Benefit                                                                 |
| ----------------------------- | ----------------------------------------------------------------------- |
| Distributed SQL engine        | Parallel execution across nodes ensures linear scalability              |
| Columnar storage              | Reads only relevant columns for faster aggregations                     |
| Real-time ingestion           | Query freshly ingested data without delay                               |
| Aggregations on any data type | Structured, JSON, full-text, geospatial, or vector                      |
| Smart indexing                | Built-in indexing plus user-defined indexes can boost performance       |



## Common Aggregation Patterns

### **Count & Grouping**

```sql
SELECT city, COUNT(*) AS trip_count
FROM trips
GROUP BY city
ORDER BY trip_count DESC
LIMIT 10;
```

### **Time-Based Aggregation**

```sql
SELECT DATE_TRUNC('day', timestamp) AS day, AVG(temperature) AS avg_temp
FROM sensor_data
GROUP BY day
ORDER BY day ASC;
```

### **Statistical Summaries**

```sql
SELECT
  MIN(response_time),
  MAX(response_time),
  AVG(response_time),
  STDDEV_POP(response_time)
FROM logs
WHERE timestamp >= now() - INTERVAL '1 day';
```

**Nested / Object Field Aggregation**

```sql
SELECT payload['device']['os'], COUNT(*) AS count
FROM events
GROUP BY payload['device']['os'];
```



## Real-World Examples

### **Industrial IoT**

Monitor and aggregate sensor readings from thousands of devices in real time.

```sql
SELECT device_id, MAX(temperature) AS max_temp
FROM readings
WHERE timestamp >= now() - INTERVAL '1 hour'
GROUP BY device_id;
```

### **E-Commerce Analytics**

Aggregate customer orders across dimensions like product, region, or time.

```sql
SELECT product_id, SUM(quantity) AS units_sold
FROM orders
WHERE order_date >= CURRENT_DATE - 30
GROUP BY product_id
ORDER BY units_sold DESC
LIMIT 20;
```

### **Fleet Monitoring**

Aggregate location and status data of vehicles in motion.

```sql
SELECT status, COUNT(*)
FROM vehicle_tracking
WHERE updated_at >= now() - INTERVAL '10 minutes'
GROUP BY status;
```



## Performance Considerations

| Optimization       | Description                                                                            |
| ------------------ | -------------------------------------------------------------------------------------- |
| Use proper indexes | On frequently grouped or filtered fields                                               |
| Avoid SELECT \*    | Only query required columns                                                            |
| Pre-aggregate      | Use views for common queries                                                           |
| Use `DATE_TRUNC`   | To bucket time for time-series data                                                    |
| Sizing & sharding  | Choose partitioning and shard size wisely (e.g., daily partitions for time-based data) |



## Aggregation Functions Supported

CrateDB supports a rich set of **SQL92-compliant** and extended functions for aggregation, including:

* `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`
* `STDDEV_POP()`, `VAR_POP()`, `PERCENTILE()`
* `APPROX_COUNT_DISTINCT()`
* **Conditional Aggregates**: `FILTER (WHERE ...)` syntax
* **Windowed Aggregations**: via `OVER(...)` clauses

Example using percentile:

```sql
SELECT PERCENTILE(response_time, 0.95) AS p95
FROM api_logs
WHERE endpoint = '/checkout';
```



## Visualization & BI Tools

CrateDB integrates seamlessly with:

* **Grafana** → Build real-time dashboards with time-series aggregations
* **Apache Superset** → Explore multidimensional data visually
* **Tableau, Power BI, Metabase** → Connect via PostgreSQL wire protocol

These tools push SQL queries to CrateDB, which returns pre-aggregated or real-time data efficiently.



## When to Use Aggregations in CrateDB

Use CrateDB when you need to:

* Aggregate over **high-ingestion** datasets (millions of records per hour)
* Analyze **real-time** metrics across structured, JSON, or time-series fields
* Build **dynamic dashboards** and run **interactive ad-hoc analytics**
* Combine aggregations with **full-text**, **geospatial**, or **vector** filters



## Learn More

* CrateDB Docs – Aggregate Functions
* Tutorial – Real-time analytics with CrateDB
* Blog – Powering dashboards with aggregations
* CrateDB Academy – Aggregations 101
