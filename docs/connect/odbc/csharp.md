(odbc-csharp)=

# ODBC with C#

:::{rubric} About
:::

Use the ODBC .NET Data Provider to access data from your C Sharp ADO\.NET
applications. The [.NET Framework Data Provider for ODBC] is available
through the [System.Data.Odbc] namespace.

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
    <PackageReference Include="System.Data.Odbc" Version="9.0.10" />
  </ItemGroup>

</Project>
```
`example.cs`
```c#
using System;
using System.Data.Odbc;

// Connect to database
string connection_string = "Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate;Database=crate;MaxVarcharSize=1073741824";
OdbcConnection connection = new OdbcConnection(connection_string);
connection.Open();

// Invoke query
OdbcCommand command = new OdbcCommand("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 5", connection);
OdbcDataReader reader = command.ExecuteReader();

// Display results
while (reader.Read())
    Console.WriteLine($"{reader.GetString(0)}: {reader.GetInt32(1)}");

// Clean up
reader.Close();
command.Dispose();
connection.Close();
```

:::{rubric} Example
:::

Create the files `example.csproj` and `example.cs` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
Invoke program.
```shell
dotnet run
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use the `Sslmode=require` parameter,
and replace username, password, and hostname with values matching
your environment.
```csharp
string connection_string = "Driver={PostgreSQL Unicode};Server=testcluster.cratedb.net;Port=5432;Sslmode=require;Uid=admin;Pwd=password";
```


[.NET Framework Data Provider for ODBC]: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/data-providers#net-framework-data-provider-for-odbc
[System.Data.Odbc]: https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc
