(connect-python)=
# Python

:::{div} sd-text-muted
Connect to CrateDB and CrateDB Cloud from Python.
:::

Individual adapters, clients, and drivers offer specific features for specific
needs of your application, so please read this enumeration carefully, to
select the optimal adapter client or driver for your purposes.

As a general recommendation, using the SQLAlchemy adapter for many reasons
isn't a bad choice, because many other frameworks will use it anyway.
A good example is the most high-level Python package `records`.

Other than this, we can recommend `psycopg3` and `asyncpg` if you are
looking at using the PostgreSQL protocol.

(python-client-official)=
## Official clients

:::{rubric} Standard
:::
Standard clients implementing the Python DB API and the CrateDB dialect for SQLAlchemy.
<small>`crate-python` uses `urllib3`. `sqlalchemy-cratedb` uses `crate-python`.</small>
:::{toctree}
crate-python
sqlalchemy-cratedb
:::

(python-client-special)=
:::{rubric} Special purpose
:::
Adapter clients and drivers for special requirements on the environment or
on performance details.
`conecta` uses Rust and Apache Arrow.
`cratedb-async` uses `httpx`.
`micropython-cratedb` uses MicroPython's standard `httplib`.
:::{toctree}
conecta
cratedb-async
micropython-cratedb
:::

(python-client-community)=
## Tertiary clients

Clients that either use the PostgreSQL wire protocol, or standard
interfaces like SQLAlchemy.
`psycopg2` and `psycopg3` use `libpq`. `aiopg` uses `psycopg2`.
`connectorx` uses Rust. `records` uses `sqlalchemy`, so it also
uses `sqlalchemy-cratedb`. `turbodbc` uses PostgreSQL ODBC.

:::{toctree}
psycopg2
psycopg3
aiopg
asyncpg
connectorx
records
turbodbc
:::

(python-dataframe)=
(df)=
(dataframe)=
(dataframes)=
(dataframe-examples)=
## Dataframe libraries

Use CrateDB together with popular open-source dataframe libraries.
Each of them is using the CrateDB SQLAlchemy dialect for database
communications.

:::::{grid} 2 3 4 4
:gutter: 3 3 4 5
:padding: 0

::::{grid-item-card} Dask
:link: dask
:link-type: ref
:link-alt: Connect to CrateDB using Dask
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6
![Dask logo](https://github.com/crate/crate-clients-tools/assets/453543/99bd2234-c501-479b-ade7-bcc2bfc1f288){height=40px}
::::

::::{grid-item-card} pandas
:link: pandas
:link-type: ref
:link-alt: Connect to CrateDB using pandas
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6
![pandas logo](https://pandas.pydata.org/static/img/pandas.svg){height=40px}
::::

::::{grid-item-card} Polars
:link: polars
:link-type: ref
:link-alt: Connect to CrateDB using Polars
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-6
![Polars logo](https://github.com/pola-rs/polars-static/raw/master/logos/polars-logo-dark.svg){height=40px}
::::

:::::

:::{tip}
The `insert_bulk` utility function from `sqlalchemy-cratedb` unlocks
a performance path, see also {ref}`sqlalchemy-cratedb:support-insert-bulk`.
About optimally configuring pandas and Dask for efficient insert operations,
see also {ref}`sqlalchemy-cratedb:dataframe`.
:::
