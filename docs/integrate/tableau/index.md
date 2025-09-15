(tableau)=
# Tableau

```{div} .float-right
[![Tableau logo](https://upload.wikimedia.org/wikipedia/en/thumb/0/06/Tableau_logo.svg/500px-Tableau_logo.svg.png?20200509180027){height=60px loading=lazy}][Tableau]
```
```{div} .clearfix
```


:::{rubric} About
:::

[Tableau] is a visual business intelligence and analytics software platform. It expresses
data by translating drag-and-drop actions into data queries through an intuitive interface.

![Tableau dashboard example](https://cratedb.com/hs-fs/hubfs/08-index.png?width=1536&name=08-index.png){h=200px}


:::{rubric} Learn
:::

::::{grid} 2
:gutter: 2

:::{grid-item-card} Blog: Connecting to CrateDB from Tableau with JDBC
:link: https://cratedb.com/blog/connecting-to-cratedb-from-tableau-with-jdbc
:link-type: url
In this tutorial, you will:
- In CrateDB, create a table and provision the Iris dataset.
- Set up the PostgreSQL JDBC driver for Tableau.
- Connect to CrateDB from Tableau using PostgreSQL JDBC.
- Make a simple visualization from your CrateDB table in Tableau.
:::

:::{grid-item-card} Article: Using CrateDB with Tableau
:link: tableau-tutorial
:link-type: ref
How to install the latest PostgreSQL JDBC driver (e.g.
`postgresql-42.7.1.jar` or newer) for using Tableau.
:::

:::{grid-item-card} Repository: CrateDB Tableau Connector
:link: https://github.com/crate/cratedb-tableau-connector
:link-type: url
:columns: 12
The native Tableau connector for CrateDB unlocks advanced SQL functionality
and resolves compatibility issues beyond standard usage.
:::

::::

:::{rubric} Notes
:::
:::{note}
We are tracking interoperability issues per [Tool: Tableau] and
[Connector: Issues], and appreciate any contributions or reports.
:::


```{seealso}
[CrateDB and Tableau]
```

:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
:::


[Connector: Issues]: https://github.com/crate/cratedb-tableau-connector/issues
[CrateDB and Tableau]: https://cratedb.com/integrations/cratedb-and-tableau
[Tableau]: https://www.tableau.com/
[Tool: Tableau]: https://github.com/crate/crate/labels/tool%3A%20Tableau
