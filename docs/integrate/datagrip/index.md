(datagrip)=
# DataGrip

:::{include} /_include/links.md
:::

```{div} .float-right
:style: "margin-left: 0.5em"
[![DataGrip logo](https://blog.jetbrains.com/wp-content/uploads/2019/01/datagrip_icon.svg){width=120px loading=lazy}][DataGrip]
```
:::{div}
[DataGrip] is a cross-platform database IDE that is tailored to suit the
specific needs of professional SQL developers.

It is available as a standalone application and is also included in
other JetBrains products like IntelliJ IDEA and PyCharm.

Connecting DataGrip to CrateDB uses the [CrateDB JDBC Driver].
:::
```{div} .clearfix
```


## Install

::::{grid} 2
:::{grid-item}
For connecting to CrateDB, install the [CrateDB JDBC Driver]
using the "Custom JARs" option when adding a database driver.
:::
:::{grid-item}
![DataGrip: add custom JAR for JDBC driver](https://github.com/user-attachments/assets/a8c1ada6-fd97-43f4-a1ba-91aba1520bdb){height=180px loading=lazy}
![DataGrip: select JDBC JARs](https://github.com/user-attachments/assets/1f925848-fac3-4265-8bd3-96f91daf03c9){height=180px loading=lazy}
:::
:::{grid-item}
[crate-jdbc-standalone] is the right choice here.
For example, download and use the [crate-jdbc-standalone-latest.jar] JAR file,
and select the driver class `io.crate.client.jdbc.CrateDriver`.
:::
:::{grid-item}
![DataGrip: set driver class io.crate.client.jdbc.CrateDriver](https://github.com/user-attachments/assets/50ccb304-5aaf-4f0b-8ae7-55445f06930c){width=400px loading=lazy}
:::
::::


## Connect

::::{grid} 2

:::{grid-item}
Now, you can add a Data Source using the CrateDB database driver.
Please specify database URL and credentials of your CrateDB cluster.
:::
:::{grid-item}
![DataGrip: add CrateDB data source](https://github.com/user-attachments/assets/147a3e8e-f1d7-413d-9e0c-1ced11333646){width=480px loading=lazy}
:::
:::{grid-item}
For connecting to [CrateDB Self-Managed] or [CrateDB Cloud],
use a connection URL like:
```
jdbc:crate://<host>:5432/
```
:::
:::{grid-item}
![DataGrip: database URL](https://github.com/user-attachments/assets/c929aa64-f032-451c-9f9d-45e6aebb12e5){width=480px loading=lazy}
:::

::::


## Usage
After refreshing, you can browse the data tree, and use the Query Console.

![DataGrip: data tree view](https://github.com/user-attachments/assets/3350a955-0a53-41d7-905b-a71cc4a767e9){height=240px loading=lazy}
![DataGrip: query console running SQL](https://github.com/user-attachments/assets/d0a2a09d-a59f-4eda-a488-09d5ce15c08d){height=240px loading=lazy}



## Learn

:::{rubric} Tutorials
:::

::::{grid}

:::{grid-item-card} Blog: Use CrateDB With DataGrip
:link: https://cratedb.com/blog/use-cratedb-with-datagrip-an-advanced-database-ide
:link-type: url
DataGrip is a cross-platform database IDE (Integrated Development Environment) that is
tailored to suit the specific needs of professional SQL developers.
With the help of the CrateDB JDBC Standalone Driver, you can use DataGrip with CrateDB.
:::

::::

:::{rubric} Notes
:::
:::{note}
We are tracking interoperability issues per [Tool: DataGrip], and appreciate
any contributions and reports.
:::

:::{seealso}
[CrateDB and DataGrip]
:::


[CrateDB and DataGrip]: https://cratedb.com/integrations/cratedb-and-datagrip
[DataGrip]: https://www.jetbrains.com/datagrip/
[Tool: DataGrip]: https://github.com/crate/crate/labels/tool%3A%20DataGrip
