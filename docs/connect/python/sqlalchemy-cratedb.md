(sqlalchemy-cratedb)=
# sqlalchemy-cratedb

:::{div} .float-right .text-right
[![CrateDB SQLAlchemy CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-sqlalchemy.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-sqlalchemy.yml)
:::
:::{div} .clearfix
:::

The [SQLAlchemy] dialect for CrateDB, based on the HTTP-based DB API client
library {ref}`crate-python:index`.
See the full documentation {ref}`here <sqlalchemy-cratedb:index>`.
The package can be installed using `pip install sqlalchemy-cratedb`.

```python
import sqlalchemy as sa

engine = sa.create_engine("crate://localhost:4200", echo=True)
connection = engine.connect()

result = connection.execute(sa.text("SELECT * FROM sys.summits;"))
for record in result.all():
    print(record)
```

[SQLAlchemy] is the Python SQL toolkit and Object Relational Mapper that
gives application developers the full power and flexibility of SQL.

Python-based {ref}`dataframe`
and {ref}`ML <machine-learning>` frameworks, and a few {ref}`ETL <etl>`
frameworks, are using SQLAlchemy as database adapter library when connecting to
[RDBMS].

- [The CrateDB SQLAlchemy Dialect]
- [Working with SQLAlchemy and CrateDB]
- [SQLAlchemy Code Examples]


[RDBMS]: https://en.wikipedia.org/wiki/RDBMS
[SQLAlchemy]: https://www.sqlalchemy.org/
[SQLAlchemy Code Examples]: https://github.com/crate/cratedb-examples/tree/main/by-language/python-sqlalchemy
[The CrateDB SQLAlchemy Dialect]: inv:sqlalchemy-cratedb:*:label#index
[Working with SQLAlchemy and CrateDB]: inv:sqlalchemy-cratedb:*:label#by-example
