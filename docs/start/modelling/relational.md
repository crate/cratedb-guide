(model-relational)=
# Relational data

CrateDB is a **distributed SQL database** that offers rich **relational data
modelling** with the flexibility of dynamic schemas and the scalability of NoSQL
systems. It supports **primary keys,** **joins**, **aggregations**, and
**subqueries**, just like traditional RDBMS systems—while also enabling hybrid
use cases with time-series, geospatial, full-text, vector search, and
semi-structured data.

Use CrateDB when you need to scale relational workloads horizontally while
keeping the simplicity of **SQL**.

## Table Definitions

CrateDB supports strongly typed relational schemas using familiar SQL syntax:

```sql
CREATE TABLE customers (
  id         TEXT DEFAULT gen_random_text_uuid() PRIMARY KEY,
  name       TEXT,
  email      TEXT,
  created_at TIMESTAMP DEFAULT now()
);
```

**Key Features:**

* Supports scalar types (`TEXT`, `INTEGER`, `DOUBLE`, `BOOLEAN`, `TIMESTAMP`,
etc.)
* `gen_random_text_uuid()`, `now()` or `current_timestamp()` recommended for
primary keys in distributed environments
* Default **replication**, **sharding**, and **partitioning** options are
built-in for scale


## Normalization vs. Embedding

CrateDB supports both **normalized** (relational) and **denormalized** (embedded
JSON) approaches with {ref}`column_policy = 'dynamic' <crate-reference:column_policy>`.

* For strict referential integrity and modularity: use normalized tables with
  joins.
* For performance in high-ingest or read-optimized workloads: embed reference
  data as nested JSON.

Example: Embedded products inside an `orders` table:

```sql
CREATE TABLE orders (
  order_id TEXT DEFAULT gen_random_text_uuid() PRIMARY KEY,
  customer_id TEXT,
  total_amount DOUBLE,
  items ARRAY(
    OBJECT(DYNAMIC) AS (
      name TEXT,
      quantity INTEGER,
      price DOUBLE
    )
  ),
  created_at TIMESTAMP DEFAULT now()
);
```

:::{note}
CrateDB lets you **query nested fields** directly using bracket
notation: `items['name']`, `items['price']`, etc.
:::

## Joins & Relationships

CrateDB supports **inner joins**, **left/right joins**, **cross joins**, **outer
joins**, and even **self joins**.

**Example: Join Customers and Orders**

```sql
SELECT c.name, o.order_id, o.total_amount
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.created_at >= CURRENT_DATE - INTERVAL '30 days';
```

Joins are executed efficiently across shards in a **distributed query planner**
that parallelizes execution.

## Aggregations & Grouping

Use familiar SQL aggregation functions (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`)
with `GROUP BY`, `HAVING`, `WINDOW FUNCTIONS` ... etc.

```sql
SELECT customer_id, COUNT(*) AS num_orders, SUM(total_amount) AS revenue
FROM orders
GROUP BY customer_id
HAVING SUM(total_amount) > 1000;
```

:::{note}
CrateDB's **columnar storage** optimizes performance for
aggregations — even on large datasets.
:::

## Constraints & Indexing

CrateDB supports:

* **Primary Keys** – enforced for uniqueness and data distribution
* **Check -** enforces custom value validation
* **Indexes** – automatic index for all columns
* **Full-text indexes -** manually defined, supports many tokenizers, analyzers
  and filters

In CrateDB every column is indexed by default, depending on the datatype a
different index is used, indexing is controlled and maintained by the database,
there is no need to `vacuum` or `re-index` like in other systems. Indexing can
be manually turned off with `INDEX OFF`.

```sql
CREATE TABLE products (
  id TEXT PRIMARY KEY,
  name TEXT,
  price DOUBLE CHECK (price >= 0),
  tag TEXT INDEX OFF, -- <------- INDEX WILL NOT BE CREATED
  description TEXT INDEX USING FULLTEXT
);
```

## Views & Subqueries

CrateDB supports **views**, **CTEs**, and **nested subqueries**.

**Example: Reusable View**

```sql
CREATE VIEW recent_orders AS
SELECT * FROM orders
WHERE created_at >= CAST(CURRENT_DATE AS TIMESTAMP) - INTERVAL '7 days';
```

**Example: Correlated Subquery**

```sql
SELECT name,
    (SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.id) AS order_count
FROM customers c;
```

**Example: Common table expression**

```sql
WITH order_counts AS (
    SELECT
        o.customer_id,
        COUNT(*) AS order_count
    FROM orders o
    GROUP BY o.customer_id
)
SELECT
    c.name,
    COALESCE(oc.order_count, 0) AS order_count
FROM customers c
LEFT JOIN order_counts oc
    ON c.id = oc.customer_id;
```

## Further Learning & Resources

* Reference Manual:
  * How to {ref}`query with joins <crate-reference:sql_joins>`
  * {ref}`SQL join statements <crate-reference:sql-select-joined-relation>`
  * {ref}`Join types and their implementation <crate-reference:concept-joins>`
* Blog posts:
  * [How to fine-tune the query
    optimizer](https://cratedb.com/blog/join-performance-to-the-rescue)
  * [Adding support for joins on virtual tables and multi-row
    subselects](https://cratedb.com/blog/joins-multi-row-subselects)
  * How we made Joins twenty three thousand times faster - part
    [#1](https://cratedb.com/blog/joins-faster-part-one),
    [#2](https://cratedb.com/blog/lab-notes-how-we-made-joins-23-thousand-times-faster-part-two),
    [#3](https://cratedb.com/blog/lab-notes-how-we-made-joins-23-thousand-times-faster-part-three),
    [Video](https://cratedb.com/resources/videos/distributed-join-algorithms)
