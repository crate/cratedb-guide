(connect-r)=

# R

:::{div} sd-text-muted
Connect to CrateDB from R applications and notebooks.
:::

:::{rubric} About
:::

[RPostgreSQL] is the canonical _R Interface to the 'PostgreSQL' Database System_.

:::{rubric} Synopsis
:::

```r
# Install driver on demand.
# RPostgreSQL: R Interface to the 'PostgreSQL' Database System
# https://cran.r-project.org/web/packages/RPostgreSQL/

# Optionally install the PostgreSQL library.
if (!requireNamespace("RPostgreSQL", quietly = TRUE)) {
    install.packages("RPostgreSQL", repos="https://cran.r-project.org")
}

# Load the DBI and PostgreSQL libraries.
library(DBI)
library(RPostgreSQL)
drv <- RPostgreSQL::PostgreSQL()

# Open a database connection, where `dbname` is the name of the CrateDB schema.
con <- dbConnect(drv,
                 host = "localhost",
                 port = 5432,
                 # For CrateDB Cloud:
                 # sslmode = "require",
                 user = "crate",
                 password = Sys.getenv("CRATEDB_PASSWORD"),
                 dbname = "testdrive"
                 )
on.exit(DBI::dbDisconnect(con), add = TRUE)

# Invoke a basic select query.
res <- dbGetQuery(con, "SELECT mountain, region, height FROM sys.summits ORDER BY height DESC LIMIT 3;")
print(res)
```

## Example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/r
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using R.
+++
Demonstrates a basic example that uses the R RPostgreSQL package.
:::

[![R](https://github.com/crate/cratedb-examples/actions/workflows/lang-r.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-r.yml)


[RPostgreSQL]: https://cran.r-project.org/web/packages/RPostgreSQL/
