(document)=
(object)=

# Document Store

<style>
.wrapper-content-right ul {
  margin-left: 0;
}
.rubric-slim p.rubric {
  margin-bottom: 0;
}
.title-slim .sd-col > * {
  margin-top: 0;
  margin-bottom: 0;
}
.no-margin > * {
  margin-top: 0 !important;
  margin-bottom: 0 !important;;
}
</style>


::::{grid}
:padding: 0
:class-row: rubric-slim

:::{grid-item}
:columns: 9

Learn how to efficiently store JSON documents or other structured data, also
nested, using CrateDB's `OBJECT` and `ARRAY` container data types, and how to
query this data with ease.

Even when using dynamic objects, i.e. when working without a strict object
schema, all attributes are indexed by default, and can be queried efficiently.

Storing documents in CrateDB provides the same convenience like the
document-oriented storage layers of Lotus Notes / Domino, CouchDB,
MongoDB, or PostgreSQL's `JSON(B)` types.

With CrateDB, compatible to PostgreSQL, you can do all of that using plain SQL.
Other than integrating well with commodity systems using standard database
access interfaces like ODBC or JDBC, it provides a proprietary HTTP interface
on top.
:::

:::{grid-item}
:columns: 3

```{rubric} Reference Manual
```
- [](inv:crate-reference#data-types-container)
- [Querying](inv:crate-reference#sql_dql_container)
- [](inv:crate-reference#scalar-objects)
- [](inv:crate-reference#scalar-arrays)
- [](inv:crate-reference#sql_dql_array_comparisons)
- [Non-existing keys](inv:crate-reference#conf-session-error_on_unknown_object_key)



```{rubric} Related
```
- [](#fulltext)
- [](#geospatial)
- [](#machine-learning)
- [](#analytics)

{tags-primary}`JSON`
{tags-primary}`Container`
{tags-primary}`Document`
{tags-primary}`Object`
{tags-primary}`Array`
{tags-primary}`Nested`
{tags-primary}`Indexed`
:::

::::


## About

CrateDB uses Lucene as a storage layer, so it inherits its concepts
about storage entities and units, in the same spirit as Elasticsearch.

:Document:
  In Lucene, the **Document** is a fundamental entity, as it is the unit of
  search and index. An index consists of one or more Documents.

:Field:
  A Document consists of one or more Fields. A Field is simply a name-value pair.

While Elasticsearch uses a [query DSL based on JSON], in CrateDB, you can work
with Lucene Documents using SQL.


## Synopsis

Store and query structured data, in this case blending capabilities of
InfluxDB and MongoDB, but with much more headroom for other features,
and using SQL instead of proprietary query languages.

::::{grid}
:padding: 0
:class-row: title-slim

:::{grid-item} **DDL**
:columns: 4

```sql
CREATE TABLE reading (
  "timestamp" TIMESTAMP, 
  "tags" OBJECT(DYNAMIC), 
  "fields" OBJECT(DYNAMIC)
);
```
:::

:::{grid-item} **DML**
:columns: 4

```text
INSERT INTO reading (
  timestamp,
  tags,
  fields
) VALUES (
  '2024-03-02T23:42:42',
  { 
    "sensor_id" = '4834CC52',
    "site_id" = 23 
  },
  { 
    "temperature" = 42.42,
    "humidity" = 84.84
  }
);
```
:::

:::{grid-item} **DQL**
:columns: 4

```sql
SELECT
  *
FROM
  reading
WHERE
  tags['sensor_id'] = 
  '4834CC52';
```
:::

::::

:::{div} no-margin
**Result**
```text
+---------------+------------------------------------------+-------------------------------------------+
|     timestamp | tags                                     | fields                                    |
+---------------+------------------------------------------+-------------------------------------------+
| 1709422962000 | {"sensor_id": "4834CC52", "site_id": 23} | {"humidity": 84.84, "temperature": 42.42} |
+---------------+------------------------------------------+-------------------------------------------+
SELECT 1 row in set (0.058 sec)
```
:::


## Usage

Working with structured data and container data types in CrateDB.

```{rubric} Object Column Strictness
```
For columns of type OBJECT, CrateDB supports different policies about the
behaviour with undefined attributes, namely STRICT, DYNAMIC, and IGNORED,
see [](inv:crate-reference#type-object-column-policy).

:STRICT:
  Reject any sub-column that is not defined upfront.
:DYNAMIC:
  INSERT operations may dynamically add new sub-columns to the
  object definition. This is the default setting.
:IGNORED:
  Also means DYNAMIC, but dynamically added sub-columns do not cause a
  schema update, and the new values will not be indexed.
  Because IGNORED columns are not recorded in the schema, you can
  insert mixed types into them. For example, one row may insert an integer and
  the next row may insert an object. Objects with a STRICT or DYNAMIC column
  policy do not allow this.


```{rubric} Querying DYNAMIC OBJECTs
```
To support querying DYNAMIC OBJECTs using SQL, where keys may not exist within
an OBJECT, CrateDB provides the [error_on_unknown_object_key] session setting. 
It controls the behaviour of querying unknown object keys to dynamic objects.

By default, CrateDB will throw an error if any of the queried object keys are
unknown. When adjusting this setting to `false`, it will return `NULL` as the
value of the corresponding key.

:::{dropdown} Example using `SET error_on_unknown_object_key = false;`
```
cr> CREATE TABLE testdrive (item OBJECT(DYNAMIC));
CREATE OK, 1 row affected  (0.563 sec)

cr> SELECT item['unknown'] FROM testdrive;
ColumnUnknownException[Column item['unknown'] unknown]

cr> SET error_on_unknown_object_key = false;
SET OK, 0 rows affected  (0.001 sec)

cr> SELECT item['unknown'] FROM testdrive;
+-----------------+
| item['unknown'] |
+-----------------+
+-----------------+
SELECT 0 rows in set (0.051 sec)
```
:::


## Learn

Written tutorials and video guides about working with CrateDB's
container data types.


:::{rubric} Tutorials
:::


::::{info-card}

:::{grid-item} **Blog: Handling Dynamic Objects in CrateDB**
:columns: 9

CrateDB combines the advantages of typical SQL databases and strict
schemas with the dynamic properties of NoSQL databases. While traditional
object-relational databases allow you to store and process JSON data only
opaquely, CrateDB handles objects as first-level citizens.

This allows users to access object properties in the same manner as columns
in a table, including full-text indexing and aggregation capabilities.
:::

:::{grid-item}
:columns: 3

[Handling Dynamic Objects in CrateDB]

{tags-primary}`Fundamentals` \
{tags-secondary}`SQL`
:::

::::


::::{info-card}

:::{grid-item} **The Basics of CrateDB Objects**
:columns: 9

Learn the basics of CrateDB Objects. This tutorial is also available
as video [Getting Started with CrateDB Objects]. 
:::

:::{grid-item}
:columns: 3

[Objects in CrateDB]

{tags-primary}`Fundamentals` \
{tags-secondary}`Docker`
{tags-secondary}`SQL`
:::

::::


::::{info-card}

:::{grid-item} **Querying Nested Structured Data**
:columns: 9

Today's data management tasks need to handle multi-structured data from
different data sources. CrateDB's dynamic OBJECT data type allows you to
store and analyze complex and nested data efficiently.

In this tutorial, we will explore how to leverage this feature in marketing
data analysis, along with the use of [generated columns], to parse and manage
URLs.
:::

:::{grid-item}
:columns: 3

[](#objects-basics)

{tags-primary}`Fundamentals`
{tags-secondary}`SQL`
:::

::::




:::{rubric} Videos
:::


::::{info-card}

:::{grid-item} **Getting Started with CrateDB Objects**
:columns: 8

In this video, you will learn the basics of CrateDB Objects. It illustrates
a simple use case to demonstrate how CrateDB Objects can add clarity
to data models.

- [Getting Started with CrateDB Objects]

The talk gives an overview of the column policies for CrateDB
OBJECTs: dynamic, strict, and ignored. It also provides examples
of how these policies affect INSERT statements. Last but not least,
it outlines how to insert, update, and delete records with OBJECT
data types.
:::

:::{grid-item}
:columns: 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/aQi9MXs2irU?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Date:** 10 Aug 2022 \
**Speakers:** Rafaela Sant'ana

{tags-primary}`Fundamentals` \
{tags-secondary}`SQL`
:::

::::



::::{info-card}

:::{grid-item} **Ingesting and Querying JSON Documents with SQL**
:columns: 8

Learn how to unleash the power of nested data with CrateDB on behalf
of an IoT use case, and a marketing analytics use case, using deeply
nested data.

- [Unleashing the Power of Nested Data: Ingesting and Querying JSON Documents with SQL]

:::

:::{grid-item}
:columns: 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/S_RHmdz2IQM?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

**Date:** 15 May 2023 \
**Speakers:** Georg Traar

{tags-primary}`Fundamentals` \
{tags-secondary}`SQL`
:::

::::


:::{seealso} **Product:**
[Multi-model Database] •
[JSON Database] •
[Dynamic Database Schemas] •
[Nested Data Structure]
:::


[Dynamic Database Schemas]: https://cratedb.com/product/features/dynamic-schemas
[error_on_unknown_object_key]: inv:crate-reference#conf-session-error_on_unknown_object_key
[generated columns]: #generated-columns
[Getting Started with CrateDB Objects]: https://youtu.be/aQi9MXs2irU?feature=shared
[Handling Dynamic Objects in CrateDB]: https://cratedb.com/blog/handling-dynamic-objects-in-cratedb
[JSON Database]: https://cratedb.com/solutions/json-database
[Multi-model Database]: https://cratedb.com/solutions/multi-model-database
[Nested Data Structure]: https://cratedb.com/product/features/nested-data-structure
[Objects in CrateDB]: https://community.cratedb.com/t/objects-in-cratedb/1188
[query DSL based on JSON]: https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html
[Unleashing the Power of Nested Data: Ingesting and Querying JSON Documents with SQL]: https://youtu.be/S_RHmdz2IQM?feature=shared

```{toctree}
:maxdepth: 1
:hidden:

objects-hands-on
```
