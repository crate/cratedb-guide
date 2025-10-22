(turbodbc)=

# turbodbc

:::{div} .float-right .text-right
[![turbodbc CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-turbodbc.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-turbodbc.yml)
:::
:::{div} .clearfix
:::

[Turbodbc] is a Python module to access relational databases via the Open
Database Connectivity (ODBC) interface. Its primary target audience are
data scientists that use databases for which no efficient native Python
drivers are available.

For maximum performance, turbodbc offers built-in NumPy and Apache Arrow
support and internally relies on batched data transfer instead of
single-record communication as other popular ODBC modules do.

- [Using CrateDB with turbodbc]


[turbodbc]: https://turbodbc.readthedocs.io/
[Using CrateDB with turbodbc]: https://github.com/crate/cratedb-examples/tree/main/by-language/python-turbodbc
