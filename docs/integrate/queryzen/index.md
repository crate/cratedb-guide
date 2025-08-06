(queryzen)=
# QueryZen

:::{rubric} About
:::

[QueryZen] makes it easier to manage SQL query statements over HTTP.

A `Zen` in QueryZen jargon is a named, parameterized, and versioned SQL query
that is created, updated, and executed over HTTP endpoints. It allows you to
decouple SQL from your application while controlling, versioning, and securing
data access from development to production.

![](https://github.com/surister/queryzen/raw/master/queryzen-docs/docs/concepts/img.png){w=700px}

:::{rubric} Features
:::

Overview:

* Create, get and delete Zens in different collections and run them in different databases.
* Automatically version queries, name and safely parameterize queries with special functions.
* High test coverage.
* Track, save and analyze statistics of your queries over time and versions.
* Everything is dockerized for easy development and deployment.

QueryZen includes:

* HTTP REST backend to handle the lifecycle of Zens.
* Task execution backend to handle the execution of the queries.
* Database driver abstraction for Python SQL drivers.
* Pythonic package to programmatically use QueryZen.

With QueryZen you can:

* Quickly create HTTP REST endpoints of your SQL data.
* Integrate your SQL data in your data pipelines with minimal configuration.
* Monitor individual query executions and analyze metrics.
* Version your SQL queries, build and test queries without affecting production.
* Create materialized views for SQL databases that do not support them.

:::{rubric} Synopsis
:::

```python
from queryzen import QueryZen

qz = QueryZen()

# Default collection is 'main' and the version is 'latest'.
qz.create("mountains", query="SELECT * FROM sys.summits WHERE country = :country AND height > :height")

# If no version is specified, it returns 'latest'.
zen = qz.get("mountains", collection="main")
print(zen)

# Invoke with default values.
result = qz.run(zen)

print(result.has_data)
print(result.as_table())
```

:::{rubric} Resources
:::

- [Documentation](https://qz.surister.dev/.)
- [Client Package](https://pypi.org/project/queryzen/)
- [Server OCI](https://hub.docker.com/r/surister/queryzen_api)
- [Source Repository](https://github.com/surister/queryzen)


[QueryZen]: https://github.com/surister/queryzen
