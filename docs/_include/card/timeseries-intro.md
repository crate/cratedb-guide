:::::{grid} auto 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

::::{grid-item-card} {material-outlined}`topic;2em` Time series: Device readings with metadata
:link: timeseries-objects
:link-type: ref
:class-footer: text-smaller

CrateDB supports effective time series analysis with enhanced features
for fast aggregations.

:::{rubric} What's Inside
:::
- Rich data types for storing structured nested data (OBJECT) alongside
  time series data.
- A rich set of built-in functions for aggregations.
- Relational JOIN operations.
- Common table expressions (CTEs).
+++
Combine time series with document data: CrateDB is all you need.
::::

::::{grid-item-card} {material-outlined}`lightbulb;2em` Time series: Analyzing weather data
:link: timeseries-analysis-weather
:link-type: ref
:class-footer: text-smaller
CrateDB provides advanced SQL features for querying time series data.

:::{rubric} What's Inside
:::
- Run aggregations with gap filling / interpolation, using common
  table expressions (CTEs) and LAG / LEAD window functions.

- Find maximum values using the MAX_BY aggregate function, returning
  the value from one column based on the maximum or minimum value of another
  column within a group.
+++
Advanced queries on time series data: CrateDB is all you need.
::::

::::{grid-item-card} {material-outlined}`area_chart;2em` Time series: Process financial data
:link: pandas-tutorial-jupyter
:link-type: ref
:class-footer: text-smaller
Acquire and store historical data from S&P-500 companies into CrateDB
using Python.

:::{rubric} What's Inside
:::
- Acquire historical stock ticker data from the Yahoo! Finance API.

- Store data into CrateDB.

- Query back data from CrateDB.
+++
Custom ETL tasks: CrateDB is all you need.
::::

:::::
