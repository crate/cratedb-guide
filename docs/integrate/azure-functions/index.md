(azure-functions)=
# Azure Functions

:::{include} /_include/links.md
:::

_Execute event-driven serverless code with an end-to-end development experience._

:::{rubric} About
:::

[Azure Functions] is a serverless solution that allows you to build robust apps
while using less code, and with less infrastructure and lower costs. Instead
of worrying about deploying and maintaining servers, you can use the cloud
infrastructure to provide all the up-to-date resources needed to keep your
applications running.

An Azure Function is a short-lived, serverless computation that is triggered
by external events. The trigger produces an input payload, which is delivered
to the Azure Function. The Azure Function then does computation with this
payload and subsequently outputs its result to other Azure Functions, computation
services, or storage services. See also [What is Azure Functions?].

:::{rubric} Learn
:::

A common pattern is to use an Azure Function to enrich and ingest data
to a CrateDB instance by connecting that Azure Function to an IoT Hub's new
messages trigger.

:::{toctree}
:maxdepth: 1
learn
:::


[Azure Functions]: https://azure.microsoft.com/en-us/products/functions
[What is Azure Functions?]: https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview
