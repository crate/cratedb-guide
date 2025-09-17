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


## pandas
:::{seealso}
Please navigate to the dedicated page about {ref}`pandas`.
:::


## Polars
:::{seealso}
Please navigate to the dedicated page about {ref}`polars`.
:::


[Apache Arrow]: https://arrow.apache.org/
[Dask]: https://www.dask.org/
[Dask DataFrames]: https://docs.dask.org/en/latest/dataframe.html
[Dask Futures]: https://docs.dask.org/en/latest/futures.html
[Polars]: https://pola.rs/

[Dask code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/dask
[Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]: https://cratedb.com/docs/python/en/latest/by-example/sqlalchemy/dataframe.html
[Guide to efficient data ingestion to CrateDB with pandas and Dask]: https://community.cratedb.com/t/guide-to-efficient-data-ingestion-to-cratedb-with-pandas-and-dask/1482
[Import weather data using Dask]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/dask-weather-data-import.ipynb
[Importing Parquet files into CrateDB using Apache Arrow and SQLAlchemy]: https://community.cratedb.com/t/importing-parquet-files-into-cratedb-using-apache-arrow-and-sqlalchemy/1161
[Polars code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/polars
