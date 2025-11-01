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
Production recommendations and troubleshooting guidelines.
::::

::::{grid-item-card} {material-outlined}`speed;2em` Capacity Management
```{toctree}
:maxdepth: 2

Scaling <scale/index>
```
+++
Best practices for scaling your cluster up and down.
::::

::::{grid-item-card} {material-outlined}`system_update_alt;2em` Software Upgrades
```{toctree}
:maxdepth: 2

upgrade/index
```
+++
Upgrading CrateDB clusters in production—from planning to execution.
::::

:::::
