(crate-python)=
# crate-python

:::{div} .float-right .text-right
[![Python DB API CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-dbapi.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-dbapi.yml)
:::
:::{div} .clearfix
:::

The `crate` Python package provides a database client implementation compatible
with the Python Database API 2.0 specification. It is used by the CrateDB
SQLAlchemy dialect.

:::{rubric} Install
:::

```shell
pip install --upgrade crate
```

:::{rubric} Synopsis (localhost)
:::

```python
from crate import client

conn = client.connect("http://localhost:4200")

with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sys.summits")
    result = cursor.fetchone()
    print(result)
```

:::{rubric} Synopsis (CrateDB Cloud)
:::

```python
from crate import client

conn = client.connect(
    "https://<name-of-your-cluster>.cratedb.net:4200",
    username="admin",
    password="<PASSWORD>",
    verify_ssl_cert=True,
)

with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sys.summits")
    result = cursor.fetchone()
    print(result)
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: crate-python:index
:link-type: ref
:link-alt: Python DBAPI driver for CrateDB
The full documentation for the Python driver.
::::

::::{grid-item-card} {octicon}`code-square;1.75em;sd-text-info` &nbsp; Example
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/python-dbapi
:link-type: url
:link-alt: Python DBAPI example
An executable example using the Python driver.
::::

::::{grid-item-card} {octicon}`arrow-right;1.75em;sd-text-info` &nbsp; SQLAlchemy dialect
:link: sqlalchemy-cratedb:index
:link-type: ref
:link-alt: Documentation about CrateDB's SQLAlchemy dialect
The SQLAlchemy dialect for CrateDB is based on the HTTP-based DB API client.
::::

:::::
