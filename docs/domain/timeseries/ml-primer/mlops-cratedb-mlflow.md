(tsml-primer-mlops-cratedb-mlflow)=

# MLOps Example using CrateDB and MLflow

[MLOps] or ML Ops is a paradigm that aims to deploy and maintain machine learning models in
production reliably and efficiently, which reflects many of the steps enumerated above, including
experiment tracking.

[MLflow] is the de-facto standard for machine learning experiment tracking and
management. It is an open-source platform and framework that helps you
manage the complete machine learning lifecycle. CrateDB provides first-class integrations with MLflow,
allowing to use the MLflow software capabilities with CrateDB as the backend store. This allows using
MLflow without additional database infrastructure.

Hereby, we demonstrate an example of a machine learning experiment program, using the
Merlion model you created [earlier](#tsml-primer-anomaly-detection).
It will record the parameters as well as the model outcome itself to MLflow.


## Prerequisites

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


## Run experiment

Define the environment variable `MLFLOW_TRACKING_URI` to point to your MLflow tracking server.
```shell
export MLFLOW_TRACKING_URI=http://127.0.0.1:5000
```

Extend the model training from the [previous example](#tsml-primer-anomaly-detection)
with the following code:

```python
import os
import mlflow

os.environ["MLFLOW_TRACKING_URI"] = "http://127.0.0.1:5000"
mlflow.set_experiment('merlion_experiment')

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


## MLflow UI

Visit the MLflow UI to interact with your flow run, and your artifact. You can do this by running
`mlflow ui` in your terminal and then navigate to `http://localhost:5000` in your browser.

![MLflow ui](/_assets/img/ml-timeseries-primer/mlflow-experiment.png){width=480px}

Open the recently tracked experiments by navigating to the corresponding experiment run.

In this screenshot, you can inspect the tracked parameters and metrics.

![MLflow tracked parameters and metrics](/_assets/img/ml-timeseries-primer/mlflow-tracks.png){width=480px}

You can also inspect the serialized model binaries, as well as the details of the model object.

![MLflow tracked model](/_assets/img/ml-timeseries-primer/mlflow-model.png){width=480px}

Kindly refer to the [CrateDB MLflow examples] and the [CrateDB MLflow handbook] for more details
about how to use CrateDB with MLflow. For additional information about MLflow itself, please refer
to the [MLflow documentation].


## Tracking Datasets

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
This strategy aligns with CrateDB being the [online feature store](#mlops-feature-store), because
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
[database VIEWs]: inv:crate-reference#ddl-views
[DVC (Data Version Control)]: https://dvc.org/
[ETS model]: https://www.statsmodels.org/dev/examples/notebooks/generated/ets.html
[Kolmogorov-Smirnov test]: https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test
[Kullback–Leibler Divergence]: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
[Merlion]: https://github.com/salesforce/Merlion
[Merlion documentation]: https://opensource.salesforce.com/Merlion/v1.0.0/examples/anomaly/1_AnomalyFeatures.html
[MLflow]: https://mlflow.org/
[MLflow data API]: https://mlflow.org/docs/latest/python_api/mlflow.data.html
[MLflow documentation]: https://mlflow.org/docs/latest/index.html
[MLOps]: https://en.wikipedia.org/wiki/MLOps
[Object column policy]: inv:crate-reference#type-object-column-policy
[Random Cut Forest]: https://docs.aws.amazon.com/sagemaker/latest/dg/randomcutforest.html
[simulating live model deployment]: https://opensource.salesforce.com/Merlion/v1.0.0/examples/anomaly/1_AnomalyFeatures.html#Simulating-Live-Model-Deployment
[time partitioning]: inv:crate-reference#partitioned-tables
[Time Series Analysis in Python – A Comprehensive Guide with Examples]: https://www.machinelearningplus.com/time-series/time-series-analysis-python/
