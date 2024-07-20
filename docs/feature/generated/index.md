(generated-columns)=

# Generated Columns

CrateDB's SQL DDL statements accept defining {ref}`crate-reference:ddl-generated-columns`.
Those columns values are computed by applying a generation expression in the context of
the current row. The generation expression can reference the values of other columns.


## Synopsis

:::{rubric} Canonical Example
:::
The generation expression is evaluated in the context of the current row.
```sql
CREATE TABLE computed (
  dividend double precision,
  divisor double precision,
  quotient GENERATED ALWAYS AS (dividend / divisor)
);
```


:::{rubric} Current Timestamp
:::
Populate a database column with the value of the current timestamp when inserting a row.
```sql
CREATE TABLE computed_non_deterministic (
  id LONG,
  last_modified TIMESTAMP WITH TIME ZONE GENERATED ALWAYS AS CURRENT_TIMESTAMP
);
```

:::{rubric} Partition Column
:::
Define the partition column, to control how CrateDB distributes data to shards.
```sql
CREATE TABLE computed_and_partitioned (
  huge_cardinality bigint,
  big_data text,
  partition_value GENERATED ALWAYS AS (huge_cardinality % 10)
) PARTITIONED BY (partition_value);
```


:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
It includes not even the most basic essentials, and needs expansion. For example,
the "Usage" and "Learn" sections are missing completely, and it's also not in the
same shape as the other pages in this section.
:::
