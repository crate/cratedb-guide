# Monitoring and health

It is important to continuously monitor your CrateDB database cluster
to detect anomalies and follow usage trends, so you can react to
them properly and timely.

CrateDB provides different kinds of observability interfaces and
support utilities, for both continuous metrics collection and
monitoring, and for ad hoc use.
This documentation page illustrates all options.

:::{rubric} Types of information
:::

CrateDB provides system information about individual cluster nodes, the
cluster as a whole, and about higher level entities it manages.
Relevant information can be inquired using different protocols and tools.

:::{rubric} Types of interfaces
:::

:JMX interface:

  CrateDB exposes telemetry data using the {ref}`jmx_monitoring`
  feature that needs to be enabled when starting CrateDB. It provides
  statistical information about queries, thread pools, and circuit
  breakers, connection information, server node information,
  and health status.

:Prometheus exporter:

  The [Crate JMX HTTP Exporter] consumes metrics information from
  the JMX collectors and exposes them via HTTP so they can be
  scraped by Prometheus.

:SQL:

  Foo.

:CFR:

  Foo.



[Crate JMX HTTP Exporter]: https://github.com/crate/jmx_exporter
