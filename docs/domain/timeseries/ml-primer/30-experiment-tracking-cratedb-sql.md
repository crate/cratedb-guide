# Experiment Tracking with CrateDB using SQL only

_Introduction to Time Series Modeling with CrateDB (Part 3)._

This is part 3 of our blog series about "Running Time Series Models in Production using CrateDB".


## Introduction

While MLflow is a handy tool, it is also possible to track your experiments exclusively using
CrateDB and SQL, without using any machine learning framework at all.

Because CrateDB provides storage support for both nested documents, and binary data, you can also
store parameters, metrics, the model configuration, and the model itself, directly into CrateDB.

The next section demonstrates it on behalf of two corresponding examples.


## Storing Experiment Metadata

CrateDB supports you in storing and recording your experiment metadata.

### 1. Deploy database schema

Create database tables in CrateDB, to store metrics and parameters.

```sql
CREATE TABLE metrics_params (
  timestamp TIMESTAMP DEFAULT now(),
  run_name TEXT,
  metrics OBJECT(DYNAMIC),
  parameters OBJECT(DYNAMIC)
);
```

Using CrateDB's dynamic `OBJECT` column, you can store arbitrary key-value pairs into the `metrics`
and `parameters` columns. This makes it possible to adjust which parameters and metrics you want to
add throughout the experiments, and evolve corresponding details while you go.

### 2. Record metrics and parameters 

Instead of recording the metrics and parameters to MLflow, as demonstrated at
[MLOps powered by CrateDB and MLflow » Experiment Tracking][ml-timeseries-blog-part-2], you will
record them by directly inserting into the database table.

```sql
INSERT INTO
  metrics_params (run_name, metrics, parameters)
VALUES ('random_run_name',
  '{"precision": 0.667, "recall": 0.667}',
  '{"anomaly_threshold": 2.5, "alm_suppress_minutes": 3.5}');
```

### 3. Read back recordings

To read back individual parameters of your recordings, you can utilize the standard
[SQL `SELECT` statements].

To retrieve all recorded metrics and parameters after a certain point in time:
```sql
SELECT *
FROM metrics_params
WHERE timestamp > '2021-01-01';
```

To retrieve specific parameters or metrics:
```sql
SELECT metrics['precision'], parameters['anomaly_threshold']
FROM metrics_params
WHERE timestamp > '2021-01-01';
```


## Storing Model Data

CrateDB supports you in storing your model data.

Independently of recording experiment metadata, you may also want to store the model itself into
CrateDB, by leveraging its [BLOB data type].

In order to store models into CrateDB, you will need two database tables:

- A regular RDBMS database table, storing the model configuration and
  relevant metadata.
- A blob database table, storing serialized models in binary format,
  usually in Python's [pickle format].

### 1. Deploy database schema

Create those tables, again utilizing CrateDB's nested object support for flexible
schema evolution:

```sql
CREATE TABLE model_config (
  timestamp TIMESTAMP DEFAULT now(),
  digest TEXT, -- this is the link to the model blog
  run_name TEXT,
  config OBJECT(DYNAMIC)
);

CREATE BLOB TABLE models;
```

### 2. Upload the model

To upload the model, run the following Python program after adjusting the spots
about the database connection and credentials.

```python
from io import BytesIO
import pickle
from crate import client

file = BytesIO()
# Serialize the model object and store it in the in-memory file
pickle.dump(model, file)

conn = client.connect(
   "https://<your-instance>.azure.cratedb.net:4200",
   username="admin",
   password="<your-password>",
   verify_ssl_cert=True,
)

blob_container = conn.get_blob_container('models')
blob_digest = blob_container.put(file)
```

Make sure to update the model configuration table accordingly:

```python
cursor = conn.cursor()
cursor.execute(
  "INSERT INTO model_config (digest, run_name, config) VALUES (?, ?, ?)", 
  (blob_digest, "random_run_name", model.config.to_dict()))
```

CrateDB automatically creates all the model config columns.

![crate model config](/_assets/img/ml-timeseries-primer/cratedb-model-configuration.png)

### 3. Read back the model

To retrieve a model from the blob store table again, you will need to get the digest value
of the model from the configuration table:

```sql
SELECT digest FROM model_config WHERE run_name = 'random_run_name';
```

Then, use this digest, i.e. the blob identifier, to get the blob payload, and
deserialize it from pickle format:

```python
blob_content = b""
for chunk in blob_container.get(digest):
  blob_content += chunk

model = pickle.loads(blob_content)
```
    

[BLOB data type]: inv:crate-reference#blob_support
[ml-timeseries-blog-part-1]: https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-machine-learning-time-series-data
[ml-timeseries-blog-part-2]: https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-part-2?hs_preview=uXVBkYrk-136061503799
[pickle format]: https://realpython.com/python-pickle-module/
[SQL `SELECT` statements]: inv:crate-reference#sql-select
