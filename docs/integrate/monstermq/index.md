(monstermq)=
# MonsterMQ

```{div} .float-right
[![MonsterMQ logo](https://monstermq.com/logo-small.png){width=180px loading=lazy}][MonsterMQ]
```
```{div} .clearfix
```

:::{rubric} About
:::

[MQTT] is an OASIS standard messaging protocol for the Internet of Things (IoT).
[MonsterMQ] is an open-source MQTT broker for factory automation and
industrial IoT that can persist MQTT topic state directly in CrateDB, using
CrateDB's PostgreSQL wire protocol, without needing an external relay such
as LorryStream. Retained/last values and message archives land straight in
CrateDB, where they can be queried with SQL and combined with other data
already stored there. MonsterMQ layers its own GraphQL, REST, and MCP APIs,
plus built-in AI agents (Gemini, Claude, OpenAI, Ollama) and OPC UA/PLC4X/
WinCC device connectors, on top of that CrateDB-backed state, giving factory
and IoT data a queryable, always-up-to-date home in CrateDB alongside
real-time access for dashboards, devices, and LLM-driven automation.

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} MonsterMQ on GitHub
:link: https://github.com/vogler75/monster-mq
:link-type: url
Source code, quick start, and full documentation.
:::

:::{grid-item-card} Database backends
:link: https://github.com/vogler75/monster-mq/blob/main/doc/databases.md
:link-type: url
How to configure CrateDB (and other databases) as a MonsterMQ storage backend.
:::

::::


[MonsterMQ]: https://monstermq.com/
[MQTT]: https://mqtt.org/