(go-pq)=
# pq

:::{rubric} About
:::

[pq] is a pure Go PostgreSQL driver for Go's `database/sql` package.

:::{rubric} Synopsis
:::

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
go mod init github.com/cratedb-guide/connect/go/pq
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


[pq]: https://github.com/lib/pq
