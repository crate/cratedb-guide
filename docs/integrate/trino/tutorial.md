(trino-tutorial)=
# Connecting to CrateDB in Trino

[Trino](https://trino.io/) (formerly known as Presto SQL) is a distributed query engine, that allows running analytical queries across different data sources via SQL. One of those data sources can be CrateDB and this article is going to look at how to configure the connection.

## Prerequisites

We assume a Trino client/server installation is already in place as per [Trino’s installation instructions](https://trino.io/docs/current/installation.html).

For this post, I installed Trino on macOS using Homebrew with `brew install trino` and my installation directory is `/usr/local/Cellar/trino/375`. Depending on your installation method, there might be different ways to start the Trino server. For the sake of this post, I start it in my console from the installation directory with the command `./bin/trino-server run`. Your preferred way of starting might differ.

## Connector configuration

Due to CrateDB’s PostgreSQL protocol compatibility, we can make use of Trino’s [PostgreSQL connector](https://trino.io/docs/current/connector/postgresql.html). Create a new file `/usr/local/Cellar/trino/375/libexec/etc/catalog/postgresql.properties` to configure the connection:

```
connector.name=postgresql
connection-url=jdbc:postgresql://<CrateDB hostname>:5432/
connection-user=<CrateDB username>
connection-password=<CrateDB password>
insert.non-transactional-insert.enabled=true
```

Please replace the placeholders for the CrateDB hostname, username, and password to match your setup. Besides the connection details, the configuration has two particularities:

* No database name: With PostgreSQL, a JDBC connection URL usually ends with a database name. We intentionally omit the database name when connecting to CrateDB for compatibility reasons.
CrateDB consists of a single database with multiple schemas, hence we do not specify a database name in the `connection-url`. If a database name is specified, you will run into an error message on certain operations (`ERROR: Table with more than 2 QualifiedName parts is not supported. Only <schema>.<tableName> works`).
* Disabling transactions: Being a database with eventual consistency, CrateDB doesn’t support transactions. By default, the PostgreSQL connector will wrap `INSERT` queries into transactions and attempt to create a temporary table. We disable this behavior with the `insert.non-transactional-insert.enabled` parameter.

## Running queries against CrateDB

Once the PostgreSQL connector is configured, we can connect to the Trino server using its CLI:

```bash
# schema refers to an existing CrateDB schema
$ ./bin/trino --catalog postgresql --schema doc
trino:doc>
```

A `SHOW TABLES` query should successfully list all existing tables in the specified CrateDB schema and you can proceed with querying them.

As CrateDB differs in some aspects from PostgreSQL, there are a few particularities to consider for your queries:

* Querying `OBJECT` columns: Columns of the data type `OBJECT` can usually be queried using the bracket notation, e.g. `SELECT my_object_column['my_object_key'] FROM my_table`. In Trino’s SQL dialect, the identifier needs to be wrapped in double quotes, such as `SELECT "my_object_column['my_object_key']" FROM my_table`.
* `INSERT` queries: When inserting, Trino addresses tables with `catalog_name.schema_name.table_name`, which currently isn't supported by CrateDB. Please see [crate/crate#12658](https://github.com/crate/crate/issues/12658) on addressing this issue.
* Data types: Not all of Trino’s [data types](https://trino.io/docs/current/language/types.html) can be mapped to CrateDB data types and vice versa.
  * For creating tables, it can be advisable to run the `CREATE TABLE` statement directly in CrateDB. This approach is also recommended if you want to configure custom table settings, such as sharding, partitioning, or replication.
  * For querying tables, a strategy can be to create views preparing data in a Trino-compatible way. For example, when dealing with the `GEO_POINT` data type, using the functions `LONGITUDE` and `LATITUDE`, splitting `GEO_POINT` into two simple, numerical values.
  * Columns with data types that cannot be mapped are skipped by Trino when importing metadata. This means that such columns cannot be queried through Trino. Creating a view can be a workaround (see the previous bullet point).
* There are [limitations in Trino](https://trino.io/docs/current/optimizer/pushdown.html) on what parts of a query are pushed down to the data source. Therefore, the performance of a query can decrease significantly when running it through Trino compared to running it on CrateDB directly.

## Conclusion

With a few parameter tweaks, Trino can successfully connect to CrateDB. The information presented in this post is the result of a short compatibility test and is likely not exhaustive. If you use Trino with CrateDB and are aware of any additional aspects, please let us know!
