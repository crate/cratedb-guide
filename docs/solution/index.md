(solutions)=
(use-cases)=

# Solutions and use cases

:::{div} sd-text-muted
CrateDB is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries. It is
PostgreSQL-compatible, and based on Lucene.

Learn how its featuers are applied within software solutions and application
platforms in different scenarios and environments.
:::

:::{toctree}
:hidden:
time-series/index
industrial/index
longterm/index
analytics/index
machine-learning/index
:::

## Explanations

:::{div} sd-text-muted
About time series and long-term data storage, real-time analytics, and machine learning.
:::

::::{grid} 1 2 2 2
:gutter: 2
:padding: 0

:::{grid-item-card} {material-outlined}`stacked_line_chart;2em` Time series data
:link: timeseries
:link-type: ref
:link-alt: About CrateDB for time series data analysis
Enhance your understanding of how to use CrateDB for time series use-cases,
and how to apply time series modeling and analysis procedures to your data.
+++
**What's inside:**
- Advanced statistical analysis
- Data visualization
- Machine learning
- Scientific computing
:::

:::{grid-item-card} {material-outlined}`manage_history;2em` Long-term store
:link: longterm-store
:link-type: ref
:link-alt: About storing time series data for the long term
Permanently keeping your raw data accessible for querying yields insightful
analysis opportunities other systems can't provide easily.
+++
**What's inside:**
- Time-based bucketing.
- Advanced querying.
- Import data using Dask.
- Optimizing storage for historic time series data.
:::

:::{grid-item-card} {material-outlined}`model_training;2em` Machine learning
:link: machine-learning
:link-type: ref
:link-alt: About CrateDB for machine learning applications
Get an overview of how CrateDB provides support for different kinds of
machine learning tasks, and learn how to integrate CrateDB with machine
learning frameworks and tools.
+++
**What's inside:**
- Vector store: Vector search, Hybrid search, LangChain
- Text-to-SQL: LlamaIndex, MCP, MindsDB
- Time series analysis: R, TensorFlow
- MLOps and model training: MLflow, PyCaret, scikit-learn
:::

::::


## Case studies

:::{div} sd-text-muted
About solutions built with CrateDB and
how others are using CrateDB successfully.
:::

CrateDB is being developed in an open-source spirit, and closely together
with its users and customers. Learn about application scenarios where CrateDB
derives many foundational features from, and how others are using CrateDB to
build real-time data management and analytics solutions and platforms.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

:::{grid-item-card} {material-outlined}`precision_manufacturing;2em` Industrial big data
:link: industrial
:link-type: ref
:link-alt: Use CrateDB in industrial data platforms
Learn how others are successfully using CrateDB within industrial,
engineering, manufacturing, production, and logistics domains.
+++
**What's inside:**
About the unique challenges and complexities of industrial big data.
:::

:::{grid-item-card} {material-outlined}`analytics;2em` Real-time analytics on raw data
:link: analytics
:link-type: ref
:link-alt: About CrateDB's analytics features
CrateDB provides real-time analytics on raw data.
Learn how others are successfully running real-time multi-tenant data
analytics applications on top of billions of records.
+++
**What's inside:**
For scenarios where all records must be retained due
to their unique value, downsampling is not applicable.
:::

::::
