(visualeaf)=
# VisuaLeaf

:::{include} /_include/links.md
:::

```{div} .float-right
:style: "margin-left: 0.5em"
[![VisuaLeaf logo](/_assets/icon/visualeaf-logo.svg){w=80px loading=lazy}](https://visualeaf.com/database/cratedb/)
```

[VisuaLeaf](https://visualeaf.com/database/cratedb/) is a cross-platform desktop
database client for Windows, macOS, and Linux, with a SQL editor, a visual query
builder, entity-relationship diagrams, and charts built from query results.

It is available as a free _Community Edition_ and as paid editions.


## Connect

::::{grid} 2

:::{grid-item}
:columns: 6
VisuaLeaf has a dedicated CrateDB connection type, which uses the standard
[PostgreSQL JDBC Driver] and pre-fills the default port `5432`,
database `doc`, and user `crate`.

1. [Download VisuaLeaf](https://visualeaf.com/download) and click **New Connection**.
2. Search for `CrateDB` and select it.
3. Enter the host, port, and credentials of your CrateDB cluster.
   When connecting to [CrateDB Self-Managed] on localhost, for evaluation
   purposes, use host `localhost`, port `5432`, and user `crate`.
   When connecting to [CrateDB Cloud], use `<clustername>.cratedb.net` as the
   host, along with the credentials of your cluster.
4. Click **Test Connection**, then **Save & Connect**.
:::
:::{grid-item}
:columns: 6
![VisuaLeaf connection settings screenshot](/_assets/img/integrations/visualeaf/visualeaf-connection-form.png){w=480px loading=lazy}
:::

::::


## Usage

Expand the connection in the **Connections** sidebar to navigate to the `doc`
schema and its tables and views.

![VisuaLeaf object tree screenshot](/_assets/img/integrations/visualeaf/visualeaf-object-tree.png){h=240px loading=lazy}

Right-click the database and choose **New SQL Editor** to write and run queries.

![VisuaLeaf query results screenshot](/_assets/img/integrations/visualeaf/visualeaf-query-results.png){w=720px loading=lazy}
