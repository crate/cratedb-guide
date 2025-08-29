(model-json)=
# JSON data

CrateDB combines the flexibility of NoSQL document stores with the power of SQL. It enables you to store, query, and index **semi-structured JSON data** using **standard SQL**, making it an excellent choice for applications that handle diverse or evolving schemas.

CrateDB’s support for dynamic objects, nested structures, and dot-notation querying brings the best of both relational and document-based data modeling—without leaving the SQL world.

## Object (JSON) Columns

CrateDB allows you to define **object columns** that can store JSON-style data structures.

```sql
CREATE TABLE events (
  id UUID PRIMARY KEY,
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

## Column Policy: Strict vs Dynamic

You can control how CrateDB handles unexpected fields in an object column:

| Column Policy | Behavior                                                    |
| ------------- | ----------------------------------------------------------- |
| `DYNAMIC`     | New fields are automatically added to the schema at runtime |
| `STRICT`      | Only explicitly defined fields are allowed                  |
| `IGNORED`     | Extra fields are stored but not indexed or queryable        |

Example with explicitly defined fields:

```sql
CREATE TABLE sensor_data (
  id UUID PRIMARY KEY,
  attributes OBJECT(STRICT) AS (
    temperature DOUBLE,
    humidity DOUBLE
  )
);
```

## Querying JSON Fields

Use **bracket notation** to access nested fields:

```sql
SELECT payload['user']['name'], payload['device']['os']
FROM events
WHERE payload['action'] = 'login';
```

CrateDB also supports **filtering, sorting, and aggregations** on nested values:

```sql
SELECT COUNT(*)
FROM events
WHERE payload['device']['os'] = 'Android';
```

```{note}
Dot-notation works for both explicitly and dynamically added fields.
```

## Querying DYNAMIC OBJECTs

To support querying DYNAMIC OBJECTs using SQL, where keys may not exist within an OBJECT, CrateDB provides the [error\_on\_unknown\_object\_key](https://cratedb.com/docs/crate/reference/en/latest/config/session.html#conf-session-error-on-unknown-object-key) session setting. It controls the behaviour when querying unknown object keys to dynamic objects.

By default, CrateDB will raise an error if any of the queried object keys are unknown. When adjusting this setting to `false`, it will return `NULL` as the value of the corresponding key.

```sql
cr> CREATE TABLE testdrive (item OBJECT(DYNAMIC));
CREATE OK, 1 row affected  (0.563 sec)

cr> SELECT item['unknown'] FROM testdrive;
ColumnUnknownException[Column item['unknown'] unknown]

cr> SET error_on_unknown_object_key = false;
SET OK, 0 rows affected  (0.001 sec)

cr> SELECT item['unknown'] FROM testdrive;
+-----------------+
| item['unknown'] |
+-----------------+
+-----------------+
SELECT 0 rows in set (0.051 sec)
```

## Arrays of OBJECTs

Store arrays of objects for multi-valued nested data:

```sql
CREATE TABLE products (
  id UUID PRIMARY KEY,
  name TEXT,
  tags ARRAY(TEXT),
  specs ARRAY(OBJECT AS (
    name TEXT,
    value TEXT
  ))
);
```

Query nested arrays with filters:

```sql
SELECT *
FROM products
WHERE 'outdoor' = ANY(tags);
```

You can also filter by object array fields:

```sql
SELECT *
FROM products
WHERE specs['name'] = 'battery' AND specs['value'] = 'AA';
```

## Combining Structured & Semi-Structured Data

CrateDB supports **hybrid schemas**, mixing standard columns with JSON fields:

```sql
CREATE TABLE logs (
  id UUID PRIMARY KEY,
  service TEXT,
  log_level TEXT,
  metadata OBJECT(DYNAMIC),
  created_at TIMESTAMP
);
```

This allows you to:

* Query by fixed attributes (`log_level`)
* Flexibly store structured or unstructured metadata
* Add new fields on the fly without migrations

## Indexing Behavior

CrateDB **automatically indexes** object fields if:

* Column policy is `DYNAMIC`
* Field type can be inferred at insert time

You can also explicitly define and index object fields:

```sql
CREATE TABLE metrics (
  id UUID PRIMARY KEY,
  data OBJECT(DYNAMIC) AS (
    cpu DOUBLE INDEX USING FULLTEXT,
    memory DOUBLE
  )
);
```

To exclude fields from indexing, set:

```sql
data['some_field'] INDEX OFF
```

```{note}
Too many dynamic fields can lead to schema explosion. Use `STRICT` or `IGNORED` if needed.
```

## Aggregating JSON Fields

CrateDB allows full SQL-style aggregations on nested fields:

```sql
SELECT AVG(payload['temperature']) AS avg_temp
FROM sensor_readings
WHERE payload['location'] = 'room1';
```

CrateDB also supports **`GROUP BY`**, **`HAVING`**, and **window functions** on object fields.

## Further Learning & Resources

* Reference Manual:
  * [Objects](inv:crate-reference:*:label#data-types-objects) and [Object Column policy](inv:crate-reference:*:label#data-types-objects)
  * [Inserting objects as JSON](inv:crate-reference:*:label#data-types-object-json)
  * [json type](inv:crate-reference:*:label#column_policy)
