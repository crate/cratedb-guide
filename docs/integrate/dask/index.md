(dask)=
# Dask

:::{div} .float-right .text-right
[![Dask logo](https://github.com/crate/crate-clients-tools/assets/453543/99bd2234-c501-479b-ade7-bcc2bfc1f288){height=60px loading=lazy}][Dask]
<br>
[![Dask CI](https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-dask.yml?branch=main)](https://github.com/crate/cratedb-examples/actions/workflows/dataframe-dask.yml)
:::
:::{div} .clearfix
:::

:::{rubric} About
:::

[Dask] is a parallel computing library for analytics with task scheduling.
It is built on top of the Python programming language, making it easy to scale
the Python libraries that you know and love, like NumPy, pandas, and scikit-learn.

- [Dask DataFrames] help you process large tabular data by parallelizing pandas,
  either on your laptop for larger-than-memory computing, or on a distributed
  cluster of computers.

- [Dask Futures], implementing a real-time task framework, allow you to scale
  generic Python workflows across a Dask cluster with minimal code changes,
  by extending Python's `concurrent.futures` interface.

:::{rubric} Install
:::

```shell
pip install 'dask[dataframe]' 'sqlalchemy-cratedb'
```

:::{rubric} Synopsis
:::

Write Dask dataframe to CrateDB.

`example.py`
```python
import dask.dataframe as dd
from sqlalchemy_cratedb import insert_bulk

CRATEDB_URI = "crate://crate:crate@localhost:4200"
TABLE_NAME = "example"

df = makeTimeDataFrame(rows=500_000, freq="s")
ddf = dd.from_pandas(df, npartitions=4)
ddf.to_sql(
    TABLE_NAME,
    uri=CRATEDB_URI,
    index=False,
    if_exists="replace",
    chunksize=20_000,
    parallel=True,
    method=insert_bulk,
)
```

:::{rubric} Quickstart example
:::

Create the file `example.py` including the synopsis code shared above.
Complete the example by using the `makeTimeDataFrame()` function.

:::{literalinclude} ../pandas/makeTimeDataFrame.py
:::

:::{include} /connect/_cratedb.md
:::
```shell
pip install 'dask[dataframe]' 'sqlalchemy-cratedb'
python example.py
```

:::{rubric} Full example
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/dask
:link-type: url
{material-regular}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using Dask.
+++
Includes basic examples of how to use Dask with CrateDB.
:::

:::{rubric} Guides
:::

- {ref}`dask-usage`

:::{rubric} Related sections
:::

- {ref}`Efficient batch/bulk INSERT operations for pandas, Dask, and Polars <sqlalchemy-cratedb:dataframe>`
- {ref}`arrow-import-parquet`
- [Import weather data using Dask]


:::{toctree}
:maxdepth: 1
:hidden:
Usage <usage>
:::


[Dask]: https://www.dask.org/
[Dask DataFrames]: https://docs.dask.org/en/latest/dataframe.html
[Dask Futures]: https://docs.dask.org/en/latest/futures.html
[Import weather data using Dask]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/dask-weather-data-import.ipynb
