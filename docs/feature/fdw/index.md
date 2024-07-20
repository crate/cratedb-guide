(fdw)=
# Foreign Data Wrapper

:::{include} /_include/links.md
:::
:::{include} /_include/styles.html
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

:::{rubric} Overview
:::
In the spirit of the PostgreSQL FDW implementation, CrateDB offers the
possibility to access database tables on remote database servers as if
they would be stored within CrateDB.

:::{rubric} About
:::
Foreign Data Wrappers allow you to make data in
foreign systems available as tables within CrateDB. You can then query
these foreign tables like regular user tables.

::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Reference Manual
:::
- {ref}`crate-reference:administration-fdw`
:::{rubric} SQL Functions
:::
- {ref}`crate-reference:ref-create-server`
- {ref}`crate-reference:ref-drop-server`
- {ref}`crate-reference:ref-create-foreign-table`
- {ref}`crate-reference:ref-drop-foreign-table`
:::{rubric} System Tables
:::
- {ref}`crate-reference:foreign_servers`
- {ref}`crate-reference:foreign_server_options`
- {ref}`crate-reference:foreign_tables`
- {ref}`crate-reference:foreign_table_options`
- {ref}`crate-reference:user_mappings`
- {ref}`crate-reference:user_mapping_options`

{tags-primary}`SQL`
{tags-primary}`FDW`
::::

:::::


## Synopsis
Connect to a remote PostgreSQL server.
```sql
CREATE SERVER my_postgresql
FOREIGN DATA WRAPPER jdbc
OPTIONS (url 'jdbc:postgresql://example.com:5432/')
```
Mount a database table.
```sql
CREATE FOREIGN TABLE doc.remote_documents (name text)
SERVER my_postgresql
OPTIONS (schema_name 'public', table_name 'documents');
```


:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
It includes not even the most basic essentials, and needs expansion. For example,
the "Details", "Usage" and "Learn" sections are missing completely.
:::



:::{seealso}
**Product:**
[Relational Database]
:::
