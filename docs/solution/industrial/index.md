(daq)=
(iiot)=
(industrial)=
(industry-40)=
# Industrial big data

:::{div} sd-text-muted
Industry 4.0, but cost-effective: CrateDB is the backbone for all the analytics.
:::

Today's industrial and logistics data acquisition and processing systems
are complex and distributed, with a very high degree of automation.

In the realm of Industrial IoT, dealing with diverse data, ranging from
slow-moving structured data, to high-frequency measurements, presents unique
challenges.
The complexities of industrial big data are characterized by its high variety,
unstructured features, different data sampling rates, and how these attributes
influence data storage, retention, and integration.

Learn how to use CrateDB in long-term storage and analytics scenarios for
industrial / IIoT / Industry 4.0 environments within
engineering, manufacturing, production, and logistics, as well as other
operational domains, or within similar environments where billions of data
records from any kinds of machines or devices need to be processed, stored,
and queried.

With CrateDB, compatible with PostgreSQL, you can do all of that using plain SQL.
Other than integrating well with commodity systems using standard database
access interfaces like ODBC or JDBC, it provides a proprietary HTTP interface
on top.


(industrial-customer-insights)=
(reference-architectures)=
:::{rubric} See also
:::

:::::{grid}
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`apartment;1.5em` Reference architectures
:columns: 12 6 4 4

:::{toctree}
:maxdepth: 1
Azure IoT <azure-iot>
Machine Learning <distributed-ml>
:::
+++
Reference architectures about how CrateDB can be used in various environments.
::::

::::{grid-item-card} {material-outlined}`group;1.5em` Customer insights
:columns: 12 6 3 3

:::{toctree}
:maxdepth: 1
abb
rauch
spgo
tgw
:::
+++
Companies that are successfully using CrateDB in their technology stack.
::::

::::{grid-item-card} {material-outlined}`factory;1.5em` Product
:columns: 12 12 5 5

- [IoT database]
- [FMCG (Fast-moving consumer goods)]
- [Logistics]
- [Manufacturing]
+++
Real-time analytics on large volumes of data from IoT devices, sensors, and
production systems in manufacturing, shipping, fulfillment, and logistics.
::::

:::::

:Related:
  {ref}`analytics` •
  {ref}`longterm-store` •
  {ref}`machine-learning`

:Tags:
  {tags-primary}`Data Historian`
  {tags-primary}`Industrial IoT`
  {tags-primary}`Industry 4.0`
  {tags-primary}`SCADA`
  {tags-primary}`MDE`

:Technologies:
  {tags-info}`DAQ`
  {tags-info}`PLC`
  {tags-info}`SPS`


[FMCG (Fast-moving consumer goods)]: https://cratedb.com/industries/fmcg
[IoT database]: https://cratedb.com/use-cases/iot-database
[Logistics]: https://cratedb.com/industries/logistics
[Manufacturing]: https://cratedb.com/industries/manufacturing
