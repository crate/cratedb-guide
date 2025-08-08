# Time series data

CrateDB employs a relational representation for time‑series, enabling you to work with timestamped data using standard SQL, while also seamlessly combining with document and context data.

## 1. Why CrateDB for Time Series?

* **Distributed architecture and columnar storage** enable very high ingest throughput with fast aggregations and near‑real‑time analytical queries.
* Handles **high cardin­ality** and **mixed data types**, including nested JSON, geospatial and vector data—all queryable via the same SQL statements.
* **PostgreSQL wire‑protocol compatible**, so it integrates easily with existing tools and drivers.

## 2. Data Model Template

A typical time‑series schema looks like this:

<pre class="language-sql"><code class="lang-sql">CREATE TABLE IF NOT EXISTS weather_data (
    ts TIMESTAMP,
    location VARCHAR,
<strong>    temperature DOUBLE,
</strong><strong>    humidity DOUBLE CHECK (humidity >= 0),
</strong>    PRIMARY KEY (ts, location)
)
WITH (column_policy = 'dynamic');
</code></pre>

Key points:

* `ts`: append‑only timestamp column
* Composite primary key `(ts, location)` ensures uniqueness and efficient sort/group by time
* `column_policy = 'dynamic'` allows schema evolution: inserting a new field auto‑creates the column.

## 3. Ingesting and Querying

### **Data Ingestion**

* Use SQL `INSERT` or bulk import techniques like `COPY FROM` with JSON or CSV files.
* Schema inference can often happen automatically during import.

### **Aggregation and Transformations**

CrateDB offers built‑in SQL functions tailor‑made for time‑series analyses:

* **`DATE_BIN(interval, timestamp, origin)`** for bucketed aggregations (down‑sampling).
* **Window functions** like `LAG()` and `LEAD()` to detect trends or gaps.
* **`MAX_BY()`** returns the value from one column matching the min/max value of another column in a group.

**Example**: compute hourly average battery levels and join with metadata:

```postgresql
WITH avg_metrics AS (
  SELECT device_id,
         DATE_BIN('1 hour', time, 0) AS period,
         AVG(battery_level) AS avg_battery
  FROM devices.readings
  GROUP BY device_id, period
)
SELECT period, t.device_id, i.manufacturer, avg_battery
FROM avg_metrics t
JOIN devices.info i USING (device_id)
WHERE i.model = 'mustang';
```

**Example**: gap detection interpolation:

```text
WITH all_hours AS (
  SELECT generate_series(ts_start, ts_end, ‘30 second’) AS expected_time
),
raw AS (
  SELECT time, battery_level FROM devices.readings
)
SELECT expected_time, r.battery_level
FROM all_hours
LEFT JOIN raw r ON expected_time = r.time
ORDER BY expected_time;
```

## 4. Downsampling & Interpolation

To reduce volume while preserving trends, use `DATE_BIN`.\
Missing data can be handled using `LAG()`/`LEAD()` or other interpolation logic within SQL.

## 5. Schema Evolution & Contextual Data

With `column_policy = 'dynamic'`, ingest JSON payloads containing extra attributes—new columns are auto‑created and indexed. Perfect for capturing evolving sensor metadata.

You can also store:

* **Geospatial** (`GEO_POINT`, `GEO_SHAPE`)
* **Vectors** (up to 2048 dims via HNSW indexing)
* **BLOBs** for binary data (e.g. images, logs)

All types are supported within the same table or joined together.

## 6. Storage Optimization

* **Partitioning and sharding**: data can be partitioned by time (e.g. daily/monthly) and sharded across a cluster.
* Supports long‑term retention with performant historic storage.
* Columnar layout reduces storage footprint and accelerates aggregation queries.

## 7. Advanced Use Cases

* **Exploratory data analysis** (EDA), decomposition, and forecasting via CrateDB’s SQL or by exporting to Pandas/Plotly.
* **Machine learning workflows**: time‑series features and anomaly detection pipelines can be built using CrateDB + external tools

## 8. Sample Workflow (Chicago Weather Dataset)

CrateDB’s sample data set captures hourly temperature, humidity, pressure, wind at three Chicago stations (150,000+ records).

Typical operations:

* Table creation and ingestion
* Average per station
* Using `MAX_BY()` to find highest temperature timestamps
* Downsampling using `DATE_BIN` into 4‑week buckets

This workflow illustrates how CrateDB scales and simplifies time series modeling.

## 9. Best Practices Checklist

| Topic                         | Recommendation                                                      |
| ----------------------------- | ------------------------------------------------------------------- |
| Schema design                 | Use composite primary key (timestamp + series key), dynamic columns |
| Ingestion                     | Use bulk import (COPY) and JSON ingestion                           |
| Aggregations                  | Use DATE\_BIN, window functions, GROUP BY                           |
| Interpolation / gap analysis  | Employ LAG(), LEAD(), generate\_series, joins                       |
| Schema evolution              | Dynamic columns allow adding fields on the fly                      |
| Mixed data types              | Combine time series, JSON, geo, full‑text in one dataset            |
| Partitioning & shard strategy | Partition by time, shard across nodes for scale                     |
| Downsampling                  | Use DATE\_BIN for aggregating resolution                            |
| Integration with analytics/ML | Export to pandas/Plotly or train ML models inside CrateDB pipeline  |

## 10. Further Learning

* Video: **Time Series Data Modeling** – covers relational & time series, document, geospatial, vector, and full-text in one tutorial.
* Official CrateDB Guide: **Time Series Fundamentals**, **Advanced Time Series Analysis**, **Sharding & Partitioning**.
* CrateDB Academy: free courses including an **Advanced Time Series Modeling** module.

