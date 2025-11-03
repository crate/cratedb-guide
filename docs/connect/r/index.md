(connect-r)=

# R

:::{div} .float-right .text-right
[![R](https://github.com/crate/cratedb-examples/actions/workflows/lang-r.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-r.yml)
:::
:::{div} .clearfix
:::

:::{div} sd-text-muted
Connect to CrateDB from R applications and notebooks.
:::

:::{rubric} About
:::

The [RPostgres] package is the canonical C++ Interface to PostgreSQL,
which is actively maintained and often preferred.
An alternative is the [RPostgreSQL] package, written in C.

:::{rubric} Synopsis
:::

`example.r`
```r
# Connect to CrateDB from R, using the "RPostgres: C++ Interface to PostgreSQL".
# https://cran.r-project.org/web/packages/RPostgres/

# Install the Postgres library on demand.
if (!requireNamespace("RPostgres", quietly = TRUE)) {
    install.packages("RPostgres", repos="https://cran.r-project.org")
}

# Load the DBI and Postgres libraries.
library(DBI)
library(RPostgres)

# Connect to database.
conn <- dbConnect(RPostgres::Postgres(),
                  host = "localhost",
                  port = 5432,
                  sslmode = "disable",
                  user = "crate",
                  password = "crate",
                  dbname = "doc"
                  )
on.exit(DBI::dbDisconnect(conn), add = TRUE)

# Invoke a basic select query.
res <- dbGetQuery(conn, "SELECT * FROM sys.summits ORDER BY height DESC LIMIT 10;")
print(res)
```

:::{rubric} SSL connection
:::

Use `sslmode = "require"`, and
replace hostname, username, and password with values matching
your environment.

Also use this variant to connect to CrateDB Cloud.
```r
conn <- dbConnect(RPostgres::Postgres(),
                  host = "testcluster.cratedb.net",
                  port = 5432,
                  sslmode = "require",
                  user = "admin",
                  password = "password",
                  dbname = "doc"
                  )
```

:::{rubric} Quickstart example
:::

Create the file `example.r` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
```shell
Rscript example.r
```

:::{rubric} Full example
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/r
:link-type: url
{material-regular}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using R.
+++
Demonstrates basic examples that use the R RPostgres and RPostgreSQL packages.
:::


[RPostgres]: https://cran.r-project.org/web/packages/RPostgres/
[RPostgreSQL]: https://cran.r-project.org/web/packages/RPostgreSQL/
