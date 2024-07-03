(blob)=
# BLOB Store

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

**CrateDB provides a blob/object storage subsystem accessible via HTTP,
similar to AWS S3.**

:::{rubric} Overview
:::
CrateDB includes support to store [binary large objects], using its
[](inv:crate-reference#blob_support) feature / subsystem. By utilizing
CrateDB's cluster features, the files can be replicated and sharded just
like regular data.
::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

```{rubric} Reference Manual
```
- [](inv:crate-reference#blob_support)

{tags-primary}`BLOB Storage`
{tags-primary}`Object Storage`
::::

:::::


## Synopsis

Example DDL statement.
```sql
CREATE BLOB TABLE myblobs CLUSTERED INTO 8 SHARDS with (number_of_replicas=3);
```


## Learn

Learn how to use CrateDB's BLOB store.

- [Exploring Blob storage in CrateDB]
- [Python driver support for BLOBs]


:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
"About", "Details", and "Usage" sections are missing, and others need expansion.
:::


[binary large objects]: https://en.wikipedia.org/wiki/Object_storage
[Exploring Blob storage in CrateDB]: https://community.cratedb.com/t/exploring-blob-storage-in-cratedb/938
[Python driver support for BLOBs]: inv:crate-python:*:*label#blobs
