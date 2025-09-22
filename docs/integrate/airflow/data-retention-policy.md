(airflow-data-retention-policy)=
# Implement a data retention policy in CrateDB using Apache Airflow

## What is a Data Retention Policy?

A data retention policy defines how long to keep data and what to do when it expires. Implement it to comply with data‑privacy rules, reduce storage, and cut costs.

## Specification of a Data Retention Policy in CrateDB

The {ref}`previous guide <airflow-export-s3>` shows how to use CrateDB and Apache Airflow to automate periodic data export to a remote filesystem on [Astronomer](https://www.astronomer.io/).
In this guide, we focus on a more complex use case: the implementation of an effective retention policy for time-series data. To define retention policies we create a new table in CrateDB with the following schema:

```sql
CREATE TABLE IF NOT EXISTS "doc"."retention_policies" (
   "table_schema" TEXT,
   "table_name" TEXT,
   "partition_column" TEXT NOT NULL,
   "retention_period" INTEGER NOT NULL,
   "strategy" TEXT NOT NULL,
   PRIMARY KEY ("table_schema", "table_name")
);
```
A retention policy assumes a partitioned table because CrateDB can delete data efficiently by dropping partitions. For each policy, store the table schema, table name, partition column, and the retention period in days.
Use the `strategy` column for future retention strategies. For now, set it to `delete`.

Next, define the table for storing demo data:

```sql
CREATE TABLE IF NOT EXISTS "doc"."raw_metrics" (
   "variable" TEXT,
   "timestamp" TIMESTAMP WITH TIME ZONE,
   "ts_day" TIMESTAMP GENERATED ALWAYS AS date_trunc('day', "timestamp"),
   "value" REAL,
   "quality" INTEGER,
   PRIMARY KEY ("variable", "timestamp", "ts_day")
)
PARTITIONED BY ("ts_day");
```

You can use a different table. Ensure the table is partitioned; here, we partition on `ts_day`. Finally, insert a 1‑day demo policy into `retention_policies`:

```sql
INSERT INTO retention_policies (table_schema, table_name, partition_column, retention_period, strategy) VALUES ('doc', 'raw_metrics', 'ts_day', 1, 'delete');
```

## Implementation in Apache Airflow

Use [Apache Airflow](https://airflow.apache.org/) to automate deletions. Once a day, fetch policies from the database and delete data whose retention period expired.

### Retrieving Retention Policies

Create a task that queries partitions affected by retention policies.
The resulting query is constructed as:
```sql
SELECT QUOTE_IDENT(p.table_schema) || '.' || QUOTE_IDENT(p.table_name),
       QUOTE_IDENT(r.partition_column),
       TRY_CAST(p.values[r.partition_column] AS BIGINT)
FROM information_schema.table_partitions p
JOIN doc.retention_policies r ON p.table_schema = r.table_schema
  AND p.table_name = r.table_name
  AND p.values[r.partition_column] < %(day)s::TIMESTAMP - (r.retention_period || ' days')::INTERVAL
WHERE r.strategy = 'delete';
```
To separate SQL logic from orchestration logic, we save the query as a file to `include/data_retention_retrieve_delete_policies.sql`.

In the query, we use the `%(day)s` placeholder which will be substituted with the logical execution date. This is especially useful in case of failing workflow: the next time Airflow will pick up the date on which the job failed. This makes job runs consistent.
Implement the query as a Python function decorated with `@task`.

The implementation of the corresponding tasks looks as follows:
```python
@task
def get_policies(ds=None):
    """Retrieve all partitions affected by a policy"""
    pg_hook = PostgresHook(postgres_conn_id="cratedb_connection")
    sql = Path("include/data_retention_retrieve_delete_policies.sql")
    return pg_hook.get_records(
        sql=sql.read_text(encoding="utf-8"),
        parameters={"day": ds},
    )
```
The first step is to create the function `get_policies` that takes as a parameter the logical date. The SQL statement gets loaded from a file. The `PostgresHook` establishes the connection with CrateDB. A `PostgresHook` takes the information from the `postgres_conn_id` and hooks us up with the CrateDB service. Then, the function executes the query and returns the result.

### Cross-Communication Between Tasks

Before implementing the next task, briefly review how tasks exchange data in a DAG.

XCom exchanges a small amount of data between tasks. Since Airflow 2.0, a Python task’s return value is stored in XCom. In our case, `get_policies` returns the partitions; the next task reads them via a reference to `get_policies` when defining dependencies.

### Applying Retention Policies

After retrieving the policies (stored in XCom), create another task that iterates over the list and deletes expired data.

The `get_policies` task returns tuples with a positional index. As this makes further processing not very readable, we map tuples to a list with named indexes:
```python
def map_policy(policy):
    return {
        "table_fqn": policy[0],
        "column": policy[1],
        "value": policy[2],
    }
```

In the DAG’s main method, use Airflow’s [dynamic task mapping] 
to execute the same task several times with different parameters:

```python
SQLExecuteQueryOperator.partial(
    task_id="delete_partition",
    conn_id="cratedb_connection",
    sql="DELETE FROM {{ params.table_fqn }} WHERE {{ params.column }} = {{ params.value }};",
).expand(params=get_policies().map(map_policy))
```

`get_policies` returns a set of policies. On each policy, the `map_policy` is
applied. The return value of `map_policy` is finally passed as `params` to the
`SQLExecuteQueryOperator`.

This leads us already to the final version of the DAG:
```python
def map_policy(policy):
    return {
        "table_fqn": policy[0],
        "column": policy[1],
        "value": policy[2],
    }


@task
def get_policies(ds=None):
    """Retrieve all partitions affected by a policy"""
    pg_hook = PostgresHook(postgres_conn_id="cratedb_connection")
    sql = Path("include/data_retention_retrieve_delete_policies.sql")
    return pg_hook.get_records(
        sql=sql.read_text(encoding="utf-8"),
        parameters={"day": ds},
    )


@dag(
    start_date=pendulum.datetime(2021, 11, 19, tz="UTC"),
    schedule="@daily",
    catchup=False,
)
def data_retention_delete():
    SQLExecuteQueryOperator.partial(
        task_id="delete_partition",
        conn_id="cratedb_connection",
        sql="DELETE FROM {{ params.table_fqn }} WHERE {{ params.column }} = {{ params.value }};",
    ).expand(params=get_policies().map(map_policy))


data_retention_delete()
```

On the `SQLExecuteQueryOperator`, a certain set of attributes are passed via `partial` instead of `expand`. These are static values that are the same for each `DELETE` statement, like the connection and task ID.

The full DAG implementation of the data retention policy can be found in our [GitHub repository](https://github.com/crate/cratedb-airflow-tutorial/blob/main/dags/data_retention_delete_dag.py). To run the workflow, we rely on Astronomer infrastructure with the same setup as shown in the {ref}`getting started <airflow-getting-started>` section.

## Summary

This guide introduced you on how to delete data whose retention period expired.
First, design policies in CrateDB. Then use Apache Airflow to automate the deletion.

The DAG implementation is straightforward: one task extracts relevant policies;
another one deletes the affected partitions.
The {ref}`next guide <airflow-data-retention-hot-cold>` covers another real‑world
example automated with Apache Airflow and CrateDB.


[dynamic task mapping]: https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html
