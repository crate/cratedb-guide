==============
Storage Usage
==============

CrateDB stores data in a row and column store, on top of that, it automatically creates an index, on reads
the index will be leveraged, and depending on the query, it will use the most efficient store.

This is one of the many features that makes CrateDB very fast when reading
and aggregating data, but it has an impact on storage.

We are going to use [Yellow taxi trip - January 2024](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) which has 2_964_624 rows

|VendorID|tpep_pickup_datetime|tpep_dropoff_datetime|passenger_count|trip_distance|RatecodeID|store_and_fwd_flag|PULocationID|DOLocationID|payment_type|fare_amount|extra|mta_tax|tip_amount|tolls_amount|improvement_surcharge|total_amount|congestion_surcharge|Airport_fee|
 |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|2|1704073016000|1704074392000|4|6.88|1|"N"|170|231|1|32.4|1|0.5|7.48|0|1|44.88|2.5|0|
|1|1704071008000|1704072649000|0|4.1|1|"N"|148|233|2|22.6|3.5|0.5|0|0|1|27.6|2.5|0|
|1|1704071126000|1704071510000|2|1|1|"N"|140|141|1|7.9|3.5|0.5|2.55|0|1|15.45|2.5|0|
|2|1704072696000|1704073070000|1|1.03|1|"N"|262|75|1|8.6|1|0.5|2.72|0|1|16.32|2.5|0|
|2|1704074134000|1704074399000|1|1.08|1|"N"|249|68|1|7.2|1|0.5|2.44|0|1|14.64|2.5|0|

will take:

- 48MB in parquet (Parquet is very optimized for storage)
- 342MB in CSV
- 1.2GB in json
- 510MB in PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1)
- 775MB in CrateDB 5.9.3 (3 nodes, default values)

At first sight, it might look that CrateDB storage takes more than PostgreSQL, but we need to dive deeper to really
understand what is going on.

