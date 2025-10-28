(odbc-csharp)=

# C#

Use the ODBC .NET Data Provider to access data from your C Sharp ADO\.NET
applications. The [.NET Framework Data Provider for ODBC] is available
through the [System.Data.Odbc] namespace.

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

```text
System.DllNotFoundException: Dependency unixODBC with minimum version 2.3.1 is required.
Unable to load shared library 'libodbc.2.dylib' or one of its dependencies. In order to help diagnose loading problems, consider setting the DYLD_PRINT_LIBRARIES environment variable: dlopen(liblibodbc.2.dylib, 0x0001): tried: 'liblibodbc.2.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OSliblibodbc.2.dylib' (no such file), '/usr/lib/liblibodbc.2.dylib' (no such file, not in dyld cache), 'liblibodbc.2.dylib' (no such file), '/usr/local/lib/liblibodbc.2.dylib' (no such file), '/usr/lib/liblibodbc.2.dylib' (no such file, not in dyld cache
```

```shell
sudo ln -s /usr/local/lib/libodbc.2.dylib /usr/local/share/dotnet/shared/Microsoft.NETCore.App/9.0.10/
```

```csharp
string connection_string = "Driver={PostgreSQL Unicode};Server=testcluster.cratedb.net;Port=5432;Sslmode=require;Uid=admin;Pwd=password";
```


[.NET Framework Data Provider for ODBC]: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/data-providers#net-framework-data-provider-for-odbc
[System.Data.Odbc]: https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc
