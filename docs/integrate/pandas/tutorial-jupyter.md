(pandas-tutorial-jupyter)=
# Automating financial data collection and storage in CrateDB with Python and pandas

:::{article-info}
---
avatar: https://sea2.discourse-cdn.com/flex020/user_avatar/community.cratedb.com/rafaelasantana/288/358_2.png
avatar-link: https://github.com/rafaelasantana
avatar-outline: muted
author: Rafaela Santana
date: April 7, 2023
read-time: 10 min read
class-container: sd-p-2 sd-outline-muted sd-rounded-1
---
:::

This tutorial will teach you how to automatically collect historical data from S&P-500
companies and store it all in CrateDB using Python.

**tl;dr**: I will go through how to

* import S&P-500 companies’ data with the Yahoo! Finance API into a Jupyter Notebook,
* set up a connection to CrateDB with Python,
* create functions to create tables, insert values, and retrieve data from CrateDB,
* upload finance market data into CrateDB

Before anything else, I must make sure I have my setup ready.

So, let’s get started.

## Setting up CrateDB, Jupyter, and Python

### CrateDB

If you’re new to CrateDB and want to get started quickly and easily, a great option is to try the **Free Tier** in CrateDB Cloud. With the **Free Tier**, you have a limited Cluster that is free forever; no payment method is required. Now, if you are ready to experience the full power of CrateDB Cloud, take advantage of the 200$ in free credits to try the cluster of your dreams.

