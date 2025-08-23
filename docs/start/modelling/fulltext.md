(model-fulltext)=
# Full-text data

CrateDB features **native full‑text search** powered by **Apache Lucene** and Okapi BM25 ranking, fully accessible via SQL. You can blend this seamlessly with other data types—JSON, time‑series, geospatial, vectors and more—all in a single SQL query platform.

## Data Types & Indexing Strategy

* By default, all text columns are indexed as `plain` (raw, unanalyzed)—efficient for equality search but not suitable for full‑text queries
* To enable full‑text search, you must define a **FULLTEXT index** with an optional language **analyzer**, e.g.:

```sql
CREATE TABLE documents (
  title       TEXT,
  body        TEXT,
  INDEX ft_body USING FULLTEXT(body) WITH (analyzer = 'english')
);
```

* You may also define **composite full-text indices**, indexing multiple columns at once:

```sql
INDEX ft_all USING FULLTEXT(title, body) WITH (analyzer = 'english');
```

## Index Design & Custom Analyzers

| Component         | Purpose                                                                      |
| ----------------- | ---------------------------------------------------------------------------- |
| **Analyzer**      | Tokenizer + token filters + char filters; splits text into searchable terms. |
| **Tokenizer**     | Splits on whitespace/characters.                                             |
| **Token Filters** | e.g. lowercase, stemming, stop‑word removal.                                 |
| **Char Filters**  | Pre-processing (e.g. stripping HTML).                                        |

CrateDB offers **built-in analyzers** for many languages (e.g. English, German, French). You can also **create custom analyzers**:

```sql
CREATE ANALYZER myanalyzer (
  TOKENIZER whitespace,
  TOKEN_FILTERS (lowercase, kstem),
  CHAR_FILTERS (html_strip)
);
```

Or **extend** a built-in analyzer:

```sql
CREATE ANALYZER german_snowball
  EXTENDS snowball
  WITH (language = 'german');
```

## Querying: MATCH Predicate & Scoring

CrateDB uses the SQL `MATCH` predicate to run full‑text queries against full‑text indices. It optionally returns a relevance score `_score`, ranked via BM25.

**Basic usage:**

```sql
SELECT title, _score
FROM documents
WHERE MATCH(ft_body, 'search term')
ORDER BY _score DESC;
```

**Searching multiple indices with weighted ranking:**

```sql
MATCH((ft_title boost 2.0, ft_body), 'keyword')
```

**You can configure match options like:**

* `using best_fields` (default)
* `fuzziness = 1` (tolerate minor typos)
* `operator = 'AND'` or `OR`
* `slop = N` for phrase proximity

**Example: Fuzzy Search**

```sql
SELECT firstname, lastname, _score
FROM person
WHERE MATCH(lastname_ft, 'bronw') USING best_fields WITH (fuzziness = 2)
ORDER BY _score DESC;
```

This matches similar names like ‘brown’ or ‘browne’.

**Example: Multi‑language Composite Search**

```sql
CREATE TABLE documents (
  name        STRING PRIMARY KEY,
  description TEXT,
  INDEX ft_en USING FULLTEXT(description) WITH (analyzer = 'english'),
  INDEX ft_de USING FULLTEXT(description) WITH (analyzer = 'german')
);
SELECT name, _score
FROM documents
WHERE MATCH((ft_en, ft_de), 'jupm OR verwrlost') USING best_fields WITH (fuzziness = 1)
ORDER BY _score DESC;
```

## Use Cases & Integration

CrateDB is ideal for searching **semi-structured large text data**—product catalogs, article archives, user-generated content, descriptions and logs.

Because full-text indices are updated in real-time, search results reflect newly ingested data almost instantly. This tight integration avoids the complexity of maintaining separate search infrastructure.

You can **combine full-text search with other data domains**, for example:

```sql
SELECT *
FROM listings
WHERE 
  MATCH(ft_desc, 'garden deck') AND
  price < 500000 AND
  within(location, :polygon);
```

This blend lets you query by text relevance, numeric filters, and spatial constraints, all in one.

## Architectural Strengths

* **Built on Lucene inverted index + BM25**, offering relevance ranking comparable to search engines.
* **Scale horizontally across clusters**, while maintaining fast indexing and search even on high volume datasets.
* **Integrated SQL interface**: eliminates need for separate search services like Elasticsearch or Solr.

## Best Practices Checklist

| Topic               | Recommendation                                                                     |
| ------------------- | ---------------------------------------------------------------------------------- |
| Schema & Indexing   | Define full-text indices at table creation; plain indices are insufficient.        |
| Language Support    | Pick built-in analyzer matching your content language.                             |
| Composite Search    | Use multi-column indices to search across title/body/fields.                       |
| Query Tuning        | Configure fuzziness, operator, boost, and slop options.                            |
| Scoring & Ranking   | Use `_score` and ordering to sort by relevance.                                    |
| Real-time Updates   | Full-text indices update automatically on INSERT/UPDATE.                           |
| Multi-model Queries | Combine full-text search with geo, JSON, numerical filters.                        |
| Analyze Limitations | Understand phrase\_prefix caveats at scale; tune analyzer/tokenizer appropriately. |

## Further Learning & Resources

* **CrateDB Full‑Text Search Guide**: details index creation, analyzers, MATCH usage.
* **FTS Options & Advanced Features**: fuzziness, synonyms, multi-language idioms.
* **Hands‑On Academy Course**: explore FTS on real datasets (e.g. Chicago neighborhoods).
* **CrateDB Community Insights**: real‑world advice and experiences from users.

## **Summary**

CrateDB combines powerful Lucene‑based full‑text search capabilities with SQL, making it easy to model and query textual data at scale. It supports fuzzy matching, multi-language analysis, composite indexing, and integrates fully with other data types for rich, multi-model queries. Whether you're building document search, catalog lookup, or content analytics—CrateDB offers a flexible and scalable foundation.\
