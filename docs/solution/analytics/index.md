(analytics)=
# Real-time raw-data analytics

:::{div} sd-text-muted
CrateDB provides real-time analytics on raw data stored for the long term.
:::

CrateDB eliminates the trade-off between data accessibility and storage costs
by keeping all high-volume raw data in the hot zone without requiring
downsampling or aggregation. Unlike traditional systems that force you to
choose between real-time query capabilities and long-term retention,
CrateDB handles billions of unique records while maintaining fast query
performance on the full dataset.

Traditional analytics pipelines rely on pre-aggregated rollups or batch
processing to handle query loads, limiting users to predefined metrics
and losing the granularity needed for ad-hoc analysis. CrateDB's
distributed architecture scales horizontally to support individual,
exploratory queries on complete raw datasets in real time, enabling
analysts to discover insights that would be invisible in downsampled data.

By keeping all records immediately available for querying, you avoid the
complexity of maintaining separate hot and cold storage tiers, ETL
pipelines for aggregation, or data movement processes. Your analytics
queries run directly on raw data across any time range, delivering the
accuracy and flexibility that business intelligence and data science
teams require.

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
- {ref}`longterm`
- {ref}`industrial`
- {ref}`machine-learning`
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
