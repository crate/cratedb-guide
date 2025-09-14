(airflow-export-s3)=
# Export data from CrateDB to S3 using Apache Airflow

## Introduction
This article covers the automation of a typical daily data export to a remote filesystem.
The idea is to report data collected from the previous day to the Amazon Simple Storage
Service (Amazon S3). To illustrate this example, we first create a new bucket on S3 called
`crate-astro-tutorial`. The official documentation on how to create a new bucket can be
found [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).

We start by setting up two environment variables for storing AWS credentials
(Access Key ID and Secret Access Key) in the `.env` file:
```bash
ACCESS_KEY_ID="<ACCESS KEY ID>"
SECRET_ACCESS_KEY="<SECRET ACCESS KEY>"
```
We base our use case on table data that has the following schema:

```sql
CREATE TABLE IF NOT EXISTS "metrics" ( 
  "hash_id" BIGINT,
  "timestamp" TIMESTAMP WITH TIME ZONE,
  "name" TEXT,
  "tags" OBJECT(DYNAMIC),
  "fields" OBJECT(DYNAMIC),
  "month" TIMESTAMP AS date_trunc('quarter', "timestamp")
)
```
In general, to export data to a file one can use the `COPY TO` statement in CrateDB. This command exports the content of a table to one or more JSON files in a given directory. JSON files have unique names and they are formatted to contain one table row per line. The `TO` clause specifies the URI string of the output location. CrateDB supports two URI schemes: `file` and `s3`. We use the `s3` scheme to access the bucket on Amazon S3. Further information on different clauses of the `COPY TO` statement can be found in the official {ref}`CrateDB documentation <crate-reference:sql-copy-to>`.

To export data from the `metrics` table to S3, we need a statement such as:

`COPY metrics TO DIRECTORY 's3://[{access_key}:{secret_key}@]<bucketname>/<path>'`

## DAG implementation

In order to build a generic DAG that is not specific to one single table configuration, we first create a file `include/table_exports.py`, containing a list of dictionaries (key/value pairs) for each table to export:
```python
TABLES = [
    {
        # fully-qualified name of the table to export
        "table": "doc.metrics",
        # name of the timestamp column to use for filtering the export
        "timestamp_column": "timestamp",
        # name and path of the target S3 bucket
        "target_bucket": "crate-astro-tutorial/metrics",
    }
]
```
The DAG itself is specified as a Python file `astro-project/dags`. It loads the above-defined `TABLES` list and iterates over it. For each entry, a corresponding `SQLExecuteQueryOperator` is instantiated, which will perform the actual export during execution. If the `TABLES` list contains more than one element, Airflow will be able to process the corresponding exports in parallel, as there are no dependencies between them.

The resulting DAG code is as follows (see the [GitHub repository](https://github.com/crate/crate-airflow-tutorial) for the complete project):
```python
import os
import pendulum
from airflow.decorators import dag, task_group
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.operators.empty import EmptyOperator
from airflow.models.baseoperator import chain
from include.table_exports import TABLES


@task_group
def export_tables():
    for export_table in TABLES:
        SQLExecuteQueryOperator(
            task_id=f"copy_{export_table['table']}",
            conn_id="cratedb_connection",
            sql="""
                    COPY {{params.table}} WHERE DATE_TRUNC('day', {{params.timestamp_column}}) = '{{macros.ds_add(ds, -1)}}'
                    TO DIRECTORY 's3://{{params.access}}:{{params.secret}}@{{params.target_bucket}}-{{macros.ds_add(ds, -1)}}';
                """,
            params={
                "table": export_table["table"],
                "timestamp_column": export_table["timestamp_column"],
                "target_bucket": export_table["target_bucket"],
                "access": os.environ.get("ACCESS_KEY_ID"),
                "secret": os.environ.get("SECRET_ACCESS_KEY"),
            },
        )


@dag(
    start_date=pendulum.datetime(2021, 11, 11, tz="UTC"),
    schedule="@daily",
    catchup=False,
)
def table_export():
    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")
    tg1 = export_tables()

    chain(start, tg1, end)


table_export()
```
The DAG has a unique ID, start date, and schedule interval and is composed of one task per table. It runs daily every day starting at 00:00.

To inject the date for which to export data, we use the `ds` [macro in Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html). This macro gives the logical date, not the actual date based on wall clock time. To make the task idempotent with regard to execution time, it is the best practice to always use the logical date or timestamp.

Based on the `timestamp_column`, a corresponding `WHERE` clause gets constructed to restrict the export to only data from the previous day.

The `target_bucket` gets extended with the date of the logical execution timestamp so that each DAG execution will copy files into a separate directory.

## DAG execution

The next step is to restart the Docker containers and go to the Airflow UI. Besides the `example_dag` that is automatically generated during project initialization, you should also see `cratedb_table_export` which we trigger manually, as illustrated:

![Screenshot 2021-11-12 at 16.23.59|690x229](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/4655021e39ff3a524b6152b3e4a0f9f4656be9df.png)

To find more details about running DAGs, go to `Browse/DAG runs` which opens a new window with details of the running DAGs, such as state, execution data, and run type:

![Screenshot 2021-11-11 at 14.12.34|690x242](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/7ca80b8c8cacfff176c160e83833a1f6f03f9126.png)
After a successful DAG execution, the data will be stored on the remote filesystem.

## Summary
This article covered a simple use case: periodic data export to a remote filesystem. In the following articles, we will cover more complex use cases composed of several tasks based on real-world scenarios. If you want to try our examples with Apache Airflow and Astronomer, you are free to check out the code on the public [GitHub repository](https://github.com/crate/crate-airflow-tutorial).
