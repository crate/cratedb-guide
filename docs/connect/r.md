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
if (!require(RPostgreSQL)) {
    install.packages("RPostgreSQL", repos="http://cran.us.r-project.org")
}
stopifnot(require(RPostgreSQL))

# Load the DBI library.
library(DBI)
drv <- dbDriver("PostgreSQL")

# Open a database connection, where `dbname` is the name of the CrateDB schema.
con <- dbConnect(drv,
                 host = "localhost",
                 port = 5432,
                 user = "crate",
                 dbname = "testdrive",
                 )

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
