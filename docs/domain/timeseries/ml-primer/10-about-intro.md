# Machine Learning for Time Series Data

_Introduction to Time Series Modeling with CrateDB (Part 1)._

This is part one of our blog series about "Introduction to Time Series Modeling with CrateDB".


## About

We will introduce you to the concept of time series modeling, and discuss
the main obstacles faced during its implementation in production. We will then introduce you
to CrateDB, highlighting its key features and benefits, why it stands out in managing time
series data, and why it is an especially good fit for supporting machine learning models in
production.

Whether you are a data scientist aiming to simplify your model deployment, a data engineer looking
to enhance your data landscape, or a tech enthusiast keen on understanding the latest trends, this
blog post will offer valuable insights and practical knowledge.

For readers familiar with [data modeling], it is important to distinguish that [time series modeling]
is a different discipline.


## Overview

### Time Series Modeling

Time series modeling is a crucial technique used across various sectors. Two main modeling
techniques comprise the field of machine learning: Time series forecasting, and anomaly
detection.

Time series forecasting has applications in predicting future sales in retail, anticipating stock market
trends in finance, predictive maintenance in manufacturing, user churn and subscription analysis
in web applications, forecasting energy demand in utilities, and many others. It involves the use
of statistical models to predict future values based on previously observed data.

### Anomaly Detection

Anomaly detection is used to identify outliers or unusual patterns in time series
data. This detection technique uses statistical and machine learning algorithms to sift through
large data sets over specific time intervals, analyzing patterns, trends, cycles, or seasonality,
to spot deviations from the norm. These anomalies could either be an error, or indicate another
kind of significant event you would like to be alerted about.

Anomaly detection is widely used in multiple fields and industries including cybersecurity, where
it identifies unusual network activity patterns that could signify a potential breach; in finance for
spotting fraudulent activities in credit card transactions; and in IoT for detecting malfunctioning
sensors and machines. Other use cases include healthcare, for monitoring unusual patient vital signs, and
predictive maintenance, where it is used to identify abnormal machine behavior, in order to prevent
system failures.

### Thoughts

While creating these models in itself is a challenging task, deploying them to production
environments in a robust manner, is often equally challenging. More often than not, you will need
to deal with large volumes of data, ensure real-time processing, manage and update feature
stores, keep track of data and model versions, all while maintaining data accuracy and integrity.

This is where CrateDB comes into play. CrateDB is a distributed SQL database, designed specifically
to handle the unique demands of time series data. It offers scalability, real-time data processing,
and ease of use, making it an ideal choice for deploying time series and anomaly detection models.

On top of that, CrateDB offers first-class analytical SQL support for time series data and
binary blob data types, which makes it possible to store and retrieve machine learning
models without needing extra infrastructure.

CrateDB is well integrated with the modern data processing and machine learning ecosystem through
both its [SQLAlchemy] dialect, and its PostgreSQL wire-protocol compatibility. It provides support
and adapters for [Apache Flink], [Apache Kafka], [Apache Spark], [pandas], [Dask], and friends, as
well as [Apache Superset], [Tableau], and [many more][more-integrations].


## Introducing CrateDB

When talking about time series modeling, the database is one of the central elements of the
architecture. It is the place where the data is stored, processed, and queried. And even more, it
can be the right spot to significantly reduce your platform complexity and simplify your
architecture.

CrateDB is specifically designed to handle the demands of time series
data. It combines the familiarity and ease of SQL with the scalability and data flexibility of
NoSQL. This makes it an ideal choice for managing large volumes of structured and unstructured data,
and for executing complex queries in near real-time.

It provides robust security features, and includes a monitoring and administration interface.

### Distributed Architecture

One of the key features of CrateDB is its distributed, shared-nothing architecture. This allows it
to handle massive
amounts of data by distributing the data and queries across multiple nodes. This not only ensures
high availability and resilience, but also provides linear scalability. As your data grows, you can
add more nodes to your CrateDB cluster to increase both its compute and storage capacity.
This makes it easy to scale your database as your business grows.

