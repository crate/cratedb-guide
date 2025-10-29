(storage-internals)=
(storage-layer)=
# Storage Layer

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
The CrateDB storage layer is based on Lucene.
:::

Lucene offers scalable and high-performance indexing, which enables efficient search and
aggregations over documents and rapid updates to the existing documents. Solr and
Elasticsearch are building upon the same technologies.
This page enumerates important concepts and implementations of Lucene used by CrateDB.

## Data structures

A single record in Lucene is called "document".

:Document:

  A document is a unit of information for search
  and indexing that contains a set of fields, where each field has a name and value. A Lucene
  index can store an arbitrary number of documents, with an arbitrary number of different fields.
  By default, all fields are indexed, nested or not, but the indexing can be turned
  off selectively.

CrateDB uses three main data structures of Lucene: Inverted indexes for text values,
BKD trees for numeric values, and doc values. Based on doc values, CrateDB implements
a column store for fast sorting and aggregations.

:Inverted index:

  The Lucene indexing strategy for text fields relies on a data structure called inverted
  index, which is defined as a "data structure storing a mapping from content, such as
  words and numbers, to its location in the database file, document or set of documents".

  Depending on the configuration of a column, the index can be plain (default) or full-text.
  An index of type "plain" indexes content of one or more fields without analyzing and
  tokenizing their values into terms. To create a "full-text" index, the field value is
  first analyzed and based on the used analyzer, split into smaller units, such as
  individual words. A full-text index is then created for each text unit separately.

  The inverted index enables a very efficient search over textual data.

:BKD tree:

  To optimize numeric range queries, Lucene uses an implementation of the Block KD (BKD)
  tree data structure. The BKD tree index structure is suitable for indexing large
  multidimensional point data sets. It is an I/O-efficient dynamic data structure based
  on the KD tree. Contrary to its predecessors, the BKD tree maintains its high space
  utilization and excellent query and update performance regardless of the number of
  updates performed on it.

  Numeric range queries based on BKD trees can efficiently search numerical fields,
  including fields defined as `TIMESTAMP` types, supporting performant date range
  queries.

:Doc values:

  Because Lucene's inverted index data structure implementation is not optimal for
  finding field values by given document identifier, and for performing column-oriented
  retrieval of data, the doc values data structure is used for those purposes instead.

  Doc values is a column-based data storage built at document index time. They store
  all field values that are not analyzed as strings in a compact column, making it more
  effective for sorting and aggregations.

:Column store:

  CrateDB implements a {ref}`column store <crate-reference:ddl-storage-columnstore>`
  based on doc values in Lucene.
  For text values, other than storing the row data as-is (and indexing each value by default),
  each value term is stored into a column-based store by default.

  This storage layout improves the performance of sorting, grouping, and aggregations,
  by keeping field data for one column packed at one place rather than scattered across documents.
  The column store is enabled by default in CrateDB and can be disabled only for text fields.
  It does not support container or geographic data types.

## Storage process

How CrateDB stores data using Lucene.

tldr; CrateDB never needs explicit VACUUMs, manual compactions, or
reindexing. The system maintains itself dynamically, which is a key advantage
for always-on analytics environments where data never stops flowing in.

:Append-only segments:

  A Lucene index is composed of one or more sub-indexes. A sub-index is called a segment,
  it is immutable, and built from a set of documents.

  When new documents are added to the
  existing index, they are added to the next segment, while previous segments are never
  modified. If the number of segments becomes too large, the system may decide to merge
  some segments and discard the freed ones. This way, adding a new document does not require
  rebuilding the whole index structure completely.

:Segment merges:

  When new data is inserted into CrateDB, it is written into small, immutable
  segments on disk. Over time, these segments are merged into larger ones by
  background tasks, balancing I/O load with query performance.

  This process, known as segment merging, achieves three critical optimizations:
  - Space compaction: Merging removes deleted or superseded records, freeing disk
  space automatically.
  - Faster queries: Larger segments reduce index overhead and improve cache efficiency.
  - No downtime: Merging occurs transparently, allowing continuous ingestion and querying.

  CrateDB uses Lucene's default TieredMergePolicy. It merges segments of roughly equal size
  and controls the number of segments per "tier" to balance search performance with merge
  overhead. Lucene's [TieredMergePolicy] documentation explains in detail how CrateDB's
  underlying merge policy decides when to combine segments.

:Table refreshes:

  CrateDB's refresh mechanism controls how often newly ingested data becomes visible
  for querying. Instead of committing every write immediately, which would degrade
  throughput, CrateDB batches writes in memory and periodically refreshes data
  segments, typically once per second by default.

  This approach strikes a balance between low-latency visibility and high ingestion
  performance, allowing users to query the most recent data almost instantly while
  maintaining efficient bulk ingestion without overwhelming the storage layer
  or exhausting other cluster resources.

::::{todo}
Enable after merging [GH-434: Indexing and storage](https://github.com/crate/cratedb-guide/pull/434).
```md
## Related sections

{ref}`indexing-and-storage` illustrates the internal workings and data structures
of CrateDB's storage layer in more detail.

:::{toctree}
:hidden:
indexing-and-storage
:::
```
::::


[TieredMergePolicy]: https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/index/TieredMergePolicy.html
