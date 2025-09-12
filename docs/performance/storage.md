# Storage Usage

CrateDB stores data in a row and column store, and automatically creates an index on top of that.
On reads, the index will be leveraged: Depending on the query, the engine will use the most efficient store.

This is one of the many features that makes CrateDB very fast when reading
and aggregating data, but it has an impact on storage size.

We are going to use [Yellow taxi trip - January 2024](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) which has 2_964_624 rows.

This is the schema:

```sql
CREATE TABLE IF NOT EXISTS "doc"."taxi" (
   "VendorID" BIGINT,
   "tpep_pickup_datetime" TIMESTAMP WITHOUT TIME ZONE,
   "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE,
   "passenger_count" BIGINT,
   "trip_distance" REAL,
   "RatecodeID" BIGINT,
   "store_and_fwd_flag" TEXT,
   "PULocationID" BIGINT,
   "DOLocationID" BIGINT,
   "payment_type" BIGINT,
   "fare_amount" REAL,
   "extra" REAL,
   "mta_tax" REAL,
   "tip_amount" REAL,
   "tolls_amount" REAL,
   "improvement_surcharge" REAL,
   "total_amount" REAL,
   "congestion_surcharge" REAL,
   "Airport_fee" REAL
)
```

It takes:

- ~`48MiB` in Parquet
- ~`342MiB` in CSV
- ~`1.2GiB` in JSON
- ~`510MiB` in PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1)
- ~`775MiB` in CrateDB 5.9.3 (3 nodes, default settings)

At first sight, it might look that in CrateDB data takes more space than in PostgreSQL,
but we need to dive deeper to really understand what is going on, the reality is the opposite.

## Table of contents

