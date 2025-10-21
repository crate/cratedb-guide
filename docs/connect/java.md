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

## Example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/java-jdbc
:link-type: url
{material-outlined}`play_arrow;2em`
Connect to CrateDB and CrateDB Cloud using JDBC.
+++
Demonstrates a basic example using both the vanilla PostgreSQL JDBC Driver
and the CrateDB JDBC Driver.
:::

## See also

For testing Java applications against CrateDB, see also documentation
about {ref}`java-junit` and {ref}`testcontainers`.
