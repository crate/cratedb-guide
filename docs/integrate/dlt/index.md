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

[dlt] (data load tool)—think ELT as Python code—is a popular,
production-ready Python library for moving data. It loads data from
various and often messy data sources into well-structured, live datasets.

dlt supports [30+ databases supported by SQLAlchemy],
and is also the workhorse behind the {ref}`ingestr` toolkit.

::::{grid}

:::{grid-item}
- **Just code**: no need to use any backends or containers.

- **Platform agnostic**: Does not replace your data platform, deployments, or security
  models. Simply import dlt in your favorite code editor, or add it to your Jupyter
  Notebook.

- **Versatile**: You can load data from any source that produces Python data structures,
  including APIs, files, databases, and more.
:::

::::


## Synopsis

Prerequisites:
Install dlt and the CrateDB destination adapter:
```shell
pip install --upgrade dlt-cratedb
```

Load data from cloud storage or files into CrateDB.
```python
import dlt
import dlt_cratedb
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
import dlt_cratedb
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

## Supported features

### Data loading

Data is loaded into CrateDB using the most efficient method depending on the data source.

- For local files, the `psycopg2` library is used to directly load files into
  CrateDB tables using the `INSERT` command.
- For files in remote storage like S3 or Azure Blob Storage,
  CrateDB data loading functions are used to read the files and insert the data into tables.

### Datasets

Use `dataset_name="doc"` to address CrateDB's default schema `doc`.
When addressing other schemas, make sure they contain at least one table. [^create-schema]

### File formats

- The [SQL INSERT file format] is the preferred format for both direct loading and staging.

### Column types

The `cratedb` destination has a few specific deviations from the default SQL destinations.

- CrateDB does not support the `time` datatype. Time will be loaded to a `text` column.
- CrateDB does not support the `binary` datatype. Binary will be loaded to a `text` column.
- CrateDB can produce rounding errors under certain conditions when using the `float/double` datatype.
  Make sure to use the `decimal` datatype if you can’t afford to have rounding errors.

### Column hints

CrateDB supports the following [column hints].

- `primary_key` - marks the column as part of the primary key. Multiple columns can have this hint to create a composite primary key.

### File staging

CrateDB supports Amazon S3, Google Cloud Storage, and Azure Blob Storage as file staging destinations.

`dlt` will upload CSV or JSONL files to the staging location and use CrateDB data loading functions
to load the data directly from the staged files.

Please refer to the filesystem documentation to learn how to configure credentials for the staging destinations.

- [AWS S3]
- [Azure Blob Storage]
- [Google Storage]

Invoke a pipeline with staging enabled.

```python
pipeline = dlt.pipeline(
  pipeline_name='chess_pipeline',
  destination='cratedb',
  staging='filesystem',  # add this to activate staging
  dataset_name='chess_data'
)
```

### dbt support

Integration with [dbt] is generally supported via [dbt-cratedb2] but not tested by us.

### dlt state sync

The CrateDB destination fully supports [dlt state sync].


## See also

:::{rubric} Examples
:::

::::{grid}

:::{grid-item-card} Usage guide: Load API data with dlt
:link: dlt-usage
:link-type: ref
Exercise a canonical `dlt init` example with CrateDB.
:::

:::{grid-item-card} Examples: Use dlt with CrateDB
:link: https://github.com/crate/cratedb-examples/tree/main/framework/dlt
:link-type: url
Executable code examples on GitHub that demonstrate how to use dlt with CrateDB.
:::

::::

:::{rubric} Resources
:::

::::{grid}

:::{grid-item-card} Package: `dlt-cratedb`
:link: https://pypi.org/project/dlt-cratedb/
:link-type: url
The dlt destination adapter for CrateDB is
based on the dlt PostgreSQL adapter.
:::

:::{grid-item-card} Related: `ingestr`
:link: ingestr
:link-type: ref
The ingestr data import/export application uses dlt as a workhorse.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Usage <usage>
:::


[^create-schema]: CrateDB does not support `CREATE SCHEMA` yet, see [CRATEDB-14601].
  This means by default, unless any table exists within a schema, the schema appears
  not to exist at all. However, it also can't be created explicitly. Schemas are
  currently implicitly created when tables exist in them.

[30+ databases supported by SQLAlchemy]: https://dlthub.com/docs/dlt-ecosystem/destinations/sqlalchemy
[AWS S3]: https://dlthub.com/docs/dlt-ecosystem/destinations/filesystem#aws-s3
[Azure Blob Storage]: https://dlthub.com/docs/dlt-ecosystem/destinations/filesystem#azure-blob-storage
[column hints]: https://dlthub.com/docs/general-usage/schema#column-hint-rules
[CRATEDB-14601]: https://github.com/crate/crate/issues/14601
[dbt]: https://dlthub.com/docs/hub/features/transformations/dbt-transformations
[dbt-cratedb2]: https://pypi.org/project/dbt-cratedb2/
[dlt]: https://dlthub.com/
[dlt state sync]: https://dlthub.com/docs/general-usage/state#syncing-state-with-destination
[Google Storage]: https://dlthub.com/docs/dlt-ecosystem/destinations/filesystem#google-storage
[SQL INSERT file format]: https://dlthub.com/docs/dlt-ecosystem/file-formats/insert-format
