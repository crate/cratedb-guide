(udf)=
# User-Defined Functions

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
CrateDB supports user-defined functions (UDFs) that can be written in JavaScript.
::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Reference Manual
:::
- {ref}`crate-reference:user-defined-functions`
:::{rubric} SQL Functions
:::
- {ref}`crate-reference:ref-create-function`
- {ref}`crate-reference:ref-drop-function`

{tags-primary}`SQL`
{tags-primary}`UDF`
::::

:::::


## Synopsis
Define function.
```sql
CREATE FUNCTION my_subtract_function(integer, integer)
RETURNS integer
LANGUAGE JAVASCRIPT
AS 'function my_subtract_function(a, b) { return a - b; }';
```
Use function.
```sql
SELECT doc.my_subtract_function(3, 1) AS col;
```
```
+-----+
| col |
+-----+
|   2 |
+-----+
SELECT 1 row in set (... sec)
```


:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
It includes not even the most basic essentials, and needs expansion. For example,
the "About", "Details", "Usage" and "Learn" sections are missing completely.
:::



:::{seealso}
**Product:**
[Relational Database]
:::
