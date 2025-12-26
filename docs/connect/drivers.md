(connect-drivers)=
# All drivers and client libraries

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Drivers and adapters for supported programming languages,
frameworks, and environments.
:::

## PostgreSQL

The drivers listed here all use the [CrateDB PostgreSQL interface].

::::{sd-table}
:widths: 2 3 5 2
:row-class: top-border

:::{sd-row}
```{sd-item}
```
```{sd-item} **Driver/Adapter**
```
```{sd-item} **Description**
```
```{sd-item} **Info**
```
:::

:::{sd-row}
```{sd-item} \-
```
```{sd-item}
[PostgreSQL ODBC](https://odbc.postgresql.org/)
```
```{sd-item}
The official PostgreSQL ODBC Driver.
For connecting to CrateDB from any environment that supports it.
```
```{sd-item}
```
:::

:::{sd-row}
```{sd-item} .NET
```
```{sd-item}
[Npgsql](https://www.npgsql.org/)
```
```{sd-item}
An open source ADO\.NET Data Provider for PostgreSQL, for program written in C#,
Visual Basic, and F#.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/npgsql/npgsql?label=latest)](https://github.com/npgsql/npgsql)
[![](https://img.shields.io/badge/example-runnable-darkcyan)](https://github.com/crate/cratedb-examples/tree/main/by-language/csharp-npgsql)
```
:::

:::{sd-row}
```{sd-item} .NET
```
```{sd-item}
[CrateDB Npgsql fork](https://cratedb.com/docs/npgsql/)
```
```{sd-item}
This fork of the official driver was needed prior to CrateDB 4.2.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/crate/npgsql?label=latest)](https://github.com/crate/npgsql)
```
:::

:::{sd-row}
```{sd-item} Golang
```
```{sd-item}
[pgx](https://github.com/jackc/pgx)
```
```{sd-item}
A pure Go driver and toolkit for PostgreSQL.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/jackc/pgx?label=latest)](https://github.com/jackc/pgx)
```
:::

:::{sd-row}
```{sd-item} Java
```
```{sd-item}
[PostgreSQL JDBC](https://jdbc.postgresql.org/)
```
```{sd-item}
The official PostgreSQL JDBC Driver.
For connecting to CrateDB from any environment that supports it.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/pgjdbc/pgjdbc?label=latest)](https://github.com/pgjdbc/pgjdbc)
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#java)
[![](https://img.shields.io/badge/example-runnable-darkcyan)](https://github.com/crate/cratedb-examples/tree/main/by-language/java-jdbc)
```
:::


:::{sd-row}
```{sd-item} Java
```
```{sd-item}
[CrateDB PgJDBC fork](https://cratedb.com/docs/jdbc/)
```
```{sd-item}
For connecting to CrateDB with specialized type system support and
other tweaks. Ignores the `ROLLBACK` statement and the `hstore` and
`jsonb` extensions.
```
```{sd-item}
[![](https://img.shields.io/maven-central/v/io.crate/crate-jdbc?label=latest)](https://github.com/crate/pgjdbc)
```
:::

:::{sd-row}
```{sd-item} Node.js
```
```{sd-item}
[node-postgres](https://node-postgres.com/)
```
```{sd-item}
A collection of Node.js modules for interfacing with a PostgreSQL database using
JavaScript or TypeScript.

Has support for callbacks, promises, async/await, connection pooling, prepared
statements, cursors, streaming results, C/C++ bindings, rich type parsing, and more.
```
```{sd-item}
[![](https://img.shields.io/npm/v/pg?label=latest&color=blue)](https://github.com/brianc/node-postgres)
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#node-postgres)
```
:::

:::{sd-row}
```{sd-item} PHP
```
```{sd-item}
[PDO_PGSQL](https://www.php.net/manual/en/ref.pdo-pgsql.php)
```
```{sd-item}
For connecting to CrateDB from PHP, supporting its PDO interface.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/php/php-src?label=latest)](https://github.com/php/php-src/tree/master/ext/pdo_pgsql)
[![](https://img.shields.io/badge/example-runnable-darkcyan)](https://github.com/crate/cratedb-examples/tree/main/by-language/php-pdo)
```
:::

:::{sd-row}
```{sd-item} PHP
```
```{sd-item}
[AMPHP](https://amphp.org/)
```
```{sd-item}
For connecting to CrateDB using AMPHP, an Async PostgreSQL client for PHP.
AMPHP is a collection of high-quality, event-driven libraries for PHP
designed with fibers and concurrency in mind.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/amphp/postgres?label=latest)](https://github.com/amphp/postgres)
[![](https://img.shields.io/badge/example-runnable-darkcyan)](https://github.com/crate/cratedb-examples/tree/main/by-language/php-amphp)
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[aiopg](https://github.com/aio-libs/aiopg)
```
```{sd-item}
For connecting to CrateDB from Python, supporting Python's async implementations
using the PEP-3156/tulip framework.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/aio-libs/aiopg?label=latest)](https://github.com/aio-libs/aiopg)
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#aiopg)
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[asyncpg](https://github.com/MagicStack/asyncpg)
```
```{sd-item}
For connecting to CrateDB from Python, supporting Python's async implementations.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/MagicStack/asyncpg?label=latest)](https://github.com/MagicStack/asyncpg)
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#asyncpg)
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[psycopg3](https://www.psycopg.org/psycopg3/docs/)
```
```{sd-item}
For connecting to CrateDB from Python, supporting Python's async implementations.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/psycopg/psycopg?label=latest)](https://github.com/psycopg/psycopg)
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#psycopg3)
```
:::

