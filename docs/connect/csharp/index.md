:::{include} /_include/links.md
:::

(connect-csharp)=
# C#

:::{div} .float-right .text-right
[![C# Npgsql](https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-npgsql.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-npgsql.yml)
[![C# EF Core](https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-efcore.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-efcore.yml)
:::
:::{div} .clearfix
:::

:::{div} sd-text-muted
Connect to CrateDB from C# .NET applications.
:::

:::{rubric} About
:::

[Npgsql] is an open-source ADO\.NET Data Provider for PostgreSQL, for programs
written in C#, F#, or Visual Basic.

:::{rubric} Synopsis
:::

`example.csproj`
```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net$(NETCoreAppMaximumVersion)</TargetFramework>
    <GenerateProgramFile>false</GenerateProgramFile>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Npgsql" Version="10.0.0-rc.1" />
  </ItemGroup>

</Project>
```
`example.cs`
```c#
using Npgsql;
using System;

// Connect to database.
var connString = "Host=localhost;Port=5432;Username=crate;Password=crate;Sslmode=disable";
var dataSourceBuilder = new NpgsqlDataSourceBuilder(connString);
var dataSource = dataSourceBuilder.Build();
var conn = dataSource.OpenConnection();

// Invoke basic query.
var cmd = new NpgsqlCommand("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3", conn);

// Display results.
var reader = cmd.ExecuteReader();
while (reader.Read())
    Console.WriteLine($"{reader.GetString(0)}: {reader.GetInt32(1)}");
```

:::{include} ../_cratedb.md
:::
```shell
export DOTNET_CLI_TELEMETRY_OPTOUT=true
dotnet run
```

:::{rubric} SSL connection
:::

:::{div}
Use the `Sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to [CrateDB Cloud].
:::

```c#
var connString = "Host=testcluster.cratedb.net;Port=5432;Username=admin;Password=password;Sslmode=require";
```

## Examples

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/csharp-npgsql
:link-type: url
{material-regular}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using .NET (C#)
+++
Demonstrates a basic example using Npgsql with CrateDB.
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/csharp-efcore
:link-type: url
{material-regular}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using the Npgsql Entity Framework
+++
Demonstrates the Npgsql Entity Framework Core provider for PostgreSQL with CrateDB.
:::

## See also

:::{div}
- [Connection Strings in ADO.NET]
- [ADO.NET Overview]
:::


[Npgsql]: https://www.npgsql.org/
