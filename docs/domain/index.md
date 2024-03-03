(domain)=
(domains)=

# Application Domains

Tutorials and guidelines about how to use CrateDB within different use case
scenarios, and how others are using it to build their data management
solutions.


```{toctree}
:maxdepth: 1

analytics/index
industrial/index
timeseries/index
../integrate/ml/index
```

:Related Features:
  [](#document) •
  [](#fulltext) •
  [](#geospatial)

```{include} /_include/styles.html
```


:::{rubric} Traditional Use Cases
:::

CrateDB is being developed in an open-source spirit, and closely together
with its users and customers. Learn about application scenarios where CrateDB
derives many foundational features from.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2


:::{grid-item-card} {material-outlined}`analytics;2em` Raw-Data Analytics
:link: analytics/index
:link-type: doc
:link-alt: About CrateDB's analytics features

CrateDB provides real-time analytics on raw data.
Learn how others are successfully running multi tenant data analytics on
top of billions of records.
+++
**What's inside:**
Never retire old records to cold storage, always keep them hot instead.
:::


:::{grid-item-card} {material-outlined}`precision_manufacturing;2em` Industrial Data
:link: industrial/index
:link-type: doc
:link-alt: Use CrateDB in industrial data platforms

Learn how others are successfully using CrateDB within industrial,
engineering, manufacturing, production, and logistics domains.
+++
**What's inside:**
About the unique challenges and complexities of industrial big data.
:::


::::


:::{rubric} Time Series Analysis and Machine Learning
:::

Apply procedures from advanced analysis, scientific computing, and other
technology domains to your data without further ado.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2


:::{grid-item-card} {material-outlined}`stacked_line_chart;2em` Time Series
:link: timeseries/index
:link-type: doc
:link-alt: About CrateDB for time series data

Learn how to use CrateDB for time series use-cases,
and how to apply time series modeling and analysis procedures
to your data.
+++
**What's inside:**
Tutorials about data-import and -export, statistical
analysis, data visualization, and machine learning.
:::


:::{grid-item-card} {material-outlined}`model_training;2em` Machine Learning
:link: machine-learning
:link-type: ref
:link-alt: About CrateDB for machine learning applications

Learn how to integrate CrateDB with machine learning frameworks and tools.
+++
**What's inside:**
Use CrateDB with LangChain, MLflow, PyCaret, scikit-learn,
and TensorFlow.
:::


::::
