(mongodb-tutorial)=
# Import data from MongoDB

In this quick tutorial, you'll use the [CrateDB Toolkit MongoDB I/O subsystem]
to import data from [MongoDB] into [CrateDB].

:::{note}
**Important:** The tutorial uses adapter software which is currently in beta testing.
If you discover any issues, please [report them] back to us.
:::

## Synopsis
Transfer data from MongoDB database/collection into CrateDB schema/table.
:::{code} shell
ctk load table \
  "mongodb+srv://admin:p..d@cluster0.nttj7.mongodb.net/testdrive/demo" \
  --cratedb-sqlalchemy-url='crate://admin:p..d@gray-wicket-systri-warrick.aks1.westeurope.azure.cratedb.net:4200/testdrive/demo?ssl=true'
:::

Query data in CrateDB.
:::{code} shell
export CRATEPW=password
crash --host=cratedb.example.org --username=user --command="SELECT * FROM testdrive.demo;"
:::

## Data Model

MongoDB stores data in collections and documents. CrateDB stores
data in schemas and tables.

- A **database** in MongoDB is a physical container for collections, similar 
  to a schema in CrateDB, which groups tables together within a database.
- A **collection** in MongoDB is a grouping of documents, similar to a table 
  in CrateDB, which is a structured collection of rows.
- A **document** in MongoDB is a record in a collection, similar to a row in 
  a CrateDB table. It is a set of key-value pairs, where each key represents
  a field, and the value represents the data.
- A **field** in MongoDB is similar to a column in a CrateDB table. In both
  systems, fields (or columns) define the attributes for the records
  (or rows/documents).
- A **primary key** in MongoDB is typically the _id field, which uniquely 
  identifies a document within a collection. In CrateDB, a primary key 
  uniquely identifies a row in a table.
- An **index** in MongoDB is similar to an index in CrateDB. Both are used to
  improve query performance by providing a fast lookup for fields (or columns)
  within documents (or rows).

-- [Databases and Collections]

## Tutorial

The tutorial heavily uses Docker to provide services and to run jobs.
Alternatively, you can use the drop-in replacement Podman.
The walkthrough uses basic example setup including MongoDB v7.0.x, CrateDB
and a few samples worth of data that is being transferred to CrateDB.

### Services

Prerequisites are running instances of CrateDB and MongoDB.

Start MongoDB.
:::{code} shell
docker run --rm -it --name=mongodb \
  --publish=27017:27017 \
  --volume="$PWD/var/lib/mongodb:/data/db" \
  mongo:latest
:::

Start CrateDB.
:::{code} shell
docker run --rm -it --name=cratedb \
  --publish=4200:4200 \
  --volume="$PWD/var/lib/cratedb:/data" \
  crate:latest -Cdiscovery.type=single-node
:::

### Sample Data

In this case we imported demo data to MongoDB in JSON format:

:::{code} shell
  [
      {
          "_id": "66bb0bd8e17c5c509fbc8b2c",
          "VendorID": 2,
          "tpep_pickup_datetime": 1563051934000,
          "tpep_dropoff_datetime": 1563053222000,
          "passenger_count": 2,
          "trip_distance": 3.29,
          "RatecodeID": 1,
          "store_and_fwd_flag": "N",
          "PULocationID": 79,
          "DOLocationID": 170,
          "payment_type": 1,
          "fare_amount": 15.5,
          "extra": 0.5,
          "mta_tax": 0.5,
          "tip_amount": 3.86,
          "tolls_amount": 0,
          "improvement_surcharge": 0.3,
          "total_amount": 23.16,
          "congestion_surcharge": 2.5,
          "airport_fee": ""
      }, ...
  ]
:::

Import data to MongoDB:
:::{code} shell
mongoimport --db testdrive --collection demo --file demodata.json --jsonArray
:::

:::{note}
`mongoimport` is part of the [MongoDB Database tools].
:::