## Table of contents
1. [How storage works](#Storage in CrateDB)
2. [Reducing storage](#reducing-storage)
3. [Disable indexing](#disable-indexing)
4. [Disable columnar store](#disable-the-columnar-store)
5. [Changing the compression algorithm](#changing-the-compression-algorithm)
6. [All results](#all-results)
7. [Data normalization](#data-normalization)

## How storage in CrateDB works.

CrateDB is a distributed database; nodes, shards, partitions and replicas are tightly integrated.

When a table is created data is sharded and distributed among nodes, this means that the memory footprint depends on
our replication and sharding strategy.

Let's break down how the `775MB` in CrateDB and the 510MB in Postgres were obtained, for `Postgres` it was straightforward:

.. code-block:: sql
SELECT pg_size_pretty( pg_total_relation_size('taxi_january') );

But for CrateDB when a table is created, sharding and replication has to be taken into account.

Issuing `create table my_table (my_column TEXT)` will create `max(4, num_data_nodes * 2)` shards.

For example, a typical 3-node cluster, it will create:

.. code-block::

`max(4, 3 * 2)`

`max(4, 6)`

`6` shards

On top of that, the default replication is the `0-1` range, so we will have a maximum of one replica, a replica multiplies the number of shards, so we will have
`6 primary shards` and `6 replica shards`, `12 total shards` physically distributed among the three nodes.

![shards.png](shards.png)

You can see how many shards you have per node and table by querying the `sys.shards` table, or use this query to have a broad overlook:

.. code-block:: sql

SELECT
  sum(num_docs) document_count,
  node ['name'] node,
  count(*) shard_count,
  array_agg(table_name) shard_table_names
FROM
  sys.shards
GROUP BY
  node ['name']

The total storage being used, can be calculated as the `avg size of 1 shard` * `total_shards`, in other words.

To check this, on the current `taxi` table that was created:

.. code-block:: sql

SELECT
  sum(size / 1_000_000) / count(*) as avg_mb_per_shard,
  sum(size) / 1_000_000 as total_mb
FROM
  sys.shards
WHERE
  table_name = 'taxi'

|avg_mb_per_shard|total_mb|
 |-|-|
|64|775|

Lets check the real disk usage, by querying `select path from sys.shards` the path where the data is stored on disk can be found.

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

As you can see, `~64M` that was gotten from querying `sys.shards`

The techniques that will be shown will reduce the disk usage of the `avg size of 1 shard`

## Reducing storage

There are a few things that can be done to reduce storage, at the cost of performance.

If there are columns that will not be used in aggregations (joins) and groupings (group by, order by),
it will have no impact on performance and might make sense to reduce its storage footprint.

We can:

- disable indexing
- disable the columnar store
- change the compression algorithm
- review your data schema

In this guide, we will explore and see how these techniques affect storage size and performance in CrateDB.

> Storage size and performance can vary significantly depending on the data schema used. This example is intended for illustrative purposes only, your mileage might vary.

## Disable indexing

By default, CrateDB creates indexes on every column; you can disable this when creating the table:

.. code-block:: sql
CREATE TABLE taxi
(
   "VendorID" BIGINT INDEX OFF,
   "tpep_pickup_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
   "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
    ...
)

The index can only be disabled when the table is created if the table is already created, and it cannot be deleted it
because there is data, it will have to be re-created.

One of the ways to achieve this is by renaming the tables, for example:

1. Rename table 'taxi' (with INDEX) to 'taxi_deleteme' with:

.. code-block:: sql
ALTER TABLE "taxi" RENAME TO "taxi_deleteme"

2. Create the new table named 'taxi'.

3. Copy data from 'taxi_deleteme' to 'taxi'.

4. Delete 'taxi_deleteme' with:

.. code-block:: sql
DROP TABLE "taxi_deleteme"

> WARNING Dropping the table deletes the data, make sure that the copy was done correctly.
> INFO: Indexing cannot be created afterward.

### Effects on storage

|avg_mb_per_shard|total_mb|
 |-|-|
|53|635|

Data was reduced `~18%`

## Disable the columnar store.

The columnar store can be disabled at table creation with

.. code-block:: sql
CREATE TABLE IF NOT EXISTS "doc"."taxi_nocolumnstore" (
   "VendorID" BIGINT STORAGE WITH (
      columnstore = false
   ),
   "tpep_pickup_datetime" TIMESTAMP WITHOUT TIME ZONE STORAGE WITH (
      columnstore = false
   ),
   "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE STORAGE WITH (
      columnstore = false
   ),
    ...
)


> As with indexing, you cannot re-add the column store once the table is created.

### Effects on storage

|avg_mb_per_shard|total_mb|
 |-|-|
|53|639|

Data was reduced: `-18%`, similar to no index.

## Changing the compression algorithm

Data is compressed when it is stored on disk, two options are available default (LZ4) and best_compression.

`best_compression` might be less performant on certain queries, but it has less storage footprint.

You can change it via table definition:

.. code-block:: sql
CREATE TABLE IF NOT EXISTS "doc"."taxi_january_nocolumnstore" (
   "VendorID" BIGINT STORAGE WITH (
      columnstore = false
   ),
    ...
) WITH (codec = 'best_compression')

### Effects on storage

|avg_mb_per_shard|total_mb|
|-|-|
|44|536|

Data was reduced: `31.25%`

## All results and what to do.

In the following table, all the above results can be found, also different combinations of them:

.. code-block:: sql

SELECT
  table_name,
  SUM(num_docs) as records,
  (SUM(size) / 1_000_000) as total_size_mb,
  (SUM(size) / count(*)) / 1_000_000 as avg_size_per_shard_in_mb,
  (SUM(size) / SUM(num_docs) :: DOUBLE) as avg_size_in_bytes_per_record
FROM
  sys.shards
WHERE
  PRIMARY
GROUP BY
  1
ORDER BY
  avg_size_per_shard_in_mb

|table_name|records|total_size_mb|avg_size_per_shard_in_mb|avg_size_in_bytes_per_record|
 |-|-|-|-|-|
|"taxi_nocolumnstore_noindex_bestcompresion"|2964624|122|20|41.172756140407685|
|"taxi_nocolumnstore_bestcompression"|2964624|205|34|69.38882367544754|
|"taxi_noindex_bestcompression"|2964624|212|35|71.51773007302107|
|"taxi_nocolumnstore_noindex"|2964624|237|39|80.03273905898354|
|"taxi_bestcompresion"|2964624|290|48|98.0695295592291|
|"taxi_noindex"|2964624|317|52|107.09909081219068|
|"taxi_nocolumnstore"|2964624|319|53|107.62769578874084|
|"taxi"|2964624|385|64|130.15281533172504|

To recapitulate: `total_size_mb` is the sum of the disk used in `mb` of all the primary shards, all primary shards make the full table.
By default every table will have a maximum of one replica.

The original `775MB` can be calculated as:

`64mb per shard * (6 primary shards + 6 replica shards) = 768`

> We get `768 ~= 775` because in reality it's not exactly `64mb` per shard, we are ignoring decimals.
> The goal is to give you an idea on how tweaking some CrateDB aspect can affect storage, being overly precise to the kilobyte level
> does not matter too much.

### What to do
Normally TODO

## Extra: Data normalization

One of the most common ways to reduce storage usage is to not write data more than once, by normalizing your tables.

Looking at this table:

[data]

We are writing `column` two times, this table is in a normalized N2 state, if normalize to 3N, it would resort in:

[data]

For this table definition, for one million rows, there is a % storage reduction.

You can read more about data normalization at [link]