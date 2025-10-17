(connect-go)=

# Go

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Use pgx to connect to CrateDB from Go applications.
:::

:::{rubric} About
:::

[pgx] is a pure Go driver and toolkit for PostgreSQL.

:::{rubric} Synopsis
:::

```go
package main

import (
  "context"
  "fmt"
  "os"

  "github.com/jackc/pgx/v5"
)

func main() {


  ctx := context.Background()
  
  // urlExample := "postgres://username:password@localhost:5432/schema_name"
  conn, err := pgx.Connect(ctx, os.Getenv("CRATE_URL"))
  if err != nil {
    fmt.Fprintf(os.Stderr, "Unable to connect to database: %v\n", err)
    os.Exit(1)
  }
  defer conn.Close(context.Background())
 
  rows, err := conn.Query(ctx, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")
  if err != nil {
    fmt.Fprintf(os.Stderr, "Query failed: %v\n", err)
    os.Exit(1)
  }
  
  for rows.Next() {
    var mountain string
    var height int
    if err := rows.Scan(&mountain, &height); err != nil {
      fmt.Fprintf(os.Stderr, "Scan failed: %v\n", err)
      os.Exit(1)
    }
    fmt.Println(mountain, height)
  }
  if err := rows.Err(); err != nil {
    fmt.Fprintf(os.Stderr, "Rows error: %v\n", err)
    os.Exit(1)
  }
}
```


## Example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/go-pgx
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using Go.
+++
Demonstrates basic examples and bulk insert operations using the pgx driver.
:::

[![Go pgx](https://github.com/crate/cratedb-examples/actions/workflows/lang-go-pgx.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-go-pgx.yml)


[pgx]: https://github.com/jackc/pgx
