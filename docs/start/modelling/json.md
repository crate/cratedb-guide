(model-json)=
# JSON data

CrateDB combines the flexibility of NoSQL document stores with the power of SQL.
It enables you to store, query, and index **semi-structured JSON data** using
**standard SQL**, making it an excellent choice for applications that handle
diverse or evolving schemas.

CrateDB’s support for dynamic objects, nested structures, and bracket notation
querying brings the best of both relational and document-based data
modelling — without leaving the SQL world.

## A Simple Table with JSON

CrateDB allows you to define **object columns** that can store JSON-style data
structures.

```sql
CREATE TABLE events (
  id TEXT PRIMARY KEY,
  timestamp TIMESTAMP,
  payload OBJECT(DYNAMIC)
);
```

This allows inserting flexible, nested JSON data into `payload`:

```json
{
  "user": {
    "id": 42,
    "name": "Alice"
  },
  "action": "login",
  "device": {
    "type": "mobile",
    "os": "iOS"
  }
}
```

## Column Policy — Strict vs Dynamic

You can control how CrateDB handles unexpected fields in an object column:

| Column Policy | Behavior                                                    |
| ------------- | ----------------------------------------------------------- |
| `DYNAMIC`     | New fields are automatically added to the schema at runtime |
| `STRICT`      | Only explicitly defined fields are allowed                  |
| `IGNORED`     | Extra fields are stored but not indexed or queryable        |

Let’s evolve our table to restrict the structure of `payload`:

```sql
CREATE TABLE events2 (
  id TEXT PRIMARY KEY,
  timestamp TIMESTAMP,
  payload OBJECT(STRICT) AS (
    temperature DOUBLE,
    humidity DOUBLE
  )
);
```

You can no longer use fields other than temperature and humidity in the payload
object.

## Querying JSON Fields

Use **bracket notation** to access nested fields:

```sql
SELECT payload['temperature'], payload['humidity']
FROM events2
WHERE payload['temperature'] >= 20.0;
```

CrateDB also supports **filtering, sorting, and aggregations** on nested values:

```sql
-- count events with high humidity
SELECT COUNT(*) AS high_humidity_events
FROM events2
WHERE payload['humidity'] > 70
```

```{note}
Bracket notation works for both explicitly and dynamically added fields.
```

## Querying DYNAMIC OBJECTs Safely

When working with dynamic objects, some keys may not exist. CrateDB provides the
[error_on_unknown_object_key](inv:crate-reference:*:label#conf-session-error_on_unknown_object_key)
session setting to control behavior in such cases.

By default, CrateDB will raise an error if any of the queried object keys are
unknown. When adjusting this setting to `false`, it will return `NULL` as the
value of the corresponding key.

```sql
cr> CREATE TABLE events (payload OBJECT(DYNAMIC));
CREATE OK, 1 row affected  (0.563 sec)

cr> SELECT payload['unknown'] FROM events;
ColumnUnknownException[Column payload['unknown'] unknown]

cr> SET error_on_unknown_object_key = false;
SET OK, 0 rows affected  (0.001 sec)

cr> SELECT payload['unknown'] FROM events;
+-------------------+
| payload['unknown']|
+-------------------+
+-------------------+
SELECT 0 rows in set (0.051 sec)
```

## Aggregating JSON Fields

CrateDB allows full SQL-style aggregations on nested fields:

```sql
SELECT AVG(payload['temperature']) AS avg_temp
FROM events3
WHERE payload['humidity'] > 20.0;
```

## Combining Structured & Semi-Structured Data

As you can see in the events table, CrateDB supports **hybrid schemas**, mixing
standard columns with JSON fields.

This allows you to:

* Query by fixed attributes (`temperature`)
* Flexibly store structured or unstructured metadata in `payload`
* Add new fields on the fly without migrations

## Indexing Behavior

CrateDB **automatically indexes** object fields if:

* Column policy is `DYNAMIC`
* Field type can be inferred at insert time

You can also explicitly define and index object fields. Let’s extend the payload
with a message field with full-text index, and also disable index for `humidity`:

```sql
CREATE TABLE events3 (
  id TEXT PRIMARY KEY,
  timestamp TIMESTAMP,
  tags ARRAY(TEXT),
  payload OBJECT(DYNAMIC) AS (
    temperature DOUBLE,
    humidity DOUBLE INDEX OFF,
    message TEXT INDEX USING FULLTEXT
  )
);
```

```{note}
Too many dynamic fields can lead to schema explosion. Use `STRICT` or `IGNORED`
if needed.
```

CrateDB also supports **`GROUP BY`**, **`HAVING`**, and **window functions** on
object fields.

## Further Learning & Resources

* Reference Manual:
  * {ref}`Objects <crate-reference:data-types-objects>`
  * {ref}`Object Column policy <crate-reference:type-object-column-policy>`
  * {ref}`json data type <crate-reference:data-type-json>`
  * {ref}`Inserting objects as JSON <crate-reference:data-types-object-json>`
