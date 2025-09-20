(statsd)=
# StatsD

```{div} .float-right
[![StatsD logo](https://avatars.githubusercontent.com/u/8270030?s=200&v=4){height=100px loading=lazy}][StatsD]
```
```{div} .clearfix
```

:::{rubric} About
:::

[StatsD] is a daemon for easy but powerful system and application
metrics and stats aggregation.

It is a network daemon that runs on the Node.js platform and listens for
statistics, like counters and timers, sent over UDP or TCP and sends
aggregates to one or more pluggable backend services.

StatsD traditionally uses the Graphite backend and its successors, but it
can also use CrateDB as a backend, by relaying data through Telegraf and
using its built-in [CrateDB Output Plugin for Telegraf].

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
