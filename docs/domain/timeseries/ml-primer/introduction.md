(tsml-primer-introduction)=

# Machine Learning for Time Series Data

_Introduction to Time Series Modeling with CrateDB (Part 1)._

This is part one of the "Machine Learning for Time Series Data Primer".

:::{rubric} Table of contents
:::

:::{contents}
:local:
:::


## About

We will introduce you to the concept of time series modeling, and discuss
the main obstacles faced during its implementation in production. We will then introduce you
to CrateDB, highlighting its key features and benefits, why it stands out in managing time
series data, and why it is an especially good fit for supporting machine learning models in
production.

Whether you are a data scientist aiming to simplify your model deployment, a data engineer looking
to enhance your data landscape, or a tech enthusiast keen on understanding the latest trends, this
article will offer valuable insights and practical knowledge.

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
ensure that the right model is used for making predictions. More on that later in this article.

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


## Conclusion

If you are excited about the potential of time-series data, want to learn more
about its usage in CrateDB, and how to optimize your MLOps workflows, then
don't miss out on [part 2](#tsml-primer-mlops-cratedb-mlflow) of this
series, which will illustrate how CrateDB supports MLOps using the powerful
MLflow Python library.

[Part 3](#tsml-primer-mlops-cratedb-sql) will demonstrate how CrateDB can
optionally support the entire MLOps lifecycle using SQL only.


## Examples

The article series includes two hands-on tutorials and references to other
sources including runnable code.

- [](#tsml-primer-anomaly-detection)
- [](#tsml-primer-mlops-cratedb-mlflow)


[Apache Flink]: https://flink.apache.org/
[Apache Lucene]: https://lucene.apache.org/
[Apache Kafka]: https://kafka.apache.org/
[Apache Spark]: https://spark.apache.org/
[Apache Superset]: inv:crate-clients-tools#apache-superset
[CrateDB Cloud]: https://cratedb.com/products/cratedb-cloud
[Dask]: https://www.dask.org/
[data modeling]: https://en.wikipedia.org/wiki/Data_modeling
[more-integrations]: https://cratedb.com/partners/technology-partners
[pandas]: https://pandas.pydata.org/
[SQLAlchemy]: https://www.sqlalchemy.org/
[Tableau]: inv:crate-clients-tools#tableau
[time series modeling]: https://en.wikipedia.org/wiki/Time_series#Models
