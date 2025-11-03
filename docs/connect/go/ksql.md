(go-ksql)=
# KSQL

:::{rubric} About
:::

[KSQL] is a simple and powerful Golang SQL library based on
`pgx` and `database/sql`.

:::{rubric} Features
:::

- Support for all common relational databases: `mysql`, `sqlite`, `sqlserver`, `postgresql`, `cratedb`
- Generic and powerful functions for Querying and Scanning data into structs
- Works on top of existing battle-tested libraries such as `database/sql` and `pgx`
- Helper functions for everyday operations, namely: Insert, Patch and Delete
- Supports `sql.Scanner` and `sql.Valuer` and also all `pgx` special types (when using `kpgx`)
- Every operation returns errors a single time, so its easier to handle them

... and many more.

:::{rubric} Synopsis
:::

`example.go`
```go
package main

import (
    "context"
    "fmt"
    "log"

    "github.com/vingarcia/ksql"
    "github.com/vingarcia/ksql/adapters/kpgx"
)

var SummitsTable = ksql.NewTable("summits")

type Summit struct {
    Mountain  string  `ksql:"mountain"`
    Region    string  `ksql:"region"`
    Height    int     `ksql:"height"`
    Latitude  float32 `ksql:"latitude"`
    Longitude float32 `ksql:"longitude"`
}

func main() {
    ctx := context.Background()

    // Connect to database.
    dbURL := "postgresql://crate:crate@localhost:5432/?sslmode=disable"
    db, err := kpgx.New(ctx, dbURL, ksql.Config{})
    if err != nil {
        log.Fatalf("unable connect to database: %s", err)
    }
    defer db.Close()

    // Invoke query.
    var rows []Summit
    db.Query(ctx, &rows, `
        SELECT
            mountain, region, height,
            LATITUDE(coordinates) AS latitude,
            LONGITUDE(coordinates) AS longitude
        FROM sys.summits
        ORDER BY height DESC
        LIMIT 5`)

    // Display results.
    for _, row := range rows {
        fmt.Printf("- %#v\n", row)
    }
}
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use `sslmode=require`, and
replace username, password, and hostname with values matching
your environment.
```go
dbURL := "postgresql://admin:password@testcluster.cratedb.net:5432/?sslmode=require"
```

:::{rubric} Quickstart example
:::

Create the file `example.go` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
```shell
go mod init github.com/cratedb-guide/connect/go/ksql
go mod tidy
go run example.go
```


[KSQL]: https://github.com/VinGarcia/ksql
