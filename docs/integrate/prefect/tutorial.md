(prefect-tutorial)=
# Building Seamless Data Pipelines Made Easy: Combining Prefect and CrateDB

## Introduction

[Prefect](https://www.prefect.io/opensource/) is an open-source workflow automation and orchestration tool for data engineering, machine learning, and other data-related tasks. It allows you to define, schedule, and execute complex data workflows in a straightforward manner.

Prefect workflows are defined using *Python code*. Each step in the workflow is represented as a "task," and tasks can be connected to create a directed acyclic graph (DAG). The workflow defines the sequence of task execution and can include conditional logic and branching. Furthermore, Prefect provides built-in scheduling features that set up cron-like schedules for the flow. You can also parameterize your flow, allowing a run of the same flow with different input values.

This tutorial will explore how CrateDB and Prefect come together to streamline data ingestion, transformation, and loading (ETL) processes with a few lines of Python code.

## Prerequisites

Before we begin, ensure you have the following prerequisites installed on your system:

* **Python 3.x**: Prefect is a Python-based workflow management system, so you'll need Python installed on your machine.
* **CrateDB**: To work with CrateDB, create a new cluster in [CrateDB Cloud](https://console.cratedb.cloud/). You can choose the CRFEE tier cluster that does not require any payment information.
* **Prefect**: Install Prefect using pip by running the following command in your terminal or command prompt: `pip install -U prefect`

## Getting started with Perfect

1. To get started with Prefect, you need to connect to Prefect’s API: the easiest way is to sign up for a free forever Cloud account at [https://app.prefect.cloud/](https://app.prefect.cloud/?deviceId=cfc80edd-a234-4911-a25e-ff0d6bb2c32a&deviceId=cfc80edd-a234-4911-a25e-ff0d6bb2c32a).
2. Once you create a new account, create a new workspace with a name of your choice.
3. Run `prefect cloud login` to [log into Prefect Cloud](https://docs.prefect.io/cloud/users/api-keys) from the local environment.

Now you are ready to build your first data workflows!

## Run your first ETL workflow with CrateDB
We'll dive into the basics of Prefect by creating a simple workflow with tasks that fetch data from a source, perform basic transformations, and load it into CrateDB. For this example, we will use [the yellow taxi trip data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz), which includes pickup time, geo-coordinates, number of passengers, and several other variables. The goal is to create a workflow that does a basic transformation on this data and inserts it into a CrateDB table named `trip_data`:

```python
import pandas as pd
from prefect import flow, task
from crate import client

CSV_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
URI = "crate://admin:password@host:5432"

@task()
def extract_data(url: str):
    df = pd.read_csv(url, compression="gzip")
    return df

@task()
def transform_data(df):
    df = df[df['passenger_count'] != 0]
    return df

@task()
def load_data(table_name, df):
    df.to_sql(table_name,URI,if_exists="replace",index=False)

@flow(name="ETL workflow", log_prints=True)
def main_flow():
    raw_data = extract_data(CSV_URL)
    data = transform_data(raw_data)
    load_data("trip_data", data)

if __name__ == '__main__':
    main_flow()
```

1. We start defining the flow by importing the necessary modules, including `prefect` for working with workflows, `pandas` for data manipulation, and `crate` for interacting with CrateDB.
2. Next, we specify the connection parameters for CrateDB and the URL for a file containing the dataset. You should modify these values according to your CrateDB Cloud setup.
3. We define three tasks using the `@task` decorator: `extract_data(url)`, `transform_data(data)`, and `load_data(table_name, transformed_data)`. Each task represents a unit of work in the workflow:
  1. The `read_data()` task loads the data from the CSV file to a `pandas` data frame.
  2. The `transform_data(data)` task takes the data frame and returns the data frame with entries where the `passenger_count` value is different than 0.
  3. The `load_data(transformed_data)` task connects to the CrateDB and loads data into the `trip_data` table.
4. We define the workflow, name it “ETL workflow“, and specify the sequence of tasks: `extract_data()`, `transform_data(data)`, and `load_data(table_name, transformed_data)`.
5. Finally, we execute the flow by calling `main_flow()`. This runs the workflow, and each task is executed in the order defined.

When you run this Python script, the workflow will read the trip data from a `csv` file, transform it, and load it into the CrateDB table. You can see the state of the flow run in the *Flows Runs* tab in Prefect UI:

![Screenshot 2023-08-01 at 09.50.02|690x328](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ecd02359cf23b5048e084faa785c7ad795bb5e57.png)

You can enrich the ETL pipeline with many advanced features available in Prefect such as parameterization, error handling, retries, and more. Finally, after the successful execution of the workflow, you can query the data in the CrateDB:

![Screenshot 2023-08-01 at 09.49.20|690x340](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/5582fcd2a677f78f8f7c6a1aa4b8e14f25dda2d1.png)

## Wrap up

Throughout this tutorial, you made a simple Prefect workflow, defined tasks, and orchestrated data transformations and loading into CrateDB. Both tools offer extensive feature sets that you can use to optimize and scale your data workflows further.

As you continue exploring, don’t forget to check out the {ref}`reference documentation <crate-reference:index>`. If you have further questions or would like to learn more about updates, features, and integrations, join the [CrateDB community](https://community.cratedb.com/). Happy data wrangling!
