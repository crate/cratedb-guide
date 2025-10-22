(asyncpg)=

# asyncpg

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


[asyncpg documentation]: https://magicstack.github.io/asyncpg/current/
