(start-fulltext)=
# Full-text search

:::{div} sd-text-muted
CrateDB enables real-time full-text search at scale.
:::

Unlike exact-match filters, **full-text search** allows **fuzzy, linguistic matching** on human language text. It tokenizes input, analyzes language, and searches for **tokens, stems, synonyms**, etc.

CrateDB supports powerful full-text search capabilities directly via the `FULLTEXT` index and the `MATCH()` SQL predicate. This allows you to **combine unstructured search with structured filtering and aggregations**—all in one query, with no need for external search systems like Elasticsearch.

CrateDB supports you whether you are working with log messages, customer feedback, machine-generated data, or IoT event streams.

## Why CrateDB for Full-text Search?

| Feature               | Benefit                                           |
| --------------------- | ------------------------------------------------- |
| Full-text indexing    | Tokenized, language-aware search on any text      |
| SQL + search          | Combine structured filters with keyword queries   |
| JSON support          | Search within nested object fields                |
| Real-time ingestion   | Search new data immediately—no sync delay         |
| Scalable architecture | Built to handle high-ingest, high-query workloads |

## Common Query Patterns

### Basic Keyword Search

```sql
SELECT id, message
FROM logs
WHERE MATCH(message, 'authentication failed');
```

### Combine with Structured Filters

```sql
SELECT id, message
FROM logs
WHERE service = 'auth'
  AND MATCH(message, 'token expired');
```

### Search Nested JSON

```sql
SELECT id, payload['comment']
FROM feedback
WHERE MATCH(payload['comment'], 'battery life');
```

### Aggregate Search Results

```sql
SELECT COUNT(*)
FROM tickets
WHERE MATCH(description, 'login')
  AND priority = 'high';
```

## Real-World Examples

### Log and Event Search

Search logs for error messages across microservices:

```sql
SELECT timestamp, service, message
FROM logs
WHERE MATCH(message, 'connection reset')
ORDER BY timestamp DESC
LIMIT 100;
```

### Customer Feedback Analysis

Extract customer sentiment from support messages:

```sql
SELECT payload['sentiment'], COUNT(*)
FROM feedback
WHERE MATCH(payload['message'], 'slow performance')
GROUP BY payload['sentiment'];
```

### Anomaly Investigation

Search across telemetry events for unexpected patterns:

```sql
SELECT *
FROM device_events
WHERE MATCH(payload['error_message'], 'overheat');
```

## Language Support and Analyzers

CrateDB supports language-specific analyzers, enabling more accurate matching across different natural languages. You can specify analyzers during table creation or at query time.

```sql
CREATE TABLE docs ( id INTEGER, text TEXT INDEX USING FULLTEXT WITH (analyzer = 'english') ); 
```

To use a specific analyzer in a query:

```sql
SELECT * FROM docs WHERE MATCH(text, 'power outage') USING 'english';
```

## Indexing and Performance Tips

| Tip                              | Why It Helps                              |
| -------------------------------- | ----------------------------------------- |
| Use `TEXT` with `FULLTEXT` index | Enables tokenized search                  |
| Index only needed fields         | Reduce indexing overhead                  |
| Pick appropriate analyzer        | Match the language and context            |
| Use `MATCH()` not `LIKE`         | Full-text is more performant and relevant |
| Combine with filters             | Boost performance using `WHERE` clauses   |

## Further reading

:::::{grid} 1 3 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`article;1.5em` Reference
:columns: 3
- {ref}`crate-reference:sql_dql_fulltext_search`
- {ref}`crate-reference:fulltext-indices`
- {ref}`crate-reference:predicates_match`
- {ref}`crate-reference:ref-create-analyzer`
::::

::::{grid-item-card} {material-outlined}`link;1.5em` Related
:columns: 3
- {ref}`start-geospatial`
- {ref}`start-vector`
- {ref}`start-hybrid`
::::

::::{grid-item-card} {material-outlined}`read_more;1.5em` Read more
:columns: 6
- [How CrateDB differs from Elasticsearch]
- [Tutorial: Full-text search on logs]
- {ref}`FTS feature details <fulltext-search>`
- {ref}`Data modeling with FTS <model-fulltext>`
::::

:::::


[How CrateDB differs from Elasticsearch]: https://archive.fosdem.org/2018/schedule/event/cratedb/
[Tutorial: Full-text search on logs]: https://community.cratedb.com/t/storing-server-logs-on-cratedb-for-fast-search-and-aggregations/1562
