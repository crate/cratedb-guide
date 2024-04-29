(fts)=
(fulltext)=
(full-text)=

# Full-Text Search

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::

**BM25 term search based on Apache Lucene, using SQL: CrateDB is all you need.**

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9


:::{rubric} Overview
:::
CrateDB can be used as a database to conduct full-text search operations
building upon the power of Apache Lucene.

CrateDB is an exceptional choice for handling complex queries and large-scale
data sets. One of its standout features are its full-text search capabilities,
built on top of the powerful Lucene library. This makes it a great fit for
organizing, searching, and analyzing extensive datasets.

:::{rubric} About
:::
[Full-text search] leverages the [BM25] search ranking algorithm, effectively
implementing the storage and retrieval parts of a [search engine].

In information retrieval, Okapi BM25 (BM is an abbreviation of best matching)
is a ranking function used by search engines to estimate the relevance of
documents to a given search query.
::::


::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

```{rubric} Reference Manual
```
- [](inv:crate-reference#sql_dql_fulltext_search)
- [](inv:crate-reference#fulltext-indices)
- [](inv:crate-reference#ref-create-analyzer)

```{rubric} Related
```
- {ref}`sql`
- {ref}`vector`
- {ref}`machine-learning`
- {ref}`query`

{tags-primary}`SQL`
{tags-primary}`Full-Text Search`
{tags-primary}`Okapi BM25`
::::

:::::


:::{rubric} Details
:::
CrateDB uses Lucene as a storage layer, so it inherits the implementation
and concepts of Lucene, in the same spirit as Elasticsearch.
The now popular BM25 method has become the default scoring formula in Lucene
and is the scoring formula used by CrateDB.

BM25 stands for "Best Match 25", the 25th iteration of this scoring algorithm.
The excellent article [BM25: The Next Generation of Lucene Relevance] compares
classic TF/IDF to [Okapi BM25], including illustrative graphs.
To learn more details about what's inside, please also refer to [Similarity in
Elasticsearch] and [BM25 vs. Lucene Default Similarity].

:::{div}
While Elasticsearch uses a [query DSL based on JSON], in CrateDB, you can work
with text search using SQL.
:::


## Synopsis

Store and query word embeddings using similarity search based on Cosine
distance.

::::{grid}
:padding: 0
:class-row: title-slim

:::{grid-item} **DDL**
:columns: auto 6 6 6

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

:::{grid-item} **DQL**
:columns: auto 6 6 6

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

::::


::::{grid}
:padding: 0
:class-row: title-slim

:::{grid-item} **DML**
:columns: auto 6 6 6

```sql
INSERT INTO documents (name, description)
VALUES
  ('Quick fox', 'The quick brown fox jumps over the lazy dog.'),
  ('Franz jagt', 'Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.')
;
```
:::

:::{grid-item} **Result**
:columns: auto 6 6 6

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

Using full-text search in CrateDB.

:::{rubric} `MATCH` predicate
:::
CrateDB's [MATCH predicate] performs a fulltext search on one or more indexed
columns or indices and supports different matching techniques.

In order to use fulltext searches on a column, a [fulltext index with an
analyzer](inv:crate-reference#sql_ddl_index_fulltext) must be created for
this column.

:::{rubric} Analyzer
:::
Analyzers consist of two parts, filters, and tokenizers. Each analyzer must
contain one tokenizer and only one tokenizer can be used.

Tokenizers decide how to divide the given text into parts. Filters perform
a series of transformations by passing the given text through a number of
operations. They are divided into token filters and character filters,
discriminating between filters applied before, or after the tokenization
step.

Popular filters are stopword lists, lowercase transformations, or word
stemmers.
The excellent article [Improve Your Text Search with Lucene Analyzers]
illustrates more details about this topic on behalf of Elasticsearch.



## Learn

Learn how to set up your database for full-text search, how to create the
relevant indices, and how to query your text data efficiently. A must-read
for anyone looking to make sense of large volumes of unstructured text data.

:::{rubric} Tutorials
:::

::::{info-card}
:::{grid-item} **Full-Text: Exploring the Netflix Catalog**
:columns: auto 9 9 9

The tutorial illustrates the BM25 ranking algorithm for information retrieval,
by exploring how to manage a dataset of Netflix titles.

{{ '{}(inv:cloud#full-text)'.format(tutorial) }}
:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`Full-Text Search` \
{tags-secondary}`BM25` \
{tags-secondary}`SQL`
:::
::::


::::{info-card}
:::{grid-item} **Custom analyzers for fuzzy text matching**
:columns: auto 9 9 9

The community discussion illustrates how to define custom analyzers for
enabling fuzzy searching, how to use synonym files, and corresponding
technical backgrounds about their implementations.

{{ '{}[custom-analyzers-fuzzy]'.format(tutorial) }}
:::
:::{grid-item}
:columns: auto 3 3 3
{tags-primary}`Introduction` \
{tags-secondary}`Full-Text Search` \
{tags-secondary}`Lucene Analyzer` \
{tags-secondary}`SQL`
:::
::::


[BM25]: https://en.wikipedia.org/wiki/Okapi_BM25
[BM25: The Next Generation of Lucene Relevance]: https://opensourceconnections.com/blog/2015/10/16/bm25-the-next-generation-of-lucene-relevation/
[BM25 vs. Lucene Default Similarity]: https://www.elastic.co/blog/found-bm-vs-lucene-default-similarity
[custom-analyzers-fuzzy]: https://community.cratedb.com/t/fuzzy-search-synonyms/889
[full-text search]: https://en.wikipedia.org/wiki/Full_text_search
[Improve Your Text Search with Lucene Analyzers]: https://medium.com/@dagliberkay/elastic-text-search-6b778de9b753
[MATCH predicate]: inv:crate-reference#predicates_match
[Okapi BM25]: https://trec.nist.gov/pubs/trec3/papers/city.ps.gz
[search engine]: https://en.wikipedia.org/wiki/Search_engine
[Similarity in Elasticsearch]: https://www.elastic.co/blog/found-similarity-in-elasticsearch
[TREC-3 proceedings]: https://trec.nist.gov/pubs/trec3/t3_proceedings.html
