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
```text
// swift-tools-version: 5.8
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "CrateDbDemo",
    dependencies: [
        .package(url: "https://github.com/vapor/postgres-kit.git", from: "2.0.0")
    ],
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products from dependencies.
        .executableTarget(
            name: "CrateDbDemo",
            path: "Sources"),
    ]
)
```
`Sources/main.swift`
```swift
import PostgresKit

let configuration = SQLPostgresConfiguration(url: "postgres://crate:crate@localhost:5432")
let source = PostgresConnectionSource(configuration: configuration)
let pool = EventLoopGroupConnectionPool(
    source: source,
    maxConnectionsPerEventLoop: 2,
    on: MultiThreadedEventLoopGroup.singleton
)
defer { pool.shutdown() }

let db = pool.database(logger: .init(label: "test")).sql()
let rows = try db.raw("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 10;").all().wait()
print(rows)
```


[postgres-kit]: https://swiftpackageindex.com/vapor/postgres-kit
