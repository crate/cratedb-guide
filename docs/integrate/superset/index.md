(superset)=
(preset)=
# Superset / Preset

```{div} .float-right .text-right
[![Apache Superset logo](https://cratedb.com/hs-fs/hubfs/Apache-Superset-Logo-392x140@2x.png?width=604&height=216&name=Apache-Superset-Logo-392x140@2x.png){height=60px loading=lazy}][Apache Superset]
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-apache-superset.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-apache-superset.yml?branch=main&label=Apache Superset" loading="lazy" alt="CI status: Apache Superset"></a>
```
```{div} .clearfix
```

[Apache Superset] is an open-source modern data exploration and visualization
platform, written in Python.
[Preset] offers a managed, elevated, and enterprise-grade SaaS for open-source
Apache Superset.

![Apache Superset dashboard hero screenshot](https://superset.apache.org/img/hero-screenshot.jpg){h=200px}
![CrateDB + Superset example dashboard](https://github.com/crate/crate-clients-tools/assets/453543/0f8f7bd8-2e30-4aca-bcf3-61fbc81da855){h=200px}

:::{dropdown} **Managed Superset**
```{div}
:style: "float: right"
[![Preset Cloud](https://github.com/crate/crate-clients-tools/assets/453543/9d07da87-8aff-4569-bf2a-0a16bf89f4bc){height=60px loading=lazy}][Preset Cloud]
```

[Preset Cloud] is a fully-managed, open-source BI for the modern data stack,
based on Apache Superset.

- **Hassle-free setup:** There is no need to install or maintain software with Preset.
  Get the latest version of Superset in a secure, reliable, and scalable SaaS experience.
- **Up-to-date Superset, always:** Access all the latest features of Superset
  released and thoroughly tested every two weeks.
- **One-click to deploy multiple workspaces:** Give each team in your organization
  a separate Superset workspace to protect sensitive data.
- **Control user roles and access:** Easily assign roles and fine-tune data access
  using RBAC and row-level security (RLS).

```{div} .clearfix
```

:::


## Install

Follow the steps in [how to install database drivers in Docker Images] to install the
[CrateDB connector package] when setting up Superset locally using Docker Compose.
```shell
echo "sqlalchemy-cratedb" >> ./docker/requirements-local.txt
```


## Connect

Use a suitable SQLAlchemy connection string matching your environment.
When connecting to [CrateDB Self-Managed] on localhost,
for evaluation purposes, use:
```
crate://crate@127.0.0.1:4200
```

When connecting to [CrateDB Cloud], use:
```
crate://<username>:<password>@<clustername>.cratedb.net:4200/?ssl=true
```


## Learn

:::{rubric} Guides
:::

::::{grid}

:::{grid-item-card} Tutorial: Set up Apache Superset with CrateDB
:link: superset-tutorial
:link-type: ref
Learn how to install Apache Superset, and how to connect it with CrateDB.
:::

::::


:::{rubric} Blog
:::

::::{grid}

:::{grid-item-card} Blog: Open‑source data warehousing and visualization
:link: https://cratedb.com/blog/use-cratedb-and-apache-superset-for-open-source-data-warehousing-and-visualization
:link-type: url
Use CrateDB and Apache Superset for open-source data warehousing and visualization.
:::

:::{grid-item-card} Blog: Introduction to time-series visualization
:link: https://cratedb.com/blog/introduction-to-time-series-visualization-in-cratedb-and-superset
:link-type: url
Introduction to time‑series visualization in CrateDB and Apache Superset.
:::

::::


:::{rubric} Webinars
:::

::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Apache Superset 101**

From connecting databases to building charts, dashboards, and interactive filters,
this video covers all the basic surfaces and workflows of Apache Superset.
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/mAIH3hUoxEE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Webinar`
{tags-secondary}`Fundamentals`
:::

::::


::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**Apache Superset and CrateDB: Introduction to Time Series Visualization**

In this webinar, we will discuss how to use different visualization options in
Superset coupled with a SQL interface to derive interesting insights and findings
from the time series dataset.

- [Introduction to time series visualization in CrateDB and Apache Superset (Webinar)]
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/21KXInqrdeg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Webinar`
{tags-secondary}`Integrations`
:::

::::


:::{rubric} Development
:::
- {ref}`superset-sandbox`
- [Verify Apache Superset with CrateDB]



```{seealso}
[CrateDB and Apache Superset]
```

:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
Sandbox <sandbox>
:::


[Apache Superset]: https://superset.apache.org/
[CrateDB and Apache Superset]: https://cratedb.com/integrations/cratedb-and-apache-superset
[CrateDB Cloud]: https://cratedb.com/product/cloud
[CrateDB connector package]: https://superset.apache.org/docs/configuration/databases#cratedb
[CrateDB Self-Managed]: https://cratedb.com/product/self-managed
[how to install database drivers in Docker Images]: https://superset.apache.org/docs/configuration/databases#installing-drivers-in-docker-images
[Preset]: https://preset.io/
[Preset Cloud]: https://preset.io/product/
[Verify Apache Superset with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/application/apache-superset
