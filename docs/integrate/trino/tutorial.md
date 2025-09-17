(trino-tutorial)=
# Connecting to CrateDB in Trino

[Trino](https://trino.io/) is a distributed SQL query engine. This tutorial shows how to configure Trino to connect to CrateDB.

## Prerequisites

Assume you have a Trino client/server installation as per the [installation instructions](https://trino.io/docs/current/installation.html).

For example, on macOS you can `brew install trino`. Start the server with `trino-server run` from your installation’s `bin` directory. Depending on your installation, the command and paths may differ.

## Connector configuration

Because CrateDB speaks the PostgreSQL wire protocol, you can use
[Trino’s PostgreSQL connector]. Create a catalog properties file
to configure the connection:

```ini
connector.name=postgresql
connection-url=jdbc:postgresql://<CrateDB hostname>:5432/
connection-user=<CrateDB username>
connection-password=<CrateDB password>
insert.non-transactional-insert.enabled=true
```

Replace the placeholders for the CrateDB hostname, username, and password. Besides the connection details, note two specifics:

* No database name: CrateDB provides a single database with multiple schemas, so omit the database name in `connection-url`. Specifying a database triggers errors for operations that include `catalog.schema.table` (e.g., `ERROR: Table with more than 2 QualifiedName parts is not supported. Only <schema>.<tableName> works`).
* Non‑transactional inserts: CrateDB doesn’t support transactions. By default, the PostgreSQL connector wraps `INSERT` statements in a transaction and uses a temporary table. Disable this with `insert.non-transactional-insert.enabled=true`.

## Running queries against CrateDB

After configuring the connector, connect to the Trino server using its CLI:

```bash
# schema refers to an existing CrateDB schema
$ ./bin/trino --catalog postgresql --schema doc
trino:doc>
```

Run `SHOW TABLES` to list all tables in the specified CrateDB schema, then query them.

Because CrateDB speaks the PostgreSQL wire protocol, use Trino’s [PostgreSQL connector](https://trino.io/docs/current/connector/postgresql.html). Create a catalog file, for example:

- macOS (Homebrew): `/usr/local/etc/trino/catalog/postgresql.properties` (or `/opt/homebrew/etc/trino/catalog/...` on Apple Silicon)
- Linux (tarball/systemd): `$TRINO_HOME/etc/catalog/postgresql.properties` or `/etc/trino/catalog/postgresql.properties`

* Querying `OBJECT` columns: Columns of the data type `OBJECT` can usually be queried using the bracket notation e.g., `SELECT my_object_column['my_object_key'] FROM my_table`. In Trino’s SQL dialect, the identifier needs to be wrapped in double quotes, such as `SELECT "my_object_column['my_object_key']" FROM my_table`.
* `INSERT` queries: When inserting, Trino addresses tables with `catalog_name.schema_name.table_name`, which currently isn't supported by CrateDB. Please see [crate/crate#12658](https://github.com/crate/crate/issues/12658) on addressing this issue.
* Data types: Not all of Trino’s [data types](https://trino.io/docs/current/language/types.html) can be mapped to CrateDB data types and vice versa.
  * For creating tables, it can be advisable to run the `CREATE TABLE` statement directly in CrateDB. This approach is also recommended if you want to configure custom table settings, such as sharding, partitioning, or replication.
  * For querying tables, a strategy can be to create views preparing data in a Trino-compatible way. For example, when dealing with the `GEO_POINT` data type, using the functions `LONGITUDE` and `LATITUDE`, splitting `GEO_POINT` into two simple, numerical values.
  * Columns with data types that cannot be mapped are skipped by Trino when importing metadata. This means that such columns cannot be queried through Trino. Creating a view can be a workaround (see the previous bullet point).
* There are [limitations in Trino](https://trino.io/docs/current/optimizer/pushdown.html) on what parts of a query are pushed down to the data source. Therefore, the performance of a query can decrease significantly when running it through Trino compared to running it on CrateDB directly.

## Conclusion

With a few parameter tweaks, Trino connects to CrateDB. This guide reflects a
short compatibility test and is not exhaustive. If you discover additional
aspects, please let us know.


[Trino’s PostgreSQL connector]: https://trino.io/docs/current/connector/postgresql.html
