(turbodbc)=

# turbodbc

:::{div} .float-right .text-right
[![turbodbc CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-turbodbc.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-turbodbc.yml)
:::
:::{div} .clearfix
:::

Turbodbc is a Python module to access relational databases via the Open
Database Connectivity (ODBC) interface. Its primary target audience are
data scientists that use databases for which no efficient native Python
drivers are available.

For maximum performance, turbodbc offers built-in NumPy and Apache Arrow
support and internally relies on batched data transfer instead of
single-record communication as other popular ODBC modules do.

:::{rubric} Install
:::

```shell
pip install --upgrade turbodbc
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: https://turbodbc.readthedocs.io/
:link-type: url
:link-alt: Turbodbc documentation
The full documentation for Turbodbc.
::::

::::{grid-item-card} {octicon}`code-square;1.75em;sd-text-info` &nbsp; Example
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/python-turbodbc
:link-type: url
:link-alt: Turbodbc example
An executable example using Turbodbc.
::::

:::::
