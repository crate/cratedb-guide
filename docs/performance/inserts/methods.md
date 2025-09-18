(insert-methods)=

# Insert Methods

CrateDB supports multiple ways to insert data.

Some insert methods can be faster than others, depending on your setup.
Choosing the best insert method is an easy way to improve insert performance.

(insert-statement-types)=

## Statement types

The three types of insert statements are:

- {ref}`Single inserts <inserts-single-inserts>`
- {ref}`UNNEST <inserts-unnest>`
- {ref}`Multiple value expressions <inserts-multiple-values>`

Each type of statement can be issued using any of the three types of
{ref}`client approaches <inserts-client-approaches>`, which we cover in
the next section.

(inserts-single-inserts)=

### Single inserts

{ref}`Single inserts <crate-reference:dml-inserting-data>` are the most basic
sort of insert statement, and look like this:

```psql
cr> INSERT INTO my_table (column_a) VALUES ("value 1");
INSERT OK, 1 row affected  (... sec)
```

Single inserts are typically very fast with CrateDB. A small cluster can
easily handle several thousand inserts per second.

However, it's important to note that:

> 1. Every insert is first applied to the primary shard
> 2. After the primary shard has been updated, the insert is then individually
>    communicated in parallel to every configured replica shard
> 3. CrateDB will not return a response until all replica shards have been
>    updated

The overhead for each insert (query parsing, planning, and execution, and
potentially network connection overhead too) starts to add up for very heavy
insert workloads.

In addition, lots of internal traffic will congest your network, which will
slow down any network-based cluster operations (i.e. inserts, distributed
reads, replication, and cluster management).

(inserts-unnest)=

### `UNNEST`

The {ref}`UNNEST <crate-reference:unnest>` function produce rows, like so:

```psql
cr> SELECT *
...   FROM UNNEST(
...          [1, 2, 3],
...          ['Arthur', 'Trillian', 'Marvin']);
+------+----------+
| col1 | col2     |
+------+----------+
|    1 | Arthur   |
|    2 | Trillian |
|    3 | Marvin   |
+------+----------+
SELECT 3 rows in set  (... sec)
```

Combine `UNNEST` with `INSERT` to insert multiple rows at once:

```psql
cr> INSERT INTO my_table (id, name)
...   (SELECT *
...      FROM UNNEST(
...             [1, 2, 3],
...             ['Arthur', 'Trillian', 'Marvin']));
INSERT OK, 3 rows affected  (... sec)
```

You should see a dramatic improvement in performance over single inserts.

Specifically, the advantages are:

- Significantly less internal network traffic
- The query only needs to be parsed, planned, and executed once
- If [translog.durability] is set to `REQUEST` (the default), an insert
  using `UNNEST` flushes the disk once for every shard written to

If your client supports query string parameter substitution, you can use the
`UNNEST` method with static prepared statements.

For example, using the CrateDB Python client, the following is possible:

```python
client.execute("""
  INSERT INTO my_table (id, name)
    (SELECT *
       FROM UNNEST(?, ?))
""", ([1, 2, 3], ["Arthur", "Trillian", "Marvin"]))
```

Here, you can vary the number of rows being inserted without having to change
the prepared statement.

:::{WARNING}
When inserting using `UNNEST`, CrateDB may drop rows that produce errors
without returning an error message. This happens when the `SELECT` using
`UNNEST` affects rows with invalid column names, or with data types that
are not internally consistent. This behavior can produce inconsistencies
and unexpected results. Refer to the [UNNEST reference documentation] for
more detail.
:::

(inserts-multiple-values)=

### Multiple value expressions

You can insert multiple rows with multiple value expressions, like so:

```psql
cr> INSERT INTO my_table (id, name)
...      VALUES (1, 'Arthur'),
...             (2, 'Trillian'),
...             (2, 'Marvin');
INSERT OK, 3 rows affected  (... sec)
```

This method of doing bulk inserts is usually slower than the `UNNEST` method,
because parsing is more expensive. The query looks nicer for humans though.

The only problem is that the structure of the insert statement is variable on
the number of rows to insert. If you are inserting a variable number of rows,
you have to prepare the SQL statement using some form of string concatenation
each time.

Query string parameter substitution is recommended over string concatenation,
and so the `UNNEST` method is recommended over the multiple value expressions
method.

(inserts-client-approaches)=

## Client approaches

The three client approaches for doing inserts are:

