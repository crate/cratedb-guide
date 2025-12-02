(use)=
(getting-started)=
# Getting Started

```{toctree}
:maxdepth: 1
:hidden:

video/index
modelling/index
query/index
import
application/index
```


:::{div} sd-text-muted
Get started fast with CrateDB: Setup or install CrateDB and try a few quick
tutorials.
:::

:::{note}
**Prefer video tutorials?** Then we have a more elaborate
<a href="https://learn.cratedb.com/" target="_blank">Academy Fundamentals course</a>
with hands-on video tutorials that walk you through setup or installation and key
concepts step by step. Or take the quick route below with our text-based
quickstart.
:::

We highly recommend to try out CrateDB with a free Cloud cluster for the
smoothest experience with integrated tutorials - no install, no
copy-pasting examples.
<br>
Alternatively, select "Local" below to install CrateDB with Docker and follow
the more manual tutorials.


````{tab-set}
```{tab-item} Cloud (Recommended)


## 1. Create your free cluster

Sign up for CrateDB Cloud and create your first cluster in 2 minutes.

:::{button-link} https://console.cratedb.cloud/
:color: primary
**Start free with CrateDB Cloud →**
:::

After logging in you will see the Cloud Console Quickstart page, with
options to try tutorials, import data, or connect programmatically.

:::{figure} /_assets/img/getting-started/cloud-quickstart.png
:alt: CrateDB Cloud Console showing Interactive Tutorials
:width: 100%
:figclass: sd-text-muted sd-font-italic sd-opacity-50

The Cloud Quickstart page
:::


## 2. Run tutorials

Once your cluster is ready, you can go through one or more of the
**interactive tutorials** directly in the browser in ~5 minutes each.
With the click of a button you will import data, execute queries, and
see the results.


## 3. Experiment in the Console

After completing a tutorial, the sample data remains in your cluster. You
can now use the **Console** in the Cloud UI to explore the data and run
your own SQL queries, perhaps with inspiration from our
{ref}`query-capabilities`.

:::{figure} /_assets/img/getting-started/cloud-console.png
:alt: CrateDB Cloud Console
:width: 100%
:figclass: sd-text-muted sd-font-italic sd-opacity-50

The Cloud Console page
:::


```
```{tab-item} Local


## 1. Install CrateDB

If you prefer to try CrateDB locally, the quickest way is using
<a href="https://docs.docker.com/get-docker/" target="_blank">Docker</a>:

:::{code} shell
docker run -p 4200:4200 -p 5432:5432 crate:latest
:::

For other installation methods, see our {ref}`install` guide.

:::{caution}
By default, the CrateDB Docker container is ephemeral, so data will not be
stored in a persistent manner. When you stop the container, all data will
be lost. For production use, consult the {ref}`Docker guide
<cratedb-docker>` to configure persistent disk volumes.
:::


## 2. Access the Admin UI

Once CrateDB is running, open your browser and navigate to
<http://localhost:4200> to access the {ref}`Admin UI
<crate-admin-ui:index>`. From here you can:

* Browse tables and data
* Execute SQL queries
* Monitor cluster health

:::{figure} /_assets/img/getting-started/admin-ui-console.png
:alt: CrateDB Admin UI Console
:width: 100%
:figclass: sd-text-muted sd-font-italic sd-opacity-50

The Admin UI Console page
:::

You will use this in the next section to run SQL statements.


## 3. Run tutorials

Learn about fundamental features of CrateDB with hands-on example
tutorials.

:::::{grid} 2
:gutter: 3
:padding: 0

::::{grid-item-card} Objects: Analyzing marketing data
:link: objects-tutorial-marketing
:link-type: ref
CrateDB's dynamic OBJECT data type can store and analyze complex and
nested data efficiently.
::::

::::{grid-item-card} Full-text: Exploring the Netflix catalog
:link: search-tutorial-netflix
:link-type: ref
Learn how to make use of CrateDB's full-text search capabilities.
::::

::::{grid-item-card} Analyzing weather data
:link: timeseries-tutorial-weather
:link-type: ref
Learn how to analyze time series data on behalf of a practical example.
::::

::::{grid-item-card} Analyzing device readings with metadata integration
:link: timeseries-tutorial-metadata
:link-type: ref
Learn how to combine time series data with metadata.
::::

:::::

## 4. Experiment in the Console

After completing one or more tutorials, you can continue to explore the
data in the Console with SQL queries, perhaps with inspiration from our
{ref}`query-capabilities`.


<!-- end tab-set -->
```
````


## What's next?

From here you can take several different directions.

```{rubric} Continue learning
```

:::::{grid} 1 2 2 3
:gutter: 3

::::{grid-item-card}
:link: https://learn.cratedb.com/
:class-header: sd-text-center

{material-outlined}`school;2em` **Learn through courses**
^^^
Get a detailed introduction to CrateDB with video explanations and
hands-on exercises through our Academy courses.
::::

::::{grid-item-card}
:link: data-modelling
:link-type: ref
:class-header: sd-text-center

{material-outlined}`schema;2em` **Data modelling**
^^^
Learn how to model structured, semi-structured, and unstructured data in
CrateDB.
::::

::::{grid-item-card}
:link: query-capabilities
:link-type: ref
:class-header: sd-text-center

{material-outlined}`search;2em` **Query capabilities**
^^^
Explore CrateDB's powerful querying features including aggregations,
full-text search, and vector search.
::::

:::::

```{rubric} Start building
```

:::::{grid} 1 2 2 3
:gutter: 3

::::{grid-item-card}
:link: start-import
:link-type: ref
:class-header: sd-text-center

{material-outlined}`upload;2em` **Import data**
^^^
Import files directly via URL in CSV, JSON or Parquet format, load sample
datasets, or use SQL `COPY FROM` as demonstrated in the tutorials.
::::

::::{grid-item-card}
:link: connect
:link-type: ref
:class-header: sd-text-center

{material-outlined}`code;2em` **Connect**
^^^
Connect to CrateDB from your application using drivers in your prefferred
programming language.
::::

::::{grid-item-card}
:link: example-applications
:link-type: ref
:class-header: sd-text-center

{material-outlined}`lightbulb;2em` **Get inspired**
^^^
Explore sample applications for inspiration when building your own
applications with CrateDB.
::::

:::::


{material-outlined}`menu_book;1.5em`
Additionally, we recommend you explore the rest of the documentation via
the left-hand navigation.

<br>

:::::{admonition} Need help?
:class: tip
<br>

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card}
:link: https://community.cratedb.com/
:class-header: sd-text-center

{material-outlined}`groups;2em` **Community**
^^^
Join our Community Forum to ask questions and connect with other CrateDB
users.
:::

:::{grid-item-card}
:link: https://cratedb.com/contact/
:class-header: sd-text-center

{material-outlined}`support;2em` **Support**
^^^
Contact our support team for assistance with your CrateDB deployment.
:::
::::
:::::
