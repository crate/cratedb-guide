(powerbi)=
# Microsoft Power BI

```{div}
:style: "float: right"
[![PowerBI logo](https://upload.wikimedia.org/wikipedia/en/thumb/2/20/Power_BI_logo.svg/192px-Power_BI_logo.svg.png?20200923233425){h=60px}][Power BI Desktop]
```
```{div}
:style: "clear: both"
```

:::{rubric} About
:::

[Power BI Desktop] is a powerful business intelligence tool that provides a set of
data analytics and visualizations. Using Power BI Desktop, users can create reports
and dashboards from large datasets.

:::{dropdown} **Details**
For connecting to CrateDB with Power BI, you can use the [Power Query PostgreSQL connector].
Earlier versions used the [PostgreSQL ODBC driver]. [](project:#powerbi-desktop) walks
you through the process of configuring that correctly.

[Power BI Service] is an online data analysis and visualization tool, making it
possible to publish your dashboards, in order to share them with others.
[](project:#powerbi-service) has a corresponding tutorial.

![](https://cratedb.com/docs/crate/howtos/en/latest/_images/powerbi-table-navigator.png){h=160px}
![](https://cratedb.com/docs/crate/howtos/en/latest/_images/powerbi-pie-chart.png){h=160px}
![](https://cratedb.com/docs/crate/howtos/en/latest/_images/powerbi-publish-success.png){h=160px}
:::

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Tutorial: Basic reports
:link: powerbi-desktop
:link-type: ref
Reports with Power BI Desktop.
:::

:::{grid-item-card} Tutorial: Real Time Reports
:link: powerbi-service
:link-type: ref
Real Time Reports using the Power BI service and the on-premises data gateway.
:::

::::

```{toctree}
:maxdepth: 1
:hidden:
Power BI Desktop <desktop>
Power BI Service <service>
```


```{seealso}
[CrateDB and Power BI]
```

[CrateDB and Power BI]: https://cratedb.com/integrations/cratedb-and-power-bi
[PostgreSQL ODBC driver]: https://odbc.postgresql.org/
[Power BI Desktop]: https://powerbi.microsoft.com/en-us/desktop/
[Power BI Service]: https://powerbi.microsoft.com/en-us/
[Power Query PostgreSQL connector]: https://learn.microsoft.com/en-us/power-query/connectors/postgresql
