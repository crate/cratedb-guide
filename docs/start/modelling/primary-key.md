# Primary key strategies

CrateDB is built for horizontal scalability and high ingestion throughput. To achieve this, operations must complete independently on each node—without central coordination. This design choice means CrateDB does **not** support traditional auto-incrementing primary key types like `SERIAL` in PostgreSQL or MySQL by default.

This page explains why that is and walks you through **five common alternatives** to generate unique primary key values in CrateDB, including a recipe to implement your own auto-incrementing sequence mechanism when needed.

## Why Auto-Increment Doesn't Exist in CrateDB

In traditional RDBMS systems, auto-increment fields rely on a central counter. In a distributed system like CrateDB, this would create a **global coordination bottleneck**, limiting insert throughput and reducing scalability.

Instead, CrateDB provides **flexibility**: you can choose a primary key strategy tailored to your use case, whether for strict uniqueness, time ordering, or external system integration.

## Primary Key Strategies in CrateDB

### 1. Use a Timestamp as a Primary Key

```sql
BIGINT DEFAULT now() PRIMARY KEY
```

**Pros**

* Auto-generated, always-increasing value
* Useful when records are timestamped anyway

**Cons**

* Can result in gaps
* Collisions possible if multiple records are created in the same millisecond

### 2. Use UUIDs (v4)

```sql
TEXT DEFAULT gen_random_text_uuid() PRIMARY KEY
```

**Pros**

* Universally unique
* No conflicts when merging from multiple environments or sources

**Cons**

* Not ordered
* Harder to read/debug
* No efficient range queries

### Use UUIDv7 for Time-Ordered IDs

UUIDv7 is a new format that preserves **temporal ordering**, making them better suited for distributed inserts and range queries.

You can use UUIDv7 in CrateDB via a **User-Defined Function (UDF)**, based on your preferred language.

**Pros**

* Globally unique and **almost sequential**
* Range queries possible

**Cons**

* Not human-friendly
* Slight overhead due to UDF use

### 4. Use External System IDs

If you're ingesting data from a source system that **already generates unique IDs**, you can reuse those:

* No need for CrateDB to generate anything
* Ensures consistency across systems

> See Replicating data from other databases to CrateDB with Debezium and Kafka for an example.

### 5. Implement a Custom Sequence Table

If you **must** have an auto-incrementing numeric ID (e.g., for compatibility or legacy reasons), you can implement a simple sequence generator using a dedicated table and client-side logic.

**Step 1: Create a sequence tracking table**

```sql
CREATE TABLE sequences (
    name TEXT PRIMARY KEY,
    last_value BIGINT
) CLUSTERED INTO 1 SHARDS;
```

**Step 2: Initialize your sequence**

```sql
INSERT INTO sequences (name, last_value)
VALUES ('mysequence', 0);
```

**Step 3: Create a target table**

```sql
CREATE TABLE mytable (
    id BIGINT PRIMARY KEY,
    field1 TEXT
);
```

**Step 4: Generate and use sequence values in Python**

Use optimistic concurrency control to generate unique, incrementing values even in parallel ingestion scenarios:

```python
# Requires: records, sqlalchemy-cratedb
import time
import records

db = records.Database("crate://")
sequence_name = "mysequence"

max_retries = 5
base_delay = 0.1  # 100 milliseconds

for attempt in range(max_retries):
    select_query = """
        SELECT last_value, _seq_no, _primary_term
        FROM sequences
        WHERE name = :sequence_name;
    """
    row = db.query(select_query, sequence_name=sequence_name).first()
    new_value = row.last_value + 1

    update_query = """
        UPDATE sequences
        SET last_value = :new_value
        WHERE name = :sequence_name
          AND _seq_no = :seq_no
          AND _primary_term = :primary_term
        RETURNING last_value;
    """
    result = db.query(
        update_query,
        new_value=new_value,
        sequence_name=sequence_name,
        seq_no=row._seq_no,
        primary_term=row._primary_term
    ).all()

    if result:
        break

    delay = base_delay * (2**attempt)
    print(f"Attempt {attempt + 1} failed. Retrying in {delay:.1f} seconds...")
    time.sleep(delay)
else:
    raise Exception("Failed to acquire sequence after multiple retries.")

insert_query = "INSERT INTO mytable (id, field1) VALUES (:id, :field1)"
db.query(insert_query, id=new_value, field1="abc")
db.close()
```

**Pros**

* Fully customizable (you can add prefixes, adjust increment size, etc.)
* Sequential IDs possible

**Cons**

* More complex client logic required
* The sequence table may become a bottleneck at very high ingestion rates

## Summary

| Strategy            | Ordered | Unique | Scalable | Human-Friendly | Range Queries | Notes                |
| ------------------- | ------- | ------ | -------- | -------------- | ------------- | -------------------- |
| Timestamp           | ✅       | ⚠️     | ✅        | ✅              | ✅             | Potential collisions |
| UUID (v4)           | ❌       | ✅      | ✅        | ❌              | ❌             | Default UUIDs        |
| UUIDv7              | ✅       | ✅      | ✅        | ❌              | ✅             | Requires UDF         |
| External System IDs | ✅/❌     | ✅      | ✅        | ✅              | ✅             | Depends on source    |
| Sequence Table      | ✅       | ✅      | ⚠️       | ✅              | ✅             | Manual retry logic   |
