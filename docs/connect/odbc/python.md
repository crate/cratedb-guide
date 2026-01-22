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
    "Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate" \
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

:::{todo}
Enable with the [Python patch](https://github.com/crate/cratedb-guide/pull/403).
```md
- {ref}`Turbodbc -- a high-performance ODBC library <turbodbc>`
```
:::

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

Use the `Sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```python
connection_string = \
    "Driver={PostgreSQL Unicode};Server=testcluster.cratedb.net;Port=5432;Uid=admin;Pwd=password;" \
    "MaxVarcharSize=1073741824;Sslmode=require;"
```


[connecting to PostgreSQL with pyodbc]: https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-PostgreSQL
[pyodbc]: https://github.com/mkleehammer/pyodbc
[pyodbc installation instructions]: https://github.com/mkleehammer/pyodbc/wiki/Install
[turbodbc]: https://turbodbc.readthedocs.io/
