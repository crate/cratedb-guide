# Storage Usage

CrateDB stores data using both row and columnar stores, with automatic
indexing on every column, enabling efficient searches without requiring
manual index creation. Indexes are leveraged for reads, and depending on
the query, the engine uses the most efficient store.

This is one of the many features that makes CrateDB very fast when reading
and aggregating data, but it has an impact on storage size.

We are going to
use [Yellow taxi trip - January 2024](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
which has 2_964_624 rows.

| VendorID | tpep_pickup_datetime | tpep_dropoff_datetime | passenger_count | trip_distance | RatecodeID | store_and_fwd_flag | PULocationID | DOLocationID | payment_type | fare_amount | extra | mta_tax | tip_amount | tolls_amount | improvement_surcharge | total_amount | congestion_surcharge | Airport_fee |
|----------|----------------------|-----------------------|-----------------|---------------|------------|--------------------|--------------|--------------|--------------|-------------|-------|---------|------------|--------------|-----------------------|--------------|----------------------|-------------|
| 2        | 1704073016000        | 1704074392000         | 4               | 6.88          | 1          | "N"                | 170          | 231          | 1            | 32.4        | 1     | 0.5     | 7.48       | 0            | 1                     | 44.88        | 2.5                  | 0           |
| 1        | 1704071008000        | 1704072649000         | 0               | 4.1           | 1          | "N"                | 148          | 233          | 2            | 22.6        | 3.5   | 0.5     | 0          | 0            | 1                     | 27.6         | 2.5                  | 0           |
| 1        | 1704071126000        | 1704071510000         | 2               | 1             | 1          | "N"                | 140          | 141          | 1            | 7.9         | 3.5   | 0.5     | 2.55       | 0            | 1                     | 15.45        | 2.5                  | 0           |
| 2        | 1704072696000        | 1704073070000         | 1               | 1.03          | 1          | "N"                | 262          | 75           | 1            | 8.6         | 1     | 0.5     | 2.72       | 0            | 1                     | 16.32        | 2.5                  | 0           |
| 2        | 1704074134000        | 1704074399000         | 1               | 1.08          | 1          | "N"                | 249          | 68           | 1            | 7.2         | 1     | 0.5     | 2.44       | 0            | 1                     | 14.64        | 2.5                  | 0           |

The taxi dataset takes:

- ~48MiB in Parquet (very optimized for storage)
- ~342MiB in CSV
- ~1.2GiB in JSON
- ~510MiB in PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1)
- ~775MiB in CrateDB 5.9.3 (3 nodes, default settings)
- ~431MiB in CrateDB 5.10.9 (3 nodes, default settings)

We will dive deeper to really understand what is going on.

:::{note}
In version 5.10 storage usage was improved, some users report up to 70% of storage reduction,
more reasonably a 30–50% can be expected for most data, the reduction percentage will vary
depending on the use case.

Read more at https://cratedb.com/blog/reducing-storage-costs-in-cratedb-v5.10

This guide has been updated to reflect the v5.10 improvements.
:::

## How storage in CrateDB works

CrateDB is a distributed database; nodes, shards, partitions and replicas are tightly integrated.

When a table is created, data is sharded and distributed among nodes. This
means that the memory footprint depends on our replication and sharding strategy.

Let's break down how the `431MiB` in CrateDB 5.10 and the `510MiB` in PostgreSQL were
obtained. For `PostgreSQL` it was straightforward:

```sql
SELECT pg_size_pretty(pg_total_relation_size('taxi_january'));
```

In CrateDB, when a table is created, sharding and replication have to be taken into account.
When a table is created with default values, it gets split in a number of shards derived using
this formula: `max(4, num_data_nodes * 2)`.

For example, on a typical 3-nodes cluster, it will create:

`num_data_nodes = 3`

`max(4, 3 * 2) = 6 shards`

On top of that, the default replication is the `0-1` range: a maximum of one replica.
A replica multiplies the number of shards, therefore creating `6 primary shards` and
`6 replica shards`, making
`12 shards` physically distributed among the three nodes.

![CrateDB shards allocation](/_assets/img/performance/shards.png)

The number of shards and tables per node can be checked by querying the `sys.shards` table:

```sql
SELECT sum(num_docs)         document_count,
       node                  ['name'] node, count(*) shard_count,
       array_agg(table_name) shard_table_names
FROM sys.shards
GROUP BY node ['name']
```

