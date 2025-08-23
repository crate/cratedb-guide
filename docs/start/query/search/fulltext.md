# Full-text search

CrateDB supports powerful **full-text search** capabilities directly within its distributed SQL engine. This allows you to **combine unstructured search with structured filtering and aggregations**—all in one query, with no need for external search systems like Elasticsearch.

Whether you're working with log messages, customer feedback, machine-generated data, or IoT event streams, CrateDB enables **real-time full-text search at scale**.

## What Is Full-text Search?

Unlike exact-match filters, full-text search allows **fuzzy, linguistic matching** on human language text. It tokenizes input, analyzes language, and searches for **tokens, stems, synonyms**, etc.

CrateDB enables this via the `FULLTEXT` index and the `MATCH()` SQL predicate.

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

## When to Use CrateDB for Full-text Search

CrateDB is ideal when you need to:

* Search human-generated data (logs, comments, messages)
* Perform search + filtering + aggregation in a **single SQL query**
* Handle **real-time ingestion** and **search immediately**
* Avoid managing a separate search engine or ETL pipeline
* Search **text within structured or semi-structured data**

## Related Features

| Feature               | Description                                          |
| --------------------- | ---------------------------------------------------- |
| Language analyzers    | Built-in support for many languages                  |
| JSON object support   | Index and search nested fields                       |
| SQL + full-text       | Unified queries for structured and unstructured data |
| Distributed execution | Fast, scalable search across nodes                   |
| Aggregations          | Group and analyze search results at scale            |

## Learn More

* Full-text Search Data Model
* MATCH Clause Documentation
* How CrateDB Differs from Elasticsearch
* Tutorial: Full-text Search on Logs

## Summary

CrateDB delivers fast, scalable, and **SQL-native full-text search**—perfect for modern applications that need to search and analyze semi-structured or human-generated text in real time. By merging search and analytics into a **single operational database**, CrateDB simplifies your stack while unlocking rich insight.
