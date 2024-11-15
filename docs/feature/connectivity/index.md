(connect)=
(connectivity)=

# Connectivity

:::{include} /_include/links.md
:::

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 9 9 9


:::{rubric} Overview
:::
CrateDB connectivity options at a glance.

You have a variety of options to connect to CrateDB, and to integrate it with
off-the-shelve, 3rd-party, open-source, and proprietary applications.

:::{rubric} About
:::
CrateDB supports both the HTTP protocol and the PostgreSQL wire protocol,
which ensures that many clients that work with PostgreSQL, will also work with
CrateDB.

Through corresponding drivers, CrateDB is compatible with JDBC, ODBC,
and other database API specifications.
By supporting SQL, CrateDB is compatible with many standard database
environments out of the box.

:::{rubric} Details
:::

CrateDB provides plenty of connectivity options with database drivers,
applications, and frameworks, in order to get time series data in and
out of CrateDB, and to connect to other applications.

To learn more, please refer to the documentation sections and hands-on
tutorials about supported client drivers, libraries, and frameworks,
and how to configure and use them with CrateDB optimally.
::::


::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

```{rubric} Reference Manual
```
- [HTTP interface]
- [PostgreSQL interface]
- [SQL query syntax]

```{rubric} Protocols and API Standards
```
- [HTTP protocol]
- [PostgreSQL wire protocol]
- [JDBC]
- [ODBC]
- [SQL]
::::

:::::


## Synopsis

In order to provide a CrateDB instance for testing purposes, use, for
example, Docker.
```shell
docker run --rm -it --publish=4200:4200 --publish=5432:5432 crate/crate:nightly
```
:::{tip}
The [CrateDB Examples] repository also includes a collection of
clear and concise examples how to connect to and work with CrateDB,
using different environments, applications, or frameworks.
:::


::::::{tab-set}

:::::{tab-item} C# / Npgsql
For more information see [Npgsql] documentation.

`program.csproj`
```cs
<Project Sdk="Microsoft.NET.Sdk">
  <ItemGroup>
    <PackageReference Include="Npgsql" Version="8.0.5" />
  </ItemGroup>
</Project>
```
`program.cs`
```csharp
using Npgsql;
using NpgsqlTypes;

var connString =
    $"Host=localhost;Port=5432;SSL Mode=Disable;" +
    $"Username=crate;Password=;Database=testdrive";

using (var conn = new NpgsqlConnection(connString)) {
    conn.Open();

    var mountains = new List<string>();
    using (var cmd = new NpgsqlCommand("SELECT mountain FROM sys.summits ORDER BY 1 LIMIT 25", conn))
    using (var reader = cmd.ExecuteReader()) {
        while (await reader.ReadAsync()) {
            mountains.Add(reader.GetString(0));
        }
        Console.WriteLine($"Mountains: {string.Join(",", mountains)}");
    }
    conn.Close();
}
```
:::::

:::::{tab-item} Golang / pgx
For more information see [pgx][golang-pgx] documentation.
```shell
go mod add pgx
```
```golang
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/jackc/pgx/v5"
)

func main() {
	dbUrl := "postgres://crate:@localhost:5432/testdrive"
	conn, err := pgx.Connect(context.Background(), dbUrl)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Unable to connect to database: %v\n", err)
		os.Exit(1)
	}
	defer conn.Close(context.Background())

	var mountain string
	err = conn.QueryRow(context.Background(), "SELECT mountain FROM sys.summits ORDER BY 1 LIMIT 25").Scan(&mountain)
	if err != nil {
		fmt.Fprintf(os.Stderr, "QueryRow failed: %v\n", err)
		os.Exit(1)
	}

	fmt.Println(mountain)
}
```
:::::

:::::{tab-item} Java / JDBC
JDBC is a standard Java API that provides a common interfaces for accessing
databases in Java.
For more information see [pgJDBC] and [CrateDB pgJDBC].
```xml
<project>
    <dependencies>
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>42.7.4</version>
        </dependency>
        <dependency>
            <groupId>io.crate</groupId>
            <artifactId>crate-jdbc</artifactId>
            <version>2.7.0</version>
        </dependency>
    </dependencies>
</project>
```
```java
import java.sql.*;
import java.util.Properties;

// You can use both drivers, vanilla pgJDBC, or CrateDB's pgJDBC.
String dburi = "jdbc:crate://localhost:5432/";
String dburi = "jdbc:postgresql://localhost:5432/";

public class Main {
    public static void main(String[] args) {
        try {
            Properties properties = new Properties();
            properties.put("user", "crate");
            properties.put("password", "");
            properties.put("ssl", false);
            Connection conn = DriverManager.getConnection(
                dburi,
                properties
            );

            Statement statement = conn.createStatement();
            ResultSet resultSet = statement.executeQuery(
                "SELECT * FROM sys.summits LIMIT 3;");
            resultSet.next();
            String mountain = resultSet.getString("mountain");

            System.out.println(mountain);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```
:::::

:::::{tab-item} JavaScript / node-postgres
For more information see [node-postgres] documentation.
```shell
npm install pg
```
```javascript
const { Client } = require("pg");

const cratedbClient = new Client({
  host: "localhost",
  port: 5432,
  user: "crate",
  password: "",
  ssl: false,
});

(async () => {
  await cratedbClient.connect();
  const result = await cratedbClient.query("SELECT * FROM sys.summits LIMIT 3;");
  console.log(result.rows);
})();
```
:::::

:::::{tab-item} JavaScript / node-crate
`node-crate` is an independent Node.js driver implementation for
CrateDB, using the `/_sql` HTTP API endpoint.
For more information see [node-crate] documentation.
```shell
npm install node-crate
```
```javascript
const crate = require("node-crate");

crate.connect(`https://crate:${encodeURIComponent("")}@localhost:4200`);

(async () => {
  const result = await crate.execute("SELECT name FROM sys.cluster");
  console.log(result.rows[0]);
})();
```
:::::

:::::{tab-item} Python / DB API
For more information see [CrateDB Python] documentation.
```shell
pip install --upgrade crate
```
```python
import crate.client
from pprint import pprint

connection = crate.client.connect("http://localhost:4200")
cursor = connection.cursor()
cursor.execute("SELECT * FROM sys.summits LIMIT 3;")
results = cursor.fetchall()
pprint(results)
cursor.close()
connection.close()
```
:::::

:::::{tab-item} Python / SQLAlchemy
For more information see [CrateDB SQLAlchemy] documentation.
```shell
pip install --upgrade sqlalchemy-cratedb
```
```python
import sqlalchemy as sa
from pprint import pprint

engine = sa.create_engine("crate://localhost:4200/doc", isolation_level="AUTOCOMMIT", echo=True)

with engine.connect() as connection:
    cursor = connection.execute(sa.text("SELECT * FROM sys.summits LIMIT 3;"))
    pprint(cursor.fetchall())
```
:::::

::::::


:::::{dropdown} PHP

:::{rubric} HTTP
:::

::::{dropdown} PDO_CRATEDB
The PHP Data Objects (PDO) is a standard PHP extension that defines a common
interface for accessing databases in PHP.
For more information see [CrateDB PDO] documentation.
```php
<?php
require 'vendor/autoload.php';

use Crate\PDO\PDO as PDO;

$pdo = new PDO(
    'crate:localhost:4200',  // Host
    'crate',                 // Username
    ''                       // Password
);

$stm = $pdo->query('SELECT * FROM sys.summits LIMIT 3;');
$record = $stm->fetch();
print $record;
?>
```
::::

::::{dropdown} DBAL
DBAL is a PHP database abstraction layer that comes with database schema
introspection, schema management, and PDO support.
For more information see [CrateDB DBAL] documentation.
```php
<?php

