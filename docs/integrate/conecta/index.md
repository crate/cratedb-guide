(conecta)=
# Conecta

:::{rubric} About
:::

[Conecta] is a library designed to load data from SQL databases into Arrow
with maximum speed and memory efficiency by leveraging zero-copy and true
concurrency in Python.

Conecta integrates natively with the arrow ecosystem by supporting several
arrow libraries: [pyarrow], [arro3] and [nanoarrow]. Additionally, the
database results can easily be converted to Polars or pandas.

:::{rubric} Features
:::

* Connection pooling
* Real multithreading
* Client-based query partitioning
* Utilities like: SQL bind parameters

:::{rubric} Install
:::

```shell
uv pip install --upgrade conecta polars pyarrow
```

:::{rubric} Usage
:::

```python
from pprint import pprint
from conecta import read_sql

table = read_sql(
    "postgres://crate:crate@localhost:5432/doc",
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

```python
[{'country': 'FR/IT',
  'height': 4808,
  'latitude': 45.8325,
  'longitude': 6.86444,
  'mountain': 'Mont Blanc',
  'region': 'Mont Blanc massif'},
 {'country': 'CH',
  'height': 4634,
  'latitude': 45.93694,
  'longitude': 7.86694,
  'mountain': 'Monte Rosa',
  'region': 'Monte Rosa Alps'},
 {'country': 'CH',
  'height': 4545,
  'latitude': 46.09389,
  'longitude': 7.85889,
  'mountain': 'Dom',
  'region': 'Mischabel'}]
```


[arro3]: https://pypi.org/project/arro3-core/
[Conecta]: https://pypi.org/project/conecta/
[nanoarrow]: https://pypi.org/project/nanoarrow/
[pyarrow]: https://pypi.org/project/pyarrow/
