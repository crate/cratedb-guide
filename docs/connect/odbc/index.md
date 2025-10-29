(odbc)=
(connect-odbc)=

# ODBC

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Connect to CrateDB with ODBC.
:::

:::{div}
Open Database Connectivity ([ODBC][ODBC definition]) is a standard application programming
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

A few examples that demonstrate CrateDB connectivity with ODBC.

:::{toctree}
:maxdepth: 1

C# <csharp>
Erlang <erlang>
Python <python>
Visual Basic <visualbasic>
:::


[ODBC definition]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
