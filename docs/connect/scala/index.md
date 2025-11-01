(connect-scala)=

# Scala

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Connect to CrateDB from Scala applications using JDBC.
:::

:::{rubric} About
:::

:::
[JDBC] is a standard Java API that provides a common interface for accessing
databases in {ref}`connect-java`.
:::

:::{rubric} Driver options
:::

:::{include} ../java/_driver_options.md
:::

:::{rubric} Synopsis
:::

`build.sbt`
```scala
scalaVersion := "3.3.7"
libraryDependencies ++= Seq(
  "org.postgresql" % "postgresql" % "42.7.8",
)
```
`example.scala`
```scala
import java.sql.{Connection, DriverManager, ResultSet}
import scala.util.Using

object Example {

  def main(args: Array[String]): Unit = {

    // Configure connection.
    val driver = "org.postgresql.Driver"
    val url = "jdbc:postgresql://localhost:5432/doc?sslmode=disable"
    val username = "crate"
    val password = "crate"

    // Connect to the database.
    Class.forName(driver)
    try {
      Using.resource(DriverManager.getConnection(url, username, password)) { connection =>

        // Run a basic query.
        val statement = connection.createStatement(ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY)
        val resultSet = statement.executeQuery("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 5")

        // Display results.
        while (resultSet.next()) {
          val mountain = resultSet.getString("mountain")
          val height = resultSet.getInt("height")
          println(mountain + ": " + height)
        }
      }
    } catch {
      case e: Exception => e.printStackTrace()
    }

  }
}
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, use `sslmode = "require"`, and
replace username, password, and hostname with values matching
your environment.
```scala
val url = "jdbc:postgresql://testcluster.cratedb.net:5432/doc?sslmode=require"
val username = "admin"
val password = "password"
```

:::{rubric} Quickstart example
:::

Create the files `build.sbt` and `example.scala` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
```shell
sbt run
```
