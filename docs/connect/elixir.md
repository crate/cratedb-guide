(connect-elixir)=

# Elixir

:::{div} sd-text-muted
Connect to CrateDB from Elixir applications.
:::

:::{rubric} About
:::

[Postgrex] is the canonical PostgreSQL driver for Elixir.

:::{rubric} Synopsis
:::

```elixir
{:ok, pid} = Postgrex.start_link(hostname: "localhost", username: "crate", password: "crate", database: "")
{:ok, #PID<0.69.0>}

Postgrex.query!(pid, "SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3", [])
```

## Example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/elixir-postgrex
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using Elixir.
+++
Demonstrates a basic example that uses the Postgrex driver.
:::

[![Elixir Postgrex](https://github.com/crate/cratedb-examples/actions/workflows/lang-elixir-postgrex.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-elixir-postgrex.yml)


[Postgrex]: https://hexdocs.pm/postgrex/readme.html
