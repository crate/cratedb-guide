(polars)=
# Polars

:::{div} .float-right .text-right
[![Polars logo](https://github.com/pola-rs/polars-static/raw/master/logos/polars-logo-dark.svg){height=60px loading=lazy}][Polars]
<br>
[![Polars CI](https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-polars.yml?branch=main)](https://github.com/crate/cratedb-examples/actions/workflows/dataframe-polars.yml)
:::
:::{div} .clearfix
:::

:::{rubric} About
:::

[Polars] is a high‑performance DataFrames library with interfaces for
Rust, Python, Node.js, and R, plus a SQL context. It is powered by a
multithreaded, vectorized query engine and written in Rust.

:::{dropdown} Features and data formats

Polars is an open-source library for data manipulation, known for being
one of the fastest data processing solutions on a single machine.
It features a well-structured, typed API that is both expressive and
easy to use. 

- **Fast:** Written from scratch in Rust and with performance in mind,
  designed close to the machine, and without external dependencies.

- **I/O:** First class support for all common data storage layers: local,
  cloud storage & databases.

- **Intuitive API:** Write your queries the way they were intended. Polars,
  internally, will determine the most efficient way to execute using its query
  optimizer. Polars' expressions are intuitive and empower you to write
  readable and performant code at the same time.

- **Out of Core:** The streaming API allows you to process your results without
  requiring all your data to be in memory at the same time.

- **Parallel:** Polars' multithreaded query engine utilizes the power of your
  machine by dividing the workload among the available CPU cores without any
  additional configuration.

- **Vectorized Query Engine:** Uses [Apache Arrow], a columnar data format, to
  process your queries in a vectorized manner and SIMD to optimize CPU usage.
  This enables cache-coherent algorithms and high performance on modern processors. 

- **Open Source:** Polars is and always will be open source. Driven by an active
  community of developers. Everyone is encouraged to add new features and contribute.
  It is free to use under the MIT license.

Polars supports reading and writing to many common data formats.
This allows you to easily integrate Polars into your existing data stack.

- Text: CSV, JSON
- Binary: Parquet, Delta Lake, Avro, Excel
- IPC: Feather, Arrow IPC
- Databases: MySQL, PostgreSQL, SQLite, Redshift, SQL Server, etc. (via ConnectorX)
- Cloud storage: Amazon S3, Azure Blob/ADLS (via fsspec‑compatible backends)

:::

:::{rubric} Install
:::

```shell
pip install 'polars[pyarrow]' sqlalchemy-cratedb
```

:::{rubric} Synopsis
:::

Write Polars dataframe to CrateDB.

`example.py`
```python
import polars as pl
import sqlalchemy as sa
from sqlalchemy_cratedb import insert_bulk

CRATEDB_URI = "crate://crate:crate@localhost:4200"
TABLE_NAME = "example"

df = pl.from_pandas(makeTimeDataFrame(rows=500_000, freq="s"))
engine = sa.create_engine(CRATEDB_URI)
df.write_database(
    engine="sqlalchemy",
    connection=engine,
    table_name=TABLE_NAME,
    if_table_exists="replace",
    engine_options={
        "method": insert_bulk,
        "chunksize": 20_000,
    },
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
pip install 'polars[pyarrow]' sqlalchemy-cratedb pandas
python example.py
```

:::{rubric} Full example
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/polars
:link-type: url
{material-regular}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using Polars.
+++
Includes basic examples of how to use Polars with CrateDB.
:::


[Apache Arrow]: https://arrow.apache.org/
[Polars]: https://pola.rs/
