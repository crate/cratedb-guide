(pandas-tutorial-start)=
# From data storage to data analysis: Tutorial on CrateDB and pandas

## Introduction

Pandas is an open-source data manipulation and analysis library for Python. It is widely used for handling and analyzing data in a variety of fields, including finance, research, etc.

One of the key benefits of pandas is its ability to handle and manipulate large datasets, making it a valuable tool for data scientists and analysts. The library provides easy-to-use data structures and functions for data cleaning, transformation, and analysis, making it an essential part of the data analysis workflow.

Using CrateDB and pandas together can be a powerful combination for handling large volumes of data and performing complex data analysis tasks. In this tutorial, we will showcase using the real-world dataset how to use CrateDB and pandas together for effective data analysis.

## Requirements

To follow along with this tutorial, you will need:

* A running instance of CrateDB 5.2.
* Python 3.x with the [pandas 2](https://pandas.pydata.org/pandas-docs/version/2.0/whatsnew/v2.0.0.html) and [crate 0.31](https://github.com/crate/crate-python) packages installed.
* A real-world dataset in CSV format. In this tutorial, we will be using the shop customer data available on [Kaggle](https://www.kaggle.com/datasets/datascientistanna/customers-dataset).

## Setting up CrateDB

Before we can start using CrateDB, we need to set it up. You can either download and install CrateDB locally via [Docker](https://crate.io/docs/crate/tutorials/en/latest/basic/index.html#docker) or [tarball](https://crate.io/docs/crate/tutorials/en/latest/basic/index.html#try-cratedb-without-installing) or use a [CrateDB Cloud](https://crate.io/download?hsCtaTracking=caa20047-f2b6-4e8c-b7f9-63fbf818b17f%7Cf1ad6eaa-39ac-49cd-8115-ed7d5dac4d63) instance with an option of the free cluster.

Once you have a running instance of CrateDB, create a new table to store the customer data dataset. Here is an SQL command to create a table:

``` sql
CREATE TABLE IF NOT EXISTS "doc"."customer_data" (
   "customerid" INTEGER,
   "gender" TEXT,
   "age" INTEGER,
   "annualincome" INTEGER,
   "spendingscore" INTEGER,
   "profession" TEXT,
   "workexperience" INTEGER,
   "familysize" INTEGER
);
```

After creating the table, you can import the customer data dataset into CrateDB using the `COPY FROM `command:

```sql 
COPY "doc"."customer_data" FROM 'file:///path/to/Customers.csv' WITH (format='csv', delimiter=',');
```

Once you have CrateDB running, you can start exploring data with pandas.

## Querying data with CrateDB and pandas

The first step is to import the `pandas` library and specify the query you want to execute on CrateDB. In our example, we want to fetch all customer data.

To read data from CrateDB and work with it in a pandas DataFrame use `read_sql` method as illustrated below.


```python
import pandas as pd

query = "SELECT * FROM customer_data"
df = pd.read_sql(query, 'crate://localhost:4200')
```

In the above code, we establish a connection to a local CrateDB instance running on localhost on port 4200, execute a SQL query, and return the results as a pandas DataFrame. You can further modify the query to retrieve only the columns you need or to filter the data based on some condition.



## Analyze the data

Now that data are loaded into the pandas DataFrame, we can perform various analyses and manipulations on it. For instance, we can group the data by a certain column and calculate the average value of another column:

```python
avg_income = df.groupby("profession")["annualincome"].mean()
```

In this example, we group the data in the DataFrame by the `profession` column and calculate the average annual income for each profession. You can plot the data about average incomes using `df.plot()` method, specifying the type of plot (a bar chart), and the columns to use for the x and y axes:

```python
import matplotlib.pyplot as plt

income_by_profession.plot(kind='bar', legend=True, rot=0)
plot.show()
```

We also use `plt.show()` from `matplotlib` to display the plot:

![python-plot|690x479, 100%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ab652c811106f6a79b911a443bb8c11099f55b98.png)


## Wrap up

That's it! You should now have a good idea of how to use CrateDB and pandas together to analyze large datasets stored in CrateDB. This allows you to take advantage of the powerful data manipulation capabilities of pandas to analyze and visualize your data.
To learn more about updates, features, and other questions you might have, join our [CrateDB](https://community.cratedb.com/) community.
