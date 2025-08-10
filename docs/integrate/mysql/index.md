(mysql)=
(mariadb)=
# MySQL and MariaDB

```{div} .float-right
[![mysql-logo](https://www.mysql.com/common/logos/powered-by-mysql-167x86.png){height=60px loading=lazy}](https://www.mysql.com/)
[![mariadb-logo](https://mariadb.com/wp-content/themes/mariadb-2025/public/images/logo-dark.4482a1.svg){height=60px loading=lazy}](https://www.mariadb.com/)
```
```{div} .clearfix
```

:::{include} /_include/links.md
:::

:::{rubric} About
:::

[MySQL] and [MariaDB] are well-known free and open-source relational database
management systems (RDBMS), available as standalone and managed variants.

:::{dropdown} **Details**
MySQL is a component of the LAMP web application software stack (and others),
which is an acronym for Linux, Apache, MySQL, Perl/PHP/Python.

When Oracle acquired Sun in 2010, Monty Widenius, MySQL's founder, forked the
open-source MySQL project to create MariaDB.
:::

:::{rubric} Synopsis
:::

```shell
uvx 'cratedb-toolkit[io-ingestr]' load table \
  "mysql://<username>:<password>@host:port/dbname?table=demo" \
  --cluster-url="crate://crate:crate@localhost:4200/testdrive/mysql_demo"
```

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Ingestr Table Loader
:link: https://cratedb-toolkit.readthedocs.io/io/ingestr/#mysql-to-cratedb
:link-type: url
Load MySQL table into CrateDB.
:::

:::{grid-item-card} Export/Import using CSV
:link: mysql-import-csv
:link-type: ref
Manually export CSV from MySQL, and import into CrateDB.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
import-csv
:::


[MariaDB]: https://mariadb.com/
[MySQL]: https://www.mysql.com/
