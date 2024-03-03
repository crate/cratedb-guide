(domain)=
(domains)=

# Application Domains

Learn how to apply CrateDB within different use case scenarios, and how others
are using CrateDB to build data management solutions and platforms.

{tags-primary}`Full-Text Search`
{tags-primary}`Document / Object / JSON`
{tags-primary}`Long Term Metrics Store`
{tags-primary}`Time Series Data`
{tags-primary}`Industrial Data`
{tags-primary}`Machine Learning`
:::


```{toctree}
:maxdepth: 1

Metrics Store <metrics/index>
analytics/index
industrial/index
timeseries/index
ml/index
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


:::{grid-item-card} {material-outlined}`manage_history;2em` Long Term Metrics Store
:link: metrics-store
:link-type: ref
:link-alt: Using CrateDB as a long term metrics store

Store metrics and telemetry data for the long term, with the benefits of
using standard database interfaces, SQL query language, and horizontal
scalability through clustering as you go.
+++
**What's inside:**
Never retire old records to cold storage,
always have them ready for historical analysis.
:::


:::{grid-item-card} {material-outlined}`analytics;2em` Raw-Data Analytics
:link: analytics
:link-type: ref
:link-alt: About CrateDB's analytics features

CrateDB provides real-time analytics on raw data.
Learn how others are successfully running real-time multi tenant data
analytics applications on top of billions of records.
+++
**What's inside:**
If you absolutely must keep the records, because they are unique,
downsampling is not an option.
:::


:::{grid-item-card} {material-outlined}`precision_manufacturing;2em` Industrial Data
:link: industrial
:link-type: ref
:link-alt: Use CrateDB in industrial data platforms

Learn how others are successfully using CrateDB within industrial,
engineering, manufacturing, production, and logistics domains.
+++
**What's inside:**
About the unique challenges and complexities of industrial big data.
:::


::::


:::{rubric} Time Series Data Analysis and Machine Learning
:::

Apply procedures from advanced analysis, scientific computing, and other
technology domains to your data without further ado.

::::{grid} 1 2 2 2
:margin: 4 4 0 0
:padding: 0
:gutter: 2


:::{grid-item-card} {material-outlined}`stacked_line_chart;2em` Time Series Data
:link: timeseries
:link-type: ref
:link-alt: About CrateDB for time series data analysis

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


:::{seealso} **Related Features:**
[](#document) •
[](#fulltext) •
[](#geospatial) •
[](#generated-columns) •
[](#udf)



```{include} /_include/styles.html
```
