(connect-rust)=

# Rust

:::{div} .float-right .text-right
[![Rust](https://github.com/crate/cratedb-examples/actions/workflows/lang-rust-postgres.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-rust-postgres.yml)
:::
:::{div} .clearfix
:::

:::{div} sd-text-muted
Connect to CrateDB from Rust applications.
:::

:::{rubric} About
:::

[postgres] is a synchronous Rust client for the PostgreSQL database.
[r2d2] is a generic connection pool for Rust.

:::{rubric} Synopsis (localhost)
:::

`main.rs`
```rust
use postgres::{Client, NoTls};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = Client::connect("postgresql://crate@localhost:5432/?sslmode=disable", NoTls)?;

    for row in client.query(
        "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3",
        &[],
    )? {
        let mountain: &str = row.get(0);
        let height: i32 = row.get(1);
        println!("{}: {}", mountain, height);
    }
    Ok(())
}
```

:::{include} ../_cratedb.md
:::
```shell
cargo init
cargo add postgres
cargo run
```

:::{rubric} Synopsis (CrateDB Cloud)
:::
For CrateDB Cloud, add TLS support and update the connection string with
your cluster details.

`main.rs`
```rust
use postgres::Client;
use native_tls::TlsConnector;
use postgres_native_tls::MakeTlsConnector;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let tls = MakeTlsConnector::new(TlsConnector::new()?);
    let mut client = Client::connect("postgresql://crate:<password>@<cluster-name>.<region>.cratedb.net:5432/?sslmode=require", tls)?;

    for row in client.query(
        "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3",
        &[],
    )? {
        let mountain: &str = row.get(0);
        let height: i32 = row.get(1);
        println!("{}: {}", mountain, height);
    }
    Ok(())
}
```

:::{include} ../_cratedb.md
:::
```shell
cargo init
cargo add postgres postgres-native-tls native-tls
cargo run
```

:::{rubric} Synopsis (connection pool)
:::

`main.rs`
```rust
use postgres::{NoTls, Row};
use r2d2_postgres::{
    r2d2::{ManageConnection, Pool},
    PostgresConnectionManager,
};
fn main {
    let pg_manager = PostgresConnectionManager::new(
        "postgresql://crate:crate@localhost:5432/?sslmode=disable"
            .parse()
            .unwrap(),
        NoTls,
    );
    let pg_pool = Pool::builder()
        .max_size(5)
        .build(pg_manager)
        .expect("Postgres pool failed");
    let mut pg_conn = pg_pool.get().unwrap();
    let result = pg_conn.query("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3", &[]);
    let rows = result.unwrap().into_iter().collect::<Vec<Row>>();
    // TODO: Display results.
    Ok(())
}
```

:::{include} ../_cratedb.md
:::
```shell
cargo init
cargo add postgres r2d2
cargo run
```

## Example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/rust-postgres
:link-type: url
{material-regular}`play_arrow;2em`
Connecting to CrateDB with Rust.
+++
Demonstrates a basic example program that uses the Rust postgres package.
:::


[postgres]: https://crates.io/crates/postgres
[r2d2]: https://crates.io/crates/r2d2
