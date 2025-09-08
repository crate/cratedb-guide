(model-timeseries)=
# Time series data

## Why CrateDB for Time Series?

CrateDB employs a relational representation for time‑series, enabling you to
work with timestamped data using standard SQL, while also seamlessly combining
with document and context data.

* While maintaining a high ingest rate, the **columnar storage** and **automatic
  indexing** let you access and analyze the data immediately with **fast
  aggregations** and **near-real-time queries**.
* Handles **high cardin­ality** and **a variety of data types**, including
  nested JSON, geospatial and vector data — all queryable via the same SQL
  statements.

## Data Model Template

A typical time‑series schema looks like this:

```sql
CREATE TABLE devices_readings (
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
   month TIMESTAMP GENERATED ALWAYS AS date_trunc('month', ts)
) PARTITIONED BY (month);
```

Key points:

* `month`  is the partitioning key, optimizing data storage and retrieval.
* Every column is stored in the column store by default for fast aggregations.
* Using **OBJECT columns** provides a structured and efficient way to organize
  complex nested data in CrateDB, enhancing both data integrity and flexibility.

## Ingesting and Querying

### **Data Ingestion**

* Use SQL `INSERT` or bulk import techniques like `COPY FROM` with JSON or CSV
  files.
* Schema inference can often happen automatically during import.

### **Aggregation and Transformations**

CrateDB offers built‑in SQL functions tailor‑made for time‑series analyses:

* **`DATE_BIN(interval, timestamp, origin)`** for bucketed aggregations
  (down‑sampling).
* **Window functions** like `LAG()` and `LEAD()` to detect trends or gaps.
* **`MAX_BY()`** returns the value from one column matching the min/max value of
  another column in a group.

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
      INTERVAL '30 second'
    ) AS expected_time
),
raw AS (
  SELECT
    ts,
    battery['level']
  FROM
    devices_readings
)
SELECT
  expected_time,
  r.battery['level']
FROM
  all_hours
  LEFT JOIN raw r ON expected_time = r.ts
ORDER BY
  expected_time;
```

### Typical time-series functions

* **Time extraction:** date_trunc, extract, date_part, now(), current_timestamp
* **Time bucketing:** date_bin, interval, age
* **Window functions:** avg(...) OVER (...), stddev(...) OVER (...), lag, lead,
  first_value, last_value, row_number,  rank, WINDOW ... AS (...)
* **Null handling:** coalesce, nullif
* **Statistical aggregates:** percentile, correlation, stddev, variance, min,
  max, sum
* **Advanced filtering & logic:** greatest, least, case when ... then ... end

## Downsampling & Interpolation

To reduce volume while preserving trends, use `DATE_BIN`. Missing data can be
handled using `LAG()`/`LEAD()` or other interpolation logic within SQL.

## Schema Evolution & Contextual Data

With `column_policy = 'dynamic'`, ingest JSON payloads containing extra
attributes—new columns are auto‑created and indexed. Perfect for capturing
evolving sensor metadata. For column-level control, use `OBJECT(DYNAMIC)` to
auto-create (and, by default, index) subcolumns, or `OBJECT(IGNORED)`to accept
unknown keys without creating or indexing subcolumns.   &#x20;

You can also store:

* **Geospatial** (`GEO_POINT`, `GEO_SHAPE`)
* **Vectors** (up to 2048 dims via HNSW indexing)
* **BLOBs** for binary data (e.g. images, logs)

All types are supported within the same table or joined together.

## Storage Optimization

* **Partitioning and sharding**: data can be partitioned by time (e.g.
  daily/monthly) and sharded across a cluster.
* Supports long‑term retention with performant historic storage.
* Columnar layout reduces storage footprint and accelerates aggregation queries.

## Advanced Use Cases

* **Exploratory data analysis** (EDA), decomposition, and forecasting via
  CrateDB’s SQL or by exporting to Pandas/Plotly.
* **Machine learning workflows**: time‑series features and anomaly detection
  pipelines can be built using CrateDB + external tools

## Further Learning & Resources

* **Documentation:** {ref}`Advanced Time Series Analysis <timeseries-analysis>`,
  {ref}`Time Series Long Term Storage <timeseries-longterm>`
* **Video:** [Time Series Data
  Modeling](https://cratedb.com/resources/videos/time-series-data-modeling) –
  covers relational & time series, document, geospatial, vector, and full-text
  in one tutorial.
* **CrateDB Academy:** [Advanced Time Series Modeling
  course](https://cratedb.com/academy/time-series/getting-started/introduction-to-time-series-data).
* **Tutorial:** [Downsampling with LTTB
  algorithm](https://community.cratedb.com/t/advanced-downsampling-with-the-lttb-algorithm/1287)
