(connect-go)=

# Go

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Use pgx to connect to CrateDB from Go applications.
:::

(go-pgx)=
## pgx

:::{rubric} About
:::

[pgx] is a pure Go driver and toolkit for PostgreSQL.

:::{rubric} Synopsis
:::

`go.mod`
```text
module github.com/cratedb-guide/connect/go/pgx
require github.com/jackc/pgx/v5 v5.7.6
```
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
    conn, _ := pgx.Connect(ctx, "postgresql://crate:crate@localhost:5432/doc?sslmode=disable")
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

:::{include} ../_cratedb.md
:::
```shell
go mod tidy
go run example.go
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use `sslmode=require`, and
replace username, password, and hostname with values matching
your environment.
```go
conn, _ := pgx.Connect(ctx, "postgresql://admin:password@testcluster.cratedb.net:5432/doc?sslmode=require")
```

:::{rubric} Example
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/go-pgx
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using Go.
+++
Demonstrates basic examples and bulk insert operations using the pgx driver.
:::

[![Go pgx CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-go-pgx.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-go-pgx.yml)


(go-pq)=
## pq

:::{rubric} About
:::

[pq] is a pure Go PostgreSQL driver for Go's database/sql package.

:::{rubric} Synopsis
:::

`go.mod`
```text
module github.com/cratedb-guide/connect/go/pq
require github.com/lib/pq v1.10.9
```
`example.go`
```go
package main

import (
    "database/sql"
    "fmt"

    _ "github.com/lib/pq"
)

func main() {

    // Connect to database.
    connStr := "postgresql://crate:crate@localhost:5432/doc?sslmode=disable"
    db, _ := sql.Open("postgres", connStr)
    defer db.Close()

    // Invoke basic query.
    rows, _ := db.Query("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")
    defer rows.Close()

    // Display results.
    for rows.Next() {
        var mountain string
        var height int
        rows.Scan(&mountain, &height)
        fmt.Println(mountain, height)
    }
}
```

:::{include} ../_cratedb.md
:::
```shell
go mod tidy
go run example.go
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use `sslmode=require`, and
replace username, password, and hostname with values matching
your environment.
```go
connStr := "postgresql://admin:password@testcluster.cratedb.net:5432/doc?sslmode=require"
```


[pgx]: https://github.com/jackc/pgx
[pq]: https://github.com/lib/pq
