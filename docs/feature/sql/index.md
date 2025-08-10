(sql)=

# SQL

:::{include} /_include/links.md
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 9 9 9

:::{rubric} Overview
:::
CrateDB's features are available using plain SQL, and it is wire-protocol
compatible to PostgreSQL.

:::{rubric} About
:::
SQL is the most widely used language for querying data and is the natural
choice for people in many roles working with data in databases.

CrateDB extends industry-standard SQL with functionalities to support
its data types, data I/O procedures, and cluster management.

:::{rubric} Details
:::
CrateDB integrates well with commodity systems using standard database
access interfaces like ODBC or JDBC, and it provides a proprietary HTTP
interface on top.

You have a variety of options to connect to CrateDB, and to integrate it with
off-the-shelve, 3rd-party, open-source, and proprietary applications.

Interfacing with your data in standard SQL syntax unlocks
manifold integration capabilities instead of resorting to specialized query
languages or DSLs like Query DSL (Elasticsearch), the MongoDB Query Language,
Flux (InfluxDB), or PromQL (Prometheus).
::::


::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Reference Manual
:::
- {ref}`crate-reference:sql`

:::{rubric} Related
:::
- {ref}`connect`
- {ref}`query`

:::{rubric} Product
:::
- [Relational Database]
- [Multi-model Database]
- [JSON Database]
- [Dynamic Database Schemas]
- [Nested Data Structure]

{tags-primary}`Query Language`
{tags-primary}`Standard Interface` \
{tags-secondary}`SQL`
{tags-secondary}`ODBC`
{tags-secondary}`JDBC`
::::

:::::



## Synopsis

Use scalar functions, sub-selects, and windowing, specifically illustrating the
DATE_BIN function for resampling time series data using DATE_BIN, also known as
grouping rows into time buckets, aka. time bucketing.

```sql
SELECT
  ts_bin,
  battery_level,
  battery_status,
  battery_temperature
FROM (
  SELECT
  DATE_BIN('5 minutes'::INTERVAL, "time", 0) AS ts_bin,
  battery_level,
  battery_status,
  battery_temperature,
  ROW_NUMBER() OVER (PARTITION 
    BY DATE_BIN('5 minutes'::INTERVAL, "time", 0)
    ORDER BY "time" DESC) AS "row_number"
  FROM doc.sensor_readings
) x
WHERE "row_number" = 1
ORDER BY 1 ASC
```


## Learn

Please inspect more advanced SQL capabilities on the [](#query) page,
and read about [](#features) in general.



:::{seealso}
**Domains:**
[](#metrics-store) •
[](#analytics) •
[](#industrial) •
[](#timeseries) •
[](#machine-learning)
:::
