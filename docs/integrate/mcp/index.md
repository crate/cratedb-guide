# Model Context Protocol (MCP)

```{toctree}
:maxdepth: 0
:hidden:

cratedb-mcp
Community servers <community>
```

## About

:::{rubric} Introduction
:::

[MCP], the Model Context Protocol, is an open protocol that enables seamless
integration between LLM applications and external data sources and tools.

Others define MCP as "It's effectively just OpenAPI for LLMs" or "It's the
USB-C port for AI", providing a uniform way to connect LLMs to resources they
can use.

:::{rubric} Details
:::

The main entities of MCP are [prompts], [resources], and [tools].
MCP clients call MCP servers, either by invoking them as a subprocess and
communicating via Standard Input/Output (stdio), Server-Sent Events (sse),
or HTTP Streams (streamable-http), see [transports].

:::{rubric} Discuss
:::

To get in touch with us to discuss CrateDB and MCP, head over to GitHub at
[Model Context Protocol (MCP) @ CrateDB] or the [Community Forum].

## Usage

You can use MCP with [CrateDB] and [CrateDB Cloud], either by selecting the
**CrateDB MCP Server** suitable for Text-to-SQL and documentation retrieval,
or by using community MCP servers that are compatible with PostgreSQL databases.

::::{grid} 1 2 2 2
:margin: 4 4 0 0

:::{grid-item-card} {material-outlined}`apps;2em` CrateDB MCP Server
:link: cratedb-mcp
:link-type: doc
:link-alt: CrateDB MCP Server

The CrateDB MCP Server, available on PyPI and popular community hubs.
:::

:::{grid-item-card} {material-outlined}`group;2em` Community MCP Servers
:link: community
:link-type: doc
:link-alt: Community MCP Servers

MCP servers mostly compatible with both PostgreSQL and CrateDB.
:::

::::

To use an MCP server, you need a [client that supports][MCP clients] the
protocol. The most notable ones are ChatGPT, Claude, Cline, Cursor,
GitHub Copilot, Mistral AI, OpenAI Agents SDK, VS Code, Windsurf,
and others.


[Community Forum]: https://community.cratedb.com/
[CrateDB]: https://cratedb.com/database
[CrateDB Cloud]: https://cratedb.com/docs/cloud/
[MCP]: https://modelcontextprotocol.io/
[MCP clients]: https://modelcontextprotocol.io/clients
[Model Context Protocol (MCP) @ CrateDB]: https://github.com/crate/crate-clients-tools/discussions/234
[Prompts]: https://modelcontextprotocol.io/docs/concepts/prompts
[Resources]: https://modelcontextprotocol.io/docs/concepts/resources
[Tools]: https://modelcontextprotocol.io/docs/concepts/tools
[Transports]: https://modelcontextprotocol.io/docs/concepts/transports
