# Relational data

CrateDB is a **distributed SQL database** that offers full **relational data modeling** with the flexibility of dynamic schemas and the scalability of NoSQL systems. It supports **primary and foreign keys**, **joins**, **aggregations**, and **subqueries**, just like traditional RDBMS systems—while also enabling hybrid use cases with time-series, geospatial, full-text, vector, and semi-structured data.

Use CrateDB when you need to scale relational workloads horizontally while keeping the simplicity of **ANSI SQL**.

## 1. Table Definitions

CrateDB supports strongly typed relational schemas using familiar SQL syntax:

```sql
CREATE TABLE customers (
  id         UUID PRIMARY KEY,
  name       TEXT,
  email      TEXT,
  created_at TIMESTAMP
);

CREATE TABLE orders (
  order_id     UUID PRIMARY KEY,
  customer_id  UUID,
  total_amount DOUBLE,
  created_at   TIMESTAMP
);
```

**Key Features:**

* Supports scalar types (`TEXT`, `INTEGER`, `DOUBLE`, `BOOLEAN`, `TIMESTAMP`, etc.)
* `UUID` recommended for primary keys in distributed environments
* Default **replication**, **sharding**, and **partitioning** options are built-in for scale

:::{note}
CrateDB supports `column_policy = 'dynamic'` if you want to mix relational and semi-structured models (like JSON) in the same table.
:::

## 2. Joins & Relationships

CrateDB supports **inner joins**, **left/right joins**, **cross joins**, and even **self joins**.

**Example: Join Customers and Orders**

```sql
SELECT c.name, o.order_id, o.total_amount
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.created_at >= CURRENT_DATE - INTERVAL '30 days';
```

Joins are executed efficiently across shards in a **distributed query planner** that parallelizes execution.

## 3. Normalization vs. Embedding

CrateDB supports both **normalized** (relational) and **denormalized** (embedded JSON) approaches.

* For strict referential integrity and modularity: use normalized tables with joins.
* For performance in high-ingest or read-optimized workloads: embed reference data as nested JSON.

Example: Embedded products inside an `orders` table:

```sql
CREATE TABLE orders (
  order_id UUID PRIMARY KEY,
  customer_id UUID,
  items ARRAY(OBJECT (
    name TEXT,
    quantity INTEGER,
    price DOUBLE
  )),
  created_at TIMESTAMP
);
```

:::{note}
CrateDB lets you **query nested fields** directly using dot notation: `items['name']`, `items['price']`, etc.
:::

## 4. Aggregations & Grouping

Use familiar SQL aggregation functions (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`) with `GROUP BY`, `HAVING`, `WINDOW FUNCTIONS`, and even `FILTER`.

```sql
SELECT customer_id, COUNT(*) AS num_orders, SUM(total_amount) AS revenue
FROM orders
GROUP BY customer_id
HAVING revenue > 1000;
```

:::{note}
CrateDB's **columnar storage** optimizes performance for aggregations—even on large datasets.
:::

## 5. Constraints & Indexing

CrateDB supports:

* **Primary Keys** – enforced for uniqueness and data distribution
* **Unique Constraints** – optional, enforced locally
* **Check Constraints** – for value validation
* **Indexes** – automatic for primary keys and full-text fields; manual for others

```sql
CREATE TABLE products (
  id UUID PRIMARY KEY,
  name TEXT,
  price DOUBLE CHECK (price >= 0)
);
```

:::{note}
Foreign key constraints are not strictly enforced at write time but can be modeled at the application or query layer.
:::

## 6. Views & Subqueries

CrateDB supports **views**, **CTEs**, and **nested subqueries**.

**Example: Reusable View**

```sql
CREATE VIEW recent_orders AS
SELECT * FROM orders
WHERE created_at >= CURRENT_DATE - INTERVAL '7 days';
```

**Example: Correlated Subquery**

```sql
SELECT name,
    (SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.id) AS order_count
FROM customers c;
```

## 7. Use Cases for Relational Modeling

| Use Case             | Description                                      |
| -------------------- | ------------------------------------------------ |
| Customer & Orders    | Classic normalized setup with joins and filters  |
| Inventory Management | Products, stock levels, locations                |
| Financial Systems    | Transactions, balances, audit logs               |
| User Profiles        | Users, preferences, activity logs                |
| Multi-tenant Systems | Use schemas or partitioning for tenant isolation |

## 8. Scalability & Distribution

CrateDB automatically shards tables across nodes, distributing both **data and query processing**.

* Tables can be **sharded and replicated** for fault tolerance
* Use **partitioning** for time-series or tenant-based scaling
* SQL queries are transparently **parallelized across the cluster**

:::{note}
Use `CLUSTERED BY` and `PARTITIONED BY` in `CREATE TABLE` to control distribution patterns.
:::

## 9. Best Practices

| Area          | Recommendation                                               |
| ------------- | ------------------------------------------------------------ |
| Keys & IDs    | Use UUIDs or consistent IDs for primary keys                 |
| Sharding      | Let CrateDB auto-shard unless you have advanced requirements |
| Join Strategy | Minimize joins over large, high-cardinality columns          |
| Nested Fields | Use `column_policy = 'dynamic'` if schema needs flexibility  |
| Aggregations  | Favor columnar tables for analytical workloads               |
| Co-location   | Consider denormalization for write-heavy workloads           |

## 10. Further Learning & Resources

* CrateDB Docs – Data Modeling
* CrateDB Academy – Relational Modeling
* Working with Joins in CrateDB
* Schema Design Guide

## 11. Summary

CrateDB offers a familiar, powerful **relational model with full SQL** and built-in support for scale, performance, and hybrid data. You can model clean, normalized data structures and join them across millions of records—without sacrificing the flexibility to embed, index, and evolve schema dynamically.

CrateDB is the modern SQL engine for building relational, real-time, and hybrid apps in a distributed world.