### SQL Query Language

CrateDB offers ease of use with its SQL interface, providing excellent SQL analytics support, on
top of structured and unstructured data, and supporting full-text search and BLOBs.

CrateDB's full-text search capabilities are powered by [Apache Lucene],
allowing you to perform complex search queries on structured and unstructured data within typical
time series modeling tasks, such as processing log files, complex sensor data, or alarm information.

### BLOB Support

Where CrateDB excels in the context of running time series models is its support for binary large
objects (BLOBs). BLOBs are used to store large binary data, such as images, audio files, or - and
that's the point - machine learning models. With CrateDB's BLOB support, you can store your trained
machine learning models directly in the same database where your time series data reside.

This not
only simplifies the model deployment process, but also allows you to easily version your models. You
can keep track of different versions of your models, roll back to a previous version if needed, and
ensure that the right model is used for making predictions. More on that later in this post.

### Benefits

CrateDB offers real-time data processing, which is crucial for time series forecasting and
anomaly detection - you want to be notified about anomalies when they arise, not 3 days later.

It
allows you to ingest and query data simultaneously, providing real-time insights into your data.
This is particularly useful when you need to make quick decisions based on the latest data, which
is almost always the case for both time series forecasting, and anomaly detection.

### Summary

CrateDB provides a powerful, scalable, and flexible solution for managing time
series data, and operating the corresponding machine learning models. 

Its unique features, such as
the distributed architecture, real-time data processing, full-text search, and BLOB support, make
it a versatile solution in the world of time series modeling, anomaly detection, and forecasting.

As an open-source system, you can customize it to fit your specific needs, and get out of vendor
lock-in situations. If you are looking for maximum operational convenience, you can utilize their
managed cloud service, [CrateDB Cloud].

As we move forward, we will explore how to leverage these features to bring your time series models
to production.


## Time Series Modeling

Time series modeling is a statistical technique that utilizes sequential data to predict future
values or events based on historical data. It involves analyzing patterns, trends, and seasonality
in past data, to forecast future events. This type of forecasting is particularly useful when dealing
with data that changes over time, such as stock prices, weather patterns, marketing & sales data, or
M2M/IoT data.

One of the key components of time series modeling is the understanding and interpretation of
certain critical properties intrinsic to time series data, such as trend, seasonality, and
cyclicality. Trend refers to the overall pattern or direction in which data is moving over a
significant period. Seasonality are the recurring patterns or cycles that are typically observed
within a specific time frame, be it daily, weekly, annually, etc. Cyclicality involves fluctuations
that occur at irregular intervals, and cannot be linked to any particular season or event.

### Applications

The ability to accurately predict future events based on past data is invaluable in many sectors.
For instance, online shops can forecast product demand to manage inventory, financial institutions
can predict stock prices to make informed investment decisions, and manufacturing companies can
anticipate machine maintenance downtimes to efficiently plan their production schedules. By making
accurate predictions, businesses can make predictive, data-based decisions, reduce risks, and
improve efficiency.

Furthermore, time series modeling is also useful for anomaly detection. Anomalies are data points
that deviate from the expected pattern or trend. They can be caused by a variety of factors, such
as human error, equipment malfunction, or cyber-attacks. By detecting anomalies early on,
businesses can take corrective actions to prevent further damage. For instance, a manufacturing
company can detect anomalies in their production process to prevent machine breakdowns and avoid
costly downtimes.

### Technical Background

Various types of models are employed in time series analysis, each with its strengths and weaknesses.
The simplest model is the autoregressive (AR) model, which assumes future values can be forecasted
from a weighted sum of the past. The moving average (MA) model, on the other hand, assumes that
future values are a function of the mean and various random error terms. More complex models, like
autoregressive integrated moving average (ARIMA) and seasonal ARIMA (SARIMA), combine strategies
from AR and MA models while also accounting for trends and seasonality. Additionally, state-of-the-art
models like Long Short-Term Memory (LSTM), a type of recurrent neural network, are effective at
capturing long-term dependencies in time series data.

