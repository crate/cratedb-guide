(connect-r)=

# R

:::{div} sd-text-muted
Connect to CrateDB from R applications and notebooks.
:::

:::{rubric} About
:::

The [RPostgres] package is the canonical C++ Interface to PostgreSQL.
An alternative is the [RPostgreSQL] package, written in C.
RPostgres is actively maintained and often preferred.

:::{rubric} Synopsis
:::

```r
# RPostgres: C++ Interface to PostgreSQL
# https://cran.r-project.org/web/packages/RPostgres/

# Optionally install the PostgreSQL library on demand.
if (!requireNamespace("RPostgres", quietly = TRUE)) {
    install.packages("RPostgres", repos="https://cran.r-project.org")
}

# Load the DBI and PostgreSQL libraries.
library(DBI)
library(RPostgres)

# Open a database connection, where `dbname` is the name of the CrateDB schema.
conn <- dbConnect(RPostgres::Postgres(),
                  host = "localhost",
                  port = 5432,
                  sslmode = "disable",
                  user = "crate",
                  password = "crate",
                  dbname = "testdrive",
                  )
on.exit(DBI::dbDisconnect(conn), add = TRUE)

# Invoke a basic select query.
res <- dbGetQuery(conn, "SELECT * FROM sys.summits ORDER BY height DESC LIMIT 10;")
print(res)
```

:::{note}
**⚠️ Security note:** The example uses hardcoded credentials and disables SSL
for simplicity. In production, use environment variables or secrets management
(e.g., `.Renviron`, keyvault) and enable TLS verification
(`sslmode="verify-full"` or `"require"`).
:::

## Example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/r
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using R.
+++
Demonstrates basic examples that use the R RPostgres and RPostgreSQL packages.
:::

[![R](https://github.com/crate/cratedb-examples/actions/workflows/lang-r.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-r.yml)


[RPostgres]: https://cran.r-project.org/web/packages/RPostgres/
[RPostgreSQL]: https://cran.r-project.org/web/packages/RPostgreSQL/
