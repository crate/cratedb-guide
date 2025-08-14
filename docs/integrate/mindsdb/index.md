(mindsdb)=
# MindsDB

```{div} .float-right
[![MindsDB logo](https://github.com/crate/crate-clients-tools/assets/32901682/feca1369-811e-4dd8-b4a8-d70e734de87e){h=60px}][MindsDB]
```
```{div} .clearfix
```

:::{rubric} About
:::

[MindsDB] is the platform for customizing AI from enterprise data. With MindsDB
and its nearly 200 integrations to [data sources] and [AI/ML frameworks], 
any developer can use their enterprise data to customize AI for their purpose, 
faster and more securely.

:::{rubric} Synopsis
:::
Connect to CrateDB from MindsDB.
```postgresql
CREATE DATABASE
    cratedb_datasource
WITH
    engine = 'crate',
    parameters = {
        "user": "crate",
        "password": "",
        "host": "127.0.0.1",
        "port": 4200,
        "schema_name": "doc"
    };
```
Use the established connection to query a database table.
```sql
SELECT * FROM cratedb_datasource.demo LIMIT 10;
```

:::{rubric} Learn
:::

MindsDB integrates with CrateDB, making data from CrateDB accessible to
a diverse range of AI/ML models.

::::{grid}

:::{grid-item-card} Tutorial: MindsDB Quickstart
:link: https://docs.mindsdb.com/quickstart-tutorial
:link-type: url
How to get started with MindsDB.
:::

:::{grid-item-card} Tutorial: Use CrateDB with MindsDB
:link: https://docs.mindsdb.com/integrations/data-integrations/cratedb
:link-type: url
Learn more about MindsDB's integration with CrateDB and see examples.
:::

::::


[AI/ML frameworks]: https://docs.mindsdb.com/integrations/ai-overview 
[data sources]: https://docs.mindsdb.com/integrations/data-overview 
[MindsDB]: https://github.com/mindsdb/mindsdb
