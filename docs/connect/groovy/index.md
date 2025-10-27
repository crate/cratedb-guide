(connect-groovy)=

# Groovy

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Use JDBC to connect to CrateDB from Groovy applications.
:::

:::{rubric} About
:::

:::
[JDBC] is a standard Java API that provides a common interface for accessing
databases in Java.
:::

:::{rubric} Driver options
:::

:::{div}
Like when using {ref}`connect-java`, you have two JDBC driver options:
The [PostgreSQL JDBC Driver] and the {ref}`crate-jdbc:index`.
PostgreSQL JDBC uses the `jdbc:postgresql://` protocol identifier,
while CrateDB JDBC uses `jdbc:crate://`.
:::

:::{rubric} Synopsis
:::

`example.groovy`
```groovy
import groovy.sql.Sql

class Example {

    static void main(String[] args) {

        // Configure database.
        Map dbConnParams = [
          url: 'jdbc:postgresql://localhost:5432/doc?sslmode=disable',
          user: 'crate',
          password: 'crate',
          driver: 'org.postgresql.Driver']

        // Connect to database, invoke query, and display results.
        Sql.withInstance(dbConnParams) { sql ->
            sql.eachRow("SELECT region, mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3") { rs ->
                println rs
            }
        }
    }

}
```
`build.gradle`
```groovy
plugins {
    id 'groovy'
    id 'application'
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.codehaus.groovy:groovy-all:3.0.25'
    runtimeOnly 'org.postgresql:postgresql:42.7.8'
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(11)
    }
}

application {
    mainClass = 'Example'
}

sourceSets {
    main.groovy.srcDirs = ['.']
}
```

:::{include} ../_cratedb.md
:::
```shell
gradle run
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use `sslmode=require`, and
replace hostname, username, and password with values matching
your environment.
```groovy
Map dbConnParams = [
  url: 'jdbc:postgresql://testcluster.cratedb.net:5432/doc?sslmode=require',
  user: 'admin',
  password: 'password',
  driver: 'org.postgresql.Driver']
```
