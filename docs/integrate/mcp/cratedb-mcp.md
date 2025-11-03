# CrateDB MCP Server

:::{div} sd-text-muted
The CrateDB MCP Server provides natural-language
Text-to-SQL and documentation retrieval.
:::

The Model Context Protocol ([MCP]) is a protocol that standardizes providing
context to language models and AI assistants.

:::{rubric} Introduction
:::

The CrateDB Model Context Protocol (MCP) Server connects AI assistants directly
to your CrateDB clusters and the CrateDB knowledge base, enabling seamless
interaction through natural language.

It serves as a bridge between AI tools and your analytics database,
allowing you to analyze data, the cluster state, troubleshoot issues, and
perform operations using conversational prompts.

:::{rubric} What's inside
:::

::::{grid} 1 2 2 2
:gutter: 2

:::{grid-item-card} {material-outlined}`description;2em` Documentation
:link: https://cratedb-mcp.readthedocs.io/
:link-type: url
:link-alt: CrateDB MCP Server README
About how to install and configure the CrateDB MCP Server,
and what's inside.
:::

:::{grid-item-card} {octicon}`package;2em` Python package
:link: https://pypi.org/project/cratedb-mcp/
:link-type: url
:link-alt: CrateDB MCP Server Python package `cratedb-mcp`
The Python package `cratedb-mcp` for public consumption.
:::

::::


:::{rubric} Example
:::

An example conversation to "talk to your data using your AI assistant of choice"
may look like this in practice. It is using a dataset about weather data, where
the user is interested in values which are beyond certain thresholds.

![Example Claude conversation screenshot using CrateDB MCP](https://github.com/user-attachments/assets/db127717-329a-4d0e-901c-3e3dcaefefb9)


:::{caution}

**Experimental:** Please note that the CrateDB MCP Server is an experimental
feature provided as-is without warranty or support guarantees. Enterprise
customers should use this feature at their own discretion.

:::

[MCP]: https://modelcontextprotocol.io/
