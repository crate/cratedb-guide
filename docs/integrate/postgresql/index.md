(postgresql)=
# PostgreSQL

```{div} .float-right
[![postgresql-logo](https://www.postgresql.org/media/img/about/press/elephant.png){height=60px loading=lazy}][PostgreSQL]
```
```{div} .clearfix
```

:::{rubric} About
:::

[PostgreSQL] is the world's most advanced open source relational database.

:::{rubric} Synopsis
:::

```shell
uvx 'cratedb-toolkit[io-ingestr]' load table \
  "postgresql://postgres:postgres@localhost:5432/test?table=public.demo" \
  --cluster-url="crate://crate:crate@localhost:4200/doc/postgresql_demo"
```

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Load data from PostgreSQL
:link: postgresql-usage
:link-type: ref
Load data from PostgreSQL into CrateDB using CrateDB Toolkit.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Usage <usage>
:::


[PostgreSQL]: https://www.postgresql.org/
