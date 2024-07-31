(timeseries-analysis-advanced)=
(timeseries-analysis-weather)=
(timeseries-querying)=

# Time Series: Analyzing Weather Data

CrateDB is a powerful database designed to handle various use cases, one of
which is managing time series data. Time series data refers to collections of
data points recorded at specific intervals over time, like the hourly
temperature of a city or the daily sales of a store.

:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 6 6 6

:::{rubric} About
:::

Effectively query observations using enhanced features for time series data.

Run aggregations with gap filling / interpolation, using common
table expressions (CTEs) and LAG / LEAD window functions.

Find maximum values using the MAX_BY aggregate function, returning
the value from one column based on the maximum or minimum value of another
column within a group.
::::

::::{grid-item}
:class: rubric-slimmer
:columns: auto 6 6 6

:::{rubric} Data
:::
For this tutorial, imagine a dataset that captures weather
readings from CrateDB offices across the globe. Each record includes:

:timestamp: The exact time of the recording.
:location: The location of the weather station.
:temperature: The temperature in degrees Celsius.
:humidity: The humidity in percentage.
:wind_speed: The wind speed in km/h.
::::

:::::


## Creating the Table

CrateDB uses SQL, the most popular query language for database management. To
store the weather data, create a table with columns tailored to the
dataset using the `CREATE TABLE` command:

:::{code} sql
CREATE TABLE "weather_data" (
    "timestamp" TIMESTAMP,
    "location" VARCHAR,
    "temperature" DOUBLE,
    "humidity" DOUBLE,
    "wind_speed" DOUBLE
);
:::

Run the above SQL command in CrateDB to set up your table. With the table ready,
you are now set to insert the dataset.


## Inserting Data

Insert the data using the `COPY FROM` SQL statement.

:::{code} sql
COPY weather_data
FROM 'https://github.com/crate/cratedb-datasets/raw/main/cloud-tutorials/data_weather.csv.gz'
WITH (format='csv', compression='gzip', empty_string_as_null=true);
:::


## Analyzing Data

Start with a basic `SELECT` statement on all columns, and limit the output to
display only 10 records, in order to quickly explore a few samples worth of data.

:::{code} sql
SELECT *
FROM weather_data
LIMIT 10;
:::

CrateDB is built for fast aggregation using the columnar storage to speed up
queries. For example, calculate the average temperature for each location by using the
`AVG` aggregation function:

:::{code} sql
SELECT location, AVG(temperature) AS avg_temp
FROM weather_data
GROUP BY location;
:::

:::{rubric} MAX_BY Aggregate Functions
:::
Computing basic averages is nothing special, but what if you need to answer more detailed
questions? For example, if you want to know the highest temperature for each
place and when it occurred.

Simple groupings might not be enough, but
thankfully, CrateDB has enhanced tools for time series data. You can use the
`max_by(returned_value, maximized_value)` function, which gives you a value (like
the time) when another value (like the temperature) is at its highest.

Let's put this to use with the following query:

:::{code} sql
SELECT location,
       max(temperature) AS highest_temp,
       max_by(timestamp, temperature) AS time_of_highest_temp
FROM weather_data
GROUP BY location;
:::

:::{rubric} Gap Filling
:::
You have probably observed by now, that there are gaps in the dataset for certain
metrics. Such occurrences are common, perhaps due to a sensor malfunction or
disconnection. To address this, the missing values need to be filled in.

Window functions paired with the `IGNORE NULLS` feature will solve your needs.
Within a Common Table Expression (CTE), we utilize window functions to
spot the next and prior non-null temperature recordings, and then compute the 
arithmetic mean to fill the gap.

:::{code} sql
WITH OrderedData AS (
    SELECT timestamp,
           location,
           temperature,
           LAG(temperature, 1) IGNORE NULLS OVER w AS prev_temp,
           LEAD(temperature, 1) IGNORE NULLS OVER w AS next_temp
    FROM weather_data
    WINDOW w AS (PARTITION BY location ORDER BY timestamp)
)
SELECT timestamp,
       location,
       temperature,
       COALESCE(temperature, (prev_temp + next_temp) / 2) AS interpolated_temperature
FROM OrderedData
ORDER BY location, timestamp;
:::

The `WINDOW` clause defines a window that partitions the data by location and
orders it by timestamp.

This ensures that the `LAG` and `LEAD` window functions operate within each
location group chronologically. If the temperature value is defined as `NULL`,
the query returns the interpolated value calculated as the average of the
previous and next available temperature readings. Otherwise, it uses the
original value.