More recent models for anomaly detection are Random Cut Forest (RCF), Variational Auto Encoders (VAE)
which are both neural network based, unsupervised learning algorithms (with VAEs surprisingly being
also very good in semi-supervised and supervised learning applications). Honorable mentions in the
field of time series anomaly detection are also the Isolation Forest (IF), One-Class Support Vector
Machine (OCSVM) models, and the excellent prophet time series analysis library, released by Facebook.

Furthermore, recent developments advise to not only use a single model for time series forecasting
and anomaly detection, but multiple ones, called an ensemble. This technique uses multiple of the
aforementioned models on the same data, and then combines their predictions to get a more accurate
result.

To get a practical hang of how time series modeling works, the next section will exercise a basic
example.


## Example: Time Series Anomaly Detection for Machine Data

### Prologue

**NOTE:** While this example should provide more depth to understanding time series modeling,
it is not intended to teach the foundations of this field of data science. Instead, it
will focus more on how to use machine learning models in production scenarios.

If you
are interested in learning more details about time series modeling, we recommend to check out [Time
Series Analysis in Python – A Comprehensive Guide with Examples], by Selva Prabhakaran.

### About

The exercise will use a dataset from the Numenta Anomaly Benchmark (NAB), which includes
real-world and artificial time series data for anomaly detection research. We will choose the
dataset about real measured temperature readings from a machine room.

The goal is to detect
anomalies in the temperature readings, which could indicate a malfunctioning machine. The dataset
simulates machine temperature measurements, and will be loaded into CrateDB upfront.

### Setup

To follow this tutorial, install the prerequisites by running the following commands in your
terminal. Furthermore, load the designated dataset into your [CrateDB Cloud] cluster.

```bash
pip install 'crate[sqlalchemy]' 'numpy==1.23.5' crash matplotlib pandas salesforce-merlion
```

Please note the following external dependencies of the [Merlion] library:

#### OpenMP
Some forecasting models depend on OpenMP. Please install it before installing this package,
in order to ensure that OpenMP is configured to work with the lightgbm package, one of
Merlion's dependencies.

When using Anaconda, please run
```shell
conda install -c conda-forge lightgbm
```
When using macOS, please install the Homebrew package manager and invoke
```shell
brew install libomp
```

#### Java
Some anomaly detection models depend on the Java Development Kit (JDK). On Debian or Ubuntu, run
```shell
sudo apt-get install openjdk-11-jdk
```
On macOS, install Homebrew, and invoke
```shell
brew tap adoptopenjdk/openjdk
brew install --cask adoptopenjdk11
```
Also, ensure that Java can be found on your `PATH`, and that the `JAVA_HOME` environment variable
is configured correctly.



### Importing Data

If you are using [CrateDB Cloud], navigate to the [Cloud Console], and use the [Data Import] feature
to import the CSV file directly from the given URL into the database table `machine_data`.
```
https://github.com/crate/cratedb-datasets/raw/main/timeseries/anomaly/nab-machine-failure.csv
```

![CrateDB Cloud Import dialog](/_assets/img/ml-timeseries-primer/cratedb-cloud-import-url.png){width=400px}
![CrateDB Cloud Import ready](/_assets/img/ml-timeseries-primer/cratedb-cloud-import-ready.png){width=400px}

The import process will automatically infer an SQL DDL schema from the shape of the data source.
When visiting the [CrateDB Admin UI] after the import process has concluded, you can observe the
`machine_data` table was created and populated correctly.

![CrateDB Admin UI data imported](/_assets/img/ml-timeseries-primer/cratedb-admin-ui-data-imported.png){width=400px}

