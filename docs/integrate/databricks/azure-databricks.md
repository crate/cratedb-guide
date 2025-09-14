(azure-databricks)=
# Introduction to Azure Databricks with CrateDB

This is a quick intro into getting started with [Azure Databricks](https://azure.microsoft.com/en-us/services/databricks/) and [CrateDB](https://cratedb.com/).

## Setup Azure Databricks

1. Add a new Databricks service to your Azure Subscription
2. Once this is done use “Launch Workspace”
3. After you are signed into Azure Databricks use the common task “New Cluster” to start a cluster for your Spark jobs execution
4. Install the [pgjdbc](https://jdbc.postgresql.org/) library (as of time of publishing `org.postgresql:postgresql:42.2.23`) from Maven for your cluster

![azure-databricks-server-install-library|300x204](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ba492250da484256ea7acf3418877da90e91d088.png){height=200} ![azure-databricks-server-select-library|500x380](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/12baccefce25f1c44da0edf12643dc8e389de9b1.png){height=320}


## Connect using Python

1. Create a new notebook of default language Python
2. Add the following code and run the notebook

```
crateUsername = "<username>"
cratePassword = "<password>"
postgresqlUrl = "jdbc:postgresql://<url-to-server>:5432/?sslmode=require";
tableName = "<tablename>"

jdbcDF = spark.read \
    .format("jdbc") \
    .option("url", postgresqlUrl) \
    .option("driver", "org.postgresql.Driver") \
    .option("dbtable", tableName) \
    .option("user", crateUsername) \
    .option("password", cratePassword) \
    .load()
jdbcDF.head(n=10)
```

3. You should see the results from CrateDB


## Connect using Scala

1. Create a new notebook with default language Scala
2. Add the following code and run the notebook

```
val crateUsername = "<username>"
val cratePassword = "<password>"
val postgresqlUrl = "jdbc:postgresql://<url-to-server>:5432/?sslmode=require";
val tableName = "<tablename>"

val jdbcDF = spark.read
       .format("jdbc")
       .option("url", postgresqlUrl)
       .option("driver", "org.postgresql.Driver")
       .option("dbtable", tableName)
       .option("user", crateUsername)
       .option("password", cratePassword)
       .option("fetchsize", 100000)
       .load()
jdbcDF.head(n=10);
```

3. You should see the results from CrateDB
