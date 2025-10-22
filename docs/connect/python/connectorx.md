(connectorx)=

# ConnectorX

:::{div} .float-right .text-right
[![ConnectorX CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-connectorx.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-connectorx.yml)
:::
:::{div} .clearfix
:::

[ConnectorX] enables you to load data from databases into Python in the
fastest and most memory-efficient way.

```python
import connectorx as cx

cx.read_sql(
    "postgresql://username:password@server:port/database",
    "SELECT * FROM lineitem",
    partition_on="l_orderkey",
    partition_num=10,
)
```

- [Connect to CrateDB using ConnectorX]


[ConnectorX]: https://sfu-db.github.io/connector-x/
[Connect to CrateDB using ConnectorX]: https://github.com/crate/cratedb-examples/tree/main/by-language/python-connectorx
