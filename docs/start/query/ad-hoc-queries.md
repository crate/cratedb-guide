# Ad-hoc queries

CrateDB is built to support **highly dynamic, ad-hoc querying,** even on large-scale, real-time datasets.

Whether you're a developer, data analyst, or operator, CrateDB lets you **ask new questions** on the fly without waiting for data pipelines, ETL, or pre-aggregated views. Thanks to its distributed SQL engine, flexible data modeling, and support for semi-structured data, CrateDB is ideal for **interactive exploration** and **live analytics**.

## 1. What Are Ad-hoc Queries?

Ad-hoc queries are **spontaneous, often one-off SQL queries** used for:

* Troubleshooting
* Exploratory analysis
* Debugging systems
* Investigating anomalies
* Supporting customer questions
* Generating quick reports

They are unpredictable by nature—and CrateDB is designed to handle exactly that.

## 2. Why CrateDB for Ad-hoc Queries?

| Feature                | Benefit                                                |
| ---------------------- | ------------------------------------------------------ |
| Distributed SQL engine | Fast performance, even on complex queries              |
| Real-time ingestion    | Query new data moments after it arrives                |
| Flexible schemas       | Combine structured, JSON, text, and geospatial data    |
| Full SQL support       | Use familiar SQL for joins, filters, sorting, and more |
| Easy integrations      | Query from CLI, notebooks, BI tools, or REST API       |

## 3. Common Query Patterns

### **Quick Filters**

```sql
SELECT *
FROM logs
WHERE service = 'auth' AND log_level = 'error'
ORDER BY timestamp DESC
LIMIT 50;
```

### **Explore Nested JSON**

```sql
SELECT payload['device']['os'], COUNT(*) AS count
FROM events
GROUP BY payload['device']['os'];
```

### **Geospatial Debugging**

```sql
SELECT id, latitude, longitude
FROM vehicles
WHERE within(geo_point(latitude, longitude), geo_polygon([...]));
```

### **Time-bound Query**

```sql
SELECT *
FROM sensor_data
WHERE timestamp > now() - INTERVAL '15 minutes';
```

### &#x20;**Join Across Tables**

```sql
SELECT o.order_id, c.name, o.total
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.order_date >= CURRENT_DATE - 7;
```

## 4. Real-World Examples

### **DevOps & Observability**

Investigate production issues by filtering logs or telemetry on the fly.

```sql
SELECT message
FROM logs
WHERE log_level = 'warn' AND host = 'api-01'
ORDER BY timestamp DESC;
```

### **Data Exploration**

Test hypotheses by slicing data in new ways without waiting for prebuilt reports.

```sql
SELECT city, AVG(duration)
FROM rides
GROUP BY city
HAVING AVG(duration) > 10;
```

### **Product Analytics**

Check how often a new product was bought after launch.

```sql
SELECT COUNT(*)
FROM orders
WHERE product_id = 'xyz123'
AND order_date >= '2025-07-01';
```

## 5. Performance Tips for Ad-hoc Queries

| Tip                  | Description                                        |
| -------------------- |----------------------------------------------------|
| Use targeted filters | Narrow your search with `WHERE` clauses            |
| Leverage indexes     | Fields are indexed by default                      |
| Avoid SELECT \*      | Select only the fields you need                    |
| Profile queries      | Use `EXPLAIN` and `ANALYZE` to inspect performance |
| Use time filters     | Especially on time-series or partitioned tables    |

## 6. Tools & Interfaces

CrateDB offers several interfaces for ad-hoc queries:

* **Admin UI Console** – Web-based SQL editor with result viewer
* **PostgreSQL Clients** – psql, DBeaver, DataGrip, etc.
* **REST API / HTTP Client** – Send ad-hoc queries over HTTP
* **CrateDB Python Client** – Ideal for notebooks and automation
* **Grafana / Superset** – Query builder UI and live dashboards

Example via REST:

```bash
curl -XPOST https://your.cratedb.cloud:4200/_sql \
  -H "Content-Type: application/json" \
  -d '{"stmt": "SELECT * FROM logs WHERE log_level = ? LIMIT 10", "args": ["error"]}'
```

## 7. When to Use CrateDB for Ad-hoc Queries

Use CrateDB when you need to:

* Explore **new patterns** in operational or business data
* Run **troubleshooting queries** across complex systems
* **Query fresh data instantly**, without waiting for batch jobs
* Combine structured + JSON + full-text + spatial + vector data
* Avoid maintaining rigid ETL pipelines or OLAP cubes

## 8. Related Features

| Feature              | Description                                    |
| -------------------- | ---------------------------------------------- |
| Dynamic schemas      | No need to predefine every field               |
| Intelligent indexing | Works out of the box for ad-hoc querying       |
| Time-series support  | Perfect for time-bound diagnostics             |
| Object columns       | Flexible modeling of JSON data                 |
| Full-text & filter   | Combine keyword search with structured queries |

## 9. Learn More

* CrateDB SQL Reference
* CrateDB Console
* Blog – How to Run Exploratory Queries
* CrateDB Academy – Querying at Scale

## 10. Summary

CrateDB is your go-to database for **fast, flexible, and reliable ad-hoc querying**. Whether you’re debugging systems, answering tough questions, or uncovering hidden insights, CrateDB empowers you to work at the **speed of thought** on **real-time data**, at any scale.
