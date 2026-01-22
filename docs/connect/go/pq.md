:::{include} /_include/links.md
:::

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
    connStr := "postgresql://crate:crate@localhost:5432/?sslmode=disable"
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

:::{rubric} SSL connection
:::

:::{div}
Use the `sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to [CrateDB Cloud].
:::

```go
connStr := "postgresql://admin:password@testcluster.cratedb.net:5432/?sslmode=require"
```

:::{rubric} Example
:::

Create the file `example.go` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
```shell
go mod init github.com/cratedb-guide/connect/go/pq
go mod tidy
go run example.go
```


[pq]: https://github.com/lib/pq
