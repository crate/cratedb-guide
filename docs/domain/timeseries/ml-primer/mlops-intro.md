(tsml-primer-mlops-intro)=

# Introduction to MLOps

_Introduction to Time Series Modeling with CrateDB (Part 2)._

This is part two of the "Machine Learning for Time Series Data Primer".

## Thoughts

While creating a machine learning model itself is an important step, it is only
the first step in the process. The real challenge is in operating a model in a
production environment.

The actual model serving and deployment, accompanied by a robust workflow for
building your models and running them in production, includes at least the
following components:

![Elements of Machine Learning Operations](/_assets/img/ml-timeseries-primer/cratedb-mlops.png){width=400px}

[MLOps] or ML Ops is a paradigm that aims to deploy and maintain machine
learning models in production reliably and efficiently, including experiment
tracking.

The next sections will explore each of these processes, and how CrateDB can help you with them.


## Data Ingestion & Management

In the context of a Machine Learning Operations workflow, especially with time series analysis, the
initial and significant step is Data Ingestion. It is the process of taking data from various sources
and funneling it into one repository where it can be accessed, used, and analyzed.

In case of time
series analysis, you are mostly concerned with datasets that have a time component - these could be
logs from web servers, sensor data, financial data, etc. Given the high volume and the high velocity
of data in these scenarios, it is imperative that the data ingestion infrastructure is built to handle
this scale and complexity.

This section will give you a detailed overview about different areas of data management, and outlines
where CrateDB has its specific strengths.

### Performance and Scalability

This is where CrateDB can play a pivotal role: One of the key capabilities is the capacity to handle the
ingestion of large amounts of data at high velocity and in near real-time, while serving many data consumers at the same time. 
CrateDB is a distributed SQL database that excels in ingesting massive amounts of machine data or logs, vital in time series
analysis.

Moreover, with its distributed architecture, CrateDB makes data ingestion more scalable
and hence, if you need to increase the number of data sources, or the rate at which the data is being
created, CrateDB effortlessly scales horizontally.

### Real-time Querying

Also, crucial is the fact that CrateDB allows you to query the data in near real-time while it is
being ingested. This feature aligns
brilliantly with the requirements of data ingestion for time series analysis as it permits immediate
action upon the data, enabling real-time insights into the trends of your time series data.

### Wide Tables and Table Joins

Notably, CrateDB can easily accommodate hundreds of columns in a single table. Looking at - for
example - M2M/IoT data from industrial machines, there are easily hundreds or even thousands of time
series from a single machine: speeds, pressures, temperatures, etc., from various axis and sensors.
The use cases are not limited to manufacturing, the same is true for personalization in e-commerce, log analysis, 
or modern application backends.

In CrateDB, you can model this data in a single table, which makes it convenient to query and analyze.
Without this feature, one is tasked with the tedious and error-prone task of joining multiple tables
to get a complete picture of the data.

### Partitioning

Another distinguishing trait of CrateDB's capacity for managing time series data is its robust
support for [time partitioning]. It enables data to be stored long-term without needing to be
aggregated and down-sampled.

This is of significant importance, because the original, un-aggregated
data often contains granular details that may be lost during aggregation. By preserving those
nuances, businesses can enjoy enhanced flexibility, be it to revisit historical data for new
insights, or conduct precise forecasting, which is crucial to strategic decision-making processes.

### Sharding

CrateDB's [Shard allocation filtering] feature permits fine-grained control about which shards
and partitions are allocated to which database node.

In combination with the time partitioning mentioned above, you are able to move
older chunks to slow but cheap spinning disks, while keeping the most recent data on fast SSDs,
all while retaining fast query speed for most recent data, and not loosing any details in older
data due aggregation or downsampling.

### Data Schema

Utilizing CrateDB's [dynamic object columns],
you can store metadata side by side with measurement data, which is especially useful for time
series data. For example, you can store the location of a sensor, the type of sensor, the unit of
measurement, etc., in the same table as the measurement data.

This again eases data modeling and
data exploration: There is no need for complex database operations, sometimes across different types
of databases, to get the complete picture about your data.

### Example

Let us discuss a small example here: Building on top of the temperature data used for the anomaly
detection model, assume multiple sensors in different locations for different machine parts.

Furthermore, these sensors also emit different data formats or units (eg. Celsius vs. Kelvin) and
some of them additionally measure CO2 concentration. In CrateDB, you can model these details to be
stored within a single column using the [OBJECT data type].

```sql
ALTER TABLE machine_data ADD COLUMN sensor_description OBJECT(DYNAMIC);
```

Now, insert the data into the table, including the sensor properties:

