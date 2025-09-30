(dask-usage)=
(dask-efficient-ingest)=
# Efficient data ingestion with Dask and CrateDB

## Introduction
Dask is a parallel computing library that enables distributed computing for tasks such as data processing and machine learning.
In this usage guide, we'll explore how to leverage the power of CrateDB, a distributed SQL database, in conjunction with Dask, to perform efficient data processing and analysis tasks.

Prerequisites:

Before getting started, you should have the following installed:

* Python 3.9 or higher
* CrateDB
* Dask

You can use pip to install Dask. To make sure that you have everything required for the most common uses of Dask (e.g., Dask Dataframe, Dask Array, etc) use the following command:

```
python -m pip install "dask[complete]"
```

## Inserting data

For this usage guide, we chose to use the California housing prices dataset, also available on [Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices?resource=download). This dataset is a popular dataset for regression tasks, consisting of median house values in census tracts in California, making it an excellent starting point for implementing basic machine learning algorithms.

Before importing data, create a california_housing table in CrateDB:

```sql
CREATE TABLE IF NOT EXISTS "doc"."california_housing" (
   "longitude" REAL,
   "latitude" REAL,
   "housing_median_age" REAL,
   "total_rooms" REAL,
   "total_bedrooms" REAL,
   "population" REAL,
   "households" REAL,
   "median_income" REAL,
   "median_house_value" REAL,
   "ocean_proximity" TEXT
)
```

Use COPY FROM command to import housing data:

```sql
COPY "doc"."california_housing" FROM 'file:///path/to/file'
```

## Using Dask to query the data

Dask provides three methods to read an SQL query or a database table into a Dataframe:
`read_sql`, `read_sql_table`, and `read_sql_query`.
The `read_sql` method is a convenience wrapper around the other two, and it will
delegate to a specific function based on the provided input. To use this method,
you will need the following parameters:

* `sql`: name of a SQL table in a database or an SQL query to be executed,
* `uri`: the full sqlalchemy URI for the database connection
* `index_col`: the index column. The index column is used by Dask to split up the query on multiple machines.

Now, let’s load the data from a California housing dataset to a Dask Dataframe:

```python
import dask
import dask.dataframe as dd
URI = 'crate://localhost:4200'

df = dd.read_sql(table_name='california_housing', con = URI, index_col = 'total_rooms') 
```

In the above example, we read the data from california_housing dataset and use total_rooms as an index column.

If you want to run read_sql with a query to be executed, you will need to provide an ***SQLAlchemy Selectable*** query. The following example shows how to query several columns from california_housing table and load the result to the Dask Dataframe.

```python
from sqlalchemy import table, column

data = table("california_housing",
        column("longitude"),
        column("latitude"),
        column("total_rooms"),
        column("total_bedrooms"),
        column("population")
)

df = dd.read_sql(sql=data.select(), con = URI, index_col = 'total_rooms')
```

Now that we loaded the data we can use the df.head() to show the first n rows in the dataset:

```python
print(df.head(n=5))
```

```python
housing_median_age   longitude  latitude  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity
                                                                                                                             
21.0                  -122.22     37.86       7099.0          1106.0      2401.0      1138.0         8.3014            358500.0        NEAR BAY
52.0                  -122.25     37.85       1627.0           280.0       565.0       259.0         3.8462            342200.0        NEAR BAY
52.0                  -122.25     37.85        919.0           213.0       413.0       193.0         4.0368            269700.0        NEAR BAY
52.0                  -122.26     37.85       2491.0           474.0      1098.0       468.0         3.0750            213500.0        NEAR BAY
52.0                  -122.26     37.85       2643.0           626.0      1212.0       620.0         1.9167            159200.0        NEAR BAY
```

### Linear regression with Dask and CrateDB

In the following example, we will illustrate how to perform a linear regression task on the California housing data. We will train a machine learning model that predicts the median house value based on the other variables in the dataset. Before we start, we need to categorize the ocean_proximity column as the only non-number column:

