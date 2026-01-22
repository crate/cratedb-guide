:::{include} /_include/links.md
:::

(connect-fsharp)=
# F#

:::{div} sd-text-muted
Connect to CrateDB from F# .NET applications.
:::

:::{rubric} About
:::

[Npgsql] is an open-source ADO\.NET Data Provider for PostgreSQL, for programs
written in C#, F#, or Visual Basic.
[Npgsql.FSharp] is a thin F#-friendly layer around it.

:::{rubric} Synopsis
:::

`example.fsproj`
```xml
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net$(NETCoreAppMaximumVersion)</TargetFramework>
    <GenerateProgramFile>false</GenerateProgramFile>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Npgsql" Version="10.0.0-rc.1" />
    <PackageReference Include="Npgsql.FSharp" Version="8.0.0" />
  </ItemGroup>

  <ItemGroup>
    <Compile Include="example.fs" />
  </ItemGroup>

</Project>
```
`example.fs`
```f#
open Npgsql.FSharp
open System

let connString = "postgres://crate:crate@localhost:5432/?sslmode=disable";

type Record = {
    mountain: string
    height: int
}

[<EntryPoint>]
let main args =
    let results = ResizeArray()

    // Connect to database.
    connString
    |> Sql.connect

    // Invoke basic query.
    |> Sql.query "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3"
    |> Sql.execute (fun read ->
        {
            mountain = read.text "mountain"
            height = read.int "height"
        })
    |> results.Add

    // Display results.
    printfn "%A" results

    // Exit program successfully.
    0
```

:::{include} ../_cratedb.md
:::
```shell
export DOTNET_CLI_TELEMETRY_OPTOUT=true
dotnet run
```

:::{rubric} SSL connection
:::

Use the `Sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```f#
let connString = "postgres://admin:password@testcluster.cratedb.net:5432/?sslmode=require";
```

## See also

:::{div}
- [Connection Strings in ADO.NET]
- [ADO.NET Overview]
:::


[Npgsql]: https://www.npgsql.org/
[Npgsql.FSharp]: https://github.com/Zaid-Ajaj/Npgsql.FSharp
