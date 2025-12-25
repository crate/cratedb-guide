(connectorx)=

# ConnectorX

:::{div} .float-right .text-right
[![ConnectorX CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-connectorx.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-connectorx.yml)
:::
:::{div} .clearfix
:::

ConnectorX enables you to load data from databases into Python in the
fastest and most memory-efficient way.

:::{rubric} Install
:::

```shell
pip install --upgrade connectorx
```

:::{rubric} Synopsis
:::

```python
import connectorx as cx

cx.read_sql(
    "postgresql://username:password@server:port/database",
    "SELECT * FROM lineitem",
    partition_on="l_orderkey",
    partition_num=10,
)
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://sfu-db.github.io/connector-x/
:link-type: url
:link-alt: ConnectorX documentation
The full documentation for ConnectorX.
::::

::::{grid-item-card} {octicon}`code-square;1.75em;sd-text-info` &nbsp; Example
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/python-connectorx
:link-type: url
:link-alt: ConnectorX example
An executable example using ConnectorX.
::::

:::::
