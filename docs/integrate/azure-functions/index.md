(azure-functions)=
# Azure Functions

:::{include} /_include/links.md
:::

```{div}
:style: "float: right;"
[![Azure Functions logo](https://www.vectorlogo.zone/logos/azurefunctions/azurefunctions-ar21.svg){h=60px}][Azure Functions]
```
```{div}
:style: "clear: both"
```

:::{rubric} About
:::

[Azure Functions] is an event-driven serverless code execution solution that
allows you to build robust apps while using less code, and with less
infrastructure and lower costs.

An Azure Function is a short-lived, serverless computation that is triggered
by external events. The trigger produces an input payload, which is delivered
to the Azure Function. The Azure Function then does computation with this
payload and subsequently outputs its result to other Azure Functions, computation
services, or storage services. See also [What is Azure Functions?].

:::{rubric} Learn
:::

::::{grid} 2

:::{grid-item-card} Data Enrichment using IoT Hub, Azure Functions and CrateDB
:link: azure-functions-learn
:link-type: ref
A common pattern is to use an Azure Function to enrich and ingest data
to a CrateDB instance by connecting that Azure Function to an IoT Hub's
new messages trigger.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
learn
:::


[Azure Functions]: https://azure.microsoft.com/en-us/products/functions
[What is Azure Functions?]: https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview
