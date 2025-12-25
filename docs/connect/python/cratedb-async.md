(cratedb-async)=

# cratedb-async

Asynchronous Python driver for CrateDB based on [HTTPX].
See the full documentation at <https://github.com/surister/cratedb-async>.

:::{rubric} Install
:::

```shell
pip install --upgrade cratedb-async
```

:::{rubric} Synopsis
:::

```python
import asyncio
from cratedb_async.client import CrateClient

async def main():
    crate = CrateClient("https://<name-of-your-cluster>.cratedb.net:4200")
    response = await crate.query("SELECT * FROM sys.summits")
    print(response.as_table())

asyncio.run(main())
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://github.com/surister/cratedb-async
:link-type: url
:link-alt: CrateDB Async httpx driver
The full documentation for the CrateDB Async httpx driver.
::::

:::::


[HTTPX]: https://www.python-httpx.org/
