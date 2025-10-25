:::{include} /_include/logos.md
:::

(pgjdbc)=
(postgresql-jdbc)=

# PostgreSQL JDBC

```{div} .float-right
[![PostgreSQL logo][PostgreSQL logo]{height=40px loading=lazy}][PostgreSQL home]
```
```{div} .clearfix
```

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Connect to CrateDB using PostgreSQL JDBC.
:::

:::{rubric} About
:::

:::{div}
The [PostgreSQL JDBC Driver] is an open-source JDBC driver written in
Pure Java (Type 4), which communicates using the PostgreSQL native
network protocol. PostgreSQL JDBC needs Java >= 8.
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
        "jdbc:postgresql://localhost:5432/doc?sslmode=disable",
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

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use the `sslmode=require` parameter,
and replace username, password, and hostname with values matching
your environment.
```java
properties.put("user", "admin");
properties.put("password", "password");
Connection conn = DriverManager.getConnection(
    "jdbc:postgresql://testcluster.cratedb.net:5432/doc?sslmode=require",
    properties
);
```

## Install

:::{rubric} Download
:::

:::{card}
:link: https://jdbc.postgresql.org/download/
:link-type: url
{material-regular}`download;2em`
Navigate to the PostgreSQL JDBC Driver installation page.
:::

:::{card}
:link: https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.8/postgresql-42.7.8.jar
:link-type: url
{material-regular}`download;2em`
Directly download the recommended `postgresql-42.7.8.jar`.
:::

:::{rubric} Maven `pom.xml`
:::
```xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.8</version>
</dependency>
```

:::{rubric} Gradle `build.gradle`
:::
```groovy
repositories {
    mavenCentral()
}
dependencies {
    implementation 'org.postgresql:postgresql:42.7.8'
}
```

## Quickstart example

Create a file `example.java` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
Download JAR file.
```shell
wget https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.8/postgresql-42.7.8.jar
```
:::{dropdown} Instructions for Windows users
If you don't have the `wget` program installed, for example on Windows, just
download the JAR file using your web browser of choice.
If you want to use PowerShell, invoke the `Invoke-WebRequest` command instead
of `wget`.
```powershell
Invoke-WebRequest https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.8/postgresql-42.7.8.jar -OutFile postgresql-42.7.8.jar
```
:::
Invoke program. Needs Java >= 21 ([JEP 445]), alternatively see [](#full-example).
```shell
java -cp postgresql-42.7.8.jar example.java
```

## Full example

:::{include} _jdbc_example.md
:::


[JEP 445]: https://openjdk.org/jeps/445
