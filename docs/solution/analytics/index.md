(analytics)=
# Real-time raw-data analytics

:::{div} sd-text-muted
CrateDB provides real-time analytics on raw data stored for the long term.
:::

In all domains of real-time analytics where you absolutely must have access to all
the records, and can't live with any down-sampled variants, because records are
unique, and need to be accounted for within your analytics queries.

If you find yourself in such a situation, you need a storage system which
manages all the high-volume data in its hot zone, to be available right on
your fingertips, for live querying. Batch jobs to roll up raw data into
analytical results are not an option, because users' queries are too
individual, so you need to run them on real data in real time.

:::{todo}
**Instructions:**
Elaborate a bit longer about the topic domain and the ingredients of this section
in an abstract way, concisely highlighting and summarizing relevant benefits,
like the `../analytics/index`, `../industrial/index`, and `../longterm/index`
pages are doing it already.
Use concise language, active voice, and avoid yapping.
:::

With CrateDB, compatible to PostgreSQL, you can do all of that using plain SQL.
Other than integrating well with commodity systems using standard database
access interfaces like ODBC or JDBC, it provides a proprietary HTTP interface
on top.

:::{rubric} See also
:::

:::::{grid}
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`link;1.5em` Related
:columns: 12 6 3 3

- {ref}`timeseries`
- {ref}`machine-learning`
- {ref}`industrial`
+++
Related topics in the same area.
::::

::::{grid-item-card} {material-outlined}`group;1.5em` Customer insights
:columns: 12 6 4 4

:::{toctree}
:maxdepth: 1
bitmovin
:::
+++
Companies that are successfully using CrateDB in their technology stack.
::::

::::{grid-item-card} {material-outlined}`factory;1.5em` Product
:columns: 12 12 5 5

- [Media & entertainment]
- [Real-time analytics database]
- [Streaming Analytics]
+++
Real-time analytics on large volumes of data from click event streams and
similar applications.
::::

:::::


:Tags:
  {tags-primary}`Analytics`
  {tags-primary}`Long Term Storage`


[Media & entertainment]: https://cratedb.com/media-entertainment
[Real-time analytics database]: https://cratedb.com/solutions/real-time-analytics-database
[Streaming Analytics]: https://cratedb.com/use-cases/streaming-analytics
