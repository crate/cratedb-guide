(document)=
(object)=

# Document Store

:::{include} /_include/links.md
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 9 9 9


:::{rubric} Overview
:::
Learn how to efficiently store JSON documents or other structured data, also
nested, using CrateDB's OBJECT and ARRAY container data types, and how to
query this data with ease.

CrateDB combines the advantages of typical SQL databases and strict
schemas with the dynamic properties of NoSQL databases. While traditional
object-relational databases allow you to store and process JSON data only
opaquely, CrateDB handles objects as first-level citizens.

:::{rubric} About
:::
This feature allows users to access object properties in the same manner as
columns in a table, including {ref}`full-text indexing <fulltext>` and
{ref}`aggregation <aggregation>` capabilities.

Even when using dynamic objects, i.e. when working without a strict object
schema, all attributes are indexed by default, and can be queried efficiently.

Storing documents in CrateDB provides the same convenience like the
document-oriented storage layers of Lotus Notes / Domino, CouchDB,
MongoDB, or PostgreSQL's JSON(B) types.

:::{rubric} Details
:::

CrateDB uses Lucene as a storage layer, so it inherits its concepts
about storage entities and units, in the same spirit as Elasticsearch.

:Document:
  In Lucene, the **Document** is a fundamental entity, as it is the unit of
  search and index. An index consists of one or more Documents.

:Field:
  A Document consists of one or more Fields. A Field is simply a name-value pair.

While Elasticsearch uses a [query DSL based on JSON], in CrateDB, you can work
with Lucene Documents using SQL.
::::


::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

```{rubric} Reference Manual
```
- {ref}`crate-reference:data-types-container`
- [Querying containers](inv:crate-reference#sql_dql_container)
- {ref}`crate-reference:scalar-objects`
- {ref}`crate-reference:scalar-arrays`
- {ref}`crate-reference:sql_dql_array_comparisons`
- [Non-existing keys](inv:crate-reference#conf-session-error_on_unknown_object_key)

```{rubric} Related
```
- {ref}`sql`
- {ref}`connect`
- {ref}`fulltext`
- {ref}`query`
- {ref}`geospatial`
- {ref}`machine-learning`
- {ref}`analytics`

{tags-primary}`JSON`
{tags-primary}`Container`
{tags-primary}`Document`
{tags-primary}`Object`
{tags-primary}`Array`
{tags-primary}`Nested`
{tags-primary}`Indexed`
::::

:::::



## Synopsis

Store and query structured data, in this case blending capabilities of
InfluxDB and MongoDB, but with much more headroom for other features,
and using SQL instead of proprietary query languages.

::::{grid}
:padding: 0
:class-row: title-slim

:::{grid-item}
:columns: auto 4 4 4
**DDL**

```sql
CREATE TABLE reading (
  "timestamp" TIMESTAMP, 
  "tags" OBJECT(DYNAMIC), 
  "fields" OBJECT(DYNAMIC)
);
```
:::

:::{grid-item}
:columns: auto 4 4 4
**DML**

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

:::{grid-item}
:columns: auto 4 4 4
**DQL**

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
see {ref}`crate-reference:type-object-column-policy`.

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
It controls the behaviour when querying unknown object keys to dynamic objects.

By default, CrateDB will raise an error if any of the queried object keys are
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


:::{rubric} Articles
:::

::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**Blog: Handling Dynamic Objects in CrateDB**

Learn fundamentals about CrateDB's OBJECT data type.

{{ '{}[Handling Dynamic Objects in CrateDB]'.format(blog) }}
:::

:::{grid-item}
:columns: auto 3 3 3

{tags-primary}`Fundamentals` \
{tags-secondary}`OBJECT`
{tags-secondary}`SQL`
:::

::::


:::{rubric} Tutorials
:::

::::{info-card}

:::{grid-item}
:columns: auto 9 9 9
**The Basics of CrateDB Objects**

Learn the basics of CrateDB Objects. This tutorial is also available
as video [Getting Started with CrateDB Objects]. 

{{ '{}[Objects in CrateDB]'.format(tutorial) }}
:::

:::{grid-item}
:columns: auto 3 3 3

{tags-primary}`Fundamentals`
{tags-primary}`Docker` \
{tags-secondary}`OBJECT`
{tags-secondary}`SQL`
:::

::::


::::{info-card}

:::{grid-item}
:columns: 9
**Querying Nested Structured Data**

Today's data management tasks need to handle multi-structured and
{ref}`nested <crate-reference:sql_dql_nested>` data from
different data sources. CrateDB's dynamic OBJECT data type allows you to
store and analyze complex and nested data efficiently.

In this tutorial, we will explore how to leverage this feature in marketing
data analysis, along with the use of [generated columns], to parse and manage
URLs.

{{ '{}(#objects-basics)'.format(tutorial) }}
:::

:::{grid-item}
:columns: auto 3 3 3

{tags-primary}`Fundamentals`
{tags-secondary}`OBJECT` \
{tags-secondary}`SQL`
:::

::::




:::{rubric} Videos
:::


::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Getting Started with CrateDB Objects**

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
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/aQi9MXs2irU?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Fundamentals` \
{tags-secondary}`OBJECT`
{tags-secondary}`SQL`
:::

::::



::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Ingesting and Querying JSON Documents with SQL**

Learn how to unleash the power of nested data with CrateDB on behalf
of an IoT use case, and a marketing analytics use case, using deeply
nested data.

- [Unleashing the Power of Nested Data: Ingesting and Querying JSON Documents with SQL]
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/S_RHmdz2IQM?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Fundamentals` \
{tags-secondary}`OBJECT`
{tags-secondary}`SQL`
:::

::::


::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Dynamic Schemas and Indexing Objects**

Learn more about OBJECTs from the perspective of dynamic schema evolution
and about OBJECT indexing.

- [Dynamic Schemas and Indexing Objects]

:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/lp51GphV9vo?start=495&si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Fundamentals` \
{tags-secondary}`OBJECT`
{tags-secondary}`SCHEMA`
:::

::::



:::{seealso} **Product:**
[Multi-model Database] •
[JSON Database] •
[Dynamic Database Schemas] •
[Nested Data Structure] •
[Relational Database]
:::



[Dynamic Schemas and Indexing Objects]: https://youtu.be/lp51GphV9vo?t=495s&feature=shared
[error_on_unknown_object_key]: inv:crate-reference#conf-session-error_on_unknown_object_key
[generated columns]: #generated-columns
[Getting Started with CrateDB Objects]: https://youtu.be/aQi9MXs2irU?feature=shared
[Handling Dynamic Objects in CrateDB]: https://cratedb.com/blog/handling-dynamic-objects-in-cratedb
[Objects in CrateDB]: https://community.cratedb.com/t/objects-in-cratedb/1188
[Unleashing the Power of Nested Data: Ingesting and Querying JSON Documents with SQL]: https://youtu.be/S_RHmdz2IQM?feature=shared

```{toctree}
:maxdepth: 1
:hidden:

learn
```
