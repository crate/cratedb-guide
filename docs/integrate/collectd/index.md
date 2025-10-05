(collectd)=
# collectd

```{div} .float-right
[![collectd example graph](https://collectd.org/images/graph-cpu.png){width=180px loading=lazy}][collectd]
```
```{div} .clearfix
```

:::{rubric} About
:::

[collectd] is a system statistics collection daemon suitable for application
performance metrics periodically and provides mechanisms to store the values
in a variety of ways.

collectd gathers metrics from various sources, e.g. the operating system,
applications, logfiles and external devices, and stores this information or
makes it available over the network. Those statistics can be used to monitor
systems, find performance bottlenecks (i.e. performance analysis) and predict
future system load (i.e. capacity planning).

:::{rubric} Synopsis
:::

Either use the `postgresql` plugin to store metrics into CrateDB,

:::{literalinclude} collectd-cratedb.conf
:::

or use the `network` plugin to forward metrics to Telegraf, then
using its built-in [CrateDB Output Plugin for Telegraf].

:::{literalinclude} collectd-telegraf.conf
:::


:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Use collectd with CrateDB
:link: collectd-usage-base
:link-type: ref
How to configure collectd to submit metrics to CrateDB.
:::

:::{grid-item-card} Use collectd with Telegraf and CrateDB
:link: collectd-usage-telegraf
:link-type: ref
How to configure collectd and Telegraf to submit metrics to CrateDB.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Usage with collectd <usage-collectd>
Usage with Telegraf <usage-telegraf>
:::


[collectd]: https://collectd.org/
[CrateDB Output Plugin for Telegraf]: https://github.com/influxdata/telegraf/tree/master/plugins/outputs/cratedb
