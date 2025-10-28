(odbc)=
(connect-odbc)=

# ODBC

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Connect to CrateDB with ODBC.
:::

:::{div}
Open Database Connectivity ([ODBC]) is a standard application programming
interface (API) for accessing database management systems (DBMS),
conceived to be independent of database systems and operating systems.
The application uses ODBC functions through an _ODBC driver manager_ and
addresses the driver and database using a _Data Source Name (DSN)_.
:::

## Installation

:::{include} /connect/odbc/install.md
:::

## Configuration

:::{include} /connect/odbc/configure.md
:::

## Examples

A few examples to demonstrate CrateDB connectivity with ODBC.

### C#

Use the ODBC .NET Data Provider to access data from your C Sharp ADO\.NET
applications. The [.NET Framework Data Provider for ODBC] is available
through the [System.Data.Odbc] namespace.

```c#
using System.Data.Odbc;

// Connect to database
string connection_string = "ODBC;Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate;Database=doc;MaxVarcharSize=1073741824";
OdbcConnection connection = new OdbcConnection(connection_string);
connection.Open();

// Invoke query
OdbcCommand command = new OdbcCommand("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 5", connection);
OdbcDataReader reader = command.ExecuteReader();

// Display results
while(reader.Read())
{
  String mountain = reader.GetString(0);
  int height = reader.GetInt32(1);
  Console.Write(mountain + ": " + height);
  Console.WriteLine();
}

// Clean up
reader.Close();
command.Dispose();
connection.Close();
```

### Erlang

The [Erlang ODBC application] provides an interface to communicate
with relational SQL-databases out of the box.

```erlang
odbc:start(),
{ok, Ref} = odbc:connect("Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate", []),
io:fwrite("~p~n", [odbc:sql_query(Ref, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")]),
```

:::{todo}
Enable with the [Erlang patch](https://github.com/crate/cratedb-guide/pull/420).
```
- {ref}`connect-erlang`
```
:::

### Python (pyodbc)

[pyodbc] is an open-source Python module that makes accessing ODBC databases
simple. It implements the DB API 2.0 specification and adds other Pythonic
convenience. For more information, please visit the
[pyodbc installation instructions] and [connecting to PostgreSQL with pyodbc].

```shell
pip install --upgrade pyodbc
```
```python
import pyodbc

# Connect to database
connection_string = \
    "Driver={PostgreSQL Unicode};Server=localhost;Port=5432;" \
    "Uid=crate;Pwd=crate;Database=doc;MaxVarcharSize=1073741824"
connection = pyodbc.connect(connection_string)

# Invoke query
cursor = connection.cursor()
cursor.execute("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 5")

# Display results
for row in cursor:
    print(row)

# Clean up
cursor.close()
connection.close()
```

### Python (turbodbc)

[turbodbc] is a Python module to access relational databases via the Open
Database Connectivity (ODBC) interface. turbodbc offers built-in NumPy and
Apache Arrow for maximum performance.

```shell
pip install --upgrade turbodbc
```
```python
import turbodbc

# Connect to database
connection_string = \
    "Driver={PostgreSQL Unicode};Server=localhost;Port=5432;" \
    "Uid=crate;Pwd=crate;Database=doc;MaxVarcharSize=1073741824"
connection = turbodbc.connect(connection_string)

# Invoke query
cursor = connection.cursor()
cursor.execute("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 5")

# Display results
for row in cursor:
    print(row)

# Clean up
cursor.close()
connection.close()
```

:::{todo}
Enable with the [Python patch](https://github.com/crate/cratedb-guide/pull/403).
```
- {ref}`Turbodbc -- a high-performance ODBC library <turbodbc>`
```
:::

### Visual Basic

:::{div}
See also [psqlODBC with Visual Basic]. Please navigate to the
[psqlODBC download site] to download and install the `psqlodbc`
driver for Windows systems.
:::

```visualbasic
Dim cn as New ADODB.Connection
Dim rs as New ADODB.Recordset

'Connect to database
cn.Open "Dsn=<MyDataSourceName>;" & _
        "Server=localhost;" & _
        "Port=5432;" & _
        "Uid=crate;" & _
        "Pwd=crate;" & _
        "Database=doc;" & _
        "MaxVarcharSize=1073741824;"

'Invoke query
rs.Open "SELECT * FROM sys.summits ORDER BY height DESC LIMIT 5", cn

'Display results
While Not rs.EOF
  Debug.Print rs!mountain & ": " & rs!height
  rs.MoveNext
Wend

'Clean up
rs.Close
cn.Close
```


[.NET Framework Data Provider for ODBC]: https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/data-providers#net-framework-data-provider-for-odbc
[connecting to PostgreSQL with pyodbc]: https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-PostgreSQL
[Erlang ODBC application]: https://www.erlang.org/docs/28/apps/odbc/odbc.html
[psqlODBC with Visual Basic]: https://odbc.postgresql.org/howto-vb.html
[pyodbc]: https://github.com/mkleehammer/pyodbc
[pyodbc installation instructions]: https://github.com/mkleehammer/pyodbc/wiki/Install
[System.Data.Odbc]: https://learn.microsoft.com/en-us/dotnet/api/system.data.odbc
[turbodbc]: https://turbodbc.readthedocs.io/
