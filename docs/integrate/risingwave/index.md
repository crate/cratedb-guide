(risingwave)=

# RisingWave

```{div}
:style: "float: right; margin-left: 0.5em"
[![](https://www.risingwave.com/_next/static/media/risingwave-logo-black-text.11ccd229.svg){w=180px}](https://www.risingwave.com/)
```

[RisingWave] is a stream processing and management platform that allows
configuring data sources, views on that data, and destinations where
results are materialized.
It provides both a Postgres-compatible SQL interface, like CrateDB,
and a DataFrame-style Python interface.

![RisingWave overview](https://github.com/user-attachments/assets/5bd27415-300d-4b8a-aa47-196eed041ed7){h=200px}

> Deliver fresh, low-latency insights from real-time streams,
> database CDC, and time-series data. Bring streaming and batch together,
> let users join and analyze both live and historical data, and persist
> results in managed Apache Iceberg™ tables.

:::{dropdown} **Managed RisingWave**
RisingWave Labs offers [managed products][RisingWave pricing]
for building prototypes, production workloads, and enterprise-level, critical
applications.
:::

```{div}
:style: "clear: both"
```

## Synopsis

:::{rubric} RisingWave
:::
Load an Apache Iceberg table, and serve it as materialized view.
```sql
CREATE SOURCE sensors_readings
WITH (
  connector = 'iceberg',
  database.name='db.db',
  warehouse.path='s3://warehouse/',
  table.name='sensors_readings',
  s3.endpoint = '<YOUR_S3_ENDPOINT>',
  s3.access.key = '<YOUR_S3_ACCESS_KEY>',
  s3.secret.key = '<YOUR_S3_SECRET_KEY>',
  s3.region = '<YOUR_S3_REGION_NAME>'
);
```
```sql
CREATE MATERIALIZED VIEW average_sensor_readings AS
SELECT
  sensor_id,
  AVG(reading) AS average_reading
FROM sensors_readings
GROUP BY sensor_id;
```
:::{rubric} CrateDB
:::
Converge into a CrateDB table for long-term persistence and efficient querying,
even on large amounts of data.
```sql
CREATE TABLE public.average_sensor_readings (
  sensor_id BIGINT PRIMARY KEY,
  average_reading DOUBLE
);
```
:::{note}
The standard approach with RisingWave would be to use its [CREATE SINK] operation
to connect to an external target.
However, because this does not currently support CrateDB, a little Python event processor
is needed to relay the data. An example implementation can be found in the tutorial
referenced below.
:::

## Learn

:::{rubric} Tutorials
:::
- An example with data coming from an Apache Iceberg table and aggregations
  materialized in real-time in CrateDB, using RisingWave.
  See {ref}`iceberg-risingwave`.

:::{note}
We are tracking interoperability issues per [Tool: RisingWave] and appreciate
any contributions and reports.
:::


[CREATE SINK]: https://docs.risingwave.com/sql/commands/sql-create-sink
[RisingWave]: https://github.com/risingwavelabs/risingwave
[RisingWave pricing]: https://www.risingwave.com/pricing/
[Tool: RisingWave]: https://github.com/crate/crate/labels/tool%3A%20RisingWave