require 'vendor/autoload.php';

$params = array(
    'driverClass' => 'Crate\DBAL\Driver\PDOCrate\Driver',
    'user' => 'crate',
    'password' = '',
    'host' => 'localhost',
    'port' => 4200
);

$connection = \Doctrine\DBAL\DriverManager::getConnection($params);
$sql = 'SELECT * FROM sys.summits LIMIT 3;';
$result = $connection->query($sql)->fetch();

print $result;
?>
```
::::


:::{rubric} PostgreSQL
:::

::::{dropdown} PDO_PGSQL
PDO_PGSQL is a driver that implements the [PHP Data Objects (PDO) interface]
to enable access from PHP to PostgreSQL databases. 
For more information see [PDO_PGSQL] documentation.
```php
<?php
$connection = new PDO("pgsql:host=localhost;port=5432;user=crate");
$cursor = $connection->query("SELECT * FROM sys.summits LIMIT 3");
print_r($cursor->fetchAll(PDO::FETCH_ASSOC));
?>
```
::::

::::{dropdown} AMPHP
AMPHP is a collection of high-quality, event-driven libraries for PHP
designed with fibers and concurrency in mind.
Benefit from concurrency by replacing your blocking I/O with non-blocking I/O,
or designing your system with non-blocking I/O from the ground up.
For more information see [AMPHP] documentation.
```php
<?php
use Amp\Postgres;
use Revolt\EventLoop;

EventLoop::run(function () {
    // Connect to CrateDB's PostgreSQL interface.
    $config = Postgres\ConnectionConfig::fromString("host=localhost port=5432 user=crate");
    $connection = yield Postgres\connect($config);

    // Query data.
    $result = yield $connection->query('SELECT * FROM sys.summits LIMIT 3;');

    // Print results.
    while (yield $result->advance()) {
        $row = $result->getCurrent();
        \printf("%s\n", $row);
    }

    // Close connection to database.
    $connection->close();
});
?>
```
::::

:::::


:::::{dropdown} Python

:::{rubric} HTTP
:::

::::{dropdown} DB API

The `crate` Python package offers a database client implementation compatible
with the Python Database API 2.0 specification, and also includes the CrateDB
SQLAlchemy dialect.
For more information see [CrateDB Python] documentation.
```shell
pip install --upgrade crate
```
```python
from crate import client
from pprint import pprint

conn = client.connect("http://localhost:4200")
with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sys.summits LIMIT 3")
    results = cursor.fetchall()
    pprint(results)
```
::::

::::{dropdown} SQLAlchemy
The [SQLAlchemy] dialect for CrateDB, based on the HTTP-based DBAPI client
library.
For more information see [CrateDB SQLAlchemy] documentation.
```shell
pip install --upgrade sqlalchemy-cratedb
```
```python
import sqlalchemy as sa

engine = sa.create_engine("crate://localhost:4200", echo=True)
with engine.connect() as conn:
    result = conn.execute(sa.text("SELECT * FROM sys.summits;"))
    for record in result.all():
        print(record)
```
::::

:::{rubric} PostgreSQL
:::

::::{dropdown} asyncpg
asyncpg is a database interface library designed specifically for PostgreSQL
and Python/asyncio. asyncpg is an efficient, clean implementation of the
PostgreSQL server binary protocol for use with Python's asyncio framework.
For more information see [asyncpg] documentation.
```shell
pip install --upgrade asyncpg
```
```python
import asyncio
import asyncpg

async def run():
    conn = await asyncpg.connect(host="localhost", port=5432, user="crate", password="", ssl=False)
    try:
        result = await conn.fetch("SELECT * FROM sys.summits LIMIT 3;")
    finally:
        await conn.close()
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
```
::::

::::{dropdown} Psycopg2
Psycopg is a popular PostgreSQL database adapter for Python. Its main features
are the complete implementation of the Python DB API 2.0 specification and the
thread safety (several threads can share the same connection).
For more information see [psycopg2] documentation.
```shell
pip install --upgrade psycopg2-binary
```
```python
import psycopg2
from pprint import pprint

