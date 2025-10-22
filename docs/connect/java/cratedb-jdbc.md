(crate-jdbc)=
(cratedb-jdbc)=

# CrateDB JDBC

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
network protocol.
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
        "jdbc:crate://localhost:5432/doc?sslmode=disable",
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

:::{include} ../_cratedb.md
:::
Download JAR file.
```shell
wget https://repo1.maven.org/maven2/io/crate/crate-jdbc-standalone/2.7.0/crate-jdbc-standalone-2.7.0.jar
```
:::{dropdown} Instructions for Windows users
If you don't have the `wget` program installed, for example on Windows, just
download the JAR file using your web browser of choice.
If you want to use PowerShell, invoke the `Invoke-WebRequest` command instead
of `wget`.
```powershell
Invoke-WebRequest https://repo1.maven.org/maven2/io/crate/crate-jdbc-standalone/2.7.0/crate-jdbc-standalone-2.7.0.jar -OutFile crate-jdbc-standalone-2.7.0.jar
```
:::
Invoke program. Needs Java >= 25 ([JEP 330]).
```shell
java -cp crate-jdbc-standalone-2.7.0.jar example.java
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use the `sslmode=require` parameter,
and replace username, password, and hostname with values matching
your environment.
```java
properties.put("user", "admin");
properties.put("password", "password");
Connection conn = DriverManager.getConnection(
    "jdbc:crate://testcluster.cratedb.net:5432/doc?sslmode=require",
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

## Full example

:::{include} _jdbc_example.md
:::


[JEP 330]: https://openjdk.org/jeps/330
