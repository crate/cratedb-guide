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

`mix.exs`
```elixir
defmodule CrateDbExample do
  use Mix.Project
  def project do
    [
      app: :cratedb_elixir_example,
      version: "0.0.0",
      deps: [{:postgrex, "~> 0.21.0"}],
    ]
  end
end
```
`example.exs`
```elixir
options = [
  hostname: "localhost",
  port: 5432,
  ssl: false,
  username: "crate",
  password: "crate",
  database: "doc",
  backoff_type: :stop,
  max_restarts: 0,
  show_sensitive_data_on_connection_error: true,
]

{:ok, conn} = Postgrex.start_link(options)
result = Postgrex.query!(conn, "SELECT region, mountain, height FROM sys.summits ORDER BY height DESC LIMIT 5", [])
IO.inspect(result)
```

:::{include} ../_cratedb.md
:::
```shell
mix deps.get
mix run example.exs
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, adjust the `ssl: true` parameter,
and replace hostname, username, and password with values matching your
environment.
```elixir
options = [
  hostname: "testcluster.cratedb.net",
  port: 5432,
  ssl: true,
  username: "admin",
  password: "password",
  database: "doc",
  backoff_type: :stop,
  max_restarts: 0,
  show_sensitive_data_on_connection_error: true,
]
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
