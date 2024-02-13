(index)=
(guides)=
(howtos)=
(tutorials)=

# CrateDB Guides and Tutorials

About how to use CrateDB and CrateDB Cloud in practice.

CrateDB is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries. It is
PostgreSQL-compatible, and based on Lucene. 


::::{grid} 3
:padding: 0


:::{grid-item-card} Installation
:link: install
:link-type: ref
:link-alt: Installing CrateDB
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5

{material-outlined}`download_for_offline;1.3em`
:::


:::{grid-item-card} Getting Started
:link: getting-started
:link-type: ref
:link-alt: Getting started with CrateDB
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5

{material-outlined}`rocket_launch;1.3em`
:::


:::{grid-item-card} Handbook
:link: handbook
:link-type: ref
:link-alt: CrateDB Handbook
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5

{material-outlined}`auto_stories;1.3em`
:::


::::



## Reference Architectures

Reference architectures illustrating how CrateDB can be used in a variety of
use-cases.

::::{grid} 1
:padding: 0


:::{grid-item-card} Reference Architectures
:link: reference-architectures
:link-type: ref
:link-alt: Reference Architectures with CrateDB
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5

![](https://cratedb.com/hs-fs/hubfs/nativesql.png?width=480&name=nativesql.png)

:::

::::




## Application Domains

Native features of CrateDB paired with auxiliary software components provide
optimal coverage of different application domains.

::::{grid} 3
:padding: 0


:::{grid-item-card} Analysis and Visualization
:link: analysis
:link-type: ref
:link-alt: Data Analysis and Visualization with CrateDB
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5

{material-outlined}`analytics;1.3em`
:::


:::{grid-item-card} Time Series Data
:link: timeseries
:link-type: ref
:link-alt: Managing Time Series Data with CrateDB
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5

{material-outlined}`query_stats;1.3em`
:::


:::{grid-item-card} Machine Learning
:link: machine-learning
:link-type: ref
:link-alt: Machine Learning with CrateDB
:padding: 3
:text-align: center
:class-card: sd-pt-3
:class-body: sd-fs-1
:class-title: sd-fs-5

{material-outlined}`model_training;1.3em`
:::


::::



```{toctree}
:hidden:

install/index
getting-started/index
handbook/index
integrate/index

reference-architectures/index
t/analysis/index
t/timeseries/index
t/ml/index
```


:::{tip}
Please also visit the [Overview of CrateDB integration tutorials].
:::

:::{seealso}
CrateDB and its documentation are open source projects. We host the source code and
issue tracker on [GitHub].
:::


[GitHub]: https://github.com/crate/cratedb-guide
[Overview of CrateDB integration tutorials]: https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015
