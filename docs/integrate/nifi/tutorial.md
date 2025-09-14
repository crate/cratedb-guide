(nifi-tutorial)=
# Connecting to CrateDB from Apache NiFi

This article describes how to connect from [Apache NiFi](http://nifi.apache.org) to CrateDB and ingest data from NiFi into CrateDB.

## Prerequisites
To follow this article, you will need:
* A CrateDB cluster
* An Apache NiFi installation that can connect to the CrateDB cluster

## Configure
First, we will set up a connection pool to CrateDB:
  1. On the main NiFi web interface, click the gear icon of your process group ("NiFi Flow" by default).
  2. Switch to "Controller Services" and click the plus icon to add a new controller.
  3. Choose "DBCPConnectionPool" as type and click "Add".
  4. Open the settings of the newly created connection pool and switch to "Properties". The table below describes in more detail which parameters need to be changed.

| Parameter                  | Description                                                                                                                                      | Sample value                                                                                            |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| Database Connection URL    | The JDBC connection string pointing to CrateDB                                                                                                  | `jdbc:postgresql://<CrateDB host>:5432/doc?ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory` |
| Database Driver Class Name | The PostgreSQL JDBC driver class name                                                                                                            | `org.postgresql.Driver`                                                                                 |
| Database Driver Location(s)| [Download](https://jdbc.postgresql.org/download/) the latest PostgreSQL JDBC driver and place it on the file system of the NiFi host | `/opt/nifi/nifi-1.13.2/postgresql-42.2.23.jar`                                                          |
| Database User              | The CrateDB user name                                                                                                                            |                                                                                                         |
| Password                   | The password of your CrateDB user                                                                                                           |                                                                                                         |

  5. After applying the changed properties, click the flash icon to enable the service.

Now the connection pool is ready to be used in one of NiFi's processors.

## Example: Read from CSV files
One common use case is to design a process in NiFi that results in data being ingested into CrateDB. As an example, we will take a CSV file from the [NYC Taxi Data](https://github.com/toddwschneider/nyc-taxi-data) repository, process it in NiFi, and then ingest it into Crate DB.

To achieve high throughput, NiFi uses by default prepared statements with configurable batch size. The optimal batch size depends on your concrete use case, 500 is typically a good starting point. Please also see the documentation on [insert performance](https://crate.io/docs/crate/howtos/en/latest/performance/inserts/index.html) for additional information.

![Screenshot 2021-04-20 at 13.58.18|576x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/474e6e5a44eb5df4928599e23b3ca2a00392b56f.png){height=480} 

In CrateDB, we first create the corresponding target table:

```sql
CREATE TABLE "doc"."yellow_taxi_trips" (
   "vendor_id" TEXT,
   "pickup_datetime" TIMESTAMP WITH TIME ZONE,
   "dropoff_datetime" TIMESTAMP WITH TIME ZONE,
   "passenger_count" INTEGER,
   "trip_distance" REAL,
   "pickup_longitude" REAL,
   "pickup_latitude" REAL,
   "rate_code" INTEGER,
   "store_and_fwd_flag" TEXT,
   "dropoff_longitude" REAL,
   "dropoff_latitude" REAL,
   "payment_type" TEXT,
   "fare_amount" REAL,
   "surcharge" REAL,
   "mta_tax" REAL,
   "tip_amount" REAL,
   "tolls_amount" REAL,
   "total_amount" REAL
);
```

After configuring the processors as described below, click the start icon on the process group window. You should see rows appearing in CrateDB after a short amount of time. If you encounter any issues, please also check NiFi's log files (`log/nifi-bootstrap.log` and `log/nifi-app.log`).

### GetFile
The `GetFile` processor points to a local directory that contains the file [yellow_tripdata_2013-08.csv](https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2013-08.csv).

### PutDatabaseRecord
The PutDatabaseRecord has a couple of properties that need to be configured:
* Record Reader: CSVReader. The CSVReader is configured to use "Use String Fields From Header" as a "Schema Access Strategy".
* Database Type: PostgreSQL
* Statement Type: INSERT
* Database Connection Pooling Service: The connection pool created previously
* Schema Name: `doc`
* Table Name: `yellow_taxi_trips`
* Maximum Batch Size: 200

## Example: Read from another SQL-based database
Data can be also be read from a SQL database and then be inserted into CrateDB:
![Screenshot 2021-07-15 at 09.59.36|690x229](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ee51baa35eddf540838d7d784cb433a1e16e1b02.png)
### ExecuteSQLRecord
Reads rows from the source database.
* Database Connection Pooling Service: A connection pool pointing to the source database
* SQL select query: The SQL query to retrieve rows as needed
* RecordWriter: JsonRecordSetWriter. JSON files are required by the following processors for conversion into SQL statements.

### ConvertJSONToSQL
Converts the generated JSON files into SQL statements.
* JDBC Connection Pool: A connection pool pointing to CrateDB
* Statement Type: INSERT
* Table Name: Name of the target table in CrateDB (without schema name)
* Schema Name: The table's schema name in CrateDB

### PutSQL
Executes the previously generated SQL statements as prepared statements.
* JDBC Connection Pool: A connection pool pointing to CrateDB
* SQL Statement: No value set
* Batch Size: 500 (the optimal value for your use case might vary)
