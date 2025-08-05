(sql-server)=
# SQL Server

:::{rubric} About
:::

```{div}
:style: "float: right; margin-left: 1em"
[![](https://github.com/crate/crate-clients-tools/assets/453543/a93a0fdb-1a1e-451e-abcb-8f705e2b03f4){w=180px}](https://www.microsoft.com/)

[![](https://github.com/crate/crate-clients-tools/assets/453543/6317965a-0b69-4d8e-bc77-e12dfc8ed338){w=180px}](https://learn.microsoft.com/en-us/sql/)
```

Microsoft [SQL Server Integration Services] (SSIS) is a component of the Microsoft
SQL Server database software that can be used to perform a broad range of data
migration tasks. 

[SSIS] is a platform for data integration and workflow applications. It features a
data warehousing tool used for data extraction, transformation, and loading (ETL).
The tool may also be used to automate maintenance of SQL Server databases and
updates to multidimensional cube data. 

Integration Services can extract and transform data from a wide variety of sources
such as XML data files, flat files, and relational data sources, and then load the
data into one or more destinations.

Integration Services includes a rich set of built-in [tasks][ssis-tasks] and
[transformations][ssis-transformations], graphical tools for building packages, and
an SSIS Catalog database to store, run, and manage packages.

```{div}
:style: "clear: both"
```


:::{rubric} Learn
:::

A demo project which uses SSIS and ODBC to read and write data from CrateDB:

- [Using SQL Server Integration Services with CrateDB]


[SQL Server Integration Services]: https://learn.microsoft.com/en-us/sql/integration-services/sql-server-integration-services
[SSIS]: https://en.wikipedia.org/wiki/SQL_Server_Integration_Services
[ssis-tasks]: https://learn.microsoft.com/en-us/sql/integration-services/control-flow/integration-services-tasks
[ssis-transformations]: https://learn.microsoft.com/en-us/sql/integration-services/data-flow/transformations/integration-services-transformations
[Using SQL Server Integration Services with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/application/microsoft-ssis
