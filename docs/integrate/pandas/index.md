(pandas)=
# pandas

:::{div} .float-right .text-right
[![pandas logo](https://pandas.pydata.org/static/img/pandas.svg){height=60px loading=lazy}][pandas]
<br>
[![pandas CI](https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-pandas.yml?branch=main)](https://github.com/crate/cratedb-examples/actions/workflows/dataframe-pandas.yml)
:::
:::{div} .clearfix
:::

:::{rubric} About
:::

[pandas] is a fast, powerful, flexible, and easy-to-use open-source data analysis
and manipulation tool, built on top of the Python programming language. It offers
data structures and operations for manipulating numerical tables and time series.

Pandas is built around data structures called Series and DataFrames. Data for these
collections can be imported from various file formats such as comma-separated values,
JSON, Parquet, SQL database tables or queries, and Microsoft Excel.
A Series is a 1-dimensional data structure built on top of NumPy's array.

:::{rubric} Install
:::

```shell
pip install pandas sqlalchemy-cratedb
```

:::{rubric} Synopsis
:::

Write pandas dataframe to CrateDB.

`example.py`
```python
import sqlalchemy as sa
from sqlalchemy_cratedb import insert_bulk

CRATEDB_URI = "crate://crate:crate@localhost:4200"
TABLE_NAME = "example"

df = makeTimeDataFrame(rows=500_000, freq="s")
engine = sa.create_engine(CRATEDB_URI)
df.to_sql(
    name=TABLE_NAME,
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=20_000,
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
pip install pandas sqlalchemy-cratedb
python example.py
```

:::{rubric} Full example
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/pandas
:link-type: url
{material-regular}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using pandas.
+++
Includes basic examples of how to use pandas with CrateDB.
:::

:::{rubric} Guides
:::

- {ref}`pandas-efficient-import`
- {ref}`pandas-tutorial-start`
- {ref}`pandas-tutorial-jupyter`

:::{rubric} Related sections
:::

- {ref}`Efficient batch/bulk INSERT operations for pandas, Dask, and Polars <sqlalchemy-cratedb:dataframe>`
- {ref}`arrow-import-parquet`


:::{toctree}
:maxdepth: 1
:hidden:
Starter tutorial <tutorial-start>
Jupyter tutorial <tutorial-jupyter>
Efficient ingest <efficient-ingest>
:::


[pandas]: https://pandas.pydata.org/
