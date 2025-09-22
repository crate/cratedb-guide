(airflow-import-parquet)=
# Automating the import of Parquet files with Apache Airflow

## Introduction

Use Airflow to import the NYC Taxi and Limousine dataset provided in Parquet format.

CrateDB supports `COPY FROM` for CSV and JSON, not Parquet. This guide is about converting
Parquet to CSV before loading.

For an alternative Parquet ingestion approach, see {ref}`arrow-import-parquet`.

## Prerequisites

Before you start, have Airflow and CrateDB running. The SQL shown below also
resides in the setup folder of the
[GitHub repository](https://github.com/crate/cratedb-airflow-tutorial).

Create two tables in CrateDB: a temporary staging table
(`nyc_taxi.load_trips_staging`) and the final table (`nyc_taxi.trips`).

Insert into the staging table first, then cast values into their final
types when inserting into `nyc_taxi.trips`. For example, `passenger_count`
is `REAL` in staging and `INTEGER` in `nyc_taxi.trips`.

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
To explore more Airflow use cases, see the related guides
{ref}`here <airflow-guides>`.

With the tools set up and tables created, proceed to the DAG.

## The Airflow DAG
![Airflow DAG workflow|690x76](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/29502f83c13d29d90ab703a399f58c6daeee6fe6.png)

The DAG pictured above represents a routine that will run every month to retrieve the latest released file by NYC TLC based on the execution date of that particular instance. Since it is configured to catch up with previous months when enabled, it will generate one instance for each previous month since January 2009 and each instance will download and process the corresponding month, based on the logical execution date.
The Airflow DAG used in this guide contains 7 tasks:
* **format_file_name:** according to the NYC Taxi and Limousine Commission (TLC) [documentation](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page), the files are named after the month they correspond to, for example:
   ```text
   https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-03.parquet
   ```
   The file path above corresponds to the data from March 2022. So, to retrieve a specific file, the task gets the date and formats it to compose the name of the specific file. Important to mention that the data is released with 2 months of delay, so it had to be taken into consideration.
* **process_parquet:** Use the formatted name to download the file to local storage and convert it from Parquet to CSV with `parquet-tools` (Apache Parquet CLI; see [Apache Arrow]).

  * `curl -o "<LOCAL-PARQUET-FILE-PATH>" "<REMOTE-PARQUET-FILE>"`
  * `parquet-tools csv <LOCAL-PARQUET-FILE-PATH> > <CSV-FILE-PATH>`

  Both commands run within one `BashOperator`.
* **copy_csv_to_s3:** Upload the transformed file to an S3 bucket and reference it in the {ref}`crate-reference:sql-copy-from` statement.
* **copy_csv_staging:** Copy the CSV file stored in S3 to the staging table described previously.
* **copy_staging_to_trips:** Copy data from the staging table to the trips table, casting columns to their final types.
* **delete_staging:** After processing, delete all rows from the staging table to prepare for the next file.
* **delete_local_parquet_csv:** Delete the local Parquet and CSV files.

The DAG was configured based on the characteristics of the data in use. In this case, there are two crucial pieces of information about the data provider:

* How often does the data get updated
* When was the first file made available

The NYC TLC publishes trip data monthly with a two‑month delay. Set the DAG to
run monthly with a start date of March 2009. The first run (logical date March
2009) downloads the file for January 2009 (logical date minus two months),
which is the first available dataset.

You may find the full code for the DAG described above available in our
[GitHub repository](https://github.com/crate/cratedb-airflow-tutorial/blob/main/dags/nyc_taxi_dag.py).

## Wrap up

The workflow represented in this guide is a simple way to import Parquet files
to CrateDB by transforming them into a CSV file. As previously mentioned, there
are other approaches out there, we encourage you to try them out.

To continue exploring CrateDB with Airflow, browse the related guides
{ref}`here <airflow-guides>`.


[Apache Arrow]: https://github.com/apache/arrow
