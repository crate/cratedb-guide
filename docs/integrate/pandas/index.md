(pandas)=
# pandas

```{div}
:style: "float: right"
[![](https://pandas.pydata.org/static/img/pandas.svg){w=180px}](https://pandas.pydata.org/)
```
```{div} .clearfix
```

:::{rubric} About
:::

[pandas] is a fast, powerful, flexible, and easy-to-use open-source data analysis
and manipulation tool, built on top of the Python programming language. It offers
data structures and operations for manipulating numerical tables and time series.

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


:::{rubric} Learn
:::
- {ref}`pandas-tutorial-start`
- {ref}`pandas-tutorial-jupyter`
- {ref}`arrow-import-parquet`
- {ref}`pandas-bulk-import`
- See also: {ref}`dask-bulk-import`
- See also: [Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]

:::{rubric} Code examples
:::
- [pandas code examples]


:::{toctree}
:maxdepth: 1
:hidden:
Starter tutorial <tutorial-start>
Jupyter tutorial <tutorial-jupyter>
Efficient ingest <efficient-ingest>
:::


[Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]: https://cratedb.com/docs/python/en/latest/by-example/sqlalchemy/dataframe.html
[pandas]: https://pandas.pydata.org/
[pandas code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/pandas
