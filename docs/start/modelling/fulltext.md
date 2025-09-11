(model-fulltext)=
# Full-text data

CrateDB offers **native full-text search** powered by **Apache Lucene** and Okapi
BM25 ranking, accessible via SQL for easy modelling and querying of large-scale
textual data. It supports fuzzy matching, multi-language analysis, and composite
indexing, while fully integrating with data types such as JSON, time-series,
geospatial, vectors, and more for comprehensive multi-model queries. Whether you
need document search, catalog lookup, or content analytics, CrateDB is an ideal
solution.

## Data Types & Indexing

By default, all text columns are indexed as `plain` (raw, unanalyzed)—efficient
for equality search but not suitable for full-text queries.

To use full-text search, add a FULLTEXT index with an optional analyzer to the
text columns you want to search:

```sql
CREATE TABLE documents (
  title       TEXT,
  body        TEXT,
  INDEX ft_title USING FULLTEXT(title) WITH (analyzer = 'english'),
  INDEX ft_body  USING FULLTEXT(body)  WITH (analyzer = 'english')
);
```

You can also index multiple columns with **composite full-text indices**:

```sql
INDEX ft_all USING FULLTEXT(title, body) WITH (analyzer = 'english');
```

For detailed options, check out the [Reference Manual](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/fulltext-indices.html).

## Analyzers

An analyzer splits text into searchable terms and consists of the following components:

* **Tokenizer -** splits on whitespace/characters
* **Token Filters -** e.g. lowercase, stemming, stop‑word removal
* **Char Filters -** pre-processing (e.g. stripping HTML).

CrateDB offers about 50 [**built-in analyzers**](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/analyzers.html#built-in-analyzers) supporting more than 30 [languages](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/analyzers.html#language).

You can **extend** a built-in analyzer:

```sql
CREATE ANALYZER german_snowball
  EXTENDS snowball
  WITH (language = 'german');
```

or create your own **custom** analyzer:

```sql
CREATE ANALYZER myanalyzer (
  TOKENIZER whitespace,
  TOKEN_FILTERS (lowercase, kstem),
  CHAR_FILTERS (html_strip)
);
```

Learn more about the [built-in analyzers](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/analyzers.html#built-in-analyzers) and how to [define your own](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/fulltext-indices.html#creating-a-custom-analyzer) with custom [tokenizers](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/analyzers.html#built-in-tokenizers) and [token filters.](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/analyzers.html#built-in-token-filters)


## Querying: MATCH Predicate & Scoring

CrateDB uses the SQL `MATCH` predicate to run full‑text queries against
full‑text indices. It optionally returns a relevance score `_score`, ranked via
BM25.

**Basic usage:**

```sql
SELECT title, _score FROM documents
WHERE MATCH(ft_body, 'search term')
ORDER BY _score DESC;
```

**Searching multiple indices with weighted ranking:**

```sql
SELECT title, _score FROM documents
WHERE MATCH((ft_body, ft_title 2.0), 'search term');
ORDER BY _score DESC;
```
Here `ft_title` is weighted twice as much as `ft_body`.

**You can configure match options like:**

* `using best_fields` (default)
* `fuzziness = 1` (tolerate minor typos)
* `operator = 'AND'` or `OR`
* `slop = N` for phrase proximity

**Example: Fuzzy Search**

```sql
SELECT title, _score
FROM documents
WHERE MATCH(ft_body, 'Jamse') USING best_fields WITH (fuzziness = 2)
ORDER BY _score DESC;
```

This matches similar words like ‘James’.

**Example: Multi‑language Composite Search**

```sql
CREATE TABLE documents (
  title       TEXT,
  body        TEXT,
  INDEX ft_en USING FULLTEXT(body) WITH (analyzer = 'english'),
  INDEX ft_de USING FULLTEXT(body) WITH (analyzer = 'german')
);

SELECT title, _score
FROM documents
WHERE MATCH((ft_en, ft_de), 'jupm OR verwrlost') USING best_fields WITH (fuzziness = 1)
ORDER BY _score DESC;
```

## Use Cases & Integration

CrateDB is ideal for searching **semi-structured large text data**—product
catalogs, article archives, user-generated content, descriptions and logs.

Because full-text indices are updated in real-time, search results reflect newly
ingested data almost instantly. This tight integration avoids the complexity of
maintaining separate search infrastructure.

You can **combine full-text search with other data domains**, for example:

```sql
SELECT *
FROM listings
WHERE
  MATCH(ft_desc, 'garden deck') AND
  price < 500000 AND
  within(location, :polygon);
```

This blend lets you query by text relevance, numeric filters, and spatial
constraints, all in one.

## Further Learning & Resources

* [**Full-text Search**](../../feature/search/fts/index.md): In-depth
  walkthrough of full-text search capabilities.
* Reference Manual:
  * {ref}`Full-text indices <crate-reference:fulltext-indices>`: Defining
    indices, extending builtin analyzers, custom analyzers.
  * {ref}`Full-text analyzers <crate-reference:sql-analyzer>`: Builtin
    analyzers, tokenizers, token and char filters.
  * {ref}`SQL MATCH predicate <crate-reference:sql_dql_fulltext_search>`:
    Details about MATCH predicate arguments and options.
* [**Hands‑On Academy Course**](https://learn.cratedb.com/cratedb-fundamentals?lesson=fulltext-search):
  explore FTS on real datasets (e.g. Chicago neighborhoods).
