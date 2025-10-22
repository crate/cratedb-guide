(pgjdbc)=
(postgresql-jdbc)=

# PostgreSQL JDBC

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
{material-regular}`download;2em`
Download and install the PostgreSQL JDBC Driver
:::


## JDBC example

:::{include} _jdbc_example.md
:::
