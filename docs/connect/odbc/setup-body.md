---
orphan: true
---

:::{rubric} Prerequisites
:::

While Windows OS typically includes an ODBC driver manager, you can
install the [unixODBC] driver manager on Linux and macOS systems.
The PostgreSQL ODBC driver is called [psqlODBC].

:Windows:

  On Windows, download the latest 64-bit driver installer
  (MSI file) from the [psqlODBC download site] and invoke it.
  [Installing PostgreSQL ODBC Drivers] includes a walkthrough
  including screenshots.

:Linux and macOS:

  On Linux and macOS, install the [unixODBC] ODBC driver manager,
  then install and register psqlODBC.

`odbcinst.ini`
```ini
[PostgreSQL ODBC]
Description     = ODBC Driver for PostgreSQL

# Linux Arch
# pacman -Sy psqlodbc
# Driver          = /usr/lib/psqlodbcw.so

# Linux Debian
# apt install --yes odbc-postgresql odbcinst unixodbc
# Driver          = /usr/lib/x86_64-linux-gnu/odbc/psqlodbcw.so

# Linux Red Hat
# yum install -y postgresql-odbc
# Driver          = /usr/lib64/psqlodbcw.so

# Linux Generic
# Driver          = /usr/lib64/libodbcpsql.so
# Setup           = /usr/lib64/libodbcpsqlS.so

# macOS
# brew install psqlodbc unixodbc
Driver          = /usr/local/lib/psqlodbcw.so
```
Before registering the driver, enable the `Driver` line matching your system.
```shell
odbcinst -i -d -f odbcinst.ini
```

:::{rubric} DSN-less configuration
:::

A typical connection string for CrateDB is:

```text
ODBC;Driver={PostgreSQL ODBC};Server=localhost;Port=5432;Uid=crate;Pwd=crate;MaxVarcharSize=1073741824
```

For some drivers, you will need to omit the `ODBC;` prefix.


[Installing PostgreSQL ODBC Drivers]: https://help.campbellsci.com/PC400%20Manual/viewpro/installing_postgresql_odbc_drivers.htm
