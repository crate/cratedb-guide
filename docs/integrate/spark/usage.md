(spark-usage)=
# Getting started with Apache Spark and CrateDB

**Apache Spark** is an open-source distributed computing framework designed for high-speed, versatile big-data processing. It offers support for various data processing tasks, such as batch processing, real-time streaming, machine learning, and graph analytics. It is a popular choice for organizations looking to analyze large datasets efficiently.

Using Apache Spark with CrateDB is a powerful combination for processing and analyzing large datasets. In this usage guide, we'll walk through the process of setting up PySpark (Python API for Spark) to work with CrateDB, including data loading, processing, and writing results back to CrateDB.

Prerequisites:

1. Running instance of [CrateDB](https://console.cratedb.cloud/)
2. Python 3.x
3. Java 11 or later

## Provision seed data to CrateDB

The following commands create the `sensor_data` table in CrateDB and generate test data:

```sql
CREATE TABLE IF NOT EXISTS "doc"."sensor_data" (
   "id" INTEGER,
   "value" INTEGER,
   "machine" TEXT
)
```

```sql
INSERT INTO sensor_data (id, value, machine)
SELECT
    id,
    floor(random()*100),
    CASE floor(random() * 3)
        WHEN 0 THEN 'machine 1'
        WHEN 1 THEN 'machine 2'
        WHEN 2 THEN 'machine 3'
        ELSE 'machine 4'
   END AS machine
FROM
  generate_series(1, 100) id;
```

## Set up Apache Spark

This usage guide will work with a single-node Apache Spark installation running on a Mac M1 machine. To set up Apache Spark on your machine use the following steps:

1. Install Java and Scala, as the Apache Spark requires both to run:

   ```shell
   brew install openjdk@11
   brew install scala
   ```

   Before verifying your Java installation, set the `JAVA_HOME` environment variable by adding the following line to your shell profile:

   `export JAVA_HOME="/usr/local/opt/openjdk@11"`

2. Install the latest version of Apache Spark (which includes PySpark):

   ```shell
   brew install apache-spark
   ```

3. Verify the installation of apache-spark and pyspark:

   ```shell
   spark-shell --version
   pyspark --version
   ```

4. Finally, as CrateDB communicates with Spark via JDBC, download the [Postgres JDBC driver](https://jdbc.postgresql.org/download/) in your working directory.
   In this usage guide, we use the `postgresql-42.7.8.jar` driver.


## Data analysis

Load dataset from database, perform analysis, and write back the results.

### Load data from CrateDB

You can load data from CrateDB into a PySpark DataFrame using the following code:

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("cratedb_test").config("spark.jars", "postgresql-42.7.8.jar").getOrCreate()
df = spark.read.format("jdbc")
               .option("url", "jdbc:postgresql://host:port/crate?sslmode=require")
               .option("driver", "org.postgresql.Driver")
               .option("user", "user")
               .option("password", "password")
               .option("dbtable", "doc.sensor_data").load()
```

1. First, you need to start a PySpark session and configure it to use the
   PostgreSQL JDBC driver by adding the JAR file to the Spark session's
   classpath.
2. Once you have configured your PySpark session, you can use the `spark.read`
   API to load data from CrateDB into a DataFrame. You'll need to provide the
   JDBC URL and specify the table or query from which you want to retrieve
   data. Make sure to specify the correct URL, table name, and authentication
   details.
3. In this example, we load all data from the `sensor_data` table. You can also
   use a SQL query instead of a table name you need to perform more complex
   data retrieval operations.
:::::

### Perform data manipulation and analysis

Once you have loaded the data into a PySpark DataFrame, you can perform various data manipulation and analysis tasks. For instance, you can filter, aggregate, and transform your data:

```python
filtered_data = df.filter(df["value"] > 25)
grouped_df = df.groupBy("machine").agg({"value": "avg"})
```

### **Write results back to CrateDB**

After processing your data, you can write the results back to CrateDB:

```python
grouped_df.write.format("jdbc").option("url", "jdbc:postgresql://host:port/crate?sslmode=require")
                .option("driver", "org.postgresql.Driver")
                .option("user", "user")
                .option("password", "password")
                .option("dbtable", "doc.aggregated_sensor_data")
                .save(mode="overwrite")
```

This code writes the resulting DataFrame back to CrateDB in a table named `aggregated_sensor_data`. Make sure to replace the connection URL and table name as needed.

After you're done with your Spark job, stop the Spark session:

`spark.stop()`

Now, you can run your code as any other Python application. After the execution is complete, you can check the content of the `aggregated_sensor_data` table:

```sql
SELECT * FROM aggregated_sensor_data;
```

![Screenshot 2023-09-18 at 14.26.01|690x211](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/2/2dbf40b9655d79097d942d953f6f12ae59758c56.png)

The result shows grouped data by the "machine" column and calculated average values.

## Wrap up

That's it! You've learned how to set up Apache Spark with CrateDB, load data from CrateDB into a Spark DataFrame, perform data manipulations, and write the results back to CrateDB. You can build more complex data pipelines and analysis workflows using this foundation.

If you are interested in learning more about CrateDB, start your cluster on
[CrateDB Cloud](https://console.cratedb.cloud/) today, including a forever free
[CRFREE](https://crate.io/lp-crfree) plan.

For further questions about CrateDB and its use cases, see also {ref}`solutions` and
the [community forum](https://community.cratedb.com/).
