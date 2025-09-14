(df)=
(dataframe)=
(dataframes)=
(dataframe-examples)=
# CrateDB and DataFrame libraries

How to use CrateDB together with popular open-source DataFrame libraries.

(dask)=
## Dask

:::{rubric} About
:::
[Dask] is a parallel computing library for analytics with task scheduling.
It is built on top of the Python programming language, making it easy to scale
the Python libraries that you know and love, like NumPy, pandas, and scikit-learn.

```{div}
:style: "float: right"
[![](https://github.com/crate/crate-clients-tools/assets/453543/99bd2234-c501-479b-ade7-bcc2bfc1f288){w=180px}](https://www.dask.org/)
```

- [Dask DataFrames] help you process large tabular data by parallelizing pandas,
  either on your laptop for larger-than-memory computing, or on a distributed
  cluster of computers.

- [Dask Futures], implementing a real-time task framework, allow you to scale
  generic Python workflows across a Dask cluster with minimal code changes,
  by extending Python's `concurrent.futures` interface.

```{div}
:style: "clear: both"
```

:::{rubric} Learn
:::
- [Guide to efficient data ingestion to CrateDB with pandas and Dask]
- [Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]
- [Import weather data using Dask]
- [Dask code examples]


(pandas)=
## pandas

:::{rubric} About
:::

```{div}
:style: "float: right"
[![](https://pandas.pydata.org/static/img/pandas.svg){w=180px}](https://pandas.pydata.org/)
```

[pandas] is a fast, powerful, flexible, and easy-to-use open-source data analysis
and manipulation tool, built on top of the Python programming language. 

Pandas (stylized as pandas) is a software library written for the Python programming
language for data manipulation and analysis. In particular, it offers data structures
and operations for manipulating numerical tables and time series.

:::{rubric} Data Model
:::
- Pandas is built around data structures called Series and DataFrames. Data for these
  collections can be imported from various file formats such as comma-separated values,
  JSON, Parquet, SQL database tables or queries, and Microsoft Excel.
- A Series is a 1-dimensional data structure built on top of NumPy's array.
- Pandas includes support for time series, such as the ability to interpolate values
  and filter using a range of timestamps.
- By default, a Pandas index is a series of integers ascending from 0, similar to the
  indices of Python arrays. However, indices can use any NumPy data type, including
  floating point, timestamps, or strings.
- Pandas supports hierarchical indices with multiple values per data point. An index
  with this structure, called a "MultiIndex", allows a single DataFrame to represent
  multiple dimensions, similar to a pivot table in Microsoft Excel. Each level of a
  MultiIndex can be given a unique name.

```{div}
:style: "clear: both"
```

:::{rubric} Learn
:::
- [Guide to efficient data ingestion to CrateDB with pandas]
- [Importing Parquet files into CrateDB using Apache Arrow and SQLAlchemy]
- [pandas code examples]
- [From data storage to data analysis: Tutorial on CrateDB and pandas]


## Polars
:::{seealso}
Please navigate to the dedicated page about {ref}`polars`.
:::


[Apache Arrow]: https://arrow.apache.org/
[Dask]: https://www.dask.org/
[Dask DataFrames]: https://docs.dask.org/en/latest/dataframe.html
[Dask Futures]: https://docs.dask.org/en/latest/futures.html
[pandas]: https://pandas.pydata.org/

[Dask code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/dask
[Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]: https://cratedb.com/docs/python/en/latest/by-example/sqlalchemy/dataframe.html
[From data storage to data analysis: Tutorial on CrateDB and pandas]: https://community.cratedb.com/t/from-data-storage-to-data-analysis-tutorial-on-cratedb-and-pandas/1440
[Guide to efficient data ingestion to CrateDB with pandas]: https://community.cratedb.com/t/guide-to-efficient-data-ingestion-to-cratedb-with-pandas/1541
[Guide to efficient data ingestion to CrateDB with pandas and Dask]: https://community.cratedb.com/t/guide-to-efficient-data-ingestion-to-cratedb-with-pandas-and-dask/1482
[Import weather data using Dask]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/dask-weather-data-import.ipynb
[Importing Parquet files into CrateDB using Apache Arrow and SQLAlchemy]: https://community.cratedb.com/t/importing-parquet-files-into-cratedb-using-apache-arrow-and-sqlalchemy/1161
[pandas code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/pandas
