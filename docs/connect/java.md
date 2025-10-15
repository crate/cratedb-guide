(connect-java)=

# Java

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Java applications mostly use JDBC to connect to CrateDB.
:::

:::
[JDBC] is a standard Java API that provides a common interface for accessing
databases in Java.
:::

:::{rubric} Driver options
:::

:::{div}
You have two JDBC driver options: The [PostgreSQL
JDBC Driver] and the {ref}`crate-jdbc:index`.
PostgreSQL JDBC uses the `jdbc:postgresql://` protocol identifier,
while CrateDB JDBC uses `jdbc:crate://`.
:::

You are encouraged to probe the PostgreSQL JDBC Driver first. This is the
most convenient option, specifically if the system you are connecting with
already includes the driver jar.

However, applications using the PostgreSQL JDBC Driver may emit PostgreSQL-specific
SQL that CrateDB does not understand. Use the CrateDB JDBC Driver instead
to ensure compatibility and allow downstream components to handle
CrateDB-specific behavior, for example, by employing a CrateDB-specific
SQL dialect implementation.

The {ref}`crate-jdbc:internals` page includes more information
about compatibility and differences between the two driver variants,
and more details about the CrateDB JDBC Driver.


## PostgreSQL JDBC

:::{rubric} Synopsis
:::

```java
Properties properties = new Properties();
properties.put("user", "admin");
properties.put("password", "<PASSWORD>");
properties.put("ssl", true);
Connection conn = DriverManager.getConnection(
    "jdbc:postgresql://<name-of-your-cluster>.cratedb.net:5432/",
    properties
);
```

:::{rubric} Maven
:::

```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.8</version>
</dependency>
```

:::{rubric} Gradle
:::

```groovy
repositories {
    mavenCentral()
}
dependencies {
    implementation 'org.postgresql:postgresql:42.7.8'
}
```

:::{rubric} Download
:::

:::{card}
:link: https://jdbc.postgresql.org/download/
:link-type: url
{material-outlined}`download;2em`
Download and install the PostgreSQL JDBC Driver.
:::

## CrateDB JDBC

:::{rubric} Synopsis
:::

```java
Properties properties = new Properties();
properties.put("user", "admin");
properties.put("password", "<PASSWORD>");
properties.put("ssl", true);
Connection conn = DriverManager.getConnection(
    "jdbc:crate://<name-of-your-cluster>.cratedb.net:5432/",
    properties
);
```

:::{rubric} Maven
:::

```xml
<dependencies>
    <dependency>
        <groupId>io.crate</groupId>
        <artifactId>crate-jdbc</artifactId>
        <version>2.7.0</version>
    </dependency>
</dependencies>
```

:::{rubric} Gradle
:::

```groovy
repositories {
    mavenCentral()
}
dependencies {
    implementation 'io.crate:crate-jdbc:2.7.0'
}
```

:::{rubric} Download
:::

:::{card}
:link: https://cratedb.com/docs/jdbc/en/latest/getting-started.html#installation
:link-type: url
{material-outlined}`download;2em`
Download and install the CrateDB JDBC Driver.
:::

:::{rubric} Full example
:::

:::{dropdown} `main.java`
```java
import java.sql.*;
import java.util.Properties;

public class Main {
    public static void main(String[] args) {
        try {
            Properties properties = new Properties();
            properties.put("user", "admin");
            properties.put("password", "<PASSWORD>");
            properties.put("ssl", true);
            Connection conn = DriverManager.getConnection(
                "jdbc:crate://<name-of-your-cluster>.cratedb.net:5432/",
                properties
            );

            Statement statement = conn.createStatement();
            ResultSet resultSet = statement.executeQuery("SELECT name FROM sys.cluster");
            resultSet.next();
            String name = resultSet.getString("name");

            System.out.println(name);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```
:::

## JDBC example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/java-jdbc
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using JDBC.
+++
Demonstrates a basic example using both the vanilla PostgreSQL JDBC Driver
and the CrateDB JDBC Driver.
:::

[![Java: JDBC, QA](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml)

## Hibernate / JPA

:::{div}
[Hibernate] is the top dog ORM for Java, supporting a range of databases,
including PostgreSQL. [JPA], or Jakarta Persistence API (formerly Java
Persistence API), is a Java specification that simplifies the process of
mapping Java objects to relational databases.
:::

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/java-quarkus-panache
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using JPA and Panache.
+++
How CrateDB can be utilized with Quarkus in a very intuitive way
using the Hibernate ORM deriving from PostgreSQL.
:::

## jOOQ

:::{div}
[jOOQ] is an internal DSL and source code generator, modelling the SQL
language as a type-safe Java API to help you write better SQL.
:::

```java
// Fetch records, with filtering and sorting.
Result<Record> result = db.select()
        .from(AUTHOR)
        .where(AUTHOR.NAME.like("Ja%"))
        .orderBy(AUTHOR.NAME)
        .fetch();

// Iterate and display records.
for (Record record : result) {
    Integer id = record.getValue(AUTHOR.ID);
    String name = record.getValue(AUTHOR.NAME);
    System.out.println("id: " + id + ", name: " + name);
}
```

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/java-jooq
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using jOOQ.
+++
Java jOOQ demo application with CrateDB using PostgreSQL JDBC.
:::

[![Java jOOQ](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-jooq.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-jooq.yml)

## Software testing

For testing Java applications against CrateDB, see also documentation
about {ref}`java-junit` and {ref}`testcontainers`.
