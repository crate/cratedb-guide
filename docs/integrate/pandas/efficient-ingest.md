(pandas-bulk-import)=
(pandas-efficient-import)=

# Efficient bulk imports with pandas

## Introduction
Bulk insert is a technique for efficiently inserting large amounts of data into a database by submitting multiple rows of data in a single database transaction. Instead of executing multiple SQL `INSERT` statements for each individual row of data, the bulk insert allows the database to process and store a batch of data at once. This approach can significantly improve the performance of data insertion, especially when dealing with large datasets.

In this tutorial, you will learn how to efficiently perform [bulk inserts](https://crate.io/docs/python/en/latest/by-example/sqlalchemy/dataframe.html) into CrateDB with [pandas](https://pandas.pydata.org/) using the `insert_bulk` method, available in the `crate` Python library. To follow along with this tutorial, you should have the following:

* A working installation of CrateDB. To get started with CrateDB check [this link](https://crate.io/lp-free-trial?hsCtaTracking=c2099713-cafa-4de6-a97e-2f86d80a788f%7C3a12b78e-e605-461c-9bd8-628d0d9e2522).
* Python, Pandas, SQLAlchemy, and the {ref}`sqlalchemy-cratedb:index` installed on your machine
* Basic familiarity with pandas and SQL

## Bulk insert to CrateDB

The following example illustrates how to implement batch insert with the pandas
library by using the `insert_bulk` support method available in the CrateDB
SQLAlchemy dialect.

```python
import sqlalchemy as sa
import crate
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_cratedb import insert_bulk
from pandas._testing import makeTimeDataFrame

INSERT_RECORDS = 5000000
CHUNK_SIZE = 50000

df = makeTimeDataFrame(nper=INSERT_RECORDS, freq="S")
engine = sa.create_engine('crate://localhost:4200')

df.to_sql(
    name="cratedb-demo",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=CHUNK_SIZE,
    method=insert_bulk,
)
```

By running this code, you will generate a DataFrame with a time-based index containing 5,000,000 rows of data. Each row represents a timestamp with a frequency of 1 second (`freq="S"`). The DataFrame is then inserted into a `cratedb-demo` table in CrateDB using the `to_sql()` method. If the table already exists, it will be replaced with the new data. The data insertion will be performed in batches, with each batch containing 50,000 records. Defining the `chunksize` parameter helps in managing memory and improving performance during the data insertion process.

The above code runs in approximately 14s on a local Mac M1 machine with 16GiB RAM. However, if we insert data to CrateDB by setting the `method` parameter to `None` (one insert per row), the execution time increases to 27sec.

## How to find the right chunksize

Determining the right chunksize depends on several factors, such as the size of your data, the number of columns in your data set, and the available memory of your machine.

The `chunksize` parameter in the `to_sql()` method controls the number of rows inserted in each batch. By default, `chunksize=None`, which means the entire DataFrame will be written to the database at once. However, when working with large datasets, it is recommended to set a smaller `chunksize` value to avoid memory issues and to improve the performance of the data insertion.

To determine the right `chunksize` value, you can try different values and observe the memory usage and the time it takes to complete the data insertion. A good starting point is to set the `chunksize` value to a fraction of the total number of rows in your DataFrame. For example, you can start with a `chunksize` value of 10,000 or 50,000 rows and see how it performs. If the data insertion is slow, you can try increasing the `chunksize` value to reduce the number of batches. On the other hand, if you encounter memory issues, you can try reducing the `chunksize` value.

## Conclusion

Congratulations! You have learned how to implement an efficient data insert into CrateDB using Pandas and `insert_bulk` method. This method allows for efficient and fast data insertion, making it suitable for handling large datasets.

If you like this tutorial and want to explore further CrateDB functionalities, please visit our [documentation](https://crate.io/docs) and join our [community](https://community.cratedb.com/).
