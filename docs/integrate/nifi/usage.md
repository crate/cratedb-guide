(nifi-usage)=
# Connecting to CrateDB from Apache NiFi

Learn how to connect from [Apache NiFi](https://nifi.apache.org) to CrateDB
and ingest data from NiFi into CrateDB.

## Prerequisites
You need:
* A CrateDB cluster
* An Apache NiFi installation that can connect to the CrateDB cluster

## Configure
Set up a connection pool to CrateDB:
1. On the main NiFi web interface, click the gear icon of your process group ("NiFi Flow" by default).
2. Switch to "Controller Services" and click the plus icon to add a new controller.
3. Choose "DBCPConnectionPool" as type and click "Add".
4. Open the new connection pool, switch to "Properties", and set the following parameters:

| Parameter                  | Description                                                                                                                            | Sample value                                                                                  |
| -------------------------- |----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Database Connection URL    | The JDBC connection string pointing to CrateDB                                                                                         | `jdbc:postgresql://<cratedb-host>:5432/?sslmode=verify-full&sslrootcert=/path/to/ca.pem`   |
| Database Driver Class Name | The PostgreSQL JDBC driver class name                                                                                                  | `org.postgresql.Driver`                                                                       |
| Database Driver Location(s)| [Download](https://jdbc.postgresql.org/download/) the latest PostgreSQL JDBC driver and place it on the file system of the NiFi host   | `${nifi.home}/lib/postgresql-42.7.8.jar`                                                      |
| Database User              | The CrateDB user name                                                                                                                  |                                                                                               |
| Password                   | The password of your CrateDB user                                                                                                      |                                                                                               |

5. Apply the properties, then click the lightning bolt to enable the service.

You can now use the connection pool in NiFi processors.

## Example: Read from CSV files
One common use case is to design a process in NiFi that results in data being
ingested into CrateDB. This example takes a CSV file from the
[NYC Taxi Data](https://github.com/toddwschneider/nyc-taxi-data) repository,
processes it in NiFi, and then ingests it into CrateDB.

NiFi uses prepared statements and batching by default. Start with a batch size
of 500 and adjust to your workload. See [insert performance] for details.

![Screenshot 2021-04-20 at 13.58.18|576x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/474e6e5a44eb5df4928599e23b3ca2a00392b56f.png){height=480} 

Create the corresponding target table in CrateDB:

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

Start the process group. Rows should appear in CrateDB shortly. To verify:

```sql
SELECT count(*) FROM doc.yellow_taxi_trips;
```
If you run into issues, check NiFi logs: `log/nifi-bootstrap.log` and
`log/nifi-app.log`.

### GetFile
The `GetFile` processor points to a local directory that contains the file [yellow_tripdata_2013-08.csv](https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2013-08.csv).

### PutDatabaseRecord
The PutDatabaseRecord has a couple of properties that need to be configured:
* Record Reader: CSVReader
  * Schema Access Strategy: "Use String Fields From Header"
  * Treat First Line as Header: true
* Database Type: PostgreSQL
* Statement Type: INSERT
* Database Connection Pooling Service: The connection pool created previously
* Schema Name: `doc`
* Table Name: `yellow_taxi_trips`
* Maximum Batch Size: 500

## Example: Read from another SQL-based database
Read data from a SQL database and insert it into CrateDB:
![Screenshot 2021-07-15 at 09.59.36|690x229](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ee51baa35eddf540838d7d784cb433a1e16e1b02.png)

### ExecuteSQLRecord
Reads rows from the source database.
* Database Connection Pooling Service: A connection pool pointing to the source database
* SQL select query: The SQL query to retrieve rows as needed
* RecordWriter: JsonRecordSetWriter. The following processors require JSON files for conversion into SQL statements.

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
* Batch Size: 500 (the optimal value varies by use case)


[insert performance]: https://crate.io/docs/crate/howtos/en/latest/performance/inserts/index.html
