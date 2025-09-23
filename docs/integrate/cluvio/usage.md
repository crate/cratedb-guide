(cluvio-usage)=
# Data Analysis with Cluvio and CrateDB

## Introduction

Use [Cluvio] with [CrateDB Cloud] to analyze data and build interactive
dashboards.

## Prerequisites

* [CrateDB Cloud cluster up and running](https://crate.io/docs/cloud/en/latest/tutorials/cluster-deployment/index.html)
* [Cluvio account](https://www.cluvio.com/)


## Set up CrateDB

Deploying a CrateDB cloud cluster has never been easier, simply follow our tutorial [here](https://crate.io/docs/cloud/en/latest/tutorials/cluster-deployment/stripe.html#cluster-deployment-stripe) and you can have a cluster up and running within minutes. We offer a CRFREE plan which offers up to 2 vCPUs, 2 GiB of memory, and 8 GiB of storage completely for free. Ideal for small-scale testing and evaluation purposes.

### Load data into CrateDB

In this usage guide, you use two tables—[flights](http://stat-computing.org/dataexpo/2009) and [airports](https://openflights.org/data.php)—from January 2008.

#### Create tables

Once you have access to the Admin UI of your cluster, execute these statements in the console:

```sql
CREATE TABLE airports (
  code character varying(3) NOT NULL,
  name character varying(100) NOT NULL,
  city character varying(50) NOT NULL,
  country character varying(50) NOT NULL,
  latitude double precision NOT NULL,
  longitude double precision NOT NULL,
  elevation integer NOT NULL
);
```

```sql
CREATE TABLE flights (
  year integer,
  month integer,
  day_of_month integer,
  day_of_week integer,
  dep_time  integer,
  crs_dep_time integer,
  arr_time integer,
  crs_arr_time integer,
  unique_carrier varchar(6),
  flight_num integer,
  tail_num varchar(8),
  actual_elapsed_time integer,
  crs_elapsed_time integer,
  air_time integer,
  arr_delay integer,
  dep_delay integer,
  origin varchar(3),
  dest varchar(3),
  distance integer,
  taxi_in integer,
  taxi_out integer,
  cancelled integer,
  cancellation_code varchar(1),
  diverted varchar(1),
  carrier_delay integer,
  weather_delay integer,
  nas_delay integer,
  security_delay integer,
  late_aircraft_delay integer,
  dep_timestamp timestamp,
  arr_timestamp timestamp
);
```

This creates 2 empty tables in your database. `flights` and `airports`, with the correct data types of the columns. 

#### Import data

Now you should import the data into the tables. We will use Console "Import" feature in this example. Use the following links:

* [Airports CSV (GZIP)]
* [Flights CSV (GZIP)]

![.csv import|690x315](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/0/059227c592c98e2025b64c1d2d22e20c24624359.png)

Make sure to use your pre-created tables in the "Table name" field, otherwise the column types may be created incorrectly. Do this for both .csv files:

![Import summary|690x224](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/3/364db0dc98d56d8e27e274fd072cb5f076cf1110.png)

After import, `airports` should contain about 5,876 rows and `flights` about 150,000 rows.

## Connect CrateDB to Cluvio

Now that you have the dataset to visualize, you can connect your cluster to Cluvio.

In Cluvio, navigate to `Settings` -> `Datasources` -> `Add datasource`:

![Connecting CrateDB to Cluvio|649x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/9/9e05b3e35de868cc4cc33efb232afcf892652276.png){width=640}

`Host` and `Password` will understandably differ for you.

After filling out the details for your cluster, press `Next: Test Connection`. If the credentials are correct, you should see this success message:

![Successful connection message|690x110](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/2/2cd3cd0945b219ca0010ce672ee9808324ba4cfa.png){width=640}

## Dashboards

A dashboard is the main point of Cluvio. It is a collection of interactive reports, giving great insight into any area of your data. These are the types of charts Cluvio offers:

* [Table Chart](https://docs.cluvio.com/chart-types/table-chart)
* [Pivot / Cohort Table Chart](https://docs.cluvio.com/chart-types/pivot-cohort-table-chart)
* [Number Chart](https://docs.cluvio.com/chart-types/number-chart)
* [Pie Chart](https://docs.cluvio.com/chart-types/pie-chart)
* [Line Chart](https://docs.cluvio.com/chart-types/line-chart)
* [Bar Chart](https://docs.cluvio.com/chart-types/bar-chart)
* [Map Chart](https://docs.cluvio.com/chart-types/map-chart)
* [Gauge Chart](https://docs.cluvio.com/chart-types/gauge-chart)
* [XY / Bubble Chart](https://docs.cluvio.com/chart-types/xy-bubble-chart)
* [Word Cloud Chart](https://docs.cluvio.com/chart-types/word-cloud-chart)
* [Histogram Chart](https://docs.cluvio.com/chart-types/histogram-chart)

![Example dashboard|690x343](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/4/4cc716d7a71c91476dfe2affa55881d39afe5d93.png){width=800px}

Now, let's create some and see how Cluvio works. Head to **[Dashboards](https://app.cluvio.com/dashboards)** -> `New Dashboard`. After naming your Dashboard, you can create your first report. Click the `New report` in the upper right.

### Number of flights and delays

The first piece of information for a given period is the number of flights and
the average departure and arrival delays. Use this query:

```sql
SELECT
       COUNT(*)       AS "Number of flights",
       AVG(dep_delay) AS "Average Departure Delay",
       AVG(arr_delay) AS "Average Arrival Delay"
FROM   doc.flights
ORDER  BY 1
``` 
This is a pretty simple query that counts the number of rows in the `flights` as the number of flights, and averages values in the `dep_delay` and `arr_delay` for the departure delays and arrival delays respectively.

![Number of flights and delays|690x117](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/4/4841404a21b56cb1e5b92736af8b79656b0912ec.png){width=800px}

After running the query, switch the visualization to the “Number” chart.

### Country distribution

This query looks at the country distribution in the `airports` table:

```sql
SELECT   country,
         COUNT(1)
FROM     doc.airports
GROUP BY country
ORDER BY 2 DESC
```

In this one, it's suitable to use pie chart to better see the distribution. We also used the `Value(%)` option for the legend, and edited the legend to show up to 25 values (countries).

![Country distribution|690x452](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/2/2f11e42d61e93395267f847b3ee91d5be0d076f9.png){width=800px}

## Filters

[Filters](https://app.cluvio.com/settings/filters) offer a great way to quickly specify the condition under which you want to display your data. 

In the `flights` table in `day_of_week` column 1 represents Monday, 2 means Tuesday, etc. Using that, we can create a filter to display data for a specific day of the week without changing the SQL in our reports.

```sql
VALUES 
(1, 'Monday'),
(2, 'Tuesday'),
(3, 'Wednesday'),
(4, 'Thursday'),
(5, 'Friday'),
(6, 'Saturday'),
(7, 'Sunday')
ORDER BY 1
```

Now we can filter the data by day of the week:

![Using filter to display data for specific day of the week|690x255](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/9/90335d44316d329ebe6d70a6a63879dec52ee5e8.png){width=800px}

Learn more in the [Cluvio Filters overview](https://docs.cluvio.com/filters/overview).

## SQL snippets

SQL snippets are small reusable pieces of code that can make your work easier within larger dataset. They are managed [here](https://app.cluvio.com/settings/sql-snippets).

We used them to create JOIN statements:

```sql
JOIN doc.airports AS origin_airport ON flights.origin = origin_airport.code
JOIN doc.airports AS dest_airport ON flights.dest = dest_airport.code
```

This snippet creates two joins between the `flights` and `airports` tables, aliasing the `airports` table as `origin_airport` and `dest_airport` for the origin and destination airports, respectively.

Then create a report using the snippet:

```sql
SELECT flights.year,
       flights.month,
       origin_airport.city AS origin_city,
       dest_airport.city AS destination_city,
       COUNT(*) AS number_of_flights
FROM doc.flights
[join_airports] -- Reference to the SQL Snippet
WHERE [flight_filters] -- Reference our filters
GROUP BY flights.year, flights.month, origin_airport.city, dest_airport.city
ORDER BY number_of_flights DESC
LIMIT 100;
```

Using SQL snippets and filters, you can quickly find the most popular
destination departing from Los Angeles (LAX) on a Tuesday.

![Popular destinations|690x309](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/7/7257af47c58215459e1fe2de135a966c19fedbd5.png){width=800px}

## Conclusion

That’s it for this. Get started in the [CrateDB Cloud Console],
connect your cluster to [Cluvio], and begin analyzing your data. Explore
features in the [Cluvio documentation].


[Airports CSV (GZIP)]: https://s3.amazonaws.com/crate.sampledata/flights/dataset-airports.csv.gz
[Flights CSV (GZIP)]: https://s3.amazonaws.com/crate.sampledata/flights/dataset-flights.csv.gz

[Cluvio]: https://www.cluvio.com/
[Cluvio documentation]: https://docs.cluvio.com/
[CrateDB Cloud]: https://console.cratedb.cloud/
[CrateDB Cloud Console]: https://console.cratedb.cloud/
