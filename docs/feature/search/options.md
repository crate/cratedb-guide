(fts-options)=
(fulltext-options)=

# Full-text Search Options

(fts-fuzzy)=
(fuzzy-search)=
## Fuzzy Search

> In a table with firstname and lastname, find matches that tolerate
> minor inversions from user input, such as `WHERE lastname = 'bronw'`,
> while the record actually includes `lastname = 'brown'`.

When accepting user input, a common approach in information retrieval to
compensate for search or spelling corrections, is to apply fuzzy searching.
CrateDB's MATCH function accepts a `fuzziness` option which provides that
feature.

:::{rubric} Examples
:::

Using a single fulltext index.
```sql
-- Start with a blank canvas.
DROP TABLE IF EXISTS person;

-- Define table schema, using a full-text index on the "lastname" column.
CREATE TABLE person (
  firstname VARCHAR,
  lastname VARCHAR, 
  INDEX lastname_ft USING FULLTEXT (lastname));

-- Provide a few samples worth of data.
INSERT INTO person (firstname, lastname)
VALUES ('charly', 'brown'), ('charly', 'braun'), ('charly', 'browne');  

-- Synchronize writes.
REFRESH TABLE person;

-- Invoke a full-text query including a typing error.
SELECT firstname, lastname, _score
FROM person
WHERE MATCH(lastname_ft, 'bronw') USING best_fields WITH (fuzziness=2)
ORDER BY _score DESC;
```

```postgresql
+-----------+----------+------------+
| firstname | lastname |     _score |
+-----------+----------+------------+
| charly    | brown    | 0.18904014 |
| charly    | browne   | 0.18904014 |
+-----------+----------+------------+
SELECT 2 rows in set (0.009 sec)
```

Using two fulltext indexes within a single query, and two typos.
```sql
-- Start with a blank canvas.
DROP TABLE IF EXISTS documents;

-- Define table schema, using two full-text indexes on the "name" column.
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

-- Provide a few samples worth of data.
INSERT INTO documents (name, description)
VALUES
  ('Quick fox', 'The quick brown fox jumps over the lazy dog.'),
  ('Franz jagt', 'Franz jagt im komplett verwahrlosten Taxi quer durch Bayern.')
;

-- Synchronize writes.
REFRESH TABLE documents;

-- Invoke a full-text query on both indexes.
SELECT name, _score
FROM documents
WHERE MATCH((ft_english, ft_german), 'jupm OR verwrlost')
  USING best_fields WITH (fuzziness=1)
ORDER BY _score DESC;
```

```postgresql
+------------+------------+
| name       |     _score |
+------------+------------+
| Franz jagt | 0.10170578 |
| Quick fox  | 0.06538229 |
+------------+------------+
SELECT 2 rows in set (0.017 sec)
```


:::{todo}
Describe other full-text search options.
:::
