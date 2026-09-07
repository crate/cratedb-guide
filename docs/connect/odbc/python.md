:::{include} /_include/links.md
:::

(odbc-python)=

# ODBC with Python

(odbc-pyodbc)=

## pyodbc

:::{rubric} About
:::

[pyodbc] is an open-source Python module that makes accessing ODBC databases
simple. It implements the DB API 2.0 specification and adds other Pythonic
convenience. For more information, please visit the
[pyodbc installation instructions] and [connecting to PostgreSQL with pyodbc].

:::{rubric} Install
:::

:::{include} /connect/odbc/install-dropdown.md
:::

Install the required Python package.
```shell
pip install --upgrade pyodbc
```

:::{rubric} Synopsis
:::

`example.py`
```python
import pyodbc

# Connect to database
connection_string = \
    "Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate;" \
    "MaxVarcharSize=1073741824;Sslmode=disable;"
connection = pyodbc.connect(connection_string)

# Invoke query
cursor = connection.cursor()
cursor.execute("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 5")

# Display results
for row in cursor:
    print(row)

# Clean up
cursor.close()
connection.close()
```

(odbc-turbodbc)=

## turbodbc

:::{rubric} About
:::

```{div} .float-right .text-right
[![Python turbodbc](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-turbodbc.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-turbodbc.yml)
```

[turbodbc] is a Python module to access relational databases via the Open
Database Connectivity (ODBC) interface. turbodbc offers built-in NumPy and
Apache Arrow for maximum performance.

```{div} .clearfix
```

:::{rubric} Install
:::

```shell
pip install --upgrade turbodbc
```

:::{rubric} Synopsis
:::

`example.py`
```python
import turbodbc

# Connect to database
connection_string = \
    "Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate;" \
    "MaxVarcharSize=1073741824;Sslmode=disable;"
connection = turbodbc.connect(connection_string)

# Invoke query
cursor = connection.cursor()
cursor.execute("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 5")

# Display results
for row in cursor:
    print(row)

# Clean up
cursor.close()
connection.close()
```

:::{seealso}

{ref}`Turbodbc -- a high-performance ODBC library <turbodbc>`

:::

(odbc-adbcbridge)=

## adbcBridge (ADBC over ODBC)

:::{rubric} About
:::

[adbcBridge] is an open-source driver for [ADBC], the Apache Arrow project's database
connectivity API. It loads an ODBC driver and returns query results as Arrow record
batches. Against CrateDB it uses the same psqlODBC
connection string as pyodbc and turbodbc, and hands the result to pandas, Polars, DuckDB
or anything else that consumes Arrow without a per-row conversion step. The same library
serves Rust, Go, Java and C# through the ADBC driver managers of those languages.
CrateDB is one of the databases it is verified against with one compatibility workload;
the [adbcBridge CrateDB entry] records the settings and what was measured.

:::{rubric} Install
:::

:::{include} /connect/odbc/install-dropdown.md
:::

Install the Python package, which bundles the driver library.
```shell
pip install --upgrade adbcbridge
```

:::{rubric} Synopsis
:::

`example.py`
```python
import adbcbridge

# Connect to database
connection_string = \
    "Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate;" \
    "MaxVarcharSize=1073741824;Sslmode=disable;"
connection = adbcbridge.connect(uri=connection_string)

# Invoke query
cursor = connection.cursor()
cursor.execute("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 5")

# Display results as an Arrow table
table = cursor.fetch_arrow_table()
print(table)

# Clean up
cursor.close()
connection.close()
```

`fetch_arrow_table()` returns a `pyarrow.Table`; `table.to_pandas()` and
`polars.from_arrow(table)` convert it without copying row by row. Bulk loading works the
other way round with `cursor.adbc_ingest("my_table", table)`, which sends one multi-row
`INSERT` per batch; run `REFRESH TABLE my_table` before counting the rows, as with any
CrateDB write.

## Example

Create the file `example.py` including the synopsis code shared above and
install the prerequisites like outlined above.

:::{include} ../_cratedb.md
:::
Invoke program.
```shell
python example.py
```

:::{rubric} SSL connection
:::

:::{div}
Use the `Sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to [CrateDB Cloud].
:::

```python
connection_string = \
    "Driver={PostgreSQL Unicode};Server=testcluster.cratedb.net;Port=5432;Uid=admin;Pwd=password;" \
    "MaxVarcharSize=1073741824;Sslmode=require;"
```


[adbcBridge CrateDB entry]: https://adbcbridge.org/matrix/#cratedb
[adbcBridge]: https://github.com/singhpratech/adbcbridge
[ADBC]: https://arrow.apache.org/adbc/
[connecting to PostgreSQL with pyodbc]: https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-PostgreSQL
[pyodbc installation instructions]: https://github.com/mkleehammer/pyodbc/wiki/Install
[pyodbc]: https://github.com/mkleehammer/pyodbc
[turbodbc]: https://turbodbc.readthedocs.io/
