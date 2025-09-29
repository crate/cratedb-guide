(marquez)=
# Marquez

:::{include} /_include/links.md
:::

```{div} .float-right
[![Marquez logo](https://marquezproject.ai/img/marquez-social-card.jpg){height=60px loading=lazy}][Marquez]
```
```{div} .clearfix
```

:::{rubric} About
:::

:::{div}
[OpenLineage] is an open source industry standard framework for data lineage.
It standardizes the definition of data lineage, the metadata that makes up
lineage data, and the approach for collecting lineage data from external systems.
[Marquez] is OpenLineage's lineage repository reference implementation.

Among other tools, OpenLineage integrates with [Apache Airflow] to collect
DAG lineage metadata so that inter-DAG dependencies are easily maintained
and viewable via a lineage graph, while also keeping a catalog of historical
runs of DAGs.
:::


:::{rubric} Learn
:::

::::{grid} 2

:::{grid-item-card} Use Marquez with CrateDB
:link: marquez-usage
:link-type: ref
Demonstrate how to run Airflow DAGs against a
CrateDB database and view lineage data in Marquez.
:::

::::

:::{toctree}
:hidden:
Usage <usage>
:::


[Marquez]: https://marquezproject.ai/
[OpenLineage]: https://openlineage.io/
