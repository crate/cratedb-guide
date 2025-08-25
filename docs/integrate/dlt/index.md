(dlt)=
# dlt

```{div} .float-right .text-right
![dlt logo](https://cdn.sanity.io/images/nsq559ov/production/7f85e56e715b847c5519848b7198db73f793448d-82x25.svg?w=2000&auto=format){loading=lazy}[dlt]
<br><br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-dlt.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-dlt.yml?branch=main&label=dlt" loading="lazy" alt="CI status: dlt"></a>
```
```{div} .clearfix
```

[dlt] (data load tool)--think ELT as Python code--is the most popular
production-ready Python library for moving data. It loads data from
various and often messy data sources into well-structured, live datasets.
dlt is used by {ref}`ingestr`.

::::{grid}

:::{grid-item}
- **Just code**: no need to use any backends or containers.

- **Platform agnostic**: Does not replace your data platform, deployments, or security
  models. Simply import dlt in your favorite AI code editor, or add it to your Jupyter
  Notebook.

- **Versatile**: You can load data from any source that produces Python data structures,
  including APIs, files, databases, and more.
:::

::::


## Synopsis

Load data from cloud storage or files into CrateDB.
```python
import dlt
from dlt.sources.filesystem import filesystem

resource = filesystem(
    bucket_url="s3://example-bucket",
    file_glob="*.csv"
)

pipeline = dlt.pipeline(
    pipeline_name="filesystem_example",
    destination=dlt.destinations.cratedb("postgresql://crate:crate@localhost:5432/"),
    dataset_name="doc",
)

pipeline.run(resource)
```

Load data from SQL databases into CrateDB.
```python
from dlt.sources.sql_database import sql_database

source = sql_database(
    "mysql+pymysql://rfamro@mysql-rfam-public.ebi.ac.uk:4497/Rfam"
)

pipeline = dlt.pipeline(
    pipeline_name="sql_database_example",
    destination=dlt.destinations.cratedb("postgresql://crate:crate@localhost:5432/"),
    dataset_name="doc",
)

pipeline.run(source)
```

## Learn

::::{grid}

:::{grid-item-card} Examples: Use dlt with CrateDB
:link: https://github.com/crate/cratedb-examples/tree/main/framework/dlt
:link-type: url
Executable code examples that demonstrate how to use dlt with CrateDB.
:::

:::{grid-item-card} Adapter: The dlt destination adapter for CrateDB
:link: https://github.com/crate/dlt-cratedb
:link-type: url
Based on the dlt PostgreSQL adapter, the package enables you to work
with dlt and CrateDB.
:::

:::{grid-item-card} See also: ingestr
:link: ingestr
:link-type: ref
The ingestr data import/export application uses dlt.
:::

::::



[databases supported by SQLAlchemy]: https://docs.sqlalchemy.org/en/20/dialects/
[dlt]: https://dlthub.com/
