(arrow-import-parquet)=
# Importing Parquet files into CrateDB using Apache Arrow and SQLAlchemy

This tutorial introduces a way to import Parquet files into CrateDB using the Apache Arrow and SQLAlchemy libraries in Python.

## What is a Parquet file?

Apache Parquet is a free and open-source column-oriented data storage format. It provides an optimized data storage and retrieval due to its efficient data compression, which is able to handle complex data structures in bulk. Even though for this tutorial we are going to use Python, Parquet files are compatible with multiple languages and data processing frameworks. Here it will be used to transfer data from a data storage to CrateDB.

## Prerequisites

Install the required libraries: **sqlalchemy-cratedb** and **pyarrow**.

```shell
pip install pyarrow sqlalchemy-cratedb
```
In this tutorial we will use a Parquet file containing information from yellow taxi rides from January 2022 in New York, refer to this [link](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) to download the file. The creation of the table will be handled by **sqlalchemy.**

## Getting started

Once everything is installed you should import the required resources as seen below.

```python
import pyarrow.parquet as pq
from uuid import uuid4
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, create_engine, DateTime, Float
```

The first step is to read the Parquet file which will be saved in the `ny_taxi_parquet` object. 

```python
parquet_path = 'yellow_tripdata_2022-01.parquet'
ny_taxi_parquet = pq.ParquetFile(parquet_path)
```

Set up the SQLAlchemy engine and session:
```python
CRATE_URI = 'crate://localhost:4200'

Base = declarative_base()
session = scoped_session(sessionmaker())
engine = create_engine(CRATE_URI, echo=False)
session.configure(bind=engine, autoflush=False, expire_on_commit=False)
```

## Creating the model

Before processing the newly imported file, the corresponding Model must be created, this is the representation of the final table, if you are using a different dataset, adapt the model to your data. Attribute names are case‑sensitive. In this example, **VendorID** in the model maps to "VendorID" in CrateDB.

```python
class TaxiTrip(Base):
    __tablename__='ny_taxi'

    # Generate a text UUID to match Column(String)
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    VendorID = Column(String)
    tpep_pickup_datetime = Column(DateTime)
    tpep_dropoff_datetime = Column(DateTime)
    passenger_count = Column(Integer)
    trip_distance = Column(Float)
    PULocationID = Column(String)
    DOLocationID = Column(String)
    RatecodeID = Column(Integer)
    store_and_fwd_flag = Column(String)
    payment_type = Column(Integer)
    fare_amount = Column(Float)
    extra = Column(Float)
    mta_tax = Column(Float)
    improvement_surcharge = Column(Float)
    tip_amount = Column(Float)
    tolls_amount = Column(Float)
    total_amount = Column(Float)
    congestion_surcharge = Column(Float)
    airport_fee = Column(Float)
```

Now if we call:

```python
Base.metadata.create_all(engine)
```
It creates the table in CrateDB if it does not exist. If you later change the schema, `create_all()` may fail. In that case, rename or drop the existing table, adjust the model, and recreate it.

For further details on how to use the SQLAlchemy with CrateDB, you can refer to the {ref}`sqlalchemy-cratedb:index`.

Next, we are going to process the parquet file by batches, this is the most efficient way of handling big amounts of data, the size of the batch will depend on the amount of rows and the specs of your machine, it is a good to try several batch sizes with a reduced dataset until you find a performance that makes sense for you.

The dataset that we are loading has ~2M rows, 60k rows seemed to perform well with our machine so we chose that number.

```python
BATCH_SIZE = 60_000

    
for batch in ny_taxi_parquet.iter_batches(batch_size=BATCH_SIZE):
    batch_row = batch.to_pylist()

    session.execute(
        TaxiTrip.__table__.insert(),
        batch_row
    )
    session.commit()
```

While the batches are processed, you should already see the new records in your CrateDB instance.

![Screen Shot 2022-06-27 at 15.11.33|690x365](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/c0014f45b2a954dad3cb4900fee8e82ab58d0019.png)
