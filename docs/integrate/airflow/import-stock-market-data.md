(airflow-import-stock-market-data)=
# Updating stock market data automatically with CrateDB and Apache Airflow

Watch this tutorial on Youtube: https://www.youtube.com/watch?v=YTTUzeaYUgQ&t=685s

If you are struggling with keeping your stock market data up to date, this tutorial walks you through exactly what you need to do so you can automate data collection and storage from SP500 companies.
![Picture by StockSnap on Pixabay](upload://tXDu25ajd6zX201Ju43lENW1uQ1.jpeg)


## Quick Overview
Let's have a quick overview of what you'll do:

You have a goal: regularly update stock market data.
To achieve your goal, you can divide it into tasks: download, prepare, and store data. You want to turn these tasks into a workflow, run it and observe the results; in other words, you want to orchestrate your workflow, and Airflow is the tool for that. 

So the first thing to do is to start CrateDB and set up a table to store your data. Then, to orchestrate the process of regular data updates, you will create an Airflow project and establish the connection to CrateDB. Once you set up your Airflow project, you will write your tasks in Python as an Airflow DAG workflow (more details later). Finally, you will set a schedule for your workflow, and it's done!

## Setup
Let's get right to the setup on a Mac machine.
You want to make sure you have Homebrew installed and Docker Desktop running.

### Run CrateDB and create a table to store data

The first to do is to run CrateDB with Docker. It's easy: once you have Docker Desktop running, copy the Docker command from the CrateDB installation page and run it in your terminal. 

```bash
docker run --publish=4200:4200 --publish=5432:5432 --env CRATE_HEAP_SIZE=1g crate:latest
```

With CrateDB running, you can now access the CrateDB Admin UI by going to your browser and typing *localhost:4200*.

Let’s now create a table to store your financial data. I'm particularly interested in the "adjusted-close" value for the stocks, so I will create a table that stores the date, the stock ticker, and the adjusted-close value. I will set the `closing_date` and `ticker` as primary keys. The final statement looks like this:
```sql
CREATE TABLE sp500 (
   closing_date TIMESTAMP,
   ticker TEXT,
   adjusted_close DOUBLE PRECISION,
   primary key (closing_date, ticker)
);
```
We are done with the Admin UI for now. Let’s return to the terminal to install Astronomer.

### Install Astronomer CLI and initialize the project
Let's return to the terminal, open a new tab, and install Astronomer with this command:

```bash
brew install astro
```

When Astronomer is ready, it's time to create a new directory for your airflow project. You can do that by running

```bash
mkdir astro-project && cd astro-project
```

Then, initialize the directory with the command

```bash
astro dev init
```
Now you have the skeleton of your Airflow project, which looks like this:

> ├── dags # directory containing all DAGs
> ├── include # additional files which are used in DAGs
> ├── .astro # project settings
> ├── Dockerfile # runtime overrides for Astronomer Docker image
> ├── packages.txt # specification of OS-level packages
> ├── plugins # custom or community Airflow plugins
> ├── setup # additional setup-related scripts/database schemas
> └── requirements.txt # specification of Python packages

Some information about the default settings: the PostgreSQL server is set up to listen on port 5432, and the web server is on port 8080. If these ports are unavailable, you can change them, and I'll show you how to do it shortly.
### Last adjustments

There are now three things you have to adjust before running Airflow:

* Add your CrateDB credentials to the `.env` file. Open the file in a text editor, and add the following line, which takes the default credentials for CrateDB, with user = crate, and password = null. (note: my internal port for running CrateDB in Docker is 5433, which I use here. If using the standard Docker command with 5432, here it should also be 5432).
   ```bash
   AIRFLOW_CONN_CRATEDB_CONNECTION=postgresql://crate:null@host.docker.internal:5433/doc?sslmode=disable
   ```
* If the default ports are unavailable, you can change them to free ports. Just open the `.astro/config.yaml` file in a text editor and update the web server port to 8081 (instead of default 8080) and Postgres port to 5435 (instead of the default 5432), like so:
   ```yaml
   project:
      name: astro-project
   webserver:
      port: 8081
   postgres:
     port: 5435
   ```

### Start Airflow
Now you are done with the last adjustments, head back to your terminal and run this command to start Airflow: `astro dev start`
You can now access Airflow in your browser at `http://localhost:8081`.

## Write the DAG

In Airflow, you define tasks as nodes on a DAG - short for Direct Acyclic Graph. That means you set the tasks to run one after the other without cycles to avoid deadlocks.
A task (or node) does not stand by itself: it depends on other tasks, and other tasks depend on it. These dependencies are the edges of the Graph and make up the DAG structure by connecting the tasks. You bring the DAG to life by writing the tasks in Python with the help of Airflow operators and Python modules. Now you’ve learned enough to start building your DAG step-by-step! 

Create a `.py` file for your DAG in your `astro-project/dags` folder; I will call it `financial_dag.py`. The DAG file has the following structure:

* Import operators and python modules
* Declare functions
* Set DAG and its tasks

### Import operators and modules

Import the operator used in this tutorial, `SQLExecuteQueryOperator`,
and the decorator to define the DAG and its tasks. You will also import
the `datetime`, `pendulum` modules to set up your schedule and the
`yfinance`, `pandas`, and `json` modules to download and manipulate the
financial data later.
```python
import datetime
import math
import json
import logging
import pendulum
import yfinance as yf
import pandas as pd
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.decorators import dag, task
```
Don’t forget to add these modules to the `requirements.txt` file inside your project like so:
```text
apache-airflow-providers-postgres>=5.3.1
apache-airflow-providers-common-sql>=1.3.1
apache-airflow[pandas]
yfinance==0.1.87
```
### Declare tasks

The next step is to declare the necessary tasks to download, prepare and insert data.  

#### Download task 

Let's first write a function to download data from `yfinance`; I will call it `download_yfinance_data`.
You can use ds for today’s date or get yesterday’s date with `airflow.macros.ds_add(ds, -1)`. You start by listing tickers from stocks of interest into a `tickers` variable. You then pass this list and the start date as arguments to the `yf.download` function and store the result in a `data` variable. `data` is a pandas data frame with various values for each stock, such as high/low, volume, dividends, and so on. Today, I will focus on the adjusted close value, so I filter data using the `Adj Close` key. Moreover, I return the data as a JSON object (instead of a data frame) because it works better with XCom, which is Airflow's mechanism to talk between tasks. Finally, you set this function as an Airflow task using the `@task` decorator and give it an execution timeout.
```python
@task(execution_timeout=datetime.timedelta(minutes=3))
def download_yfinance_data(ds=None):
    """Downloads Adjusted Close data from S&P 500 companies"""

    # list of stocks of interest
    tickers = {"AAPL", "AMZN", "META", "TSLA"}
    data = yf.download(tickers, start=ds)["Adj Close"]
    return data.to_json()
```
#### Prepare data task

Next in our code comes a `prepare_data` task, making the insert task more manageable later. In this function, you get the data in JSON as a parameter and transform it into a data frame for easier manipulation. Then, you take the `closing_date`, `ticker`, and `adj_close` columns from the `sp500` table you created and make them keys in a dictionary. You turn each data frame row into a dictionary with these keys. Finally, you add each of these dictionaries into a `values_dict` list, and done! Mark it as a task with the `@task` decorator, and give an execution timeout. Now the data is ready for the last task: insert it into CrateDB.

```python
@task(execution_timeout=datetime.timedelta(minutes=3))
def prepare_data(string_data):
    """Creates a list of dictionaries with clean data values"""

    # transforming to dataframe for easier manipulation
    df = pd.DataFrame.from_dict(json.loads(string_data), orient="index")

    values_dict = []
    for col, closing_date in enumerate(df.columns):
        for row, ticker in enumerate(df.index):
            adj_close = df.iloc[row, col]

            if not (adj_close is None or math.isnan(adj_close)):
                values_dict.append(
                    {
                        "closing_date": closing_date,
                        "ticker": ticker,
                        "adj_close": adj_close,
                    }
                )
            else:
                logging.info(
                    "Skipping %s for %s, invalid adj_close (%s)",
                    ticker,
                    closing_date,
                    adj_close,
                )

    return values_dict
```
#### Insert data task
So you have a list of dictionaries, each having values to import into CrateDB. For each of these values, you want to execute the `INSERT` statement, and that's when the `expand` method comes in handy. What Airflow does here is similar to defining the task in for loop: it creates n copies of the task, one for each input. 

You use the `SQLExecuteQueryOperator` to execute SQL statements against CrateDB using the `cratedb_connection` you defined in the beginning. Your final task looks like this:
```python
SQLExecuteQueryOperator.partial(
    task_id="insert_data_task",
    conn_id="cratedb_connection",
    sql="""
        INSERT INTO doc.sp500 (closing_date, ticker, adjusted_close)
        VALUES (%(closing_date)s, %(ticker)s, %(adj_close)s)
        ON CONFLICT (closing_date, ticker) DO UPDATE SET adjusted_close = excluded.adjusted_close
        """,
).expand(parameters=prepared_data)
```
#### Main execution method

Finally, it’s time to wrap everything up in your main execution method, `financial_data_import`. Here, you start by storing the downloaded data from `download_yfinance_data` into a `yfinance_data` variable and then storing in `prepared_data` the results from `prepare_data`. Then, the `SQLExecuteQueryOperator` is called to perform the `INSERT`.

```python
def financial_data_import():
    yfinance_data = download_yfinance_data()

    prepared_data = prepare_data(yfinance_data)

    SQLExecuteQueryOperator.partial(
        task_id="insert_data_task",
        conn_id="cratedb_connection",
        sql="""
            INSERT INTO doc.sp500 (closing_date, ticker, adjusted_close)
            VALUES (%(closing_date)s, %(ticker)s, %(adj_close)s)
            ON CONFLICT (closing_date, ticker) DO UPDATE SET adjusted_close = excluded.adjusted_close
            """,
    ).expand(parameters=prepared_data)
```
### Set DAG and its tasks

Now that you have your main execution method, it's time to put the DAG together. You start with the `@dag` decorator and define the `schedule` parameter; in my case, I'll make it run `daily`. You can also give it a `start_date` for the first DAG run, for example, from 2022-12-01. If the start date is before the current date, by default, Airflow will attempt to backfill all missed DAG runs. If you don't want that to happen, set the `catchup` parameter to false.
```python
@dag(
    start_date=pendulum.datetime(2022, 1, 10, tz="UTC"),
    schedule="@daily",
    catchup=False,
)
```
Your DAG structure will look like this: you first add the operators and modules, then the tasks. Then comes the DAG definition followed by the primary execution method: in this case, `financial_data_import`. The last line calls the main method, and your Airflow DAG is ready!

```python
import datetime
import math
import json
import logging
import pendulum
import yfinance as yf
import pandas as pd
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.decorators import dag, task

@task(execution_timeout=datetime.timedelta(minutes=3))
def download_yfinance_data(ds=None):

@task(execution_timeout=datetime.timedelta(minutes=3))
def prepare_data(string_data):


@dag(
    start_date=pendulum.datetime(2022, 1, 10, tz="UTC"),
    schedule="@daily",
    catchup=False,
)
def financial_data_import():
    yfinance_data = download_yfinance_data()

    prepared_data = prepare_data(yfinance_data)

    SQLExecuteQueryOperator.partial(
        task_id="insert_data_task",
        conn_id="cratedb_connection",
        sql="""
            INSERT INTO doc.sp500 (closing_date, ticker, adjusted_close)
            VALUES (%(closing_date)s, %(ticker)s, %(adj_close)s)
            ON CONFLICT (closing_date, ticker) DO UPDATE SET adjusted_close = excluded.adjusted_close
            """,
    ).expand(parameters=prepared_data)


financial_data_import()
```
## Execute DAG in Airflow UI

Now that your DAG code is ready, you can interact with it from the Airflow UI. Navigate to `http://localhost:8081` and enter the default credentials (user = admin, password = admin) to access the Airflow UI. You should now see the DAG you just created under the DAGs tab.
![Airflow UI](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/d2af26bcf371807a0600c7f8a40ef03e1a908154.png)
Next to the DAG's name, you find a toggle button to pause/unpause the DAG's execution. And if you click on the DAG's name, you get redirected to a page with different views for your DAG. For example, clicking on **Graph** will show you the tasks you have recreated; you can check out your code on the **Code** tab, and the **Grid** gives you information about your last runs and access to the logs.

A play button on the top right triggers the DAG manually. So let's click on it to test our DAG.
![Trigger DAG](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/a5aa46cd07831d2ea1c5d5eeca4c3074706ac12d.jpeg)

On the **Grid** view, you can click on these squares to check out the execution details.
![Grid view](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/e018fafe7a041ad64fe5ed4bf2ed1535baa1442b.jpeg)

## Check out the data in the Admin UI
Now that your task is executed let's check the data in CrateDB!
In the Admin UI, select your table in the tables tab and click **Query Table**. You should now see some of the records you just imported! From now on, you can easily access your financial data in CrateDB and use it as you like.
![Admin UI](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/90bdad96483410084363ad078750e8347c79be8f.jpeg)
