(aiopg)=

# aiopg

aiopg is a python library for accessing a PostgreSQL database from the asyncio
(PEP-3156/tulip) framework. It wraps asynchronous features of the Psycopg
database driver.

:::{rubric} Install
:::

```shell
pip install --upgrade aiopg
```

:::{rubric} Synopsis
:::

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

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://aiopg.readthedocs.io/
:link-type: url
:link-alt: aiopg documentation
The full documentation for aiopg.
::::

:::::
