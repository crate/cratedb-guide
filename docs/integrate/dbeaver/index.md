(dbeaver)=
# DBeaver

:::{include} /_include/links.md
:::

```{div}
:style: "float: right; margin-left: 0.5em"
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/DBeaver_logo.svg/512px-DBeaver_logo.svg.png){w=120px}][DBeaver]
```

[DBeaver] is a multipurpose cross-platform database tool for developers,
database administrators, analysts, and everyone working with data.

It is available as an open-source version _DBeaver Community_ and
as a commercial version _DBeaver PRO_.


## Connect

::::{grid} 2

:::{grid-item}
:columns: 7
Please specify database URL and credentials of your CrateDB cluster.
For connecting to CrateDB, the standard [PostgreSQL JDBC Driver]
will be used.

When connecting to [CrateDB Self-Managed] on localhost,
for evaluation purposes, use:
```
jdbc:postgresql://localhost:5432/crate
```

When connecting to [CrateDB Cloud], use:
```
jdbc:postgresql://<clustername>.cratedb.net:5432/crate
```
:::
:::{grid-item}
:columns: 5
![Image](https://github.com/user-attachments/assets/630fcc7c-21c5-4070-be72-e38041c19d8e){w=480px}
:::

::::


## Usage
Use the tree menu on the left-hand pane to navigate to the `doc` schema and
its tables. Navigate to the Data tab to browse your table data.

![Image](https://cratedb.com/hs-fs/hubfs/Screen-Shot-2019-04-05-at-17.15.05.png?width=1600&name=Screen-Shot-2019-04-05-at-17.15.05.png){h=240px}
![Image](https://cratedb.com/hs-fs/hubfs/Screen-Shot-2019-04-05-at-17.15.13.png?width=1600&name=Screen-Shot-2019-04-05-at-17.15.13.png){h=240px}


## Learn

:::{rubric} Tutorials
:::

::::{grid}

:::{grid-item-card} Blog: Use CrateDB With DBeaver
:link: https://cratedb.com/blog/cratedb-dbeaver
:link-type: url
DBeaver is a multipurpose database tool for developers and database administrators.
With the help of the CrateDB JDBC Standalone Driver, you can use DBeaver with CrateDB.
:::

::::

:::{rubric} Notes
:::
:::{note}
A few data types of CrateDB need special considerations.
- `ARRAY` types are recognised as such in reads, also work for inserts through the GUI.
  They need to use curly brackets syntax `{1,2}` instead of `[1,2]`.
- `OBJECT` types are seen as string, and are ok to insert via GUI.
- `GEO_POINT` types are seen as `STRING`, for insert through GUI, please use parentheses.
- `GEO_SHAPE` types are seen as `STRING`, are ok to insert via GUI.
- `FLOAT_VECTOR` types are seen as `ARRAY` on read, and can be inserted
  using the GUI with same considerations as `ARRAY`s.
:::
:::{note}
We are tracking interoperability issues per [Tool: DBeaver], and appreciate
any contributions and reports.
:::

:::{seealso}
[CrateDB and DBeaver]
:::


[CrateDB and DBeaver]: https://cratedb.com/integrations/cratedb-and-dbeaver
[DBeaver]: https://dbeaver.io/
[Tool: DBeaver]: https://github.com/crate/crate/labels/tool%3A%20DBeaver
