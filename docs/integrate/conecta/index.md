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
uv pip install --upgrade conecta pandas polars pyarrow
```

:::{rubric} Usage
:::

```python
from pprint import pprint
from conecta import read_sql

table = read_sql(
    "postgres://crate:crate@localhost:5432/doc",
    query="SELECT country, region, mountain, height, coordinates FROM sys.summits ORDER BY height DESC LIMIT 3",
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
[{'coordinates': [6.86444, 45.8325],
  'country': 'FR/IT',
  'height': 4808,
  'mountain': 'Mont Blanc',
  'region': 'Mont Blanc massif'},
 {'coordinates': [7.86694, 45.93694],
  'country': 'CH',
  'height': 4634,
  'mountain': 'Monte Rosa',
  'region': 'Monte Rosa Alps'},
 {'coordinates': [7.85889, 46.09389],
  'country': 'CH',
  'height': 4545,
  'mountain': 'Dom',
  'region': 'Mischabel'}]
```
```text
  country             region    mountain  height          coordinates
0   FR/IT  Mont Blanc massif  Mont Blanc    4808   [6.86444, 45.8325]
1      CH    Monte Rosa Alps  Monte Rosa    4634  [7.86694, 45.93694]
2      CH          Mischabel         Dom    4545  [7.85889, 46.09389]
shape: (3, 5)
```
```text
┌─────────┬───────────────────┬────────────┬────────┬─────────────────────┐
│ country ┆ region            ┆ mountain   ┆ height ┆ coordinates         │
│ ---     ┆ ---               ┆ ---        ┆ ---    ┆ ---                 │
│ str     ┆ str               ┆ str        ┆ i32    ┆ list[f64]           │
╞═════════╪═══════════════════╪════════════╪════════╪═════════════════════╡
│ FR/IT   ┆ Mont Blanc massif ┆ Mont Blanc ┆ 4808   ┆ [6.86444, 45.8325]  │
│ CH      ┆ Monte Rosa Alps   ┆ Monte Rosa ┆ 4634   ┆ [7.86694, 45.93694] │
│ CH      ┆ Mischabel         ┆ Dom        ┆ 4545   ┆ [7.85889, 46.09389] │
└─────────┴───────────────────┴────────────┴────────┴─────────────────────┘
```


[arro3]: https://pypi.org/project/arro3-core/
[Conecta]: https://pypi.org/project/conecta/
[nanoarrow]: https://pypi.org/project/nanoarrow/
[pyarrow]: https://pypi.org/project/pyarrow/
