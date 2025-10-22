(timeseries-objects)=
(timeseries-with-metadata)=
(timeseries-tutorial-metadata)=

# Analyzing Device Readings with Metadata Integration

:::{article-info}
---
avatar: https://sea2.discourse-cdn.com/flex020/user_avatar/community.cratedb.com/marija/288/428_2.png
avatar-link: https://github.com/marijaselakovic
avatar-outline: muted
author: Marija Selakovic
date: November 15, 2023
read-time: 6 min read
class-container: sd-p-2 sd-outline-muted sd-rounded-1
---
:::

:::{include} /_include/links.md
:::

CrateDB is highly regarded as an optimal database solution for managing
time series data thanks to its unique blend of features. It is particularly
effective when you need to combine time series data with metadata, for
instance, in scenarios where data like sensor readings or log entries, need
to be augmented with additional context for more insightful analysis.


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slimmer
:columns: auto 6 6 6

:::{rubric} About
:::

CrateDB supports effective time series analysis with enhanced features
for fast aggregations.

- Rich data types for storing structured nested data (OBJECT) alongside
  time series data.
- A rich set of built-in functions for aggregations.
- Relational JOIN operations.
- Common table expressions (CTEs).

::::

::::{grid-item}
:class: rubric-slimmer
:columns: auto 6 6 6

:::{rubric} Data
:::
This tutorial illustrates how to effectively query time series data with
metadata, in order to conduct comprehensive data analysis.

It uses a time series dataset that includes telemetry readings from appliances,
such as battery, CPU, and memory information, as well as metadata information
like manufacturer, model, and firmware version.
::::

:::::


## Creating the Tables

:::{div}
The fastest and easiest way to get started with CrateDB is by deploying a
free tier (CRFREE) cluster on [CrateDB Cloud][CrateDB Cloud Console]. Otherwise,
see the {ref}`install` section to run CrateDB yourself.
:::

CrateDB uses SQL, the most popular query language for database management. To
store the device readings and the device info data, define two tables with
columns tailored to the datasets.

To get started, let’s use a time series dataset that captures various device
readings, such as battery, CPU, and memory information. Each record includes:

:ts: Timestamp when each reading was taken.
:device_id: Identifier of the device.
:battery: Object containing battery level, status, and temperature.
:cpu: Object containing average CPU loads over the last 1, 5, and 15 minutes.
:memory: Object containing information about the device's free and used memory.

The second dataset in this tutorial contains metadata information about various
devices. Each record includes:

:device_id: Identifier of the device.
:api_version: Version of the API that the device supports.
:manufacturer: Name of the manufacturer of the device.
:model: Model name of the device.
:os_name: Name of the operating system running on the device.

Create the tables using the `CREATE TABLE` command:

:::{code} sql
CREATE TABLE IF NOT EXISTS doc.devices_readings (
   "ts" TIMESTAMP WITH TIME ZONE,
   "device_id" TEXT,
   "battery" OBJECT(DYNAMIC) AS (
      "level" BIGINT,
      "status" TEXT,
      "temperature" DOUBLE PRECISION
   ),
   "cpu" OBJECT(DYNAMIC) AS (
      "avg_1min" DOUBLE PRECISION,
      "avg_5min" DOUBLE PRECISION,
      "avg_15min" DOUBLE PRECISION
   ),
   "memory" OBJECT(DYNAMIC) AS (
      "free" BIGINT,
      "used" BIGINT
   )
);
:::

:::{code} sql
CREATE TABLE IF NOT EXISTS doc.devices_info (
   "device_id" TEXT,
   "api_version" TEXT,
   "manufacturer" TEXT,
   "model" TEXT,
   "os_name" TEXT
);
:::

Using objects in the `devices_readings` dataset allows for the structured and efficient organization of complex, nested data, enhancing both data integrity and flexibility. 

## Inserting Data

Now, insert the data using the `COPY FROM` SQL statement.

:::{code} sql
COPY doc.devices_info
FROM 'https://cdn.crate.io/downloads/datasets/cratedb-datasets/cloud-tutorials/devices_info.json.gz'
WITH (compression='gzip', empty_string_as_null=true)
RETURN SUMMARY;
:::

:::{code} sql
COPY doc.devices_readings
FROM 'https://cdn.crate.io/downloads/datasets/cratedb-datasets/cloud-tutorials/devices_readings.json.gz'
WITH (compression='gzip', empty_string_as_null=true)
RETURN SUMMARY;
:::

## Analyzing Data


:::{rubric} JOIN Operations
:::
To illustrate `JOIN` operations, the first query retrieves the 30 rows of combined data from two tables, `devices.readings` and `devices.info`, based on a matching `device_id` in both. It effectively merges the detailed readings and corresponding device information, providing a comprehensive view of each device's status and metrics.

:::{code} sql
SELECT *
FROM devices.readings r
JOIN devices.info i ON r.device_id = i.device_id
LIMIT 30;
:::


:::{rubric} Aggregate Values
:::
The next query illustrates the calculation of summaries for aggregate values. In particular, it finds average battery levels (`avg_battery_level`) for each day and shows the result in an ascending order.

