:::{include} /_include/links.md
:::

(connect-visualbasic)=
# Visual Basic

:::{div} sd-text-muted
Connect to CrateDB from Visual Basic .NET applications.
:::

:::{rubric} About
:::

[Npgsql] is an open source ADO\.NET Data Provider for PostgreSQL, for programs
written in C#, F#, or Visual Basic.

:::{rubric} Synopsis
:::

`example.vbproj`
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
`example.vb`
```visualbasic
Imports Npgsql
Imports System

Module Example

    Public Sub Main(args As String())
        Dim cs As String
        Dim cn As NpgsqlConnection
        Dim dr As NpgsqlDataReader

        'Connect to database.
        cs = "Host=localhost;Port=5432;Username=crate;Password=crate;Database=doc;Sslmode=disable"
        cn = New NpgsqlConnection(cs)
        cn.Open()

        'Invoke basic query.
        Dim sSQL = "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3"
        Dim cmd As New NpgsqlCommand(sSQL, cn)

        'Display results.
        dr = cmd.ExecuteReader()
        Do While dr.Read()
            Console.WriteLine(dr.GetString(0) & ": " & dr.GetInt32(1))
        Loop

        'Clean up.
        dr.Close()
        cn.Close()
    End Sub

End Module
```

:::{include} ../_cratedb.md
:::
```shell
export DOTNET_CLI_TELEMETRY_OPTOUT=true
dotnet run
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use `Sslmode=require`, and
replace hostname, username, and password with values matching
your environment.
```visualbasic
cs = "Host=testcluster.cratedb.net;Port=5432;Username=admin;Password=password;Database=doc;Sslmode=require"
```

## See also

:::{div}
- [Connection Strings in ADO.NET]
- [ADO.NET Overview]
:::


[Npgsql]: https://www.npgsql.org/
[Npgsql.FSharp]: https://github.com/Zaid-Ajaj/Npgsql.FSharp
