# Atlan

```{div} .float-right
[![Atlan logo](https://website-assets.atlan.com/img/atlan-blue.svg){height=60px loading=lazy}][Atlan]
```
```{div} .clearfix
```

[Atlan] is an active metadata platform for modern data teams, that helps
them discover, understand, trust, govern, and collaborate on data assets.
Their product slogan is "Atlan -- The Active Metadata Platform".

:::{rubric} Overview
:::

The Atlan platform serves as a collaborative workspace for data teams,
allowing organizations to catalog, discover, and govern data assets across
cloud data warehouses, business intelligence tools, and data pipelines.

Atlan addresses what it describes as enterprise "data
chaos", the challenge organizations face managing data across dozens of tools
and systems. The platform serves as what the company calls a "metadata control
plane" that integrates with modern data infrastructure including cloud data
warehouses like Snowflake and Databricks, as well as business intelligence
and data science tools.

:::{rubric} Architecture
:::

Atlan distinguishes itself from traditional data catalogs through its "active
metadata" architecture, which programmatically harvests metadata such as logs,
query history, and usage metrics to automate governance tasks. This contrasts
with passive catalogs that rely on manual metadata entry.

Atlan's architecture emphasizes integration and automation over manual
processes. The platform is designed to integrate with existing data
infrastructure rather than requiring organizations to replace their current
tools.

:::{rubric} Features
:::

The Atlan software platform provides several key functions:

:Data Cataloging:
  
  Automated indexing of data assets including tables, columns, and dashboards
  to enable search and discovery across an organization's data infrastructure.

:Data Lineage:

  Visualization tools that track data flow from source to consumption, designed
  to assist with root cause analysis and impact assessments when making changes
  to data systems.
  
:Data Governance:

  Tools for managing access policies, masking sensitive data, and supporting
  regulatory compliance requirements such as GDPR and CCPA.

:AI Governance:

  Governance capabilities for AI models, including tracking the lineage of
  data used to train large language models (LLMs).

:::{rubric} Connect
:::

Please follow the [CrateDB connector for Atlan] documentation to learn how to
connect and catalog CrateDB assets in Atlan. Connect your data across
many more sources and destinations, see [Atlan connector gallery].


[Atlan]: https://atlan.com/
[Atlan connector gallery]: https://atlan.com/connectors/
[CrateDB connector for Atlan]: https://docs.atlan.com/apps/connectors/database/cratedb