::::


## HTTP

The drivers listed here all use the [CrateDB HTTP interface].

::::{sd-table}
:widths: 2 3 5 2
:row-class: top-border

:::{sd-row}
```{sd-item}
```
```{sd-item} **Driver/Adapter**
```
```{sd-item} **Description**
```
```{sd-item} **Info**
```
:::

:::{sd-row}
```{sd-item} MicroPython
```
```{sd-item}
[micropython-cratedb](https://github.com/crate/micropython-cratedb)
```
```{sd-item}
A MicroPython library connecting to the CrateDB HTTP API.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/crate/micropython-cratedb?label=latest)](https://github.com/crate/micropython-cratedb)
```
:::

:::{sd-row}
```{sd-item} Node.js
```
```{sd-item}
[node-crate](https://www.npmjs.com/package/node-crate)
```
```{sd-item}
A JavaScript library connecting to the CrateDB HTTP API.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/megastef/node-crate?label=latest)](https://github.com/megastef/node-crate)
[![](https://img.shields.io/badge/example-application-darkcyan)](https://github.com/crate/devrel-shipping-forecast-geo-demo)
```
:::

:::{sd-row}
```{sd-item} PHP
```
```{sd-item}
[CrateDB PDO driver](https://cratedb.com/docs/pdo/)
```
```{sd-item}
For connecting to CrateDB from PHP.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/crate/crate-pdo?label=latest)](https://github.com/crate/crate-pdo)
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#connect-php)
```
:::

:::{sd-row}
```{sd-item} PHP
```
```{sd-item}
[CrateDB DBAL adapter](https://cratedb.com/docs/dbal/)
```
```{sd-item}
For connecting to CrateDB from PHP, using DBAL and Doctrine.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/crate/crate-dbal?label=latest)](https://github.com/crate/crate-dbal)
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#connect-php)
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[CrateDB Python driver](https://cratedb.com/docs/python/)
```
```{sd-item}
For connecting to CrateDB from Python. Provides [CrateDB BLOB support].
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/crate/crate-python?label=latest)](https://github.com/crate/crate-python)
[![](https://img.shields.io/badge/docs-by%20example-darkgreen)][python-dbapi-by-example]
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#crate-python)
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[SQLAlchemy dialect](https://cratedb.com/docs/sqlalchemy-cratedb/)
```
```{sd-item}
For connecting to CrateDB from Python, using SQLAlchemy.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/crate/sqlalchemy-cratedb?label=latest)](https://github.com/crate/sqlalchemy-cratedb)
[![](https://img.shields.io/badge/docs-by%20example-darkgreen)][python-sqlalchemy-by-example]
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#sqlalchemy-cratedb)
```
:::

:::{sd-row}
```{sd-item} Python
```
```{sd-item}
[CrateDB Async Python driver](https://github.com/surister/cratedb-async)
```
```{sd-item}
For connecting to CrateDB from Python, supporting Python's async implementations
by using the `httpx` HTTP client.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/surister/cratedb-async?label=latest)](https://github.com/surister/cratedb-async)
```
:::

:::{sd-row}
```{sd-item} Ruby
```
```{sd-item}
[CrateDB Ruby driver](https://github.com/crate/crate_ruby)
```
```{sd-item}
A Ruby client library for CrateDB.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/crate/crate_ruby?label=latest)](https://github.com/crate/crate_ruby)
[![](https://img.shields.io/badge/example-snippet-darkcyan)](#ruby)
[![](https://img.shields.io/badge/example-runnable-darkcyan)](https://github.com/crate/cratedb-examples/tree/main/by-language/ruby)
```
:::

:::{sd-row}
```{sd-item} Ruby
```
```{sd-item}
[CrateDB ActiveRecord adapter](https://github.com/crate/activerecord-crate-adapter)
```
```{sd-item}
Ruby on Rails ActiveRecord adapter for CrateDB.
```
```{sd-item}
[![](https://img.shields.io/github/v/tag/crate/activerecord-crate-adapter?label=latest)](https://github.com/crate/activerecord-crate-adapter)
```
:::

::::


```{tip}
Please visit the {ref}`build-status` page for an overview about the integration
status of the client drivers listed above, and more.
```


[CrateDB HTTP interface]: inv:crate-reference:*:label#interface-http
[CrateDB PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