Verify data is present:
:::{code} shell
docker exec -it mongodb mongosh
:::

:::{code} shell
use testdrive
db.demo.find().pretty()
:::

### Data Import

First, create these command aliases, for better UX.
:::{code} shell
alias crash="docker run --rm -it --link=cratedb ghcr.io/crate-workbench/cratedb-toolkit:latest crash"
alias ctk="docker run --rm -it ghcr.io/crate/cratedb-toolkit:latest  ctk"
:::

Now, import data from MongoDB database/collection into CrateDB schema/table.
:::{code} shell
ctk load table \
  "mongodb://localhost:27017/testdrive/demo" \
  --cratedb-sqlalchemy-url="crate://crate@cratedb:4200/testdrive/demo"
:::

Verify that relevant data has been transferred to CrateDB.
:::{code} shell
crash --host=cratedb --command="SELECT * FROM testdrive.demo;"
:::

## Cloud to Cloud

The procedure for importing data from [MongoDB Atlas] into [CrateDB Cloud] is
similar, with a few small adjustments.

First, helpful aliases again:
:::{code} shell
alias ctk="docker run --rm -it ghcr.io/crate/cratedb-toolkit:latest ctk"
alias crash="docker run --rm -it ghcr.io/crate-workbench/cratedb-toolkit:latest crash"
:::

You will need your credentials for both CrateDB and MongoDB. 
These are, with examples:

**CrateDB Cloud**
* Host: ```gray-wicket-systri-warrick.aks1.westeurope.azure.cratedb.net```
* Username: ```admin```
* Password: ```-9..nn```

**MongoDB Atlas**
  * Host: ```cluster0.nttj7.mongodb.net```
  * User: ```admin```
  * Password: ```a1..d1```

For CrateDB, the credentials are displayed at time of cluster creation.
For MongoDB, they can be found in the [cloud platform] itself.

Now, same as before, import data from MongoDB database/collection into 
CrateDB schema/table.
:::{code} shell
ctk load table \
  "mongodb+srv://admin:a..1@cluster0.nttj7.mongodb.net/testdrive/demo" \
  --cratedb-sqlalchemy-url='crate://admin:-..n@gray-wicket-systri-warrick.aks1.westeurope.azure.cratedb.net:4200/testdrive/demo?ssl=true'
:::

::: {note}
Note the **necessary** `ssl=true` query parameter at the end of both database connection URLs
when working on Cloud-to-Cloud transfers.
:::

Verify that relevant data has been transferred to CrateDB.
:::{code} shell
crash --hosts 'https://admin:-..n@gray-wicket-systri-warrick.aks1.westeurope.azure.cratedb.net:4200' --command 'SELECT * FROM testdrive.demo;'
:::

## More information

There are more ways to apply the I/O subsystem of CrateDB Toolkit as
pipeline elements in your daily data operations routines. Please visit the 
[CrateDB Toolkit MongoDB I/O subsystem] documentation, to learn more about what's possible.

The MongoDB I/O subsystem is based on the [migr8] migration utility package. Please also
check its documentation to learn about more of its capabilities, supporting
you when working with MongoDB.


[cloud platform]: https://cloud.mongodb.com
[CrateDB]: https://github.com/crate/crate
[CrateDB Cloud]: https://console.cratedb.cloud/
[CrateDB Toolkit MongoDB I/O subsystem]: https://cratedb-toolkit.readthedocs.io/io/mongodb/loader.html
[Databases and Collections]: https://www.mongodb.com/docs/manual/core/databases-and-collections/
[migr8]: https://cratedb-toolkit.readthedocs.io/io/mongodb/migr8.html
[MongoDB]: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-community-with-docker/
[MongoDB Atlas]: https://www.mongodb.com/cloud/atlas
[MongoDB Database tools]: https://www.mongodb.com/docs/database-tools/installation/installation-linux/
[report them]: https://github.com/crate-workbench/cratedb-toolkit/issues
