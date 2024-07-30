(fts)=
(fulltext)=
(full-text)=
(fulltext-search)=

# Full-Text Search

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

**BM25 term search based on Apache Lucene, using SQL: CrateDB is all you need.**

:::{rubric} Overview
:::
CrateDB can be used as a database to conduct full-text search operations
building upon Apache Lucene.

CrateDB is an exceptional choice for handling complex queries and large-scale
data sets. One of its standout features are its full-text search capabilities,
built on top of the powerful Lucene library. This makes it a great fit for
organizing, searching, and analyzing extensive datasets.

:::{rubric} About
:::
[Full-text search] leverages the [BM25] search ranking algorithm, effectively
implementing the storage and retrieval parts of a [search engine].

For managing a [full-text search] index for text values, Lucene uses an
[inverted index] data structure, and the [Okapi BM25] search ranking algorithm. 

The inverted index data structure is a central component of a typical [search
engine indexing] algorithm. Together with ranking, which enables search result
relevance features, both effectively provide the storage and retrieval parts
of a [search engine].
::::


::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

```{rubric} Reference Manual
```
- [](inv:crate-reference#sql_dql_fulltext_search)
- [](inv:crate-reference#fulltext-indices)
- [](inv:crate-reference#predicates_match)
- [](inv:crate-reference#ref-create-analyzer)

```{rubric} Related
```
- {ref}`sql`
- {ref}`vector-search`
- {ref}`hybrid-search`
- {ref}`query`

{tags-primary}`SQL`
{tags-primary}`Full-Text Search`
{tags-primary}`Okapi BM25`
::::

:::::


:::{rubric} Full-text search using SQL
:::
:::{div}
CrateDB uses Lucene as a storage layer, so it inherits the implementation
and concepts of Lucene, in the same spirit as the Apache Solr search server,
and Elasticsearch.
While Elasticsearch uses a [query DSL based on JSON], in CrateDB, you can work
with text search using SQL, using a PostgreSQL-compatible interface.
:::

:::{rubric} Details about the inverted index
:::
Lucene's indexing strategy for text fields relies on a data structure called
[inverted index], which enables very efficient search over textual data, and is
defined as a "data structure storing a mapping from content, such as words and
numbers, to its location in the database file, document or set of documents".

Depending on the configuration of a column, the index can be plain (default)
or full-text. An index of type "plain" indexes content of one or more fields
without analyzing and tokenizing their values into terms.

To create a "full-text" index, the field value is first analyzed and, based on
the used analyzer, split into smaller units, such as individual words, a
processing step called tokenization. A full-text index is then created for each
text unit separately.

:::{rubric} Details about ranking with BM25
:::
In information retrieval, {abbr}`Okapi BM25 (BM is an abbreviation of "best
matching", BM25 stands for "Best Match 25", the 25th iteration of this scoring
algorithm.)` is a popular ranking function used by search engines to estimate
the relevance of documents to a given search query.
The BM25 method has become the default scoring formula in Lucene, and is also
the relevance scoring formula used by CrateDB.

The article [BM25: The Next Generation of Lucene Relevance] compares
traditional TF/IDF to BM25, including illustrative graphs.
To learn more details about what's inside, please also refer to [Similarity in
Elasticsearch] and [BM25 vs. Lucene Default Similarity].


## Synopsis

Populate and query a Lucene full-text index using SQL.

::::{grid}
:padding: 0
:class-row: title-slim

:::{grid-item}
:columns: auto 6 6 6
**DDL**

```sql
CREATE TABLE documents (
  name STRING PRIMARY KEY,
  description TEXT,
  INDEX ft_english
    USING FULLTEXT(description) WITH (
      analyzer = 'english'
    ),
  INDEX ft_german
    USING FULLTEXT(description) WITH (
      analyzer = 'german'
    )
);
```
:::

:::{grid-item}
:columns: auto 6 6 6
**DML**

```sql
INSERT INTO documents (name, description)
VALUES
  ('Quick fox', 'The quick brown fox jumps over the lazy dog.'),
  ('Franz jagt', 'Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.')
;
```
:::

:::{grid-item}
:columns: auto 6 6 6
**DQL**

```sql
SELECT name, _score
FROM documents
WHERE
  MATCH(
    (ft_english, ft_german),
    'jump OR verwahrlost'
  )
ORDER BY _score DESC;
```
:::

:::{grid-item}
:columns: auto 6 6 6
**Result**

```text
+------------+------------+
| name       |     _score |
+------------+------------+
| Franz jagt | 0.13076457 |
| Quick fox  | 0.13076457 |
+------------+------------+
SELECT 2 rows in set (0.034 sec)
```
:::

::::


## Usage

Full-text search in CrateDB means using the MATCH predicate, and optionally
configuring analyzers.

:::{rubric} MATCH predicate
:::
CrateDB's [MATCH predicate] performs a fulltext search on one or more indexed
columns or indices and supports different matching techniques.
In order to use fulltext searches on a column, a [fulltext index with an
analyzer](inv:crate-reference#sql_ddl_index_fulltext) must be created for
this column.


:::{rubric} Analyzers, Tokenizers, and Filters
:::
Analyzers consist of two parts, tokenizers and filters. With CrateDB, you
can define custom analyzers, or configure the standard analyzers according
to your needs.


## Learn

Learn how to set up your database for full-text search, how to create the
relevant indices, and how to query your text data efficiently. A few must-reads
for anyone looking to make sense of large volumes of unstructured text data.

:::{rubric} Advanced Features
:::

::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**FTS Options**

Learn about the stack of options relevant for full-text search,
like applying [](#fts-fuzzy), or using [](#fts-synonyms).

{hyper-navigate}`Full-Text Search Options <project:#fts-options>`

:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`FTS Options` \
{tags-secondary}`Fuzzy Matching` \
{tags-secondary}`Synonyms`
:::
::::


::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**Custom Analyzers**

This tutorial illustrates how to define custom analyzers using the `CREATE
ANALYZER` SQL command, for example to use fuzzy searching, how to use synonym
files, and corresponding technical backgrounds about their implementations.

{hyper-navigate}`Analyzers, Tokenizers, and Filters <project:#fts-analyzer>`

:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`Full-Text Search` \
{tags-secondary}`Lucene Analyzer`
:::
::::


:::{rubric} Tutorials
:::

::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**Exploring the Netflix catalog using full-text search**

The tutorial illustrates the BM25 ranking algorithm for information retrieval,
by exploring how to manage a dataset of Netflix titles.

{hyper-navigate}`Netflix Tutorial <search-basics>`


:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`Full-Text Search` \
{tags-secondary}`BM25`
:::
::::


:::{rubric} Articles
:::

::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**Indexing and Storage in CrateDB**

This article explores the internal workings of the storage layer in CrateDB,
with a focus on Lucene's indexing strategies.

{hyper-navigate}`Indexing and Storage in CrateDB <[Indexing and Storage in CrateDB]>`

The CrateDB storage layer is based on Lucene indexes.
Lucene offers scalable and high-performance indexing which enables efficient search
and aggregations over documents and rapid updates to the existing documents.
We will look at the three main Lucene structures that are used within CrateDB:
Inverted Indexes for text values, BKD-Trees for numeric values, and Doc Values.

:Inverted Index:
    You will learn how inverted indexes are implemented in Lucene and CrateDB.

:BKD Tree:
    Better understand the BKD tree, starting from KD trees, and how this data
    structure supports range queries in CrateDB.

:Doc Values:
    This data structure supports more efficient querying document fields by id,
    performs column-oriented retrieval of data, and improves the performance of
    aggregation and sorting operations.

:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`Lucene Indexing`
:::
::::


::::{info-card}
:::{grid-item}
:columns: auto 9 9 9
**Indexing Text for Both Effective Search and Accurate Analysis**

This article explores how Qualtrics uses CrateDB in Text iQ to provide text
analysis services for everything from sentiment analysis to 
identifying key topics, and powerful search-based data exploration.

{hyper-navigate}`Indexing Text for Both Effective Search and Accurate Analysis
<[Indexing Text for Both Effective Search and Accurate Analysis]>`

CrateDB uses Elasticsearch technology under the hood to manage cluster
creation and communication, and also exposes an Elasticsearch API that provides
access to all the indexing capabilities in Elasticsearch that Qualtrics needed.

The articles explains integral parts of an FTS text processing pipeline,
including analyzers, optionally using tokenizers or character filters,
and how they can be customized to specific needs, using plugins for CrateDB.

:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`Analyzer, Tokenizer` \
{tags-secondary}`Plugin`
:::
::::


:::{toctree}
:maxdepth: 2
:hidden:

options
analyzer
learn
:::



[BM25]: https://en.wikipedia.org/wiki/Okapi_BM25
[BM25: The Next Generation of Lucene Relevance]: https://opensourceconnections.com/blog/2015/10/16/bm25-the-next-generation-of-lucene-relevation/
[BM25 vs. Lucene Default Similarity]: https://www.elastic.co/blog/found-bm-vs-lucene-default-similarity
[full-text search]: https://en.wikipedia.org/wiki/Full_text_search
[Indexing and Storage in CrateDB]: https://cratedb.com/blog/indexing-and-storage-in-cratedb
[Indexing Text for Both Effective Search and Accurate Analysis]: https://www.qualtrics.com/eng/indexing-text-for-both-effective-search-and-accurate-analysis/
[inverted index]: https://en.wikipedia.org/wiki/Inverted_index
[MATCH predicate]: inv:crate-reference#predicates_match
[Okapi BM25]: https://trec.nist.gov/pubs/trec3/papers/city.ps.gz
[search engine]: https://en.wikipedia.org/wiki/Search_engine
[search engine indexing]: https://en.wikipedia.org/wiki/Index_(search_engine)
[Similarity in Elasticsearch]: https://www.elastic.co/blog/found-similarity-in-elasticsearch
[TREC-3 proceedings]: https://trec.nist.gov/pubs/trec3/t3_proceedings.html