conn = psycopg2.connect(host="localhost", port=5432, user="crate", password="", sslmode="disable")

with conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM sys.summits")
        results = cursor.fetchall()
        pprint(results)
```
::::

::::{dropdown} Psycopg3
Psycopg 3 is a newly designed PostgreSQL database adapter for the Python
programming language. Psycopg 3 presents a familiar interface for everyone who
has used Psycopg 2 or any other DB-API 2.0 database adapter, but allows to use
more modern PostgreSQL and Python features, such as:

- Asynchronous support
- COPY support from Python objects
- A redesigned connection pool
- Support for static typing
- Server-side parameters binding
- Prepared statements
- Statements pipeline
- Binary communication
- Direct access to the libpq functionalities

For more information see [psycopg3] documentation.
```shell
pip install --upgrade 'psycopg[binary]'
```
```python
import psycopg

with psycopg.connect("postgres://crate@localhost:5432/doc") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM sys.summits LIMIT 3")
        for record in cursor:
            print(record)
```
::::

:::::


## Learn

::::{grid} 2 3 3 3
:padding: 0

:::{grid-item-card} Ecosystem Catalog
:link: catalog
:link-type: ref
:link-alt: Ecosystem Catalog
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller
{material-outlined}`category;3.5em`
+++
Explore all open-source and partner applications and solutions.
:::

:::{grid-item-card} Driver Support
:link: crate-clients-tools:connect
:link-type: ref
:link-alt: Driver Support
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller
{material-outlined}`link;3.5em`
+++
List of HTTP and PostgreSQL client drivers, and tutorials.
:::

:::{grid-item-card} Integration Tutorials
:link: integrate
:link-type: ref
:link-alt: Integration Tutorials
:padding: 3
:class-card: sd-pt-3
:class-title: sd-fs-5
:class-body: sd-text-center
:class-footer: text-smaller
{material-outlined}`local_library;3.5em`
+++
Learn how to integrate CrateDB with applications and tools.
:::

::::



[AMPHP]: https://amphp.org/
[asyncpg]: https://magicstack.github.io/asyncpg/current/
[CrateDB DBAL]: inv:crate-dbal:*:label#index
[CrateDB Examples]: https://github.com/crate/cratedb-examples
[CrateDB PDO]:  inv:crate-pdo:*:label#index
[CrateDB pgJDBC]: https://cratedb.com/docs/jdbc/
[CrateDB Python]: inv:crate-python:*:label#index
[CrateDB SQLAlchemy]: inv:sqlalchemy-cratedb:*:label#index
[Driver Support]: inv:crate-clients-tools:*:label#connect
[Ecosystem Catalog]: inv:crate-clients-tools:*:label#index
[golang-pgx]: https://github.com/jackc/pgx
[HTTP interface]: inv:crate-reference:*:label#interface-http
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity
[node-crate]: https://www.npmjs.com/package/node-crate
[node-postgres]: https://www.npmjs.com/package/pg
[Npgsql]: https://www.npgsql.org/
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PDO_PGSQL]: https://www.php.net/manual/en/ref.pdo-pgsql.php
[pgJDBC]: https://jdbc.postgresql.org
[PHP Data Objects (PDO) interface]: https://www.php.net/manual/en/intro.pdo.php
[PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[psycopg2]: https://www.psycopg.org/docs/
[psycopg3]: https://www.psycopg.org/psycopg3/docs/
[SQL]: https://en.wikipedia.org/wiki/Sql
[SQL query syntax]: inv:crate-reference:*:label#sql
[SQLAlchemy]: https://www.sqlalchemy.org


```{include} /_include/styles.html
```
