(go-pgx)=
# pgx

:::{div} .float-right .text-right
[![Go pgx CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-go-pgx.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-go-pgx.yml)
:::
:::{div} .clearfix
:::

:::{rubric} About
:::

[pgx] is a pure Go driver and toolkit for PostgreSQL.

:::{rubric} Features
:::

- Support for approximately 70 different PostgreSQL types
- Connection pool with after-connect hook for arbitrary connection setup
- Adapter for Go's standard `database/sql` interface
- Automatic statement preparation and caching
- Single-round trip query mode
- Full TLS connection control
- Tracing and logging support
- Batch queries

... and many more.

:::{rubric} Synopsis
:::

`example.go`
```go
package main

import (
    "context"
    "fmt"

    "github.com/jackc/pgx/v5"
)

func main() {
    ctx := context.Background()

    // Connect to database.
    conn, _ := pgx.Connect(ctx, "postgresql://crate:crate@localhost:5432/?sslmode=disable")
    defer conn.Close(ctx)

    // Invoke basic query.
    rows, _ := conn.Query(ctx, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")
    defer rows.Close(ctx)

    // Display results.
    for rows.Next() {
        var mountain string
        var height int
        rows.Scan(&mountain, &height)
        fmt.Println(mountain, height)
    }
}
```

:::{rubric} SSL connection
:::

Use the `sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```go
conn, _ := pgx.Connect(ctx, "postgresql://admin:password@testcluster.cratedb.net:5432/?sslmode=require")
```

:::{rubric} Quickstart example
:::

Create the file `example.go` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
```shell
go mod init github.com/cratedb-guide/connect/go/pgx
go mod tidy
go run example.go
```

:::{rubric} Full example
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/go-pgx
:link-type: url
{material-regular}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using Go.
+++
Demonstrates basic examples and bulk insert operations using the pgx driver.
:::


[pgx]: https://github.com/jackc/pgx
