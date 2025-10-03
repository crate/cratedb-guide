(connect-python)=
# Python

This guide demonstrates how to connect to a CrateDB Cloud cluster using different
kinds of Python drivers. Individual drivers offer specific features for specific
needs of your application, so consider reading this enumeration carefully.

(python-drivers-official)=
## Official drivers

(crate-python)=
### crate-python

The `crate` Python package offers a database client implementation compatible
with the Python Database API 2.0 specification, and also includes the CrateDB
SQLAlchemy dialect. See the full documentation {ref}`here <crate-python:index>`.
The package can be installed using `pip install crate`.

```python
from crate import client

conn = client.connect("https://<name-of-your-cluster>.cratedb.net:4200", username="admin", password="<PASSWORD>", verify_ssl_cert=True)

with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sys.summits")
    result = cursor.fetchone()
    print(result)
```

(sqlalchemy-cratedb)=
### sqlalchemy-cratedb

The [SQLAlchemy] dialect for CrateDB, based on the HTTP-based DBAPI client
library [crate-python].
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


(python-drivers-community)=
## Community drivers

(cratedb-async)=

### cratedb-async

Asynchronous Python driver for CrateDB based on [HTTPX].
See the full documentation at <https://github.com/surister/cratedb-async>.
The package can be installed using `pip install cratedb-async`.

```python
import asyncio
from cratedb_async.client import CrateClient

async def main():
    crate = CrateClient("https://<name-of-your-cluster>.cratedb.net:4200")
    response = await crate.query("SELECT * FROM sys.summits")
    print(response.as_table())

asyncio.run(main())
```

(psycopg2)=

### psycopg2

Psycopg is a popular PostgreSQL database adapter for Python. Its main features
are the complete implementation of the Python DB API 2.0 specification and the
thread safety (several threads can share the same connection).
For more information, see the [psycopg documentation].

```python
import psycopg2

conn = psycopg2.connect(host="<name-of-your-cluster>.cratedb.net", port=5432, user="admin", password="<PASSWORD>", sslmode="require")

with conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM sys.summits")
        result = cursor.fetchone()
        print(result)
```

(psycopg3)=

### psycopg3

[Psycopg 3] is a newly designed PostgreSQL database adapter for the Python
programming language. Psycopg 3 presents a familiar interface for everyone who
has used Psycopg 2 or any other DB-API 2.0 database adapter, but allows to use
more modern PostgreSQL and Python features, such as:

- Asynchronous support
- COPY support from Python objects
- A redesigned connection pool
- Support for static typing
- Server-side parameters binding
- Prepared statements
- Statements pipeline
- Binary communication
- Direct access to the libpq functionalities

```python
import psycopg

with psycopg.connect("postgres://crate@localhost:5432/doc") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM sys.summits")
        for record in cursor:
            print(record)
```

(aiopg)=

### aiopg

aiopg is a python library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the Psycopg
database driver.
For more information, see the [aiopg documentation].

```python
import asyncio
import aiopg

async def run():
    async with aiopg.create_pool(host="<name-of-your-cluster>.cratedb.net", port=5432, user="admin", password="<PASSWORD>", sslmode="require") as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT * FROM sys.summits")
                result = await cursor.fetchone()
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
```

(asyncpg)=

### asyncpg

asyncpg is a database interface library designed specifically for PostgreSQL
and Python/asyncio. asyncpg is an efficient, clean implementation of the
PostgreSQL server binary protocol for use with Python's asyncio framework.
For more information, see the [asyncpg documentation].

```python
import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(host="<name-of-your-cluster>.cratedb.net", port=5432, user="admin", password="<PASSWORD>", ssl=True)
    try:
        result = await conn.fetch("SELECT * FROM sys.summits")
    finally:
        await conn.close()
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
```


(python-dataframe)=
(df)=
(dataframe)=
(dataframes)=
(dataframe-examples)=
## Dataframe libraries

How to use CrateDB together with popular open-source DataFrame libraries.

### Dask
- {ref}`dask`

### pandas
- {ref}`pandas`

### Polars
- {ref}`polars`



[aiopg documentation]: https://aiopg.readthedocs.io/
[asyncpg documentation]: https://magicstack.github.io/asyncpg/current/
[httpx]: https://www.python-httpx.org/
[psycopg 3]: https://www.psycopg.org/psycopg3/docs/
[psycopg documentation]: https://www.psycopg.org/docs/

[RDBMS]: https://en.wikipedia.org/wiki/RDBMS
[SQLAlchemy]: https://www.sqlalchemy.org/
[SQLAlchemy Code Examples]: https://github.com/crate/cratedb-examples/tree/main/by-language/python-sqlalchemy
[The CrateDB SQLAlchemy Dialect]: inv:sqlalchemy-cratedb:*:label#index
[Working with SQLAlchemy and CrateDB]: inv:sqlalchemy-cratedb:*:label#by-example
