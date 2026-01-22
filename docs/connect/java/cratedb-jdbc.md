:::{include} /_include/logos.md
:::

(crate-jdbc)=
(cratedb-jdbc)=

# CrateDB JDBC

```{div} .float-right
[![Java: JDBC, QA](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml)
```
```{div} .clearfix
```

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Connect to CrateDB using CrateDB JDBC.
:::

:::{rubric} About
:::

:::{div}
The [CrateDB JDBC Driver] is an open-source JDBC driver written in
Pure Java (Type 4), which communicates using the PostgreSQL native
network protocol. CrateDB JDBC needs Java >= 11.
:::

:::{rubric} Synopsis
:::

`example.java`
```java
import java.sql.*;

void main() throws SQLException {

    // Connect to database.
    Properties properties = new Properties();
    properties.put("user", "crate");
    properties.put("password", "crate");
    Connection conn = DriverManager.getConnection(
        "jdbc:crate://localhost:5432/?sslmode=disable",
        properties
    );
    conn.setAutoCommit(true);

    // Invoke query.
    Statement st = conn.createStatement();
    st.execute("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 5;");

    // Display results.
    ResultSet rs = st.getResultSet();
    while (rs.next()) {
        System.out.printf(Locale.ENGLISH, "%s: %d\n", rs.getString(1), rs.getInt(2));
    }
    conn.close();

}
```

:::{rubric} SSL connection
:::

Use the `sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```java
properties.put("user", "admin");
properties.put("password", "password");
Connection conn = DriverManager.getConnection(
    "jdbc:crate://testcluster.cratedb.net:5432/?sslmode=require",
    properties
);
```

## Install

:::{rubric} Download
:::

:::{card}
:link: https://cratedb.com/docs/jdbc/en/latest/getting-started.html#installation
:link-type: url
{material-regular}`download;2em`
Navigate to the CrateDB JDBC Driver installation page.
:::

:::{card}
:link: https://repo1.maven.org/maven2/io/crate/crate-jdbc-standalone/2.7.0/crate-jdbc-standalone-2.7.0.jar
:link-type: url
{material-regular}`download;2em`
Directly download the recommended `crate-jdbc-standalone-2.7.0.jar`.
:::

:::{card} Linux / macOS
```shell
wget https://repo1.maven.org/maven2/io/crate/crate-jdbc-standalone/2.7.0/crate-jdbc-standalone-2.7.0.jar
```
:::
:::{card} Windows
```powershell
Invoke-WebRequest https://repo1.maven.org/maven2/io/crate/crate-jdbc-standalone/2.7.0/crate-jdbc-standalone-2.7.0.jar -OutFile crate-jdbc-standalone-2.7.0.jar
```
:::

:::{rubric} Maven `pom.xml`
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

:::{rubric} Gradle `build.gradle`
:::
```groovy
repositories {
    mavenCentral()
}
dependencies {
    implementation 'io.crate:crate-jdbc:2.7.0'
}
```

## Run

:::{rubric} Quickstart example
:::

Create the file `example.java` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
Invoke program. This example needs Java >= 25 ([JEP 512]),
with earlier versions please use the full example.
```shell
java -cp crate-jdbc-standalone-2.7.0.jar example.java
```

:::{rubric} Full example
:::

:::{include} _jdbc_example.md
:::


[JEP 512]: https://openjdk.org/jeps/512