The total storage being used by a table can be calculated as the `average size of 1 shard` *
`total_shards`.

Applying this to the `taxi` table that was created beforehand:

```sql
SELECT TRUNC(sum(size / (1024.0 * 1024.0)) / count(*), 2),
       TRUNC(sum(size) / (1024.0 * 1024.0), 2) as total_mib
FROM sys.shards
WHERE table_name = 'taxi'
```

CrateDB v5.9.3

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 61.59             | 739.12    |

CrateDB v5.10.9

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 35.89             | 430.79    |

The average size of a shard is ~35MiB; `35.89MiB * 12 shards = ~430.68 MiB`.

You can check the actual size of a shard by inspecting the filesystem.
Use `select table_name, path from sys.shards` to show the file path of the individual shards.

```shell
sh-5.1# pwd
/data/data/nodes/0/indices/LeFVb9VMT_G68tZs0vOuyA
sh-5.1# du -sh ./* | sort -h
8.0K	./_state
36M	./2
36M	./3
36M	./4
36M	./5
```

## Reducing storage

The following techniques can help to reduce the average size of one shard.

Please note reducing disk usage often comes at the cost of performance.

If there are columns that will not be used in aggregations (joins) and groupings (group by, order
by),
it will have no impact on performance and might make sense to reduce its storage footprint.

Things that can be done:

- disable indexing
- disable the columnar store
- call optimize table (only in >=v5.10)
- change the compression algorithm
- review the data schema

> Disk size improvements can vary depending on the data types, schema and even disk manufacturer.
> This example is intended for illustrative purposes only.

## Disable indexing

By default, CrateDB creates indexes on every column; this can be disabled when creating the table:

```sql
CREATE TABLE taxi_noindex
(
    "VendorID"              BIGINT INDEX OFF,
    "tpep_pickup_datetime"  TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
    "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF, ...
)
```

The index can only be disabled when the table is created, if the table already exists,
it will have to be re-created.

One of the ways of re-creating a table is by `renaming`, for example:

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

:::{attention}
Dropping the table deletes the data, make sure that the copy was done correctly.
:::

:::{attention}
Disabled indexes can't be re-added without recreating the table.
:::

### Effects on storage

CrateDB v5.9.3

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 53                | 635       |

CrateDB v5.10.9

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 23                | 285       |

Disk space used was reduced `~13.11%` in v5.9 - original was **739.12MiB**
Disk space used was reduced `~33.87%` in v5.10 - original was **430.79MiB**

## Disable the columnar store

The columnar store can be disabled at table creation with:

```sql
CREATE TABLE IF NOT EXISTS "doc"."taxi_nocolumnstore"
(
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

CrateDB v5.9.3

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 53                | 639       |

CrateDB v5.10.9

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 39                | 471       |

Disk space used was reduced `~13.11%` in v5.9 similar to `no_index` - original was **739.12MiB**
Disk space used was increased `~10%` in v5.10 - original was **430.79MiB**

:::{note}
When columnstore is off, data needs to be stored somewhere else (row store), which is less efficient
in terms of disk usage, as column stores are designed specifically for each datatype.

In v5.10, we don’t recommend that you turn off column storage.
:::

## Upgrade to v5.10 and `OPTIMIZE TABLE`

CrateDB v5.10 introduced a new table storage format that can reduce storage up to 50% in comparison.

The easiest way to gain massive storage reduction is to update to the latest version available.

Additionally, as part of CrateDB's background operations, index segments are merged and optimized;
you would typically see storage usage being automatically reduced as more data gets added to the
table. Nonetheless, you can trigger these optimizations manually by running:

`OPTIMIZE TABLE <table_name> WITH (max_num_segments=1)`

If a table is ingesting data continuously, it makes sense to let CrateDB merge and optimize the
segments.
If you run this command and storage usage doesn't decrease within minutes; it's most likely
that they were already optimized.

## Changing the compression algorithm

Data is compressed when it is stored on disk, two options are available `default` (LZ4) and
`best_compression`.

`best_compression` might be less performant on certain queries, but it has less storage footprint.

It can be changed via table definition:

```sql
CREATE TABLE IF NOT EXISTS "doc"."taxi_january_nocolumnstore"
(
    "VendorID" BIGINT, ...
) WITH (codec = 'best_compression')
```

### Effects on storage

CrateDB v5.9.3

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 44                | 536       |

CrateDB v5.10.9

| avg_mib_per_shard | total_mib |
|-------------------|-----------|
| 36                | 436       |

Disk space used was reduced `~27.86%` in v5.9 - original was **739.12MiB**
Disk space used was reduced `~1%` in v5.10 - original was **430.79MiB**

> In v5.10 depending on your data, changing the compression algorithm might not yield storage
> improvements.

## All results and what to do

In the following table, all the above results can be found, also different combinations of them:

```sql
SELECT table_name,
       SUM(num_docs)                          as records,
       (SUM(size) / (1024 * 1024))            as total_size_mib,
       (SUM(size) / count(*)) / (1024 * 1024) as avg_mib_per_shard,
       (SUM(size) / SUM(num_docs) :: DOUBLE)  as avg_bytes_per_record