```sql
INSERT INTO machine_data (timestamp, value, sensor_description)
    VALUES (1686022200000, 81, '{
    "type": "SX39",
    "unit": "celsius",
    "features": [
        "temperature",
        "co2",
        "pressure"
    ],
    "location": "axis-b-2"
    }');
```

CrateDB automatically creates the schema based on the inserted data.

![Dynamic Object Schema with CrateDB](/_assets/img/ml-timeseries-primer/cratedb-schema-object.png){width=480px}

Without additional steps, you can query the data as follows. To inquire all sensors with
the CO2 feature, use this SQL statement:

```sql
SELECT * FROM machine_data WHERE 'co2' = ANY(sensor_description['features']);
```

![Result of nested object query](/_assets/img/ml-timeseries-primer/cratedb-sensor-record.png){width=480px}

**Tip:** `OBJECT` columns are very convenient and flexible.
During development, more often than not, you need to add additional metadata attributes to your
data model entities. This is possible without further ado.

CrateDB will automatically add the appropriate nested objects when referring to them within the
INSERT statement. To learn more about how CrateDB handles object columns and how to configure them,
please refer to the [Object column policy] documentation.


## Exploratory Data Analysis

Exploratory Data Analysis (EDA) is an indispensable stage in the machine learning workflow, including
time series analysis. EDA involves visualizing, summarizing, and analyzing data, to uncover patterns,
anomalies, or relationships within the dataset.

The objective of this step is to gain an understanding
and intuition of the data, identify potential issues, and guide feature engineering and model building.

### Requirements and Features

Requirements for EDA include efficient data handling, storage, and both interactive and automated
querying capabilities, along with robust support for standards-based, open-source data analysis and
visualization libraries, in order to leverage the full potential of data exploration.

CrateDB provides features to support the exploration phase in form of robust SQL syntax support that
encompasses commands and functions specific to time series data. Some examples, amongst others, are:

### Last Observation Carried Forward

More often than not, you are working with time series data using different sampling intervals. When
processing such data, you will most likely run into situations where you will have gaps in your data,
mostly represented by non-value symbols like `NULL` or `NaN`.

![Alt text](/_assets/img/ml-timeseries-primer/cratedb-missing-values.png){width=480px}

To fill these gaps, you can use CrateDB's `LAG` function, with their `IGNORE NULLS` option.

```sql
SELECT "time",
    COALESCE(battery_level, LAG(battery_level) IGNORE NULLS OVER w) AS battery_level,
    COALESCE(battery_status, LAG(battery_status) IGNORE NULLS OVER w) AS battery_status,
    COALESCE(battery_temperature, LAG(battery_temperature) IGNORE NULLS OVER w) AS battery_temperature
FROM machine_data
WINDOW w AS (ORDER BY "time");
ORDER BY "time";
```

### Resampling

Another option is to resample your time series data to use the same intervals on the time axis.
You can use CrateDB's `date_bin` function for that purpose. This query will resample the data
to 5 minute intervals, and return the most recent value for each interval.

```sql
SELECT ts_bin,
   battery_level,
   battery_status,
   battery_temperature
FROM (
SELECT DATE_BIN('5 minutes'::INTERVAL, "time", 0) AS ts_bin,
        battery_level,
        battery_status,
        battery_temperature,
        ROW_NUMBER() OVER (PARTITION BY DATE_BIN('5 minutes'::INTERVAL, "time", 0) ORDER BY "time" DESC) AS "row_number"
FROM machine_data
) x
WHERE "row_number" = 1
ORDER BY 1 ASC
```

### Window Functions

Window functions are of high importance for convenient EDA. They have been presented in the
"Last Observation Carried Forward" example already.

### Joins

I can't stress the importance of joins in EDA scenarios. When designing your core data model, you
will certainly end up with having time series data in one table, and corresponding metadata in
another one.

Without database joins, you can easily end up loading large amounts of data into your application
just for the purpose on doing joins there, putting huge stress on your application infrastructure.

With CrateDB, you can push down join operations to the database cluster, only needing to load the
results into your application.

```sql
SELECT m.timestamp, AVG(m.temperature), d.location
FROM measurements m INNER JOIN devices d
ON m.device_id = d.id
GROUP BY m.timestamp, d.location
ORDER BY m.timestamp;
```

### Other Exploratory Data Analysis Features

CrateDB's **seamless integration** with contemporary data visualization tools like Grafana, or
libraries like Matplotlib, and compatibility with the Java- and Python-based data ecosystem and
corresponding libraries and frameworks such as pandas, Dask, or Spark, ensures easy, effective,
and rapid EDA capabilities.

CrateDB's **time partitioning** is also great for EDA. CrateDB automatically selects the partitions
to load data from, based on the time filter in your query expression. This allows CrateDB to only
touch the chunks of data relevant to the query you are interested in.

