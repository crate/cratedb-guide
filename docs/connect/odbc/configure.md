---
orphan: true
---

For connecting to CrateDB, either address the database using a named
connection (DSN), e.g. using `Dsn=CrateDB`, or address it directly
using the driver, like `Driver={PostgreSQL Unicode}`.

:::{rubric} DSN configuration
:::

For connecting to the database using a DSN,
a typical connection string for CrateDB is:
```text
Dsn=CrateDB
```

:::::{tab-set}

::::{tab-item} Windows
On Windows, you will create a DSN using the ODBC driver manager UI.
To set up a DSN (Data Source Name), click the "System DSN" tab. Click "Add".
Select "PostgreSQL Unicode" and click "Finish".
The [illustrated walkthrough][Installing PostgreSQL ODBC drivers on Windows]
also covers that part.
::::

::::{tab-item} Linux and macOS
With unixODBC, configure a DSN within an `.odbc.ini` or `/etc/odbc.ini`
file.

`~/.odbc.ini` 
```ini
[CrateDB]
Description=CrateDB
Driver=PostgreSQL Unicode
Server=localhost
Port=5432
Uid=crate
Pwd=crate
MaxVarcharSize=1073741824
```

::::

:::::


:::{rubric} DSN-less configuration
:::

For directly connecting using a driver, without a registered DSN,
a typical connection string for CrateDB is:
```text
Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate;MaxVarcharSize=1073741824
```
