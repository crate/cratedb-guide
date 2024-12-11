(dbeaver)=
# DBeaver

```{div}
:style: "float: right; margin-left: 0.5em"
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/DBeaver_logo.svg/512px-DBeaver_logo.svg.png){w=120px}](https://dbeaver.io/)
```

[DBeaver] is a multipurpose cross-platform database tool for developers,
database administrators, analysts, and everyone working with data.

It is available as an open-source version _DBeaver Community_ and
as a commercial version _DBeaver PRO_.


## Install

::::{grid} 2
:::{grid-item}
For connecting to CrateDB, the [CrateDB JDBC Driver] will be used.
:::
:::{grid-item}
![Image](https://github.com/user-attachments/assets/ebd11a53-4d4a-4a9b-bed2-25909e618929){w=480px}
:::
::::


## Connect

::::{grid} 2

:::{grid-item}
Please specify database URL and credentials of your CrateDB cluster.

When connecting to [CrateDB Self-Managed] on localhost,
for evaluation purposes, use:
```
jdbc:crate://localhost:5432/
```

When connecting to [CrateDB Cloud], use:
```
jdbc:crate://<clustername>.cratedb.net:5432/
```
:::
:::{grid-item}
![Image](https://github.com/user-attachments/assets/3288ab3f-a70a-42db-8b99-051ea3051c84){w=480px}
:::
:::{grid-item}
When selecting CrateDB, drivers will be downloaded automatically
on the first use.

Alternatively, download and use the [crate-jdbc-standalone-2.7.0.jar] JAR file,
and select the driver class `io.crate.client.jdbc.CrateDriver`.
:::
:::{grid-item}
![Image](https://github.com/user-attachments/assets/5436f893-06d8-433f-94b3-72dddb5a13e1){w=480px}
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
- [Blog: Use CrateDB With DBeaver]

:::{rubric} Product
:::
- [CrateDB and DBeaver]

:::{rubric} Notes
:::
:::{note}
We are tracking interoperability issues per [Tool: DBeaver], and appreciate
any contributions and reports.
:::


[Blog: Use CrateDB With DBeaver]: https://cratedb.com/blog/cratedb-dbeaver
[CrateDB and DBeaver]: https://cratedb.com/integrations/cratedb-and-dbeaver
[CrateDB Cloud]: https://cratedb.com/product/cloud
[CrateDB JDBC Driver]: https://cratedb.com/docs/jdbc/
[CrateDB Self-Managed]: https://cratedb.com/product/self-managed
[crate-jdbc-standalone]: https://repo1.maven.org/maven2/io/crate/crate-jdbc-standalone/
[crate-jdbc-standalone-2.7.0.jar]: https://repo1.maven.org/maven2/io/crate/crate-jdbc-standalone/2.7.0/crate-jdbc-standalone-2.7.0.jar
[DBeaver]: https://dbeaver.io/
[Tool: DBeaver]: https://github.com/crate/crate/labels/tool%3A%20DBeaver