Considering that typical exploration workflows are based on raw data, not resampled yet, because
you simply don't know how to aggregate your data yet without losing potentially meaningful insights,
this is an important property of CrateDB.


## Feature Engineering

Feature engineering is a crucial step in the machine learning process, whereby raw data is transformed
into features that can improve the performance of a machine learning model, or make a model possible at
all. This can involve simple transformations, encoding categorical variables, generating interaction
features, and more.

In time series analysis, feature engineering is often more complex due to temporal dependencies and
unique characteristics such as trend, seasonality, and auto-correlation. Here are some commonly used
features in time series analysis and how they can be created:

1. **Lagged Values**: These are values from a prior period in time. If you are predicting the stock
   price for tomorrow, based on, for example, the stock price today, yesterday, or a few days ago,
   those would be lagged values.

2. **Rolling Window Statistics**: A common approach for feature engineering in time series analysis,
   is to create features that summarize the values in a window of time. For instance, the arithmetic
   mean, standard deviation, or skewness of the past 7 days, 30 days, or any other period could be
   useful for prediction.

3. **Date Time Features**: Depending on the specifics of the task and the available data, other features
   as the hour of day, day of week, month, quarter, year, and whether the instance is on a holiday or not,
   can be used. This can be created using pandas' `.dt` accessor.

4. **Domain-Specific Features**: These are features specific to your dataset or problem, and require
   domain knowledge to craft. For instance, in predicting stock prices, features could be various financial
   indicators like PE ratio, or EPS.

CrateDB's SQL syntax and time partitioning capabilities are of great help here. For example,
to create lagged values, you can use the [window function] support in CrateDB, together with the  
`LAG` function:

```sql
SELECT
  dept_id,
  year,
  budget,
  LAG(budget) OVER(PARTITION BY dept_id) prev_budget
FROM financial_table
as t (dept_id, year, budget);
```

(mlops-feature-store)=
### Online Feature Store

You will not only need these features for training, but also for inference. This is where an online
feature store comes into play.

An online feature store is a production-grade repository where your live, operational data is
stored for machine learning operations. Its main purpose is to serve features in real-time to
operational or online machine learning models. These stores improve the consistency of features
between training and serving, help manage features, and ensure low latency access for real-time
predictions.

As data arrives continuously in time series analysis, the feature store needs to process new data
quickly and almost in real-time. Traditional feature stores designed for static features like
customer demographics or behavior mostly do not offer the scaling requirements specifically needed
for highly dynamic time series data.

Utilizing CrateDB's high-speed data ingestion, and low-latency query performance even with complex
SQL queries, as well as their support for [database VIEWs],
you can define features in a view data model and get up-to-date features as soon as new data
arrives.


## Model building and training

Model building at its core is the step where you will use the raw data and the created feature to
actually select and train a machine learning model.

This article will not dive into the details of creating machine learning
models. For a quick recap, please also refer to the introduction chapter at
[](#tsml-primer-anomaly-detection).


## Experiment Tracking

Experiment tracking is one of the more overlooked but majorly important steps of any machine
learning endeavour. It refers to the practice of systematically recording and organizing
information concerning your model building and training efforts, such as the models used,
hyperparameters, feature transformations, and ultimately, the results and performance metrics.

In even the simplest machine learning project, you will want to test several models with a variety
of parameters, so maintaining a methodical documentation helps you in avoiding redundancy,
understanding discrepancies between results, and finding the best usability of the model.

I can't stress the importance of experiment tracking enough, so let me enumerate a few topics
why you also should be concerned about it.


1. **Reproducability**: It ensures you or any member of your team can reproduce an experiment at
any time. This is particularly vital when you have to verify your results or try to improve
your model in the future.


2. **Collaboration**: In a team setting, experiment tracking fosters a seamless collaboration
because everyone can understand and access all experiment details, enhancing overall productivity.


3. **Model comparison**: With the tracked data and performance metrics, you can compare different
models and choose the one best suited to your problem. This step alone justifies the need for
experiment tracking and any investment required to implement it.


4. **Accountability**: Documenting all the steps of your experiment ensures accountability in your
machine learning process.


[database VIEWs]: inv:crate-reference#ddl-views
[dynamic object columns]: https://cratedb.com/blog/handling-dynamic-objects-in-cratedb
[MLOps]: https://en.wikipedia.org/wiki/MLOps
[OBJECT data type]: inv:crate-reference#type-object
[Shard allocation filtering]: inv:crate-reference#ddl_shard_allocation
[time partitioning]: inv:crate-reference#partitioned-tables
[window function]: inv:crate-reference#window-functions
