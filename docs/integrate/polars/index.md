(polars)=
# Polars

```{div}
:style: "float: right; margin-left: 0.5em"
[![Polars logo](https://github.com/pola-rs/polars-static/raw/master/logos/polars-logo-dark.svg){w=180px}][Polars]
```
```{div} .clearfix
```

:::{rubric} About
:::

[Polars] is a blazingly fast DataFrames library with language bindings for
Rust, Python, Node.js, R, and SQL. Polars is powered by a multithreaded,
vectorized query engine, it is open source, and written in Rust.

- **Fast:** Written from scratch in Rust and with performance in mind,
  designed close to the machine, and without external dependencies.

- **I/O:** First class support for all common data storage layers: local,
  cloud storage & databases.

- **Intuitive API:** Write your queries the way they were intended. Polars,
  internally, will determine the most efficient way to execute using its query
  optimizer. Polars' expressions are intuitive and empower you to write
  readable and performant code at the same time.

- **Out of Core:** The streaming API allows you to process your results without
  requiring all your data to be in memory at the same time.

- **Parallel:** Polars' multi-threaded query engine utilises the power of your
  machine by dividing the workload among the available CPU cores without any
  additional configuration.

- **Vectorized Query Engine:** Uses [Apache Arrow], a columnar data format, to
  process your queries in a vectorized manner and SIMD to optimize CPU usage.
  This enables cache-coherent algorithms and high performance on modern processors. 

- **Open Source:** Polars is and always will be open source. Driven by an active
  community of developers. Everyone is encouraged to add new features and contribute.
  It is free to use under the MIT license.

:::{rubric} Data formats
:::

Polars supports reading and writing to many common data formats.
This allows you to easily integrate Polars into your existing data stack.
 
- Text: CSV & JSON
- Binary: Parquet, Delta Lake, AVRO & Excel
- IPC: Feather, Arrow
- Databases: MySQL, Postgres, SQL Server, Sqlite, Redshift & Oracle
- Cloud Storage: S3, Azure Blob & Azure File


:::{rubric} Learn
:::
- [Polars code examples]


[Polars]: https://pola.rs/
[Polars code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/polars
