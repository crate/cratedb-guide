(airflow-data-retention-policy)=
# Implementing a data retention policy in CrateDB using Apache Airflow

## What is a Data Retention Policy?

A data retention policy describes the practice of storing and managing data for a designated period of time. Once a data set completes its retention period, it should be deleted or archived, depending on requirements. Implementing data retention policies in the right way ensures compliance with existing guidelines and regulations, such as data privacy law, optimizes storage space by discarding outdated data and reduces storage costs.

## Specification of a Data Retention Policy in CrateDB
In the [previous tutorial](https://community.cratedb.com/t/cratedb-and-apache-airflow-part-one/901), we illustrated how to use CrateDB and Apache Airflow to automate periodic data export to a remote filesystem with the infrastructure provided by [Astronomer](https://www.astronomer.io/). In this tutorial, we focus on a more complex use case: the implementation of an effective retention policy for time-series data. To define retention policies we create a new table in CrateDB with the following schema:

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
The retention policy requires the use of a partitioned table, as in CrateDB, data can be deleted in an efficient way by dropping partitions. Therefore, for each retention policy, we store table schema, table name, the partition column, and the retention period defining how many days data should be retained.
The `strategy` column is reserved for future implementations of additional data retention policies. For now, we will always set it to the value `delete`.

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

You may also use a different table. The important part is that data should be partitioned: in our case, we partition the table on the `ts_day` column. Finally, we store the retention policy of 1 day for demo data in the `retention_policies` table:

```sql
INSERT INTO retention_policies (table_schema, table_name, partition_column, retention_period, strategy) VALUES ('doc', 'raw_metrics', 'ts_day', 1, 'delete');
```

## Implementation in Apache Airflow
To automate the process of deleting expired data we use [Apache Airflow](https://airflow.apache.org/). Our workflow implementation does the following: _once a day, fetch policies from the database, and delete all data for which the retention period expired._

### Retrieving Retention Policies
The first step consists of a task that queries partitions affected by retention policies. We do this by joining `retention_policies` and `information_schema.table_partitions` tables and selecting values with expired retention periods. In CrateDB, `information_schema.table_partitions` [{ref}`documentation <crate-reference:is_table_partitions>`] contains information about all partitioned tables including the name of the table, schema, partition column, and the values of the partition.
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
To implement the query above we use a regular Python method, annotated with `@task` to make it executable by Airflow. The most important reason behind choosing this type of operator is the need to pass the query result to the next operator. In our case that would be the list of affected partitions. However, it would be natural to expect that we want to execute a query on CrateDB as an `SQLExecuteQueryOperator`, but since this operator always returns `None` as a result, we would not be able to access the query result outside the operator.

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
Before we continue into the implementation of the next task in Apache Airflow, we would like to give a brief overview of how the data is communicated between different tasks in a DAG. For this purpose, Airflow introduces the [XCom](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html) system. Simply speaking `XCom` can be seen as a small object with storage that allows tasks to `push` data into that storage that can be later used by a different task in the DAG.

The key thing here is that it allows the exchange of a **small** amount of data between tasks. From Airflow 2.0, the return value of a Python method used as a task will be automatically stored in `XCom`. For our example, this means that the `get_policies` return value is available from the next task after the `get_policies` operator executes. To access the data from another task, a reference to the previous task can be passed to the next task when defining dependencies between tasks.

### Applying Retention Policies
Now that we retrieved the policies and Airflow automatically saved them via `XCom`, we need to create another task that will go through each element in the list and delete expired data.

The `get_policies` task returns tuples with a positional index. As this makes further processing not very readable, we map tuples to a list with named indexes:
```python
def map_policy(policy):
    return {
        "table_fqn": policy[0],
        "column": policy[1],
        "value": policy[2],
    }
```

In the DAG’s main method, use Airflow’s [dynamic task mapping](https://airflow.apache.org/docs/apache-airflow/2.3.0/concepts/dynamic-task-mapping.html) to execute the same task several times with different parameters:

```python
SQLExecuteQueryOperator.partial(
    task_id="delete_partition",
    conn_id="cratedb_connection",
    sql="DELETE FROM {{params.table_fqn}} WHERE {{params.column}} = {{params.value}};",
).expand(params=get_policies().map(map_policy))
```

`get_policies` returns a set of policies. On each policy, the `map_policy` is applied. The return value of `map_policy` is finally passed as `params` to the `SQLExecuteQueryOperator`.

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
        sql="DELETE FROM {{params.table_fqn}} WHERE {{params.column}} = {{params.value}};",
    ).expand(params=get_policies().map(map_policy))


data_retention_delete()
```

On the `SQLExecuteQueryOperator`, a certain set of attributes are passed via `partial` instead of `expand`. These are static values that are the same for each `DELETE` statement, like the connection and task ID.

The full DAG implementation of the data retention policy can be found in our [GitHub repository](https://github.com/crate/crate-airflow-tutorial/blob/main/dags/data_retention_delete_dag.py). To run the workflow, we rely on Astronomer infrastructure with the same setup as shown in the {ref}`getting started <airflow-getting-started>` section.

## Summary
This tutorial gives a guide on how to delete data with expired retention policies. The first part shows how to design policies in CrateDB and then, how to use Apache Airflow to automate data deletion. The DAG implementation is fairly simple: the first task performs the extraction of relevant policies, while the second task makes sure that affected partitions are deleted. In the following tutorial, we will focus on another real-world example that can be automated with Apache Airflow and CrateDB.
