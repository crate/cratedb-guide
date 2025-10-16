(connect-scala)=

# Scala

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Use JDBC to connect to CrateDB from Scala applications.
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

```scala
import java.sql.{Connection, DriverManager, ResultSet}


object ScalaJdbcDemo {

  def main(args: Array[String]) {
    
    // Connect to the database
    val driver = "org.postgresql.Driver"
    val url = "jdbc:postgresql://<name-of-your-cluster>.cratedb.net:5432/"
    val username = "crate"
    val password = "crate"
    try {
      Class.forName(driver)
      var connection:Connection = DriverManager.getConnection(url, username, password)

      // Invoke query
      val statement = connection.createStatement(ResultSet.TYPE_FORWARD_ONLY, ResultSet.CONCUR_READ_ONLY)
      val resultSet = statement.executeQuery("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")
      
      // Display results
      while ( resultSet.next() ) {
        val mountain = resultSet.getString("mountain")
        val height = resultSet.getInteger("height")
        println(mountain + ": " + height)
      }
    } catch {
      case e => e.printStackTrace
    }
    
    // Clean up
    connection.close()
  }

}
```
