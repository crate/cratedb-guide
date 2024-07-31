(query)=
(querying)=
(advanced-querying)=
# Advanced Querying

:::{include} /_include/links.md
:::

About all the advanced querying features of CrateDB, unifying data types
and query characteristics. Mix full-text search with time series aspects,
and run powerful aggregations or other kinds of complex queries on your data.

CrateDB supports effective [time series](#timeseries) analysis with fast
aggregations, relational features for [JOIN](#join) operations, and a rich
set of built-in functions.


(at-a-glance)=
## At a Glance

:::::{info-card}

::::{grid-item}
:columns: auto 9 9 9
**Analyzing Device Readings**

Effectively query measurement readings using enhanced features for time series data.

Run aggregations with gap filling / interpolation, using common
table expressions (CTEs) and LAG / LEAD window functions.

Find maximum values using the MAX_BY aggregate function, returning
the value from one column based on the maximum or minimum value of another
column within a group.

:::{code} sql
WITH OrderedData AS (
  SELECT timestamp,
    location,
    temperature,
    LAG(temperature, 1) IGNORE NULLS OVER w AS prev_temp,
    LEAD(temperature, 1) IGNORE NULLS OVER w AS next_temp
  FROM weather_data
  WINDOW w AS (PARTITION BY location ORDER BY timestamp)
)
SELECT
  timestamp,
  location,
  temperature,
  COALESCE(temperature, (prev_temp + next_temp) / 2)
    AS interpolated_temperature
FROM OrderedData
ORDER BY location, timestamp;
:::

{{ '{}(#timeseries-analysis-advanced)'.format(tutorial) }}
::::

::::{grid-item}
:columns: 3
{tags-primary}`Aggregation` \
{tags-primary}`CTE` \
{tags-primary}`Gap Filling` \
{tags-primary}`Interpolation` \
{tags-primary}`Window Functions`

{tags-secondary}`Time Series` \
{tags-secondary}`SQL`
::::

:::::


:::::{info-card}

::::{grid-item}
:columns: auto 9 9 9
**Time Bucketing**

Based on sensor data, this query calculates:
- time-buckets of 10 seconds
- different aggregations per time-bucket and host group

:::{code} sql
SELECT
  FLOOR(EXTRACT(epoch FROM m.timestamp) / 10) * 10 AS period,
  h.host_group,
  MIN(m.fields['usage_user']) AS "min",
  AVG(m.fields['usage_user']) AS "avg",
  MAX(m.fields['usage_user']) AS "max"
FROM telegraf.metrics m
LEFT JOIN telegraf.hosts h ON h.host_name = m.tags['host']
WHERE tags['cpu'] = 'cpu-total'
  AND m.timestamp > NOW() - '150 seconds'::INTERVAL
GROUP BY 1, 2
ORDER BY 1 DESC;
:::
::::

::::{grid-item}
:columns: 3
{tags-primary}`Aggregation` \
{tags-primary}`Grouping` \
{tags-primary}`Time Bucketing` \
{tags-primary}`Time Intervals`

{tags-secondary}`Time Series` \
{tags-secondary}`SQL`
::::

:::::


(aggregation)=
(aggregations)=
## Aggregations
Fast aggregations, even with complex queries.
- [Analyzing Device Readings with Metadata Integration]

## Bulk Operations

You can use the [bulk operations interface] feature to perform many inserts in
a single operation. See also [bulk operations for INSERTs].
The advantages are:

- Significantly less internal network traffic than executing each insert
  statement individually.

- Even though you're executing multiple insert statements, the bulk query
  only needs to be parsed, planned, and executed once.


(cte)=
(ctes)=
## CTEs
[Time Series: Analyzing Weather Data]


(hyperloglog)=
## HyperLogLog

[HyperLogLog] is an efficient approximate cardinality estimation algorithm.

CrateDB's [hyperloglog_distinct] aggregate function calculates an approximate
count of distinct non-null values using the [HyperLogLog++] algorithm.
See also [Introducing: HyperLogLog].


## LOCF / NOCB
https://community.cratedb.com/t/interpolating-missing-time-series-values/1010


## LTTB
https://community.cratedb.com/t/advanced-downsampling-with-the-lttb-algorithm/1287

(maximum-minimum)=
## Maximum/Minimum Values
[Analyzing Device Readings with Metadata Integration]
[Time Series: Analyzing Weather Data]

## Search
CrateDB provides capabilities for full-text search, vector search, and hybrid
search, all based on vanilla SQL.

- {ref}`fulltext-search`
- {ref}`geo-search`
- {ref}`vector-search`
- {ref}`hybrid-search`


## Time Bucketing
https://community.cratedb.com/t/resampling-time-series-data-with-date-bin/1009

(unnest)=
## UNNEST
- [UNNEST]
- [Optimizing storage for historic time-series data]
- [Ingesting into CrateDB with UNNEST and Node.js]
- [Ingesting into CrateDB with UNNEST and Golang]

(window-functions)=
## Window Functions
- [Window functions in CrateDB]
- [Time Series: Analyzing Weather Data]



:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
It only includes a few pointers to advanced use cases, which need expansion.
It is also not in the same shape as the other pages in this section.
:::


:::{seealso}
**Features:**
[](#relational)

**Domains:**
[](#metrics-store) •
[](#analytics) •
[](#industrial) •
[](#timeseries) •
[](#machine-learning)

**Product:**
[Relational Database] •
[Indexing, Columnar Storage, and Aggregations]
:::


:::{seealso}
**Features:**
[](#relational)

**Domains:**
[](#metrics-store) •
[](#analytics) •
[](#industrial) •
[](#timeseries) •
[](#machine-learning)

**Product:**
[Relational Database] •
[Indexing, Columnar Storage, and Aggregations]
:::


[Analyzing Device Readings with Metadata Integration]: #timeseries-analysis-metadata
[bulk operations interface]: inv:crate-reference#http-bulk-ops
[bulk operations for INSERTs]: #inserts_bulk_operations
[HyperLogLog]: https://en.wikipedia.org/wiki/HyperLogLog
[HyperLogLog++]: https://research.google/pubs/hyperloglog-in-practice-algorithmic-engineering-of-a-state-of-the-art-cardinality-estimation-algorithm/
[hyperloglog_distinct]: inv:crate-reference#aggregation-hyperloglog-distinct
[Ingesting into CrateDB with UNNEST and Golang]: https://community.cratedb.com/t/connecting-to-cratedb-from-go/642#unnest-5
[Ingesting into CrateDB with UNNEST and Node.js]: https://community.cratedb.com/t/connecting-to-cratedb-with-node-js/751#ingesting-into-cratedb-with-unnest-3
[Introducing: HyperLogLog]: https://cratedb.com/blog/feature-focus-making-things-hyper-fast-fast
[Optimizing storage for historic time-series data]: https://community.cratedb.com/t/optimizing-storage-for-historic-time-series-data/762
[Time Series: Analyzing Weather Data]: #timeseries-analysis-weather
[UNNEST]: #inserts_unnest
[Window functions in CrateDB]: https://community.cratedb.com/t/window-functions-in-cratedb/1398
