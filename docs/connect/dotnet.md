(connect-dotnet)=

# .NET

:::{div} sd-text-muted
Use Npgsql to connect to CrateDB from .NET applications.
:::

:::{rubric} About
:::

[Npgsql] is an open source ADO\.NET Data Provider for PostgreSQL, for programs
written in C#, Visual Basic, and F#.

:::{rubric} Synopsis
:::

```c#
using Npgsql;

var connString = "Host=localhost;Username=crate;Password=crate;Database=testdrive";

var dataSourceBuilder = new NpgsqlDataSourceBuilder(connString);

await using var dataSource = dataSourceBuilder.Build();
await using var conn = await dataSource.OpenConnectionAsync();

await using var cmd = new NpgsqlCommand("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3", conn);
await using var reader = await cmd.ExecuteReaderAsync();
while (await reader.ReadAsync())
    Console.WriteLine($"{reader.GetString(0)} ({reader.GetInt32(1)})");
```

## Examples

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/csharp-npgsql
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using .NET (C#)
+++
Demonstrates a basic example using Npgsql with CrateDB.
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/csharp-efcore
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using the Npgsql Entity Framework
+++
Demonstrates the Npgsql Entity Framework Core provider for PostgreSQL with CrateDB.
:::

[![C# Npgsql](https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-npgsql.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-npgsql.yml)
[![C# EF Core](https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-efcore.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-efcore.yml)


[Npgsql]: https://www.npgsql.org/
