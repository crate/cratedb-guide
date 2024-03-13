(join)=
(relational)=

# Relational / JOINs

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: 9


:::{rubric} Overview
:::
CrateDB implements the relational concept of joining tables.

:::{rubric} About
:::
When selecting data from CrateDB, you can join one or more relations
(tables) to combine columns into one result set.

Joins are essential operations in relational databases. They create a
link between rows based on common values and allow the meaningful
combination of these rows.

CrateDB supports joins effectively from the beginning and, due to its
distributed nature, allows you to work with large amounts of data.
::::



::::{grid-item}
:class: rubric-slim
:columns: 3

```{rubric} Reference Manual
```
- [Join concepts][manual-join-concept]
- [Join types][manual-join-types]
- [Joined relation][manual-joined-relation]

```{rubric} Related
```
- {ref}`sql`
- {ref}`query`
- {ref}`fulltext`
- {ref}`geospatial`
- {ref}`vector`

{tags-primary}`SQL`
{tags-primary}`JOIN`
::::

:::::


::::{info-card}

:::{grid-item} **Blog: Support for Joins on Multi-Row Sub-Selects**
:columns: auto 9 9 9
:class: rubric-slim

Joining on virtual tables is a crucial feature for many users, and it is
especially useful when doing analytics on your data.
A virtual table is what we call the result set returned by a subquery.

Being able to use sub-selects as virtual tables for the lifetime of a query
is very useful because it means that you can slice and dice your data multiple
ways without having to alter your source data, or store duplicate versions of
it.

{{ '{}[blog-join-vtable]'.format(blog) }}

```{rubric} Example
```
```sql
SELECT *
      FROM (SELECT *
              FROM table_1
          ORDER BY column_a
             LIMIT 100)
        AS virtual_table_1,
INNER JOIN (SELECT *
              FROM (SELECT *
                      FROM table_2
                  ORDER BY column_b
                     LIMIT 100)
                AS virtual_table_2
          GROUP BY column_c)
        AS virtual_table_3
     ON virtual_table_1.column_a = 
        virtual_table_3.column_a
```
:::

:::{grid-item}
:columns: 3
{tags-primary}`Lab Notes`

{tags-secondary}`Join Feature`
{tags-secondary}`Sub-Selects`

{tags-info}`2018`
:::

::::


::::{info-card}

:::{grid-item} **Blog: How We Made Joins 23 Thousand Times Faster**
:columns: auto 9 9 9

Introduces you to the nested-loop join, equi-join, sorted merge vs.
hash join, and the block hash join algorithms, and the advancement
into a distributed block hash join algorithm.

This blog post illustrates the implementation of the distributed
block hash join algorithm to support users who want to run joins
on large tables for their analytics needs.

[![Joins x23 - Part 1](https://img.shields.io/badge/Open-Part%201-darkblue?logo=GitHub)][blog-joins-faster-part1]
[![Joins x23 - Part 2](https://img.shields.io/badge/Open-Part%202-darkblue?logo=GitHub)][blog-joins-faster-part2]
[![Joins x23 - Part 2](https://img.shields.io/badge/Open-Part%203-darkblue?logo=GitHub)][blog-joins-faster-part3] \
{material-outlined}`link;1.3em` [FOSDEM '22: Distributed Join Algorithms in CrateDB]
:::

:::{grid-item}
:columns: 3
{tags-primary}`Lab Notes`

{tags-secondary}`CrateDB Internals`
{tags-secondary}`Join Algorithms`

{tags-info}`2018`
:::

::::


::::{info-card}

:::{grid-item} **Blog: Fine-tuning the query optimizer in CrateDB**
:columns: auto 9 9 9
:class: rubric-slim

In cases where you need it, the query optimizer, which tries to find the best
logical plan possible for a given query, can be fine-tuned for specific
queries, in order to yield better performance.

By default, the effective join order is based on table statistics collected
into the `pg_catalog.pg_stats` system table.

CrateDB offers the option to disable join-reordering and rely exactly on the
order of the tables as described in the query, which is helpful to get more
control over the query execution.

{{ '{}[blog-join-reordering]'.format(blog) }}

```{rubric} Example
```
```sql
SET optimizer_reorder_hash_join = false;
SET optimizer_reorder_nested_loop_join = false;
```
:::


:::{grid-item}
:columns: 3
{tags-primary}`Tuning Tipps`

{tags-secondary}`Join Performance`
{tags-secondary}`Performance Settings`

{tags-info}`2023`
:::

::::


:::{seealso}
**Features:**
[](#querying)

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


[blog-joins-faster-part1]: https://cratedb.com/blog/joins-faster-part-one
[blog-joins-faster-part2]: https://cratedb.com/blog/lab-notes-how-we-made-joins-23-thousand-times-faster-part-two
[blog-joins-faster-part3]: https://cratedb.com/blog/lab-notes-how-we-made-joins-23-thousand-times-faster-part-three
[blog-join-reordering]: https://cratedb.com/blog/join-performance-to-the-rescue
[blog-join-vtable]: https://cratedb.com/blog/joins-multi-row-subselects
[FOSDEM '22: Distributed Join Algorithms in CrateDB]: https://cratedb.com/resources/videos/distributed-join-algorithms
[manual-join-concept]: inv:crate-reference#concept-joins
[manual-join-types]: inv:crate-reference#sql_joins
[manual-joined-relation]: inv:crate-reference#sql-select-joined-relation
