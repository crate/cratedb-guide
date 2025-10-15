(connect-rust)=

# Rust

:::{div} sd-text-muted
Connect to CrateDB from Rust applications.
:::

:::{rubric} About
:::

[postgres] is a synchronous Rust client for the PostgreSQL database.

:::{rubric} Synopsis
:::

```rust
use postgres::{Client, NoTls};

let mut client = Client::connect("host=localhost user=crate", NoTls)?;

for row in client.query("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3", &[])? {
    let mountain: &str = row.get(0);
    let height: i32 = row.get(1);

    println!("found mountain: {} {}", mountain, height);
}
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
