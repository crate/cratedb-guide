(records)=

# Records

:::{div} .float-right .text-right
[![records (framework)](https://github.com/crate/cratedb-examples/actions/workflows/framework-records.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/framework-records.yml)
:::
:::{div} .clearfix
:::

[Records] is a deceptively simple but powerful library for making raw SQL
queries to most relational databases. Powered by SQLAlchemy and Tablib,
it covers many database types and allows you to export your results to
CSV, XLS, JSON, HTML Tables, YAML, or pandas dataframes with a single
line of code.

```shell
pip install --upgrade records sqlalchemy-cratedb
```
```python
import records

db = records.Database("crate://", echo=True)
rows = db.query("SELECT region, mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")
data = rows.all()

print(rows.export("json"))
```


[Records]: https://github.com/kennethreitz/records
