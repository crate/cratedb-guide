---
orphan: true
---

While Windows typically includes an ODBC driver manager, you can
install the [unixODBC] driver manager on Linux and macOS systems.
The PostgreSQL ODBC driver is called [psqlODBC].

:::::{tab-set}

::::{tab-item} Windows
On Windows, download the latest 64-bit driver (MSI file)
from the [psqlODBC download site] and install it.
[Installing PostgreSQL ODBC drivers on Windows] includes an illustrated walkthrough.
::::

::::{tab-item} Linux
On Linux, install the [unixODBC] ODBC driver manager
and the psqlODBC driver.
[Installing PostgreSQL ODBC drivers on Linux] includes an illustrated walkthrough.

Arch Linux
```shell
pacman -Sy psqlodbc
```
Debian and derivatives
```shell
apt install --yes odbc-postgresql odbcinst unixodbc
```
Red Hat and derivatives
```shell
yum install -y postgresql-odbc
```

Verify installation.
```shell
odbcinst -q -d
```
```
[PostgreSQL ANSI]
[PostgreSQL Unicode]
```
::::

::::{tab-item} macOS
On macOS, install the [unixODBC] ODBC driver manager
and the psqlODBC driver, then register it.

```shell
# macOS
brew install psqlodbc unixodbc
```
`odbcinst.ini`
```ini
[PostgreSQL Unicode]
Description     = PostgreSQL ODBC driver (Unicode version)
Driver          = /usr/local/lib/psqlodbcw.so
```
```shell
odbcinst -i -d -f odbcinst.ini
```
Verify installation.
```shell
odbcinst -q -d
```
```
[PostgreSQL Unicode]
```
::::

:::::


[Installing PostgreSQL ODBC drivers on Linux]: https://www.dbi-services.com/blog/installing-the-odbc-drivers-for-postgresql/
[Installing PostgreSQL ODBC drivers on Windows]: https://help.campbellsci.com/PC400%20Manual/viewpro/installing_postgresql_odbc_drivers.htm
