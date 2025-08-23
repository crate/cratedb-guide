(performance)=
(performance-guides)=
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
Scaling <scaling>
Storage <storage>
```
+++
Guidance on balancing shard allocation, optimizing ingestion performance,
planning memory capacity, and limits/recommendations related to storage.
::::

::::{grid-item-card} {material-outlined}`speed;2em` Performance Handbook
```{toctree}
:maxdepth: 1

inserts/index
selects
optimization
```
+++
Design SQL statements for maximum performance and lower resource usage.
Applicable when latency matters, or when a resource‑heavy query could
overload your cluster.
::::

:::::