- {ref}`Standard querying <inserts-standard-querying>`
- {ref}`Bulk operations <inserts-bulk-operations>`
- {ref}`Prepared statements <inserts-prepared-statements>`

Each client approach can be used to insert {ref}`any type of insert statement
<insert-statement-types>`.

(inserts-standard-querying)=

### Standard querying

The standard way of issuing insert statements executes one statement at a time
and does not make use of {ref}`inserts-bulk-operations` or any special
{ref}`inserts-prepared-statements` client feature.

For example, using the CrateDB Python client, here's a {ref}`single insert
<inserts-single-inserts>`:

```python
client.execute("INSERT INTO my_table (column_a) VALUES (?)", ["value 1"])
```

(inserts-bulk-operations)=

### Bulk operations

You can use the {ref}`bulk operations <crate-reference:http-bulk-ops>` feature
of the {ref}`CrateDB HTTP endpoint <crate-reference:interface-http>` to perform
many inserts in a single operation.

The advantages are the same as using the {ref}`UNNEST method <inserts-unnest>`:

- Significantly less internal network traffic than executing each insert
  statement individually
- Even though you're executing multiple insert statements, the bulk query only
  needs to be parsed, planned, and executed once
- If [translog.durability] is set to `REQUEST` (the default), a bulk insert
  only flushes the disk once for every shard written to

Because the advantages are the same as using the `UNNEST` method, you
typically will not see a performance improvement by combining bulk operations
with `UNNEST` statements or statements with {ref}`multiple value expressions
<inserts-multiple-values>`.

Bulk operations are typically done with {ref}`single insert statements
<inserts-single-inserts>` as an alternative to the `UNNEST` method.

:::{SEEALSO}
{ref}`Performance: Bulk inserts <bulk-inserts>`
:::

(inserts-prepared-statements)=

### Prepared statements

Some clients offer a prepared statements feature. Prepared statements are
parsed by CrateDB and can then be executed any number of times without having
to re-parse.

This functionality is often presented as batch execution. [The JDBC client],
for instance, provides the [addBatch] and [executeBatch] methods.

For example:

```java
PreparedStatement preparedStatement = connection.prepareStatement(
    "INSERT INTO my_table (id, first_name) VALUES (?, ?)");

preparedStatement.setString(1, "Arthur");
preparedStatement.addBatch();

preparedStatement.setString(1, "Trillian");
preparedStatement.addBatch();

preparedStatement.setString(1, "Marvin");
preparedStatement.addBatch();

int[] results = preparedStatement.executeBatch();
```

In addition to reducing parsing overhead, prepared statement execution requests
use the binary protocol, contain almost no headers, and are executed over an
already established connection.

Typically, prepared statements are used {ref}`single insert statements
<inserts-single-inserts>`.

Prepared statements with single inserts will usually perform better than
{ref}`standard querying <inserts-standard-querying>` with single inserts, and
should be comparable to standard querying with both the {ref}`UNNEST
method <inserts-unnest>` and {ref}`multiple value expressions
<inserts-multiple-values>`.

## Testing

Follow the basic {ref}`inserts performance testing
<testing-inserts-performance>` procedure.

To test {ref}`bulk operations <inserts-bulk-operations>`, you should:

1. Configure the setup you would like to test
2. Run a number of different tests against that setup, using different
   `--bulk-size` settings
3. Evaluate your throughput results (perhaps by plotting your results on a
   graph so that you can see the response curve)

Try out different setups and re-run the test.

Please note that `INSERT INTO` statements using a query, and the `COPY FROM`
statement, are using overload protection to ensure performance of other queries
in parallel. Refer to the {ref}`Overload Protection <crate-reference:overload_protection>`
documentation on how to modify these parameters.

At the end of this process, you will have a better understanding of the
throughput of your cluster with different setups and under different loads.

[addbatch]: https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#addBatch(java.lang.String)
[benchmarking]: https://cratedb.com/blog/insert-boost-on-replicas
[cr8]: https://codeberg.org/mfussenegger/cr8/
[executebatch]: https://docs.oracle.com/javase/7/docs/api/java/sql/Statement.html#executeBatch()
[the jdbc client]: https://cratedb.com/docs/jdbc/
[translog.durability]: https://cratedb.com/docs/crate/reference/en/latest/sql/reference/create_table.html#translog-durability
[unnest reference documentation]: https://cratedb.com/docs/crate/reference/en/latest/sql/statements/insert.html?highlight=unnest#description
