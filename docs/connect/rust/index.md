(connect-rust)=

# Rust

:::{div} sd-text-muted
Connect to CrateDB from Rust applications.
:::

:::{rubric} About
:::

[postgres] is a synchronous Rust client for the PostgreSQL database.

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
```shell
cargo init
cargo add postgres postgres-native-tls native-tls
cargo run
```


## Example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/rust-postgres
:link-type: url
{material-outlined}`play_arrow;2em`
Connecting to CrateDB with Rust.
+++
Demonstrates a basic example program that uses the Rust postgres package.
:::

[![Rust](https://github.com/crate/cratedb-examples/actions/workflows/lang-rust-postgres.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-rust-postgres.yml)


[postgres]: https://crates.io/crates/postgres
