# Relational data

CrateDB is a **distributed SQL database** that offers rich **relational data modeling** with the flexibility of dynamic schemas and the scalability of NoSQL systems. It supports **primary keys,** **joins**, **aggregations**, and **subqueries**, just like traditional RDBMS systems—while also enabling hybrid use cases with time-series, geospatial, full-text, vector search, and semi-structured data.

Use CrateDB when you need to scale relational workloads horizontally while keeping the simplicity of **SQL**.

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

* Supports scalar types (`TEXT`, `INTEGER`, `DOUBLE`, `BOOLEAN`, `TIMESTAMP`, etc.)
* `gen_random_text_uuid()`, `now()` or `current_timestamp()` recommended for primary keys in distributed environments
* Default **replication**, **sharding**, and **partitioning** options are built-in for scale

:::{note}
CrateDB supports `column_policy = 'dynamic'` if you want to mix relational and semi-structured models (like JSON) in the same table.
:::

## Joins & Relationships

CrateDB supports **inner joins**, **left/right joins**, **cross joins**, **outer joins**, and even **self joins**.

**Example: Join Customers and Orders**

```sql
SELECT c.name, o.order_id, o.total_amount
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.created_at >= CURRENT_DATE - INTERVAL '30 days';
```

Joins are executed efficiently across shards in a **distributed query planner** that parallelizes execution.

## Normalization vs. Embedding

CrateDB supports both **normalized** (relational) and **denormalized** (embedded JSON) approaches.

* For strict referential integrity and modularity: use normalized tables with joins.
* For performance in high-ingest or read-optimized workloads: embed reference data as nested JSON.

Example: Embedded products inside an `orders` table:

```sql
CREATE TABLE orders (
  order_id TEXT DEFAULT gen_random_text_uuid() PRIMARY KEY,
  items ARRAY(
    OBJECT(DYNAMIC) AS (
      name TEXT,
      quantity INTEGER,
      price DOUBLE
    )
  ),
  created_at TIMESTAMP
);
```

:::{note}
CrateDB lets you **query nested fields** directly using bracket notation: `items['name']`, `items['price']`, etc.
:::

## Aggregations & Grouping

Use familiar SQL aggregation functions (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`) with `GROUP BY`, `HAVING`, `WINDOW FUNCTIONS` ... etc.

```sql
SELECT customer_id, COUNT(*) AS num_orders, SUM(total_amount) AS revenue
FROM orders
GROUP BY customer_id
HAVING revenue > 1000;
```

:::{note}
CrateDB's **columnar storage** optimizes performance for aggregations—even on large datasets.
:::

## Constraints & Indexing

CrateDB supports:

* **Primary Keys** – enforced for uniqueness and data distribution
* **Check -** enforces custom value validation
* **Indexes** – automatic index for all columns
* **Full-text indexes -** manually defined, supports many tokenizers, analyzers and filters

In CrateDB every column is indexed by default, depending on the datatype a different index is used, indexing is controlled and maintained by the database, there is no need to `vacuum` or `re-index` like in other systems. Indexing can be manually turned off.

```sql
CREATE TABLE products (
  id TEXT PRIMARY KEY,
  name TEXT,
  price DOUBLE CHECK (price >= 0),
  tag TEXT INDEX OFF,
  description TEXT INDEX using fulltext
);
```

## Views & Subqueries

CrateDB supports **views**, **CTEs**, and **nested subqueries**.

**Example: Reusable View**

```sql
CREATE VIEW recent_orders AS
SELECT * FROM orders
WHERE created_at >= CURRENT_DATE::TIMESTAMP - INTERVAL '7 days';
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

## Use Cases for Relational Modeling

| Use Case             | Description                                      |
| -------------------- | ------------------------------------------------ |
| Customer & Orders    | Classic normalized setup with joins and filters  |
| Inventory Management | Products, stock levels, locations                |
| Financial Systems    | Transactions, balances, audit logs               |
| User Profiles        | Users, preferences, activity logs                |
| Multi-tenant Systems | Use schemas or partitioning for tenant isolation |

## Scalability & Distribution

CrateDB automatically shards tables across nodes, distributing both **data and query processing**.

* Tables can be **sharded and replicated** for fault tolerance
* Use **partitioning** for time-series or tenant-based scaling
* SQL queries are transparently **parallelized across the cluster**

:::{note}
Use `CLUSTERED BY` and `PARTITIONED BY` in `CREATE TABLE` to control distribution patterns.
:::

## Best Practices

| Area          | Recommendation                                               |
| ------------- | ------------------------------------------------------------ |
| Keys & IDs    | Use UUIDs or consistent IDs for primary keys                 |
| Sharding      | Let CrateDB auto-shard unless you have advanced requirements |
| Join Strategy | Minimize joins over large, high-cardinality columns          |
| Nested Fields | Use `column_policy = 'dynamic'` if schema needs flexibility  |
| Aggregations  | Favor columnar tables for analytical workloads               |
| Co-location   | Consider denormalization for write-heavy workloads           |

## Further Learning & Resources

* CrateDB Docs – Data Modeling
* CrateDB Academy – Relational Modeling
* Working with Joins in CrateDB
* Schema Design Guide

## Summary

CrateDB offers a familiar, powerful **relational model with full SQL** and built-in support for scale, performance, and hybrid data. You can model clean, normalized data structures and join them across millions of records, without sacrificing the flexibility to embed, index, and evolve schema dynamically.

CrateDB is the modern SQL engine for building relational, real-time, and hybrid apps in a distributed world.
