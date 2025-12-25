(records)=

# Records

:::{div} .float-right .text-right
[![records (framework)](https://github.com/crate/cratedb-examples/actions/workflows/framework-records.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/framework-records.yml)
:::
:::{div} .clearfix
:::

Records is a deceptively simple but powerful library for making raw SQL
queries to most relational databases. Powered by SQLAlchemy and Tablib,
it covers many database types and allows you to export your results to
CSV, XLS, JSON, HTML Tables, YAML, or pandas dataframes with a single
line of code.

:::{rubric} Install
:::

```shell
pip install --upgrade records sqlalchemy-cratedb
```

:::{rubric} Synopsis
:::

```python
import records

db = records.Database("crate://", echo=True)
rows = db.query("SELECT region, mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")
data = rows.all()

print(rows.export("json"))
```


:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://github.com/kennethreitz/records
:link-type: url
:link-alt: Records documentation
The full documentation for Records.
::::

::::{grid-item-card} {octicon}`code-square;1.75em;sd-text-info` &nbsp; Example
:link: https://github.com/crate/cratedb-examples/tree/main/framework/records
:link-type: url
:link-alt: Records library example
An executable example using Records as a library.
::::

::::{grid-item-card} {octicon}`code-square;1.75em;sd-text-info` &nbsp; Example
:link: https://github.com/crate/cratedb-examples/tree/main/application/records
:link-type: url
:link-alt: Records program example
An executable example using Records as a CLI.
::::

:::::
