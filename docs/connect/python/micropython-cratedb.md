(micropython-cratedb)=

# micropython-cratedb

:::{div} .float-right .text-right
[![MicroPython CI](https://github.com/crate/micropython-cratedb/actions/workflows/tests.yml/badge.svg)](https://github.com/crate/micropython-cratedb/actions/workflows/tests.yml)
:::
:::{div} .clearfix
:::

A MicroPython library connecting to the CrateDB HTTP API.

:::{rubric} Install
:::

```shell
mpremote mip install github:crate/micropython-cratedb
```

:::{rubric} Synopsis
:::

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


:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://github.com/crate/micropython-cratedb
:link-type: url
:link-alt: CrateDB MicroPython driver
The full documentation for the CrateDB Driver for MicroPython.
::::

:::::
