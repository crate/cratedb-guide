(tsml-primer-anomaly-detection)=

# Anomaly Detection Example for Machine Data

## Prologue

**NOTE:** While this example should provide more depth to understanding time series modeling,
it is not intended to teach the foundations of this field of data science. Instead, it
will focus more on how to use machine learning models in production scenarios.

If you
are interested in learning more details about time series modeling, we recommend to check out [Time
Series Analysis in Python – A Comprehensive Guide with Examples], by Selva Prabhakaran.

## About

The exercise will use a dataset from the Numenta Anomaly Benchmark (NAB), which includes
real-world and artificial time series data for anomaly detection research. We will choose the
dataset about real measured temperature readings from a machine room.

The goal is to detect
anomalies in the temperature readings, which could indicate a malfunctioning machine. The dataset
simulates machine temperature measurements, and will be loaded into CrateDB upfront.

## Setup

To follow this tutorial, install the prerequisites by running the following commands in your
terminal. Furthermore, load the designated dataset into your [CrateDB Cloud] cluster.

```bash
pip install 'crate[sqlalchemy]' 'numpy==1.23.5' crash matplotlib pandas salesforce-merlion
```

Please note the following external dependencies of the [Merlion] library:

### OpenMP
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

### Java
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



## Importing Data

If you are using [CrateDB Cloud], navigate to the [Cloud Console], and use the [Data Import] feature
to import the CSV file directly from the given URL into the database table `machine_data`.
```
https://github.com/crate/cratedb-datasets/raw/main/machine-learning/timeseries/nab-machine-failure.csv
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
crash --command "COPY machine_data FROM 'https://github.com/crate/cratedb-datasets/raw/main/machine-learning/timeseries/nab-machine-failure.csv';"
```

Note: If you are connecting to CrateDB Cloud, use the options
`--hosts 'https://<hostname>:4200' --username '<username>'`. In order to run the program
non-interactively, without being prompted for a password, use `export CRATEPW='<password>'`.


## Loading Data

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

## Downsampling

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

## Plotting

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

## Observations

Please note the blue highlighted areas above - these are real, observed anomalies in the dataset.
You will use them later to evaluate the model. The first anomaly is a planned shutdown of the
machine. The second anomaly is difficult to detect and directly led to the third anomaly, a
catastrophic failure of the machine.

You see that there are some nasty spikes in the data, which make anomalies hard to differentiate
from ordinary measurements. However, as you will see later, modern models are quite good at finding
exactly those spots.

## Model Training

To get there, let's train a small anomaly detection model. As mentioned in the introduction, there
are a multitude of options to choose from. This article will not go into the very details of model
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

## Evaluation

Let's visually confirm the model performance:

![Temperature with detected anomalies](/_assets/img/ml-timeseries-primer/temperature-anomaly-detected.png)

The model is able to detect the anomalies, a very good result for the first try, and without any
parameter tuning. The next steps will bring this model to production.

In a real-world scenario, you want to further improve the model by tuning the parameters and
evaluating the model performance on a validation dataset. However, for the sake of simplicity,
this step will be skipped. Please refer to the [Merlion documentation] for more information on
how to do this.


[Cloud Console]: https://console.cratedb.cloud/
[CrateDB Admin UI]: https://cratedb.com/docs/crate/admin-ui/
[CrateDB Cloud]: https://cratedb.com/products/cratedb-cloud
[Data Import]: https://community.cratedb.com/t/importing-data-to-cratedb-cloud-clusters/1467
[ETS model]: https://www.statsmodels.org/dev/examples/notebooks/generated/ets.html
[Merlion]: https://github.com/salesforce/Merlion
[Merlion documentation]: https://opensource.salesforce.com/Merlion/v1.0.0/examples/anomaly/1_AnomalyFeatures.html
[Random Cut Forest]: https://docs.aws.amazon.com/sagemaker/latest/dg/randomcutforest.html
[Time Series Analysis in Python – A Comprehensive Guide with Examples]: https://www.machinelearningplus.com/time-series/time-series-analysis-python/
