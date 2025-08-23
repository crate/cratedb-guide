(performance)=
# Performance Guides

:::{div} sd-text-muted
Best practices and tips for sharding, scaling, and performance tuning.
:::

:::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`tune;2em` Allocation and Capacity
```{toctree}
:maxdepth: 1

Sharding <sharding>
scaling
storage
```
+++
About under- and over-allocation of shards vs. finding the right balance,
optimizing for ingestion performance, memory capacity planning, and
about limits and recommendations related to storage details.
::::

::::{grid-item-card} {material-outlined}`speed;2em` Performance Handbook
```{toctree}
:maxdepth: 1

inserts/index
selects
optimization
```
+++
Optimally design your SQL query statements for maximum performance and
less resource consumption.
When milliseconds matter, or otherwise a query using too many resources
would set your cluster on fire.
::::

:::::
