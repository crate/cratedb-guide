(statsd)=
# StatsD

```{div} .float-right
[![StatsD logo](https://avatars.githubusercontent.com/u/8270030?s=200&v=4){height=100px loading=lazy}][StatsD]
```
```{div} .clearfix
```

:::{rubric} About
:::

[StatsD] provides easy but powerful system and application
metrics and stats aggregation.

This network daemon runs on the Node.js platform and listens for
statistics, like counters and timers, sent over UDP or TCP. It then sends
aggregates to one or more pluggable backend services.

StatsD traditionally uses the Graphite backend and its successors, but you
can also configure it to use CrateDB as a backend by relaying data through Telegraf
with its built-in [CrateDB Output Plugin for Telegraf].

:::{rubric} Synopsis
:::

Configure Telegraf using the StatsD input plugin and the CrateDB output plugin.

:::{literalinclude} telegraf.conf
:::


:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Tutorial: Use StatsD with CrateDB
:link: statsd-tutorial
:link-type: ref
How to configure StatsD and Telegraf to submit statistics to CrateDB.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
:::


[CrateDB Output Plugin for Telegraf]: https://github.com/influxdata/telegraf/tree/master/plugins/outputs/cratedb
[StatsD]: https://github.com/statsd/statsd