If you want to exercise the data import on your workstation, use the `crash` command-line program.
```shell
crash --command 'CREATE TABLE IF NOT EXISTS "machine_data" ("timestamp" TIMESTAMP, "value" REAL);'
crash --command "COPY machine_data FROM 'https://github.com/crate/cratedb-datasets/raw/main/timeseries/anomaly/nab-machine-failure.csv';"
```

Note: If you are connecting to CrateDB Cloud, use the options
`--hosts 'https://<hostname>:4200' --username '<username>'`. In order to run the program
non-interactively, without being prompted for a password, use `export CRATEPW='<password>'`.


### Loading Data

First, you will load the dataset into a pandas DataFrame and convert the `timestamp` column to a
Python `datetime` object.

```python
from crate import client
import pandas as pd

# Connect to database.
conn = client.connect(
    "https://<your-instance>.azure.cratedb.net:4200",
    username="admin",
    password="<your-password>",
    verify_ssl_cert=True)

# Query and load data.
with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, value "
                   "FROM machine_data ORDER BY timestamp ASC")
    data = cursor.fetchall()

# Convert to pandas DataFrame.
time_series = pd.DataFrame(
        [{'timestamp': pd.Timestamp.fromtimestamp(item[0] / 1000), 'value': item[1]}
            for item in data])

# Set the timestamp as the index.
time_series = time_series.set_index('timestamp')
```

### Downsampling

**TIP:** CrateDB provides many useful analytical functions tailored for time series data. One of
them is the `date_bin` which bins the input timestamp to the specified interval - which makes it
very handy to resample data.

In general, for time series modeling, you often want to sample your data with a high frequency, in
order not to miss any events. However, this results in huge data volumes, increasing the costs of
model training. Here, it is best practice to down-sample your data to reasonable intervals.

This SQL statement demonstrates CrateDB's `date_bin` function to down-sample the data to 5 minute
intervals, reducing both amount of data and complexity of the modeling process.

```sql
SELECT
    DATE_BIN('5 min'::INTERVAL, "timestamp", 0) AS timestamp,
    MAX(value) AS temperature
FROM machine_data
GROUP BY timestamp
ORDER BY timestamp ASC
```

### Plotting

Next, plot the data to get a better understanding of the dataset.

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

anomalies = [
    ["2013-12-15 17:50:00.000000", "2013-12-17 17:00:00.000000"],
    ["2014-01-27 14:20:00.000000", "2014-01-29 13:30:00.000000"],
    ["2014-02-07 14:55:00.000000", "2014-02-09 14:05:00.000000"]
]

plt.figure(figsize=(12,7))
line, = plt.plot(time_series.index, time_series['value'], linestyle='solid', color='black', label='Temperature')

# Highlight anomalies
ctr = 0
for timeframe in anomalies:
    ctr += 1
    plt.axvspan(pd.to_datetime(timeframe[0]), pd.to_datetime(timeframe[1]), color='blue', alpha=0.3, label=f'Anomaly {ctr}')

# Formatting x-axis for better readability
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))
plt.gcf().autofmt_xdate()  # Rotate & align the x labels for a better view

plt.title('Temperature Over Time', fontsize=20, fontweight='bold', pad=30)
plt.ylabel('Temperature')
# Add legend to the right
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
```

![Temperature over time with anomalies](/_assets/img/ml-timeseries-primer/temperature-anomaly-score.png)

### Observations

Please note the blue highlighted areas above - these are real, observed anomalies in the dataset.
You will use them later to evaluate the model. The first anomaly is a planned shutdown of the
machine. The second anomaly is difficult to detect and directly led to the third anomaly, a
catastrophic failure of the machine.

You see that there are some nasty spikes in the data, which make anomalies hard to differentiate
from ordinary measurements. However, as you will see later, modern models are quite good at finding
exactly those spots.

### Model Training

To get there, let's train a small anomaly detection model. As mentioned in the introduction, there
are a multitude of options to choose from. This post will not go into the very details of model
selection, and will just use the [Merlion] library, an excellent open-source time series
analysis package developed by Salesforce.

[Merlion] implements an end-to-end machine
learning framework, that includes loading and transforming data, building and training models,
post-processing model outputs, and evaluating model performance. It supports various time series
learning tasks, including forecasting, anomaly detection, and change point detection.

Start by first splitting the dataset into training and test data. The exercise will use
unsupervised learning, so you want to train the model on data without anomalies, and then
check whether it is able to detect the anomalies in the test data. The data will be split at
2013-12-15.

```python
from merlion.utils import TimeSeries

