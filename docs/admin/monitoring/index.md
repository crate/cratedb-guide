(diagnostics)=
(monitoring)=

# Monitoring and diagnostics

It is important to continuously monitor your CrateDB database cluster
to detect anomalies and follow usage trends, so you can react to
them properly and timely.

CrateDB provides system information about the cluster as a whole,
individual cluster nodes, and about the entities and resources it manages.
Relevant information can be inquired using different protocols and tools.

:::{rubric} Types of information
:::

Different kinds of observability interfaces and support utilities
are available, for both continuous metrics collection and monitoring,
and for ad hoc use.
This enumeration includes a few popular and recommended options.

:::{rubric} Types of interfaces
:::

:JMX:

  CrateDB exposes telemetry data using the {ref}`jmx_monitoring`
  feature that needs to be enabled when starting CrateDB. It provides
  statistical information about queries, thread pools, and circuit
  breakers, and information about connections, server nodes,
  and health status.

  Information gathered by the JMX collectors can be provided to
  the Prometheus exporter or other observability and monitoring
  systems.

:SQL:

  CrateDB provides cluster and system information at runtime,
  through system tables located in the `sys` schema,
  which can be queried using SQL.

  {ref}`systables` illustrates how inquiring system tables
  works, and how to interpret the results. [^systables-more]

  {ref}`crate-reference:jobs_operations_logs` shares details
  about how to inspect the activities currently taking place
  in a cluster, reflected through cluster jobs and operations
  system tables.

:Prometheus:

  The [Crate JMX HTTP Exporter] is a Prometheus exporter that consumes
  metrics information from CrateDB's JMX collectors and exposes them
  via HTTP so they can be scraped by Prometheus, and, for example,
  subsequently displayed in Grafana, or processed into Alertmanager.

  [Monitoring a CrateDB cluster with Prometheus and Grafana] illustrates
  a full setup for making CrateDB-specific metrics available to Prometheus.
  The tutorial uses the _Crate JMX HTTP Exporter_ for exposing telemetry
  information, the _Prometheus SQL Exporter_ for conducting system table
  inquiries, and the _Prometheus Node Exporter_ for collecting OS metrics.

:CLI / HTTP:

  CrateDB is accompanied by a few looking-glass utilities that
  inquire its system tables to generate reports and display
  diagnostic output, or record it for later or remote inspection.

  The reporting tools support you to automate capturing information and
  enriching it into textual and tabular reports, or machine-readable formats.
  The analysis tools support you to discover anomalies and performance
  bottlenecks in your cluster.

  **Reports:** {ref}`ctk:cluster-info`, {ref}`ctk:cfr`, {ref}`ctk:settings`, {ref}`ctk:tail`. \
  **Analysis:** CrateDB XMover, CrateDB Shard Analyzer.


[^systables-more]: CrateDB provides the `sys` schema which contains
  virtual {ref}`system tables <crate-reference:system-information>`.
  These tables are read-only and can be queried to get statistical
  real-time information about the cluster, its nodes, and their shards.


[Crate JMX HTTP Exporter]: https://github.com/crate/jmx_exporter
[Monitoring a CrateDB cluster with Prometheus and Grafana]: https://community.cratedb.com/t/monitoring-a-self-managed-cratedb-cluster-with-prometheus-and-grafana/1236