:::{code} sql
SELECT date_trunc('day', ts) AS "day", AVG(battery['level']) AS avg_battery_level
FROM doc.devices_readings
GROUP BY "day"
ORDER BY "day";
:::


:::{rubric} Rolling Averages and Window Functions
:::
Rolling averages are crucial in time series analysis because they help smooth out short-term fluctuations and reveal underlying trends by averaging data points over a specified period. This approach is particularly effective in mitigating the impact of outliers and noise in the data, allowing for a clearer understanding of the true patterns in the time series. 

The following example illustrates the average (`AVG`), minimum (`MIN`), and maximum (`MAX`) battery temperature over a window of the last 100 temperature readings (`ROWS BETWEEN 100 PRECEDING AND CURRENT ROW`). The window is defined in descending order by timestamp (`ts`) and can be adapted to support different use cases. 

:::{code} sql
SELECT r.device_id,
       AVG(battery['temperature']) OVER w AS "last 100 temperatures",
       MIN(battery['temperature']) OVER w AS "min temperature",
       MAX(battery['temperature']) OVER w AS "max temperature"
FROM doc.devices_readings r
JOIN doc.devices_info i ON r.device_id = i.device_id
WINDOW w AS (ORDER BY "ts" DESC ROWS BETWEEN 100 PRECEDING AND CURRENT ROW);
:::


:::{rubric} Most Recent Observation
:::
The next query shows how to extract the most recent reading for each device of
the _mustang_ model. The query selects the latest timestamp (`MAX(r.ts)`),
which represents the most recent reading time, and the corresponding latest
readings for battery, CPU, and memory. It uses `MAX_BY` for each respective
component, using the timestamp as the determining factor.

These results are grouped by `device_id`, `manufacturer`, and `model` to ensure
that the latest readings for each unique device are included. This query is
particularly useful for monitoring the most current status of specific devices
in a fleet.

:::{code} sql
SELECT 
    MAX(r.ts) as time,
    r.device_id,
    MAX_BY(r.battery, r.ts) as battery,
    MAX_BY(r.cpu, r.ts) as cpu,
    MAX_BY(r.memory, r.ts) as memory,
    i.manufacturer,
    i.model
FROM 
    devices_readings r
JOIN 
    devices_info i ON r.device_id = i.device_id
WHERE 
    i.model = 'mustang'
GROUP BY 
    r.device_id, i.manufacturer, i.model;
:::


:::{rubric} Common Table Expressions (CTEs)
:::
Finally, we illustrate the use of Common Table Expressions (CTEs) on behalf of
a complex query to aggregate and analyze device readings and metadata information.
The query relies on three CTEs to temporarily capture data.

:max_timestamp:
    Find the most recent timestamp (`MAX(ts)`) in the
    `doc.devices_readings` table. This CTE is used to focus the analysis
    on recent data.

:device_readings_agg:
    Calculate the average battery level and temperature for each
    device, but only for readings taken within the last week, as defined by
    `r.ts >= m.max_ts - INTERVAL '1 week'`. 

:device_model_info:
    Select details from the `doc.devices_info` table, specifically
    the `device_id`, `manufacturer`, `model`, and `api_version`, but only for
    devices with an API version between 21 and 25.

The main `SELECT` statement joins the `device_readings_agg` and `device_model_info`
CTEs, and aggregates data to provide the average battery level and temperature
for each combination of manufacturer, model, and API version.
It also provides the number of readings (`COUNT(*)`) for each grouping.

The query aims to provide a detailed analysis of the battery performance (both level and temperature) for devices with specific API versions, while focusing only on recent data. It allows for a better understanding of how different models and manufacturers are performing in terms of battery efficiency within a specified API range and time frame.

:::{code} sql
WITH 
max_timestamp AS (
    SELECT MAX(ts) AS max_ts
    FROM doc.devices_readings
),
device_readings_agg AS (
    SELECT 
        r.device_id,
        AVG(r.battery['level']) AS avg_battery_level,
        AVG(r.battery['temperature']) AS avg_battery_temperature
    FROM 
        devices_readings r, max_timestamp m
    WHERE 
        r.ts >= m.max_ts - INTERVAL '1 week'
    GROUP BY 
        r.device_id
),
device_model_info AS (
    SELECT 
        device_id,
        manufacturer,
        model,
        api_version
    FROM 
        devices_info
    WHERE 
        api_version BETWEEN 21 AND 25
)
SELECT 
    info.manufacturer,
    info.model,
    info.api_version,
    AVG(read.avg_battery_level) AS model_avg_battery_level,
    AVG(read.avg_battery_temperature) AS model_avg_battery_temperature,
    COUNT(*) AS readings_count
FROM 
    device_readings_agg read
JOIN 
    device_model_info info 
ON 
    read.device_id = info.device_id
GROUP BY 
    info.manufacturer, 
    info.model, 
    info.api_version
ORDER BY 
    model_avg_battery_level DESC;
:::


:::{rubric} Conclusion
:::

This tutorial has guided you through the process of querying and
analyzing time series data with CrateDB, demonstrating how to effectively merge
device metrics with relevant metadata.

These techniques and queries are important for unlocking deeper insights into
device performance, equipping you with the skills needed to harness the full
potential of time series data in real-world applications.
