(airflow-import-parquet)=
# Automating the import of Parquet files with Apache Airflow

## Introduction
Using Airflow to import the NYC Taxi and Limousine dataset in Parquet format.

Currently, Parquet imports using COPY FROM are not supported by CrateDB, it only supports CSV and JSON files instead. Because of that, we implemented a different approach from simply changing the previous implementation from CSV to Parquet.

First and foremost, keep in mind the strategy presented here for importing Parquet files into CrateDB, we have already covered this topic in a previous tutorial using a different approach from the one introduced in this tutorial, so feel free to have a look [here](https://community.cratedb.com/t/import-parquet-files-into-cratedb-using-apache-arrow-and-sqlalchemy/1161) and explore with the different possibilities out there.

## Prerequisites

Before getting started, you need to have some knowledge of Airflow and an instance of Airflow already running. Besides that, a CrateDB instance should already be set up before moving on with this tutorial. This SQL is also available in the setup folder in our [GitHub repository](https://github.com/crate/crate-airflow-tutorial).

We start by creating the two tables in CrateDB: A temporary staging table (`nyc_taxi.load_trips_staging`) and the final destination table (`nyc_taxi.trips`).

In this case, the staging table is a primary insertion point, which was later used to cast data to their final types. For example, the `passenger_count` column is defined as `REAL` in the staging table, while it is defined as `INTEGER` in the `nyc_taxi.trips` table.

```sql
CREATE TABLE IF NOT EXISTS "nyc_taxi"."load_trips_staging" (
   "VendorID" INTEGER,
   "tpep_pickup_datetime" TEXT,
   "tpep_dropoff_datetime" TEXT,
   "passenger_count" REAL,
   "trip_distance" REAL,
   "RatecodeID" REAL,
   "store_and_fwd_flag" TEXT,
   "PULocationID" INTEGER,
   "DOLocationID" INTEGER,
   "payment_type" INTEGER,
   "fare_amount" REAL,
   "extra" REAL,
   "mta_tax" REAL,
   "tip_amount" REAL,
   "tolls_amount" REAL,
   "improvement_surcharge" REAL,
   "total_amount" REAL,
   "congestion_surcharge" REAL,
   "airport_fee" REAL
);

CREATE TABLE IF NOT EXISTS "nyc_taxi"."trips" (
   "id" TEXT NOT NULL,
   "cab_type_id" INTEGER,
   "vendor_id" TEXT,
   "pickup_datetime" TIMESTAMP WITH TIME ZONE,
   "pickup_year" TIMESTAMP WITH TIME ZONE GENERATED ALWAYS AS DATE_TRUNC('year', "pickup_datetime"),
   "pickup_month" TIMESTAMP WITH TIME ZONE GENERATED ALWAYS AS DATE_TRUNC('month', "pickup_datetime"),
   "dropoff_datetime" TIMESTAMP WITH TIME ZONE,
   "store_and_fwd_flag" TEXT,
   "rate_code_id" INTEGER,
   "pickup_location" GEO_POINT,
   "dropoff_location" GEO_POINT,
   "passenger_count" INTEGER,
   "trip_distance" DOUBLE PRECISION,
   "trip_distance_calculated" DOUBLE PRECISION GENERATED ALWAYS AS DISTANCE("pickup_location", "dropoff_location"),
   "fare_amount" DOUBLE PRECISION,
   "extra" DOUBLE PRECISION,
   "mta_tax" DOUBLE PRECISION,
   "tip_amount" DOUBLE PRECISION,
   "tolls_amount" DOUBLE PRECISION,
   "ehail_fee" DOUBLE PRECISION,
   "improvement_surcharge" DOUBLE PRECISION,
   "congestion_surcharge" DOUBLE PRECISION,
   "total_amount" DOUBLE PRECISION,
   "payment_type" TEXT,
   "trip_type" INTEGER,
   "pickup_location_id" INTEGER,
   "dropoff_location_id" INTEGER,
   "airport_fee" DOUBLE PRECISION
)
PARTITIONED BY ("pickup_year");
```
To better understand how Airflow works and its applications, you can check other tutorials related to that topic [here](https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015). Also, if you are starting with CrateDB and haven’t set up any CrateDB instances before, have a look at our [documentation](https://crate.io/docs/crate/tutorials/en/latest/) and if you have any questions, otherwise, feel free to write a question in our [community](https://community.cratedb.com/).

Ok! So, once the tools are already set up with the corresponding tables created, we should be good to go.

## The Airflow DAG
![Airflow DAG workflow|690x76](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/29502f83c13d29d90ab703a399f58c6daeee6fe6.png)

The DAG pictured above represents a routine that will run every month to retrieve the latest released file by NYC TLC based on the execution date of that particular instance. Since it is configured to catch up with previous months when enabled, it will generate one instance for each previous month since January 2009 and each instance will download and process the corresponding month, based on the logical execution date.
The Airflow DAG used in this tutorial contains 6 tasks which are described below:

* **format_file_name:** according to the NYC Taxi and Limousine Commission (TLC) [documentation](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), the files are named after the month they correspond to, for example:
   ``` 
  https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-03.parquet
   ```
   The file path above corresponds to the data from March 2022. So, to retrieve a specific file, the task gets the date and formats it to compose the name of the specific file. Important to mention that the data is released with 2 months of delay, so it had to be taken into consideration.
* **process_parquet:** afterward, the name is used to download the file to local storage and then transform it from the Parquet format into CSV using CLI tools of [Apache Arrow](https://github.com/apache/arrow), as follows:
   * `curl -o "<LOCAL-PARQUET-FILE-PATH>" "<REMOTE-PARQUET-FILE>"`
   * `parquet-tools csv <LOCAL-PARQUET-FILE-PATH> > <CSV-FILE-PATH>`
   Both tasks are executed within one Bash Operator.
* **copy_csv_to_s3:** Once the newly transformed file is available, it gets uploaded to an S3 Bucket to then, be used in the [COPY FROM](https://crate.io/docs/crate/reference/en/5.1/sql/statements/copy-from.html) SQL.
* **copy_csv_staging:** copy the CSV file stored in S3 to the staging table described previously.
* **copy_stating_to_trips:** finally, copy the data from the staging table to the trips table, casting the columns that are not in the right type yet.
* **delete_staging:** after it is all processed, clean up the staging table by deleting all rows, and preparing for the next file.
* **delete_local_parquet_csv:** delete the files (Parquet and CSV) from the storage.

The DAG was configured based on the characteristics of the data in use. In this case, there are two crucial pieces of information about the data provider:

* How often does the data get updated
* When was the first file made available

In this case, according to the NYC TLC website “Trip data is published monthly (with two months delay)”. So, the DAG is set up to run monthly, and given the first file was made available in January 2009, the start date was set to March 2009. But why March and not January? As previously mentioned, the files are made available with 2 months of delay, so the first DAG instance, which has a logical execution date equal to "March 2009" will retrieve March as the current month minus 2, corresponding to January 2009, the very first file ever published.

You may find the full code for the DAG described above available in our [GitHub repository](https://github.com/crate/crate-airflow-tutorial/blob/main/dags/nyc_taxi_dag.py).

## Wrap up

The workflow represented in this tutorial is a simple way to import Parquet files to CrateDB by transforming them into a .csv file. As previously mentioned, there are other approaches out there, we encourage you to try them out. If you want to continue to explore CrateDB use cases with Airflow, have a look [here](https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015).