To start with CrateDB Cloud, [navigate to the CrateDB website](https://cratedb.com/download?hsCtaTracking=caa20047-f2b6-4e8c-b7f9-63fbf818b17f%7Cf1ad6eaa-39ac-49cd-8115-ed7d5dac4d63) and follow the steps to create your CrateDB Cloud account. Once you log in to the CrateDB Cloud UI, select **Deploy Cluster** to create your free cluster, and you are ready to go!

![cratedb-cloud-free-tier](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/26fc603ca998d39631f93f1eb7c5dbd30f437e56.gif)

With my CrateDB Cluster up and running, I can ensure Python is set up.

### Python

Python is a good fit for this project: it’s simple, highly readable, and has valuable analytics libraries for free.

I download [Python](https://www.python.org/downloads/), then reaccess the terminal to check if Python was installed and which version I have with the command
`pip3 --version`,
which tells me I have Python 3.9 installed.

All set!

### Jupyter

The [Jupyter Notebook](https://jupyter.org/) is an open-source web application that creates and shares documents containing live code, equations, visualizations, and narrative text.

A Jupyter Notebook is an excellent environment for this project. It contains executable documents (the code) and human-readable documents (tables, figures, etc.) in the same place!

I follow the [Jupiter Installation tutorial](https://jupyter.org/install.html) for the Notebook, which is quickly done with Python and the terminal command
`pip3 install notebook`
and now I run the Notebook (using Jupyter 1.0.0) with the command
`jupyter notebook`

Setup done!

Now I can access my Jupyter Notebook by opening the URL printed in the terminal after running this last command. In my case, it is at http://localhost:8888/

## Creating a Notebook

On Jupyter’s main page, I navigate to the **New** button on the top right and select **Python 3 (ipykernel)**

![Jupyter Notebook](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/b53c7cbe73ef268108e856e19bf946d4cf0d987b.png){w=800px}

An empty notebook opens. 

To make sure everything works before starting my project, I

* call the notebook “financial-data-with-cratedb”, 
* write a ‘Hello World!’ line with

```python
print('Hello World!')
```

* run the code snippet by pressing `Alt` + `Enter` (or clicking on the **Run** button)

![Hello World program](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/e25efa994ab0afefe946e2ec5b99d4b9b31cfad8.jpeg){w=800px}

Great, it works! Now I can head to the following steps to download the financial data. 

## Getting all S&P-500 ticker symbols from Wikipedia

When I read [yfinance](https://pypi.org/project/yfinance/)’s documentation (version 0.1.63), I find the `history` function, which gets a ticker symbol as a parameter and downloads the data from this company.

I want to download data from all S&P-500 companies, so having a list with all their symbols would be perfect.

I then found [this tutorial by Edoardo Romani](https://medium.com/data-science/how-to-automate-financial-data-collection-with-python-using-tiingo-api-and-google-cloud-platform-b11d8c9afaa1), which shows how to get the symbols from the [List of S&P-500 companies' Wikipedia page](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) and store them in a list.

So, in my Notebook, I import [BeautifulSoup 4.10.0](https://beautiful-soup-4.readthedocs.io/en/latest/) and [requests 2.26.0](https://pypi.org/project/requests/) to pull out HTML files from Wikipedia and create the following function:

```python
import requests
from bs4 import BeautifulSoup

def get_sp500_ticker_symbols():

    # getting html from SP500 Companies List wikipedia page
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    r = requests.get(url,timeout = 2.5)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')

    # getting rows from wikipedia's table
    components_table = soup.find_all(id = "constituents")
    data_rows = components_table[0].find("tbody").find_all("tr")[1:]

    # extracting ticker symbols from the data rows
    tickers = []
    for row in range(len(data_rows)):
        stock = list(filter(None, data_rows[row].text.split("\n")))
        symbol = stock[0]
        if (symbol.find('.') != -1):
            symbol = symbol.replace('.', '-')
        tickers.append(symbol)
    tickers.sort()
    return tickers
```

What this function does is:

* it finds the S&P-500 companies table components in the Wikipedia page’s HTML code
* it extracts the table rows from the components and stores it in the `data_rows` variable
* it splits `data_rows` into the `stock` list, where each element contains information about one stock (Symbol, Security, SEC filings, …)
* it takes the Symbol for each `stock` list element and adds it to the `tickers` list
* finally, it sorts the `tickers` list in alphabetical order and returns it

To check if it works, I will call this function and print the results with 

```python
tickers = get_sp500_ticker_symbols()
print(tickers)
```

and it looks like this: 

![get_sp500_ticker_symbols()](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/49935a7dbb2153ee7f6a24d99c44132f562e1e20.png){w=800px}

Now that I have a list of all the stock tickers, I can move on and download their data with `yfinance`.

## Downloading financial data with yfinance

[Pandas](https://pandas.pydata.org/) is a famous package in Python, often used for Data Science. It shortens the process of handling data, has complete yet straightforward data representation forms, and makes tasks like filtering data easy.

Its key data structure is called a DataFrame, which allows storage and manipulation of tabular data: in this case, the columns are going to be the financial variables (such as “date”, “ticker”, “closing price”…) and the rows are going to be filled with data about the S&P-500 companies.

So, the first thing I do is import the `yfinance`(0.1.63) and `pandas`(2.0.0)

```python
import yfinance as yf
import pandas as pd
```
And now, I have designed a function to download the data from a company from a given period.

First, I create a `data` DataFrame to store the stocks' `closing_date`, `ticker`, and `close_value`.

I get the data from the ticker on that period with the `Ticker.history` function from `yfinance`. I store the result in the `history` DataFrame, rename the index (which contains the date) to `closing_date`, as this is the column name I prefer for CrateDB, and then reset the index. Instead of having the date as the index, I have a column called `closing_date`, which has the date information, and the rows are indexed trivially (like 0, 1, 2, …). I also add a `ticker` column containing the current ticker and rename the `Close` column to match the `close_value` name in the `data` DataFrame. Finally, I add the `closing_date`, `ticker`, and `close_value` data for that ticker to my `data` DataFrame.

The function returns the `data` DataFrame containing the `closing_date`, `ticker`, and `close_value` data for the given ticker over the `period`.

This is what `download_data` looks like:
```python
def download_data(ticker, period):

    data = pd.DataFrame(columns=['closing_date', 'ticker', 'close_value'])

    # downloading history for this ticker ticker
    info = yf.Ticker(ticker)
    history = info.history(period=period)
    history.index.names = ['closing_date']
    history.reset_index(inplace=True)

    # adding a column for the ticker
    history['ticker'] = ticker

    # renaming column to fit into dataframe
    history.rename(columns={'Close': 'close_value'}, inplace=True)

    # adding values to the dataframe
    data = pd.concat(
        [data, history[['closing_date', 'ticker', 'close_value']]])

    return data
```

To check if everything works, I execute the function and store it in the `my_data` variable, and print the result:

```python
my_data = download_data('AAPL', '1mo')
my_data
```
and it looks like this:

![calling-download-data|690x348](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/6174430a9bd94b8956e2ba012267ca67a335d53b.png){w=800px}


## Connecting to CrateDB

In the **Overview** tab of my CrateDB Cloud Cluster I find several ways to connect to CrateDB with CLI, Python, JavaScript, among others. So I select the **Python** option and choose one of the variants, such as **psycopg2**(version 2.9.1).

![connections-for-cratedb-cloud|690x386](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/2891e21d7ad9cd34eed068153285530badb0dc66.png){w=800px}

I copy the code to connect and add my password to it in the `<PASSWORD>` field. It creates a `conn` variable, which stores the connection, and a `cursor` variable, which allows Python code to execute PostgreSQL commands. I adapt the code slightly so I leave the `cursor` open to use it later on. It then looks like this:
```python
# pip install psycopg2-binary
import psycopg2 as ps

conn = ps.connect(host="<YOUR_CLUSTER>", port=5432, user="admin", password="<PASSWORD>", sslmode="require")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sys.cluster")
result = cursor.fetchone()
print(result)
```
When I run this code it prints `('my-cluster',)`, which is the name I have to my cluster, so the connection works!

Now I can create more functions to create tables in CrateDB, insert my data values into a table, and retrieve data!

## Creating functions for CrateDB

### Creating table

I will have the `closing_date`, `ticker`, and `close_value` columns in my table. Also, I want to give the table name as a parameter and only create a new table in case the table does not exist yet. I use the SQL keywords `CREATE TABLE IF NOT EXISTS` in my function.

Now I must create the complete statement as a string and execute it with the `cursor.execute`command:

```python
def create_table(table_name):
    columns = "(closing_date TIMESTAMP, ticker TEXT, close_value FLOAT)"
    statement = "CREATE TABLE IF NOT EXISTS \"" + table_name + "\"" + columns + ";"
    cursor.execute(statement)
```

Now I can move on to creating an insert function.

### Inserting values into CrateDB

I want to create a function that:

* gets the table name and the data as parameters
* makes an insert statement for this data
* executes this statement

*(In the next steps, I review each part of this function. However, I have a snippet of the complete function at the end of this section)*

Formatting the entries is crucial for successful insertion.

However, because of that, this function became rather long: so I will go through each section separately and then join them all in the end.

* Before anything else, I import the `math` module to use later in this function.
* The function starts by creating an empty list called `values_array`. This list will hold the formatted values I want to insert into the table.
* Next, I loop through each row of the `data` and extract the row values using the `iloc` method, which returns the values of the specified row.
* For each row, I check if the `close_value` value for that row is `NaN` (not a number), and if so, set it to -1. This is done to handle missing data.
* Then I format the `closing_date` value to match the timestamp format that the table expects. The date is first converted to a string in the format “YYYY-MM-DD”, then a time in the format “T00:00:00Z” is added to the end. The resulting string is then wrapped in single quotes to create a string that matches the expected timestamp format.
* Finally, I create a string representing the values for this row in the format `(closing_date, ticker, close_value)`, and append it to the `values_array` list. I repeat this process for each row in the `data` DataFrame.

```python
import math

def insert_values(table_name, data):

    values_array = []

    # adding each closing date, ticker and close value tuple to values array
    for row in range(len(data)):

        # saving entries from the ith row as a list of date values
        row_values = data.iloc[row, :]

        # checking if there is a NaN entry and setting it to -1
        close_value = row_values['close_value']
        if (math.isnan(close_value)):
            close_value = -1

        # formatting date entries to match timestamp format
        closing_date = row_values['closing_date'].strftime("%Y-%m-%d")
        closing_date = "'{}'".format(
            closing_date + "{time}".format(time="T00:00:00Z"))

        # putting a comma between values tuples, but not on the last tuple
        values_array.append("({},\'{}\',{})".format(
            closing_date, row_values['ticker'], close_value))
```

* After all the row values have been added to the `values_array` list, I create a new table with the specified name (if it does not already exist) using the `create_table` function.
* Then I create the first part of the SQL `INSERT` statement, which includes the table name and the column names we insert into (`closing_date`, `ticker`, and `close_value`). This part of the statement is stored in the `insert_stmt` variable.
* Next, I add the values tuples from `values_array` to the `insert_stmt`, separated by commas. The final SQL `INSERT` statement is created by concatenating the `insert_stmt` variable and a semicolon at the end.

```python 
    # creates a new table (in case it does not exist yet)
    create_table(table_name)

    # first part of the insert statement
    insert_stmt = "INSERT INTO \"{}\" (closing_date, ticker, close_value) VALUES ".format(
        table_name)

    #  adding data tuples to the insert statement
    insert_stmt += ", ".join(values_array) + ";"
```
* Finally, the function executes the `INSERT` statement using the `cursor.execute()` method, and prints out a message indicating how many rows were inserted into the table.

```python
    cursor.execute(insert_stmt)

    print("Inserted " + str(len(data)) + " rows in CrateDB")
```
In summary, in `insert_values`, I take the table name and the data, format the data into a SQL `INSERT` statement, and insert the data into the specified table.

This is what the complete function looks like:

```python
import math

def insert_values(table_name, data):

    values_array = []

    # adding each closing date, ticker and close value tuple to values array
    for row in range(len(data)):

        # saving entries from the ith row as a list of date values
        row_values = data.iloc[row, :]

        # checking if there is a NaN entry and setting it to -1
        close_value = row_values['close_value']
        if (math.isnan(close_value)):
            close_value = -1

        # formatting date entries to match timestamp format
        closing_date = row_values['closing_date'].strftime("%Y-%m-%d")
        closing_date = "'{}'".format(
            closing_date + "{time}".format(time="T00:00:00Z"))

        # putting a comma between values tuples, but not on the last tuple
        values_array.append("({},\'{}\',{})".format(
            closing_date, row_values['ticker'], close_value))

    # creates a new table (in case it does not exist yet)
    create_table(table_name)

    # first part of the insert statement
    insert_stmt = "INSERT INTO \"{}\" (closing_date, ticker, close_value) VALUES ".format(
        table_name)

    #  adding data tuples to the insert statement
    insert_stmt += ", ".join(values_array) + ";"

    cursor.execute(insert_stmt)

    print("Inserted " + str(len(data)) + " rows in CrateDB")
```
Now I can move on to the next function, which is quite handy regarding automation.

### Selecting the last inserted Date

I want my stock market data in CrateDB to be up to date, requiring I run this script regularly.

However, I do not want to download data I already have or have duplicate entries in CrateDB.

That’s why I create this function, which selects the most recent date from the data in my CrateDB table. I will use this date to calculate the period to download data from in the `download_data` function: this way, this function will only download new data!

```python
def select_last_inserted_date(table_name):

    # creating table (only in case it does not exist yet)
    create_table(table_name)

    # selecting the maximum date in my table
    statement = "select max(closing_date) from " + table_name + ";"
    cursor.execute(statement)

    # fetching the results from the query
    last_date_data = cursor.fetchall()
    last_date = last_date_data[0][0]

    # if the query is empty or the date is None, start by 2023/01/01
    if (len(last_date_data) == 0 or last_date is None):
        print("No data yet, will return: 2023-01-01")
        return datetime.strptime("2023-01-01", "%Y-%m-%d")

    # printing the last date
    print("Most recent data on CrateDB from: " + last_date.strftime("%Y-%m-%d"))

    return last_date
```
In the `get_period_to_download` function, I calculate the difference between today and the last inserted date and return the corresponding period.

```python
from datetime import datetime, timedelta

def get_period_to_download(last_date):

    # calculating the difference between today and the last date
    today = datetime.now()
    days_difference = today - last_date.replace(tzinfo=None)

    # return the period corresponding to the difference, or 1 year

    if (days_difference < timedelta(days=5)):
        return '5d'
    elif (days_difference < timedelta(weeks=4)):
        return '1mo'
    elif (days_difference < timedelta(weeks=13)):
        return '3mo'
    elif (days_difference < timedelta(weeks=26)):
        return '6mo'
    else:
        return '1y'
```
The only thing missing is a method to wrap up everything. Let’s move on to it!

### Updating the table

This method wraps up all the others.

* I first get the most recent date in the table with `select_last_inserted_date`
* Then I calculate the period between today and this date with `get_period_to_download`
* I take the list of all SP 500 tickers with `get_sp500_ticker_symbols`
* And then, for each of these tickers, I download the data with `download_data` and insert it in CrateDB with `insert_values`

This is what the final function looks like:

```python
def update_table(table_name):

    # getting the last date in the table
    last_date = select_last_inserted_date(table_name)

    # calculating the period to download data from
    period = get_period_to_download(last_date)

    # getting all SP 500 tickers
    tickers = get_sp500_ticker_symbols()

    # downloading and inserting data from each ticker
    for ticker in tickers:
        data = download_data(ticker, period)
        insert_values(table_name, data)
```

## Final Test

I have all the necessary functions ready to work!

To have a clean final test, I

* place all the functions at the beginning of the Notebook and run their code blocks
* leave the CrateDB connection and the `update_table` call at the end 

```python
# Connecting to CrateDB
conn = ps.connect(host="<YOUR_CLUSTER>", port=5432,
                  user="admin", password="<PASSWORD>", sslmode="require")
cursor = conn.cursor()

# Updating table
table_name = "sp500"

update_table(table_name)
```

I navigate to the CrateDB Admin UI, where I see the new table **sp500** was created and that it is filled with the financial data.

![sp500-data-cratedb|690x405](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/868f1a3b16b58884779377892908243a8779b15f.png){w=800px}


I make a simple query to get Apple’s data from my **sp500** table 

```sql
SELECT * 
FROM "admin"."sp500"
WHERE ticker = 'AAPL'
ORDER BY closing_date LIMIT 100;
```
And instantly get the results.

![apple-data|690x405](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/9e2fbb2abdf2946bf063466de4f8468650c6d578.png){w=800px}

Now I can run this script whenever I want to update my database with new data!

## Wrap up

In this post, I introduced a method to download financial data from Yahoo Finance using Python and pandas and showed how to insert this data in CrateDB.

I profited from CrateDB’s high efficiency in rapidly inserting a large amount of data into my database and presented a method to get the most recent input date from CrateDB. That way, I can efficiently keep my records in CrateDB up to date!
