(psycopg2)=

# psycopg2

Psycopg is a popular PostgreSQL database adapter for Python. Its main features
are the complete implementation of the Python DB API 2.0 specification and the
thread safety (several threads can share the same connection).

:::{rubric} Install
:::

```shell
pip install --upgrade psycopg2-binary
```

:::{rubric} Synopsis
:::

```python
import psycopg2

conn = psycopg2.connect(host="<name-of-your-cluster>.cratedb.net", port=5432, user="admin", password="<PASSWORD>", sslmode="require")

with conn:
    with conn.cursor() as cursor:
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
:link: https://www.psycopg.org/docs/
:link-type: url
:link-alt: psycopg2 documentation
The full documentation for psycopg2.
::::

:::::
