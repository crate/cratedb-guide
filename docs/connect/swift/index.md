(connect-swift)=

# Swift

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Connect to CrateDB from Swift applications.
:::

:::{rubric} About
:::

[postgres-kit] is a non-blocking, event-driven Swift client for PostgreSQL.

:::{rubric} Synopsis
:::

`Package.swift`
```swift
// swift-tools-version:6.0

import PackageDescription

let package = Package(
    name: "CrateDbDemo",
    dependencies: [
        .package(url: "https://github.com/vapor/postgres-kit.git", "2.0.0"..<"3.0.0")
    ],
    targets: [
        .executableTarget(
            name: "CrateDbDemo",
            dependencies: [.product(name: "PostgresKit", package: "postgres-kit")],
            path: "Sources"
            ),
    ]
)
```
`Sources/main.swift`
```swift
import PostgresKit

let configuration = try SQLPostgresConfiguration(url: "postgresql://crate:crate@localhost:5432/?tlsmode=disable")
let source = PostgresConnectionSource(sqlConfiguration: configuration)
let pool = EventLoopGroupConnectionPool(
    source: source,
    maxConnectionsPerEventLoop: 2,
    on: MultiThreadedEventLoopGroup.singleton
)
defer { pool.shutdown() }

let db = pool.database(logger: .init(label: "test")).sql()
let rows = try db.raw("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3;").all().wait()

struct Record: Codable {
    var mountain: String
    var region: String
    var height: Int
}

for row in rows {
    let record = try row.decode(model: Record.self)
    print("\(record.mountain): \(record.height)")
}
```

:::{include} ../_cratedb.md
:::
```shell
swift run
```

:::{rubric} SSL connection
:::

Use the `tlsmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```swift
let configuration = try SQLPostgresConfiguration(url: "postgresql://admin:password@testcluster.cratedb.net:5432/?tlsmode=require")
```


[postgres-kit]: https://swiftpackageindex.com/vapor/postgres-kit
