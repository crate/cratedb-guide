(cratedb-async)=

# cratedb-async

Asynchronous Python driver for CrateDB based on [HTTPX].
See the full documentation at <https://github.com/surister/cratedb-async>.
The package can be installed using `pip install cratedb-async`.

```python
import asyncio
from cratedb_async.client import CrateClient

async def main():
    crate = CrateClient("https://<name-of-your-cluster>.cratedb.net:4200")
    response = await crate.query("SELECT * FROM sys.summits")
    print(response.as_table())

asyncio.run(main())
```


[HTTPX]: https://www.python-httpx.org/