FROM sys.shards
WHERE table_name LIKE 'taxi%'
GROUP BY 1
ORDER BY total_size_mib
```

CrateDB v5.9.3

| table_name                                   | records | total_size_mib | avg_mib_per_shard | avg_bytes_per_record |
|----------------------------------------------|---------|----------------|-------------------|----------------------|
| "taxi__noindex_nocolumnstore_bestcompresion" | 2964624 | 122            | 20                | 41                   |
| "taxi_nocolumnstore_bestcompression"         | 2964624 | 205            | 34                | 69                   |
| "taxi_noindex_bestcompression"               | 2964624 | 212            | 35                | 71                   |
| "taxi_noindex_nocolumnstore"                 | 2964624 | 237            | 39                | 80                   |
| "taxi_bestcompresion"                        | 2964624 | 290            | 48                | 98                   |
| "taxi_noindex"                               | 2964624 | 317            | 52                | 107                  |
| "taxi_nocolumnstore"                         | 2964624 | 319            | 53                | 107                  |
| "taxi"                                       | 2964624 | 385            | 64                | 130                  |

CrateDB v5.10.9

| table_name                                   | records | total_size_mib | avg_mib_per_shard | avg_bytes_per_record |
|----------------------------------------------|---------|----------------|-------------------|----------------------| 
| "taxi_noindex_nocolumnstore_bestcompression" | 2964624 | 113            | 18                | 40.01650765830675    |
| "taxi_noindex_bestcompression"               | 2964624 | 135            | 22                | 47.98841067197729    |
| "taxi_noindex"                               | 2964624 | 142            | 23                | 50.380041448763826   |
| "taxi_noindex_nocolumnstore"                 | 2964624 | 152            | 25                | 53.92698838031399    |
| "taxi_nocolumnstore_bestcompression"         | 2964624 | 195            | 32                | 69.21123150861627    |
| "taxi"                                       | 2964624 | 215            | 35                | 76.17595485970566    |
| "taxi_bestcompression"                       | 2964624 | 218            | 36                | 77.14465341979286    |
| "taxi_nocolumnstore"                         | 2964624 | 236            | 39                | 83.49627406375986    |

To summarize:

1. `total_size_mib` is the sum of the disk used in `MiB` of all the primary shards.
2. All primary shards make up the full table.
3. By default, every table will have a maximum of one replica.

The original `775MiB` in v5.9 can be calculated as:

`64MiB per shard * (6 primary shards + 6 replica shards) = 768 MiB`

> The result are slightly off `768 ~= 775` because in this example, decimals are being truncated.
> The goal is to give you an idea on how tweaking some CrateDB aspect can affect storage, being
> overly precise to the kilobyte level doesn’t matter too much.

Query with everything applied:

```sql
CREATE TABLE IF NOT EXISTS "doc"."taxi_nocolumnstore_noindex_bestcompression"
(
    "VendorID" BIGINT INDEX OFF STORAGE WITH(
        columnstore = false
) ,
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

If some columns are never used for aggregations or groupings, there will be no performance penalty.
That might change in the future as your use case and data evolve, re-adding indexes or column store
at later stages is tricky, as the table will need to be re-created and data copied over,
which might need some downtime, depending on the setup.

When designing your data model, it is important to evaluate your current and future needs to
minimize
any future overhead.

## Extra: Data normalization

One of the most common ways to reduce storage size is to not write data more than once, by
normalizing your tables.

We encourage you to read more about [database normalization].

[database normalization]: https://en.wikipedia.org/wiki/Database_normalization
