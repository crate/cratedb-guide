(crate-jdbc)=
(cratedb-jdbc)=

# CrateDB JDBC

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
{material-regular}`download;2em`
Download and install the CrateDB JDBC Driver
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

:::{include} _jdbc_example.md
:::


[![Java: JDBC, QA](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml)
