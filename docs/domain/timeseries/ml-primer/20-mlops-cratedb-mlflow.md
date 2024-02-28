# MLOps powered by CrateDB and MLflow

_Introduction to Time Series Modeling with CrateDB (Part 2)._

This is part 2 of our blog series about "Running Time Series Models in Production using CrateDB".


## Thoughts

While creating a machine learning model itself is an important step, it is only the first step in the process. The real
challenge is in operating a model in a production environment.

The actual model serving and deployment, accompanied by a robust workflow for building your
models and running them in production, includes at least the following components:

![Elements of Machine Learning Operations](/_assets/img/ml-timeseries-primer/cratedb-mlops.png){width=400px}

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

A [lot](https://crate.io/blog/an-introduction-to-machine-learning)
was [already](https://crate.io/blog/machine-learning-and-cratedb-part-one)
[written](https://crate.io/blog/machine-learning-cratedb-jupyter) about
[how](https://crate.io/blog/machine-learning-and-cratedb-part-three-experiment-design-and-linear-regression)
to [create](https://www.machinelearningplus.com/time-series/time-series-analysis-python/) good time
series models, this is why we are not diving into the details here. For a quick primer, please also refer
to chapter [Time Series Anomaly Detection for Machine Data][ml-timeseries-blog-part-1].


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

### MLOps and MLflow

[MLOps] or ML Ops is a paradigm that aims to deploy and maintain machine learning models in
production reliably and efficiently, which reflects many of the steps enumerated above, including
experiment tracking.

[MLflow] is the de-facto standard for machine learning experiment tracking and
management. It is an open-source platform and framework that helps you
manage the complete machine learning lifecycle. CrateDB provides first-class integrations with MLflow,
allowing to use the MLflow software capabilities with CrateDB as the backend store. This allows using
MLflow without additional database infrastructure.

### Example

Hereby, we demonstrate an example of a machine learning experiment program, using the
Merlion model you created [earlier][ml-timeseries-blog-part-1].
It will record the parameters as well as the model outcome itself to MLflow.


#### Prerequisites

Install MLflow, including the CrateDB MLflow adapter.
```shell
pip install mlflow-cratedb
```

Run the MLflow tracking server.
```shell
mlflow-cratedb server --backend-store-uri='crate://admin:<your-password></your-password>@<your-instance>.azure.cratedb.net:4200?ssl=true&schema=mlflow'
```
Make sure to change `<your-password>` and `<your-instance>` to your own CrateDB Cloud
connection details.


#### Run experiment

Define the environment variable `MLFLOW_TRACKING_URI` to point to your MLflow tracking server.
```shell
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```

Extend the model training from the [previous example][ml-timeseries-blog-part-1]
with the following code:

```python
import os
import mlflow

os.environ["MLFLOW_TRACKING_URI"] = "http://127.0.0.1:5000"
mlflow.set_experiment('merlion_experiment_blog')

with mlflow.start_run():
    # model-training code here
    pass
```

Create a validation dataset, which contains the real anomalies. Make sure to keep this code
inside the scope of the `with mlflow.start_run():` block.

```python
# Prepare the validation labels
anomaly_labels = [
    ["2013-12-15 17:50:00.000000", "2013-12-17 17:00:00.000000"],
    ["2014-01-27 14:20:00.000000", "2014-01-29 13:30:00.000000"],
    ["2014-02-07 14:55:00.000000", "2014-02-09 14:05:00.000000"]
]

anomaly_labels = [[pd.to_datetime(start), pd.to_datetime(end)] for start, end in anomaly_labels]
time_series['test_labels'] = 0
for start, end in anomaly_labels:
    time_series.loc[(time_series.index >= start) & (time_series.index <= end), 'test_labels'] = 1

test_labels = TimeSeries.from_pd(time_series["test_labels"])

p = TSADMetric.Precision.value(ground_truth=test_labels, predict=test_pred)
r = TSADMetric.Recall.value(ground_truth=test_labels, predict=test_pred)
f1 = TSADMetric.F1.value(ground_truth=test_labels, predict=test_pred)
mttd = TSADMetric.MeanTimeToDetect.value(ground_truth=test_labels, predict=test_pred)
print(f"Precision: {p:.4f}, Recall: {r:.4f}, F1: {f1:.4f}\n"
      f"Mean Time To Detect: {mttd}")
```

Instruct MLflow to log the model metrics as well as some parameters.

```python
mlflow.log_metric("precision", p)
mlflow.log_metric("recall", r)
mlflow.log_metric("f1", f1)
mlflow.log_metric("mttd", mttd.total_seconds())
mlflow.log_param("anomaly_threshold", model.config.threshold.alm_threshold)
mlflow.log_param("min_alm_window", model.config.threshold.min_alm_in_window)
mlflow.log_param("alm_suppress_minutes", model.config.threshold.alm_suppress_minutes)
mlflow.log_param("ensemble_size", model.config.combiner.n_models)
```

**TIP:** With Merlion models, to get the model configuration, use the
`model.config.to_dict()` method.

Finally, store the model itself to the MLflow artifacts store.
```python
# Save the model to MLflow
model.save("model")
mlflow.log_artifact("model")
```


#### MLflow UI

Visit the MLflow UI to interact with your flow run, and your artifact. You can do this by running
`mlflow ui` in your terminal and then navigate to http://localhost:5000 in your browser.

![MLflow ui](/_assets/img/ml-timeseries-primer/mlflow-experiment.png){width=480px}

Open the recently tracked experiments by navigating to the corresponding experiment run.

In this screenshot, you can inspect the tracked parameters and metrics.

![MLflow tracked parameters and metrics](/_assets/img/ml-timeseries-primer/mlflow-tracks.png){width=480px}

You can also inspect the serialized model binaries, as well as the details of the model object.

![MLflow tracked model](/_assets/img/ml-timeseries-primer/mlflow-model.png){width=480px}

Kindly refer to the [CrateDB MLflow examples] and the [CrateDB MLflow handbook] for more details
about how to use CrateDB with MLflow. For additional information about MLflow itself, please refer
to the [MLflow documentation].


### Tracking Datasets

In addition to tracking models and parameters, a good experiment tracking system needs to track
the datasets used for training as well. This ensures reproducibility and traceability of the
model training process.

The CrateDB database is a natural fit for this task. It is able to store the raw data as well
as featured data, making them easily accessible for both, the training process as well as
experiment observability.
Additionally, when talking about time series data , CrateDB can utilize a critical fact of
time-based datasets: the time dimension is - within certain limits - immutable.

This allows for a simple yet effective way of versioning your datasets: Use the time dimension as
ever-increasing primary key for your data. CrateDB's support for [time partitioning] makes this
even more convenient, as it allows for highly efficient access to the data of a specific time
period.
For efficient versioning, use CrateDB [database VIEWs] on top of your time series data to create
a logical representation and abstraction per version of your dataset.
This strategy aligns with CrateDB being the [online feature store](#online-feature-store), because
both the features and the versions about to be tracked might be based on the same views.

Additional benefits are derived in terms of dataset version scalability. While even modern solutions
like [DVC (Data Version Control)] are limited in terms of how many versions they can realistically
handle and how fast they can access them, CrateDB's distributed architecture in combination with
time partitioning allows for virtually unlimited dataset versions, and efficient access to any of
them.

## Model Monitoring

Over time, a model's performance can degrade, largely due to shifts in data, known as concept drift,
or changes in the time series trends and patterns.

Model monitoring ensures that the insights or predictions generated by the model remain
accurate, reliable, and beneficial to the organization's decision-making process.

An example might be the COVID-19 pandemic, which
resulted in a significant increase in credit card usage. This increase might have caused a finance
fraud model that was trained on pre-pandemic data to start making inaccurate predictions, if not
adjusted accordingly.

### Requirements and Features

The requirements for effective model monitoring include: the ability to track model predictions and
actual outcomes, measure ongoing model performance, detect anomalies or performance drops, and
trigger alerts for necessary updates or adjustments to the model. It also requires a robust setup
for collecting, processing, and storing real-time data.

And that's again where CrateDB provides a solid foundation for model monitoring. Its highly
scalable data ingestion capabilities let you permanently store all the model predictions
side-by-side with the actual inputs, making all the required data needed to retrain your models
available in a single place.

### Best Practices

A good way to deal with changes in data over time is to create a baseline performance benchmark,
constantly watch the predictions from your model, and compare them with the training data and the
performance benchmark.

This can help spot differences right when they happen. You can use simple
tests or checks to look for strange patterns or shifts in the data. Keeping a close eye on the
data lets organizations find and fix changes fast, and this helps the model to stay right on
target and keep doing a good job.

More elaborate methods involve constantly validating the distribution of both the input data and
the predicted data, and running alerts if the distribution changes significantly. This can be
done by using statistical tests like the [Kolmogorov-Smirnov test], or the
[Kullback–Leibler Divergence].


![Model Monitoring](/_assets/img/ml-timeseries-primer/cratedb-model-monitoring.png){width=480px}


## Model Tuning and Retraining

Model tuning and retraining is the final but very crucial part of a machine learning
workflow, and it is even more pertinent in time series analysis where patterns and trends evolve
over time.

It refers to the process of periodically adjusting the parameters of your model, tuning
and retraining it with new data, to account for new patterns and trends, and shrink the feedback loop
for any changes. This keeps your model current and ensures it continues to make accurate predictions.

To effectively tune and retrain time series models, you should:

- Continuously monitor model performance: Use metrics suited for time series, like MAE (Mean Average
  Error) or RMSE (Root Mean Squared Error).

- Re-evaluate the model periodically: Use updated data to check changing patterns and to reassess the
  model’s accuracy and performance.

- As time series data are evolving naturally, it is best practice to retrain models in fixed
  intervals. Make sure to have both the raw data available, and verify the experiment tracking
  and performance monitoring steps after the new model is trained, to potentially catch any model
  degradations.

For retraining anomaly detection models, you might have the "benefit" of having real anomalies in
your new data, allowing for a supervised update of your model.

On this topic, we would like to kindly refer you to the [Merlion documentation] about [simulating live
model deployment], for specific information about retraining a Merlion-based model.


## Conclusion

Running time series models in production requires more than just creating the models themselves. It
involves dealing with large volumes of data, ensuring real-time processing, managing and updating
feature stores, and maintaining data accuracy and integrity.

CrateDB, a distributed multi-model SQL database, offers a powerful solution for handling these challenges. It provides
scalability, real-time data processing, and ease of use, making it an ideal choice for deploying
time series and anomaly detection models.

CrateDB's distributed architecture enables it to handle massive amounts of data while ensuring high
availability and scalability. Its real-time data processing capabilities are crucial for time series
analysis, allowing for immediate insights and timely anomaly detection. Additionally, CrateDB's
support for binary large objects (BLOBs) can simplify model deployment by enabling the storage and
retrieval of machine learning models directly within the database.

Furthermore, CrateDB's SQL syntax, time partitioning, and window function support, makes it
well-suited for exploratory data analysis and feature engineering. Its integration with popular
data visualization tools, and compatibility with Python, pandas, and other popular data processing
frameworks, facilitate efficient analysis and visualization of time series data.

Moreover, CrateDB's usability extends to model monitoring, experiment tracking, and model tuning.
With its ability to store and query large volumes of data, CrateDB provides a solid foundation for
model monitoring, enabling organizations to stay alert to changes in model performance and data
patterns.

Experiment tracking and model versioning can be achieved directly within CrateDB,
simplifying collaboration and reproducibility. Lastly, model tuning and retraining are made more
manageable with CrateDB's support for real-time data processing and the availability of up-to-date
data.

In summary, CrateDB offers a complete solution for running time series models in production,
addressing the challenges of data ingestion, management, exploratory data analysis, feature
engineering, model building, and monitoring. Its unique features, scalability, and ease of use,
make it a valuable asset in the realm of time series modeling and anomaly detection.


[CrateDB MLflow examples]: https://github.com/crate-workbench/mlflow-cratedb/tree/main/examples
[CrateDB MLflow handbook]: https://github.com/crate-workbench/mlflow-cratedb/blob/main/docs/handbook.md
[database VIEWs]: https://crate.io/docs/crate/reference/en/latest/general/ddl/views.html
[DVC (Data Version Control)]: https://dvc.org/
[dynamic object columns]: https://crate.io/blog/handling-dynamic-objects-in-cratedb
[ETS model]: https://www.statsmodels.org/dev/examples/notebooks/generated/ets.html
[Kolmogorov-Smirnov test]: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test
[Kullback–Leibler Divergence]: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
[Merlion]: https://github.com/salesforce/Merlion
[Merlion documentation]: https://opensource.salesforce.com/Merlion/v1.0.0/examples/anomaly/1_AnomalyFeatures.html
[MLflow]: https://mlflow.org/
[MLflow data API]: https://mlflow.org/docs/latest/python_api/mlflow.data.html
[MLflow documentation]: https://mlflow.org/docs/latest/index.html
[MLOps]: https://en.wikipedia.org/wiki/MLOps
[ml-timeseries-blog-part-1]: https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-machine-learning-time-series-data
[OBJECT data type]: https://crate.io/docs/crate/reference/en/latest/general/ddl/data-types.html#object
[Object column policy]: https://crate.io/docs/crate/reference/en/latest/general/ddl/data-types.html#object-column-policy
[Random Cut Forest]: https://docs.aws.amazon.com/sagemaker/latest/dg/randomcutforest.html
[Shard allocation filtering]: https://crate.io/docs/crate/reference/en/latest/general/ddl/shard-allocation.html
[simulating live model deployment]: https://opensource.salesforce.com/Merlion/v1.0.0/examples/anomaly/1_AnomalyFeatures.html#Simulating-Live-Model-Deployment
[time partitioning]: https://crate.io/docs/crate/reference/en/latest/general/ddl/partitioned-tables.html
[Time Series Analysis in Python – A Comprehensive Guide with Examples]: https://www.machinelearningplus.com/time-series/time-series-analysis-python/
[window function]: https://crate.io/docs/crate/reference/en/latest/general/builtins/window-functions.html
