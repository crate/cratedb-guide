(connect-kotlin)=

# Kotlin

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Use JDBC to connect to CrateDB from Kotlin applications.
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

`example.kt`
```kotlin
import java.sql.DriverManager
import java.util.*

fun main() {

    // Connect to database.
    val jdbcUrl = "jdbc:postgresql://localhost:5432/doc?sslmode=disable"
    // val jdbcUrl = "jdbc:crate://localhost:5432/doc?sslmode=disable"

    val connection = DriverManager.getConnection(jdbcUrl, "crate", "crate")

    // Invoke query.
    val query = connection.prepareStatement("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3")
    val result = query.executeQuery()

    // Display results.
    while (result.next()) {
        val mountain = result.getString("mountain")
        val height = result.getInt("height")
        println("${mountain}: ${height}")
    }

}
```
`build.gradle.kts`
```kotlin
plugins {
    java
    kotlin("jvm") version "2.2.20"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    runtimeOnly("org.postgresql:postgresql:42.7.8")
    // runtimeOnly("io.crate:crate-jdbc:2.7.0")
}

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(11))
    }
}

application {
    mainClass = "ExampleKt"
}

kotlin {
    sourceSets.main {
        kotlin.srcDir(".")
    }
}
```

:::{include} ../_cratedb.md
:::
```shell
gradle run
```

:::{rubric} SSL connection
:::

Use the `sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```kotlin
val jdbcUrl = "jdbc:postgresql://testcluster.cratedb.net:5432/doc?sslmode=require"
// val jdbcUrl = "jdbc:crate://testcluster.cratedb.net:5432/doc?sslmode=require"
val connection = DriverManager.getConnection(jdbcUrl, "admin", "password")
```
