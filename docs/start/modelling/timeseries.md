# Time series data

CrateDB employs a relational representation for time‑series, enabling you to work with timestamped data using standard SQL, while also seamlessly combining with document and context data.

## Why CrateDB for Time Series?

* While maintaining a high ingest rate, its **columnar storage** and **automatic indexing** let you access and analyze the data immediately with **fast aggregations** and **near-real-time queries**.
* Handles **high cardin­ality** and **a variety of data types**, including nested JSON, geospatial and vector data—all queryable via the same SQL statements.
* **PostgreSQL wire‑protocol compatible**, so it integrates easily with existing tools and drivers.

## Data Model Template

A typical time‑series schema looks like this:

```sql
CREATE TABLE IF NOT EXISTS devices_readings (
   ts TIMESTAMP WITH TIME ZONE,
   device_id TEXT,
   battery OBJECT(DYNAMIC) AS (
      level BIGINT,
      status TEXT,
      temperature DOUBLE PRECISION
   ),
   cpu OBJECT(DYNAMIC) AS (
      avg_1min DOUBLE PRECISION,
      avg_5min DOUBLE PRECISION,
      avg_15min DOUBLE PRECISION
   ),
   memory OBJECT(DYNAMIC) AS (
      free BIGINT,
      used BIGINT
   ),
   month timestamp with time zone GENERATED ALWAYS AS date_trunc('month', ts)
) PARTITIONED BY (month);
```

Key points:

* `month`  is the partitioning key, optimizing data storage and retrieval.
* Every column is stored in the column store by default for fast aggregations.
* Using **OBJECT columns** in the `devices_readings` table provides a structured and efficient way to organize complex nested data in CrateDB, enhancing both data integrity and flexibility.

## Ingesting and Querying

### **Data Ingestion**

* Use SQL `INSERT` or bulk import techniques like `COPY FROM` with JSON or CSV files.
* Schema inference can often happen automatically during import.

### **Aggregation and Transformations**

CrateDB offers built‑in SQL functions tailor‑made for time‑series analyses:

* **`DATE_BIN(interval, timestamp, origin)`** for bucketed aggregations (down‑sampling).
* **Window functions** like `LAG()` and `LEAD()` to detect trends or gaps.
* **`MAX_BY()`** returns the value from one column matching the min/max value of another column in a group.

**Example**: compute hourly average battery levels and join with metadata:

```sql
WITH avg_metrics AS (
  SELECT device_id,
         DATE_BIN('1 hour'::interval, ts, 0) AS period,
         AVG(battery['level']) AS avg_battery
  FROM devices_readings
  GROUP BY device_id, period
)
SELECT period, t.device_id, i.manufacturer, avg_battery
FROM avg_metrics t
JOIN devices_info i USING (device_id)
WHERE i.model = 'mustang';
```

**Example**: gap detection interpolation:

```sql
WITH all_hours AS (
  SELECT
    generate_series(
      '2025-01-01',
      '2025-01-02',
      '30 second' :: interval
    ) AS expected_time
),
raw AS (
  SELECT
    ts,
    battery ['level']
  FROM
    devices_readings
)
SELECT
  expected_time,
  r.battery ['level']
FROM
  all_hours
  LEFT JOIN raw r ON expected_time = r.ts
ORDER BY
  expected_time;
```

## Down-sampling & Interpolation

To reduce volume while preserving trends, use `DATE_BIN`.\
Missing data can be handled using `LAG()`/`LEAD()` or other interpolation logic within SQL.

## Schema Evolution & Contextual Data

With `column_policy = 'dynamic'`, ingest JSON payloads containing extra attributes—new columns are auto‑created and indexed. Perfect for capturing evolving sensor metadata. For column-level control, use `OBJECT(DYNAMIC)` to auto-create (and, by default, index) subcolumns, or `OBJECT(IGNORED)`to accept unknown keys without creating or indexing subcolumns.   &#x20;

You can also store:

* **Geospatial** (`GEO_POINT`, `GEO_SHAPE`)
* **Vectors** (up to 2048 dims via HNSW indexing)
* **BLOBs** for binary data (e.g. images, logs)

All types are supported within the same table or joined together.

## Storage Optimization

* **Partitioning and sharding**: data can be partitioned by time (e.g. daily/monthly) and sharded across a cluster.
* Supports long‑term retention with performant historic storage.
* Columnar layout reduces storage footprint and accelerates aggregation queries.

## Advanced Use Cases

* **Exploratory data analysis** (EDA), decomposition, and forecasting via CrateDB’s SQL or by exporting to Pandas/Plotly.
* **Machine learning workflows**: time‑series features and anomaly detection pipelines can be built using CrateDB + external tools

## Sample Workflow (Chicago Weather Dataset)

In [this lesson of the CrateDB Academy](https://cratedb.com/academy/fundamentals/data-modelling-with-cratedb/hands-on-time-series-data) introducing Time Series data, we provide a sample data set that captures hourly temperature, humidity, pressure, wind at three Chicago stations (150,000+ records).

Typical operations:

* Table creation and ingestion
* Average per station
* Using `MAX_BY()` to find highest temperature timestamps
* Down-sampling using `DATE_BIN` into 4‑week buckets

This workflow illustrates how CrateDB scales and simplifies time series modeling.

## Best Practices Checklist

| Topic                         | Recommendation                                                                     |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| Schema design and evolution   | Dynamic columns add fields as needed; diverse data types ensure proper typing      |
| Ingestion                     | Use bulk import (COPY) and JSON ingestion                                          |
| Aggregations                  | Use DATE\_BIN, window functions, GROUP BY                                          |
| Interpolation / gap analysis  | Employ LAG(), LEAD(), generate\_series, joins                                      |
| Mixed data types              | Combine time series, JSON, geo, full‑text in one dataset                           |
| Partitioning & shard strategy | Partition by time, shard across nodes for scale                                    |
| Down-sampling                 | Use DATE\_BIN for aggregating resolution or implement your own strategy using UDFs |
| Integration with analytics/ML | Export to pandas/Plotly to train your ML models                                    |

## Further Learning

* **Video:** [Time Series Data Modeling](https://cratedb.com/resources/videos/time-series-data-modeling) – covers relational & time series, document, geospatial, vector, and full-text in one tutorial.
* **CrateDB Academy:** [Advanced Time Series Modeling course](https://cratedb.com/academy/time-series/getting-started/introduction-to-time-series-data).
