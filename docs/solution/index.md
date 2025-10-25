(solutions)=
(use-cases)=

# Solutions and use cases

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

## See also

:::{div} sd-text-muted
Other notable features of CrateDB.
:::

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2

:::{grid-item-card} {material-outlined}`search;2em` Full-text and semantic search
:link: search-overview
:link-type: ref
:link-alt: About CrateDB's search features
CrateDB enables you to build powerful search experiences for websites,
applications, and enterprise data.
+++
**What's inside:**
Learn how to leverage full-text, geospatial-,
vector-, and hybrid-search capabilities.
:::

:::{grid-item-card} {material-outlined}`manage_history;2em` Metrics and telemetry data store
:link: metrics-store
:link-type: ref
:link-alt: Using CrateDB as a long-term metrics store
Store metrics and telemetry data for the long term, with the benefits of
using standard database interfaces, SQL query language, and horizontal
scalability through clustering as you go.
+++
**What's inside:**
Never retire old records to cold storage,
always have them ready for historical analysis.
:::

::::
