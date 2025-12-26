(sqlalchemy-cratedb)=
# sqlalchemy-cratedb

:::{div} .float-right .text-right
[![CrateDB SQLAlchemy CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-sqlalchemy.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-sqlalchemy.yml)
:::
:::{div} .clearfix
:::

[SQLAlchemy] is the Python SQL toolkit and Object Relational Mapper that
gives application developers the full power and flexibility of SQL.

Python-based {ref}`dataframe`
and {ref}`ML <machine-learning>` frameworks, and a few {ref}`ETL <etl>`
frameworks, are using SQLAlchemy as database adapter library when connecting to
[RDBMS].

The [SQLAlchemy] dialect for CrateDB is based on the HTTP-based DB API client
library {ref}`crate-python:index`.

:::{rubric} Install
:::

```shell
pip install --upgrade sqlalchemy-cratedb
```

:::{rubric} Synopsis
:::

```python
import sqlalchemy as sa

engine = sa.create_engine("crate://localhost:4200", echo=True)
connection = engine.connect()

result = connection.execute(sa.text("SELECT * FROM sys.summits;"))
for record in result.all():
    print(record)
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: sqlalchemy-cratedb:index
:link-type: ref
:link-alt: Python SQLAlchemy dialect for CrateDB
The full documentation for the CrateDB SQLAlchemy dialect.
::::

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; By example
:link: sqlalchemy-cratedb:by-example
:link-type: ref
:link-alt: CrateDB SQLAlchemy dialect by example
Working with SQLAlchemy and CrateDB.
::::

::::{grid-item-card} {octicon}`code-square;1.75em;sd-text-info` &nbsp; Example
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/python-sqlalchemy
:link-type: url
:link-alt: SQLAlchemy code Examples
An executable example using the SQLAlchemy dialect.
::::

:::::


[RDBMS]: https://en.wikipedia.org/wiki/RDBMS
[SQLAlchemy]: https://www.sqlalchemy.org/
