(cloud)=
# Cloud Native

:::{include} /_include/links.md
:::


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

**CrateDB is designed to support cloud computing from the beginning.**

:::{rubric} Overview
:::
CrateDB works well in cloud computing environments, managed or unmanaged.

:::{rubric} About
:::

CrateDB is offered as a managed service available on AWS, Azure, and GCP, and also
as a fully open source edition.

:::{rubric} Details
:::

CrateDB is an SQL database for enterprise data warehouse workloads,
that works across clouds and scales with your data.
It lets you run analytics over vast amounts of data in near real time,
even with complex queries.

You can run CrateDB anywhere. Whether you want complete peace of mind with the
DBaaS model, or deploy CrateDB yourself, we have the right option for you.

CrateDB is highly flexible and can be deployed on private or public cloud,
on-premises, edge, or in hybrid environments to meet your organization's
needs.

- {ref}`cloud:index` is a fully managed, terabyte-scale, and cost-effective analytics
  database offered as DBaaS.

- [CrateDB OSS] is the right option to deploy CrateDB yourself, to contribute
  features, and to explore and inspect its source code.


::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Reference Manual
:::
- {ref}`crate-reference:node_discovery`
- {ref}`guide:install-cloud`

:::{rubric} Guides
:::
- {ref}`guide:clustering`
- {ref}`guide:azure`
- {doc}`guide:install/cloud/aws/index`

:::{rubric} CrateDB Cloud
:::
- {ref}`cloud:index`
- {ref}`Documentation <cloud:index>`
- [Web Console]

{tags-primary}`Cloud`
{tags-primary}`AWS`
{tags-primary}`Azure`
{tags-primary}`GCP`
::::

:::::


## Usage

Applications that support operating CrateDB in cloud environments.

- {ref}`cloud-cli:index`
  is a command-line interface (CLI) tool for interacting with CrateDB Cloud.

- [CrateDB Kubernetes Operator]
  provides a convenient way to run CrateDB clusters on Kubernetes.



:::{seealso} **Product:**
[CrateDB Editions]
:::


:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
It only includes the most basic essentials, and needs expansion. For example,
the "Synopsis" and "Learn" sections are missing completely, referring to
corresponding tutorials and other educational material.
:::


[CrateDB Editions]: https://cratedb.com/database/editions
[CrateDB Kubernetes Operator]: https://github.com/crate/crate-operator/
[CrateDB OSS]: https://github.com/crate/crate
[Web Console]: https://console.cratedb.cloud/
