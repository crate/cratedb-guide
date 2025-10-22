(micropython-cratedb)=

# micropython-cratedb

:::{div} .float-right .text-right
[![MicroPython CI](https://github.com/crate/micropython-cratedb/actions/workflows/tests.yml/badge.svg)](https://github.com/crate/micropython-cratedb/actions/workflows/tests.yml)
:::
:::{div} .clearfix
:::

A MicroPython library connecting to the CrateDB HTTP API.
See the full documentation at <https://github.com/crate/micropython-cratedb>.
The package can be installed using `mpremote mip install github:crate/micropython-cratedb`.

```python
import cratedb

crate = cratedb.CrateDB(
    host="localhost",
    port=4200,
    user="crate",
    password="crate",
    use_ssl=False
)

response = crate.execute(
    "SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3"
)

print(response)
```
