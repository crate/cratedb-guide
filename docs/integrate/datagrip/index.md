(datagrip)=
# DataGrip

:::{include} /_include/links.md
:::

```{div}
:style: "float: right; margin-left: 0.5em"
[![](https://blog.jetbrains.com/wp-content/uploads/2019/01/datagrip_icon.svg){w=120px}](https://www.jetbrains.com/datagrip/)
```

[DataGrip] is a cross-platform database IDE that is tailored to suit the
specific needs of professional SQL developers.

It is available as a standalone application and is also included into
other JetBrains products like IntelliJ IDEA and PyCharm.

Connecting DataGrip to CrateDB uses the [CrateDB JDBC Driver].

```{div}
:style: "clear: both"
```


## Install

::::{grid} 2
:::{grid-item}
For connecting to CrateDB, install the [CrateDB JDBC Driver]
using the "Custom JARs" option when adding a database driver.
:::
:::{grid-item}
![Image](https://github.com/user-attachments/assets/a8c1ada6-fd97-43f4-a1ba-91aba1520bdb){h=180px}
![Image](https://github.com/user-attachments/assets/1f925848-fac3-4265-8bd3-96f91daf03c9){h=180px}
:::
:::{grid-item}
[crate-jdbc-standalone] is the right choice here.
For example, download and use the [crate-jdbc-standalone-latest.jar] JAR file,
and select the driver class `io.crate.client.jdbc.CrateDriver`.
:::
:::{grid-item}
![Image](https://github.com/user-attachments/assets/50ccb304-5aaf-4f0b-8ae7-55445f06930c){w=400px}
:::
::::


## Connect

::::{grid} 2

:::{grid-item}
Now, you can add a Data Source using the CrateDB database driver.
Please specify database URL and credentials of your CrateDB cluster.
:::
:::{grid-item}
![Image](https://github.com/user-attachments/assets/147a3e8e-f1d7-413d-9e0c-1ced11333646){w=480px}
:::
:::{grid-item}
For connecting to [CrateDB Self-Managed] or [CrateDB Cloud],
use a connection URL like:
```
jdbc:crate://<host>:5432/
```
:::
:::{grid-item}
![Image](https://github.com/user-attachments/assets/c929aa64-f032-451c-9f9d-45e6aebb12e5){w=480px}
:::

::::


## Usage
After refreshing, you can browse the data tree, and use the Query Console.

![Image](https://github.com/user-attachments/assets/3350a955-0a53-41d7-905b-a71cc4a767e9){h=240px}
![Image](https://github.com/user-attachments/assets/d0a2a09d-a59f-4eda-a488-09d5ce15c08d){h=240px}



## Learn

:::{rubric} Tutorials
:::
- [Blog: Use CrateDB With DataGrip]

:::{rubric} Product
:::
- [CrateDB and DataGrip]

:::{rubric} Notes
:::
:::{note}
We are tracking interoperability issues per [Tool: DataGrip], and appreciate
any contributions and reports.
:::


[Blog: Use CrateDB With DataGrip]: https://cratedb.com/blog/use-cratedb-with-datagrip-an-advanced-database-ide
[CrateDB and DataGrip]: https://cratedb.com/integrations/cratedb-and-datagrip
[DataGrip]: https://www.jetbrains.com/datagrip/
[Tool: DataGrip]: https://github.com/crate/crate/labels/tool%3A%20DataGrip