train_data = TimeSeries.from_pd(time_series[time_series.index < pd.to_datetime('2013-12-15')])
test_data = TimeSeries.from_pd(time_series[time_series.index >= pd.to_datetime('2013-12-15')])
```

![Test/Train Split](/_assets/img/ml-timeseries-primer/temperature-train-test.png)

Now, train the model using the Merlion `DefaultDetector`, which is an anomaly detection model that
balances performance and efficiency. Under the hood, the `DefaultDetector` is an ensemble of an
[ETS model] and a [Random Cut Forest] model, both are excellent for general purpose anomaly detection.

```python
from merlion.models.defaults import DefaultDetectorConfig, DefaultDetector

model = DefaultDetector(DefaultDetectorConfig())
model.train(train_data=train_data)
```

### Evaluation

Let's visually confirm the model performance:

![Temperature with detected anomalies](/_assets/img/ml-timeseries-primer/temperature-anomaly-detected.png)

The model is able to detect the anomalies, a very good result for the first try, and without any
parameter tuning. The next steps will bring this model to production.

In a real-world scenario, you want to further improve the model by tuning the parameters and
evaluating the model performance on a validation dataset. However, for the sake of simplicity,
this step will be skipped. Please refer to the [Merlion documentation] for more information on
how to do this.

If you are excited about the potential of time-series data, want to learn more about its
usage in CrateDB, and how to optimize your MLOps workflows, then don't miss out on part 2 of
this blog post series. We will show you how CrateDB supports MLOps using the powerful MLflow
Python library. In Part 3, we will take it a step further by demonstrating how CrateDB can
support an entire MLOps lifecycle. Stay tuned for more.


[Apache Flink]: https://flink.apache.org/
[Apache Lucene]: https://lucene.apache.org/
[Apache Kafka]: https://kafka.apache.org/
[Apache Spark]: https://spark.apache.org/
[Apache Superset]: inv:crate-clients-tools#apache-superset
[Cloud Console]: https://console.cratedb.cloud/
[CrateDB Admin UI]: https://cratedb.com/docs/crate/admin-ui/
[CrateDB Cloud]: https://cratedb.com/products/cratedb-cloud
[Dask]: https://www.dask.org/
[Data Import]: https://community.cratedb.com/t/importing-data-to-cratedb-cloud-clusters/1467#import-from-url-1
[data modeling]: https://en.wikipedia.org/wiki/Data_modeling
[ETS model]: https://www.statsmodels.org/dev/examples/notebooks/generated/ets.html
[Merlion]: https://github.com/salesforce/Merlion
[Merlion documentation]: https://opensource.salesforce.com/Merlion/v1.0.0/examples/anomaly/1_AnomalyFeatures.html
[more-integrations]: https://cratedb.com/partners/technology-partners
[pandas]: https://pandas.pydata.org/
[Random Cut Forest]: https://docs.aws.amazon.com/sagemaker/latest/dg/randomcutforest.html
[SQLAlchemy]: https://www.sqlalchemy.org/
[Tableau]: inv:crate-clients-tools#tableau
[Time Series Analysis in Python – A Comprehensive Guide with Examples]: https://www.machinelearningplus.com/time-series/time-series-analysis-python/
[time series modeling]: https://en.wikipedia.org/wiki/Time_series#Models