```python
df=df.categorize(columns='ocean_proximity')
df['ocean_proximity'] = df['ocean_proximity'].cat.as_known().cat.codes
```

The above code will transform the last column so that it contains a number representing a certain category, as illustrated below:
```python
print(df.compute().head(3))
```
```python
housing_median_age   longitude  latitude  total_rooms  total_bedrooms  population  households  median_income  median_house_value ocean_proximity                                                                                                                             
21.0                  -122.22     37.86       7099.0          1106.0      2401.0      1138.0         8.3014            358500.0                3
52.0                  -122.25     37.85       1627.0           280.0       565.0       259.0         3.8462            342200.0                3
52.0                  -122.25     37.85        919.0           213.0       413.0       193.0         4.0368            269700.0                3    
```

The next step is to split the data into training and testing sets and for that, we can use the dask_ml library. For the linear regression estimator to work with the data we need to transform training and testing sets into Dask arrays:

```python
from dask_ml.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop('median_house_value', axis=1), df['median_house_value'], test_size=0.2, shuffle=True)

X_train= X_train.to_dask_array(lengths=True)
X_test = X_test.to_dask_array(lengths=True)
y_train = y_train.to_dask_array(lengths=True)
y_test = y_test.to_dask_array(lengths=True)
```

Now we can perform a linear regression task on the data. First, we need to create a linear regression estimator and fit the estimator to the training data:

```python
from dask_ml.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
```

In the last line, we use the estimator to make predictions on the testing data. To evaluate the performance of our linear regression model, we can calculate the mean squared error (MSE) and the coefficient of determination (R²) on the testing data:

```python
from dask_ml.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean squared error: {mse:.2f}')
print(f'R² score: {r2:.2f}')
```

The last two lines will output the mean squared error and R² score for our linear regression model.

## Using Dask to write to CrateDB

Dask also provides support for storing Dask Dataframe to a SQL table with the to_sql method. To illustrate the concurrent write of a Dask Dataframe to CrateDB we first create a Pandas DataFrame using the makeTimeDataFrame function with a frequency of one second and a total of 1,5 million periods as illustrated below.

```python
from pandas._testing import makeTimeDataFrame
df = makeTimeDataFrame(nper=1_500_000, freq="S")
```

Then, we create the Dask Dataframe from the Pandas Dataframe and divide the data into 4 partitions, allowing for parallel processing:

```python
ddf = dd.from_pandas(df, npartitions=4)
```

Finally, with the to_sql() method we load the data to a CrateDB database:

```python
ddf.to_sql("demo", uri=URI, index=False, if_exists="replace", chunksize=10000, parallel=True)
```

The to_sql() method takes several arguments:

* `"demo"`: the name of the table where the data will be loaded.
* `uri`: the connection string to the CrateDB database.
* `index=False`: specifies that the index column in the DataFrame should not be included in the database table.
* `if_exists="replace"`: specifies that if the table already exists, it should be replaced with the new data. Other possible values are 'fail', 'replace', and 'append'.
* `chunksize=10000`: the number of rows to be inserted at a time. It may be helpful to experiment with different chunk sizes to find the optimal value for the specific use case.
* `parallel=True`: specifies that the insertion process should be done in parallel.

On an M1 machine with 16 GB of RAM, the entire process of loading the 1.5 million records worth of data into the database, takes approximately 15 seconds. Without using `parallel=True`, the total runtime increases to 22 seconds, thus demonstrating that it is more efficient than running insert operations subsequently.

## Conclusions

In this usage guide, we've covered the essentials of using CrateDB with Dask for efficient data processing and analysis. By combining the distributed capabilities of CrateDB with the parallel computing power of Dask, you can unlock the potential to handle large-scale datasets, perform complex queries, and leverage advanced analytics techniques.

To learn more about updates, features, and other questions you might have, join our [CrateDB community](https://community.cratedb.com/).