1. [How storage works](#how-storage-in-cratedb-works)
2. [Reducing storage](#reducing-storage)
3. [Disable indexing](#disable-indexing)
4. [Disable columnar store](#disable-the-columnar-store)
5. [Changing the compression algorithm](#changing-the-compression-algorithm)
6. [All results](#all-results-and-what-to-do)
7. [Data normalization](#extra-data-normalization)

## How storage in CrateDB works.

CrateDB is a distributed database; nodes, shards, partitions and replicas are tightly integrated.

When a table is created, data is sharded and distributed among nodes. This
means that the memory footprint depends on our replication and sharding strategy.

Let's break down how the `775MiB` in CrateDB and the `510MiB` in PostgreSQL were
obtained. For `PostgreSQL` it was straightforward:

```sql
SELECT pg_size_pretty(pg_total_relation_size('taxi_january'));
```

For CrateDB when a table is created, sharding and replication has to be taken into account.
When a table is created with default values, it gets partitioned in `max(4, num_data_nodes * 2)` shards.
For example, a typical 3-node cluster, it will create:

`max(4, 3 * 2) = 6 shards` 

On top of that, the default replication is the `0-1` range, a maximum of one replica.
A replica multiplies the number of shards, therefore creating `6 primary shards` and `6 replica shards`, making
`12 total shards` physically distributed among the three nodes.

![CrateDB shards allocation](/_assets/img/performance/shards.png)


You can see how many shards you have per node and table by querying the `sys.shards` table, or use
this query to have a broad overlook:

The number of shards per node and table can be checked by querying the `sys.shards` table:

```sql
SELECT sum(num_docs)         document_count,
       node                  ['name'] node, count(*) shard_count,
       array_agg(table_name) shard_table_names
FROM sys.shards
GROUP BY node ['name']
```

The total storage being used, can be calculated as the `avg size of 1 shard` * `total_shards`.

Applying this to the `taxi` table that was created beforehand:

```sql
SELECT sum(size / (1024 * 1024)) / count(*) as avg_mb_per_shard,
       sum(size) / (1024 * 1024) as total_mib
FROM sys.shards
WHERE table_name = 'taxi'

-- | avg_mib_per_shard | total_mib |
-- |------------------|----------|
-- | 61               | 739      |

```


This can be checked locally; querying `select table_name, path from sys.shards` shows the file path of the shard.

```shell
sh-5.1# pwd
/data/data/nodes/0/indices/LeFVb9VMT_G68tZs0vOuyA
sh-5.1# du -sh ./* | sort -h
8.0K	./_state
63M	./2
63M	./3
63M	./4
63M	./5
```

## Reducing storage

The following techniques can help to reduce the average size of one shard.

Please note reducing disk usage often comes at the cost of performance.

If there are columns that will not be used in aggregations (joins) and groupings (group by, order by),
it will have no impact on performance and might make sense to reduce its storage footprint.

Things that can be done:

- disable indexing
- disable the columnar store
- change the compression algorithm
- review the data schema

> Disk size improvements can vary depending on the data types, schema and even disk manufacturer. This example is intended for
> illustrative purposes only.

## Disable indexing

By default, CrateDB creates indexes on every column; this can be disabled when creating the table:

```sql
CREATE TABLE taxi
(
    "VendorID"              BIGINT INDEX OFF,
    "tpep_pickup_datetime"  TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
    "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
    ...
)
```

The index can only be disabled when the table is created, if the table already exists and it cannot
be deleted, it will have to be re-created.

One of the ways of re-creating a table is by renaming it, for example:

1. Rename table `taxi` (with INDEX) to `taxi_deleteme` with:

```sql
ALTER TABLE "taxi"
    RENAME TO "taxi_deleteme"
```

2. Create the new table named `taxi` with indexes off.

3. Copy data from `taxi_deleteme` to `taxi`.

```sql
INSERT INTO "taxi" (SELECT * FROM "taxi_deleteme")
```

4. Delete `taxi_deleteme` with:

```sql
DROP TABLE "taxi_deleteme"
```

> WARNING: Dropping the table deletes the data, make sure that the copy was done correctly.

> INFO: Indexes cannot be re-added after table creation.

### Effects on storage

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 53                | 635       |

Data was reduced `~13.11%`

## Disable the columnar store.

The columnar store can be disabled at table creation with:

```sql
CREATE TABLE IF NOT EXISTS "doc"."taxi_nocolumnstore"(
    "VendorID" BIGINT STORAGE WITH(
        columnstore = false
   ) ,
   "tpep_pickup_datetime" TIMESTAMP WITHOUT TIME ZONE STORAGE WITH (
      columnstore = false
   ),
   "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE STORAGE WITH (
      columnstore = false
   ),
    ...
)
```

> As with indexing, it can only be turned off at table creation time.

### Effects on storage

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 53                | 639       |

Data was reduced: `~13.11%`, similar to `no_index`.

## Changing the compression algorithm

Data is compressed when it is stored on disk, two options are available `default` (LZ4) and
`best_compression`.

`best_compression` might be less performant on certain queries, but it has less storage footprint.

You can change it via table definition:

```sql
CREATE TABLE IF NOT EXISTS "doc"."taxi_january_nocolumnstore" (
    "VendorID" BIGINT,
    ...
) WITH (codec = 'best_compression')
```

### Effects on storage

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 44                | 536       |

Data was reduced: `~27.86%`

## All results and what to do.

In the following table, all the above results can be found, also different combinations of them:

```sql
SELECT table_name,
       SUM(num_docs)           as records,
       (SUM(size) / (1024 * 1024)) as total_size_mb,
       (SUM(size) / count(*)) / (1024 * 1024) as avg_size_per_shard_in_mib,
       (SUM(size) / SUM(num_docs) :: DOUBLE) as avg_size_in_bytes_per_record
FROM sys.shards
WHERE
    PRIMARY
GROUP BY
    1
ORDER BY
    avg_size_per_shard_in_mb
```

| table_name                                  | records | total_size_mib | avg_size_per_shard_in_mib | avg_bytes_per_record |
|---------------------------------------------|---------|----------------|---------------------------|----------------------|
| "taxi_nocolumnstore_noindex_bestcompresion" | 2964624 | 122            | 20                        | 41                   |
| "taxi_nocolumnstore_bestcompression"        | 2964624 | 205            | 34                        | 69                   |
| "taxi_noindex_bestcompression"              | 2964624 | 212            | 35                        | 71                   |
| "taxi_nocolumnstore_noindex"                | 2964624 | 237            | 39                        | 80                   |
| "taxi_bestcompresion"                       | 2964624 | 290            | 48                        | 98                   |
| "taxi_noindex"                              | 2964624 | 317            | 52                        | 107                  |
| "taxi_nocolumnstore"                        | 2964624 | 319            | 53                        | 107                  |
| "taxi"                                      | 2964624 | 385            | 64                        | 130                  |

To summarize:

1. `total_size_mib` is the sum of the disk used in `MiB` of all the primary shards
2. All primary shards make the full table.
3. By default, every table will have a maximum of one replica.

The original `775MiB` can be calculated as:

`64mb per shard * (6 primary shards + 6 replica shards) = 768`

> The result are slightly off `768 ~= 775` because in this example, decimals are being ignored.
> The goal is to give you an idea on how tweaking some CrateDB aspect can affect storage, being
> overly precise to the kilobyte level does not matter too much.

Query with everything applied:

```sql
CREATE TABLE IF NOT EXISTS "doc"."taxi_nocolumnstore_noindex_bestcompresion" (
   "VendorID" BIGINT INDEX OFF STORAGE WITH (
      columnstore = false
   ),
   "tpep_pickup_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF STORAGE WITH (
      columnstore = false
   ),
   "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF STORAGE WITH (
      columnstore = false
   ),
   ...
   WITH (codec = 'best_compression')
```

### What to do

CrateDB's default settings are optimized for performance.

If some columns will never be used for aggregations or groupings, there will be no performance penalty.
That might change in the future as your use case and data needs evolve,
re-adding indexes or column store at later stages will need re-creating tables, 
which might need some downtime, depending on the setup.

When designing your data model, it is important to evaluate your current and future needs to minimize
any future overhead.

## Extra: Data normalization

One of the most common ways to reduce storage size is to not write data more than once, by normalizing your tables.

Read more about it in https://en.wikipedia.org/wiki/Database_normalization

