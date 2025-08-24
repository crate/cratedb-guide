(admin)=
(administration)=
# Administration

:::{div} sd-text-muted
Best practices for administering CrateDB database clusters.
:::

:::::{grid} 1 2 3 3
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`lightbulb;2em` General
```{toctree}
:maxdepth: 1

bootstrap-checks
create-user
going-into-production
memory
circuit-breaker
troubleshooting/index
```
+++
Production and troubleshooting guidelines and system resource considerations.
::::

::::{grid-item-card} {material-outlined}`speed;2em` Cluster
```{toctree}
:maxdepth: 1

clustering/index
sharding-partitioning
../performance/index
```
+++
Best practices and tips for clustering, sharding, partitioning, and performance tuning.
::::

::::{grid-item-card} {material-outlined}`system_update_alt;2em` Software Upgrades
```{toctree}
:maxdepth: 2

upgrade/index
```
+++
Guidelines for upgrading CrateDB clusters in production—from planning to execution.
::::

:::::
