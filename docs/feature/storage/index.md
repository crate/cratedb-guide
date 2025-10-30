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
  This storage layout improves the performance of sorting, grouping, and aggregations,
  by keeping field data for one column packed at one place rather than scattered across documents.

  For all supported value types, field values are indexed and automatically stored
  in the column-based store. It does not support container or geographic data types.

  The column store is enabled by default in CrateDB and can optionally be disabled
  on a per-field level. The purpose of disabling is to reduce storage requirements
  and achieve better write performance, when the columnar store is not needed for
  those columns.

## Storage process

How CrateDB stores data using Lucene.

tldr; In daily operations, CrateDB never needs explicit VACUUMs, manual
compactions, or reindexing. [^recreate-tables]
The system maintains itself dynamically, which is a key advantage for
always-on analytics environments where data never stops flowing in.

[^recreate-tables]: While CrateDB is maintenance-free in daily operations,
  you will need to [recreate tables] on major version upgrades.

:Append-only segments:

  Lucene only appends data to segment files, which means that data written
  to the disc will never be mutated.

  A Lucene index is composed of one or more sub-indexes. A sub-index is called a segment,
  it is immutable, and built from a set of documents.

  When new documents are added to the
  existing index, they are added to the next segment, while previous segments are never
  modified. If the number of segments becomes too large, the system may decide to merge
  some segments and discard the freed ones. This way, adding a new document does not require
  rebuilding the whole index structure completely.

:Segment merges:

  When data is written to CrateDB, it is written into subsequent immutable
  segments on disk. Over time, to reduce their number, these segments are
  merged into larger ones by background tasks, balancing I/O load with
  query performance.
  This process is called {ref}`optimization <crate-reference:optimize>`.

  This process, known as segment merging, achieves three critical optimizations:
  - Space compaction: Merging removes deleted or superseded records, freeing disk
  space automatically.
  - Faster queries: Larger segments reduce index overhead and improve cache efficiency.
  - No downtime: Merging occurs transparently, allowing continuous ingestion and querying.

  CrateDB uses Lucene's default TieredMergePolicy for automatically merging segments
  in the background. It merges segments of roughly equal size
  and controls the number of segments per "tier" to balance search performance with merge
  overhead. Lucene's [TieredMergePolicy] documentation explains in detail how CrateDB's
  underlying merge policy decides when to combine segments.

  You can invoke segment merges manually by using the
  {ref}`OPTIMIZE TABLE <crate-reference:sql-optimize>` SQL command.
  This achieves the best optimization, especially after heavy insert operations,
  for example, after initially loading table data from another system.

:Table refreshes:

  CrateDB's refresh mechanism controls how often newly ingested data becomes visible
  for querying. Instead of committing every write immediately, which would degrade
  throughput, CrateDB batches writes in memory and refreshes data
  segments when needed. For performance reasons, refreshes won't happen on shards
  which aren't queried for some time (idling).

  This approach strikes a balance between low-latency visibility and high ingestion
  performance, allowing users to query the most recent data almost instantly while
  maintaining efficient bulk ingestion without overwhelming the storage layer
  or exhausting other cluster resources.

  CrateDB refreshes tables once per second by default, however this can be configured
  on a per-table level by using the {ref}`crate-reference:sql-create-table-refresh-interval`
  table parameter.
  You can also "force a refresh" manually by using the
  {ref}`REFRESH TABLE <crate-reference:sql-refresh>` SQL command.

## Related sections

{ref}`indexing-and-storage` illustrates the internal workings and data structures
of Lucene in more detail, and how CrateDB's storage layer uses them.

:::{toctree}
:hidden:
indexing-and-storage
:::


[recreate tables]: https://cratedb.com/docs/crate/reference/en/latest/admin/system-information.html#tables-need-to-be-recreated
[TieredMergePolicy]: https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/index/TieredMergePolicy.html
