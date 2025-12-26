(asyncpg)=

# asyncpg

asyncpg is a database interface library designed specifically for PostgreSQL
and Python/asyncio. asyncpg is an efficient, clean implementation of the
PostgreSQL server binary protocol for use with Python's asyncio framework.

:::{rubric} Install
:::

```shell
pip install --upgrade asyncpg
```

:::{rubric} Synopsis
:::

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

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://magicstack.github.io/asyncpg/current/
:link-type: url
:link-alt: asyncpg documentation
The full documentation for asyncpg.
::::

:::::
