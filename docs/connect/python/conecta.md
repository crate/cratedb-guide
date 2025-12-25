(conecta-intro)=

# Conecta

:::{div} .float-right .text-right
[![conecta-core CI](https://github.com/surister/conecta/actions/workflows/test_core.yml/badge.svg)](https://github.com/surister/conecta/actions/workflows/test_core.yml)
[![conecta-python CI](https://github.com/surister/conecta/actions/workflows/test_python.yml/badge.svg)](https://github.com/surister/conecta/actions/workflows/test_python.yml)
:::
:::{div} .clearfix
:::

{ref}`conecta` is a library designed to load data from SQL databases into
Arrow with maximum speed and memory efficiency by leveraging zero-copy and
true concurrency in Python.

:::{rubric} Install
:::

```shell
pip install --upgrade conecta
```

:::{rubric} Synopsis
:::

```python
from pprint import pprint
from conecta import read_sql

table = read_sql(
    "postgres://crate:crate@localhost:5432/",
    queries=["SELECT country, region, mountain, height, latitude(coordinates), longitude(coordinates) FROM sys.summits ORDER BY height DESC LIMIT 3"],
)

# Display in Python format.
pprint(table.to_pylist())

# Optionally convert to pandas dataframe.
print(table.to_pandas())

# Optionally convert to Polars dataframe.
import polars as pl
print(pl.from_arrow(table))
```
