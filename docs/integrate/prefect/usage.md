(prefect-usage)=
# Combine Prefect and CrateDB for building seamless data pipelines 

## Introduction

[Prefect](https://www.prefect.io/opensource/) is an open-source workflow orchestration tool for data engineering, machine learning, and other data tasks. You define, schedule, and execute complex data workflows with straightforward Python code.

You define Prefect workflows in Python. Each step is a “task,” and tasks form a directed acyclic graph (DAG). Flows can branch and include conditional logic. Prefect also provides built‑in scheduling and flow parameters so you can run the same flow with different inputs.

This usage guide shows how to combine CrateDB and Prefect to streamline ETL with a few lines of Python.

## Prerequisites

Before we begin, ensure you have the following prerequisites installed on your system:

* **Python 3.x**: Prefect is a Python-based workflow management system, so you'll need Python installed on your machine.
* **CrateDB**: To work with CrateDB, create a new cluster in [CrateDB Cloud](https://console.cratedb.cloud/). You can choose the CRFEE tier cluster that does not require any payment information.
* **Prefect**: Install Prefect using pip: `pip install -U prefect`
* **SQLAlchemy + CrateDB dialect**: `pip install -U sqlalchemy sqlalchemy-cratedb`

## Getting started with Prefect

1. To get started with Prefect, connect to Prefect’s API by signing up for a free Cloud account at [https://app.prefect.cloud/](https://app.prefect.cloud/).
2. Once you create a new account, create a new workspace with a name of your choice.
3. Run `prefect cloud login` to [log into Prefect Cloud](https://docs.prefect.io/cloud/users/api-keys) from the local environment.

Now you are ready to build your first data workflows!

## Run your first ETL workflow with CrateDB

This section walks you through a simple workflow that fetches data, applies a basic transformation, and loads it into CrateDB. It uses the [yellow taxi trip dataset](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz), which includes pickup time, geo‑coordinates, passenger count, and other fields. The goal is to write transformed data to a CrateDB table named `trip_data`:

```python
import pandas as pd
from prefect import flow, task
from sqlalchemy import create_engine

CSV_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
URI = "crate://admin:password@host:4200"
engine = create_engine(URI)

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
    df.to_sql(table_name, engine, if_exists="replace", index=False)

@flow(name="ETL workflow", log_prints=True)
def main_flow():
    raw_data = extract_data(CSV_URL)
    data = transform_data(raw_data)
    load_data("trip_data", data)

if __name__ == '__main__':
    main_flow()
```

1. Start by importing the necessary modules: `prefect` for workflows, `pandas` for data manipulation, and SQLAlchemy for the database connection.
2. Specify the CrateDB connection URI and the dataset URL. Modify these values for your CrateDB Cloud setup.
3. Define three tasks with the `@task` decorator—`extract_data(url)`, `transform_data(df)`, and `load_data(table_name, df)`:

    1. `extract_data()` reads the CSV into a pandas DataFrame.
    2. `transform_data(df)` filters out rows where `passenger_count` is 0.
    3. `load_data(table_name, df)` writes the data to the `trip_data` table in CrateDB.

4. Define the flow, name it “ETL workflow,” and order the tasks: `extract_data()`, `transform_data()`, then `load_data()`.
5. Execute the flow by calling `main_flow()`. Prefect runs each task in order.

When you run the script, the workflow reads the trip data from a CSV file, transforms it, and loads it into CrateDB. You can see the state of the run in the *Flow Runs* tab in the Prefect UI:

![Screenshot 2023-08-01 at 09.50.02|690x328](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ecd02359cf23b5048e084faa785c7ad795bb5e57.png)

You can enrich the pipeline with Prefect features such as parameters, error handling, and retries. After a successful run, query the data in CrateDB:

![Screenshot 2023-08-01 at 09.49.20|690x340](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/5582fcd2a677f78f8f7c6a1aa4b8e14f25dda2d1.png)

## Wrap up

In this usage guide, you created a simple Prefect workflow, defined tasks, and orchestrated data transformations and loading into CrateDB. Both tools offer extensive features that help you optimize and scale your data workflows.

As you continue exploring, don’t forget to check out the {ref}`reference documentation <crate-reference:index>`. If you have further questions or would like to learn more about updates, features, and integrations, join the [CrateDB community](https://community.cratedb.com/). Happy data wrangling!
