(kestra-tutorial)=
# Setting up data pipelines with CrateDB and Kestra

[Kestra.io](http://kestra.io/) is an open-source workflow automation and orchestration tool that enables users to automate and manage complex workflows in a streamlined and efficient manner. The tool provides a wide range of features and integrations, including Postgres, Git, Docker, Kubernetes, and more, making automating processes across different platforms and environments easy. Kestra comes with a user-friendly web-based interface, allowing users to create, modify, and manage workflows ***without the need for any coding skills***.

In this tutorial, we will show you how CrateDB integrates with Kestra using the PostgreSQL plugin to create an efficient and scalable data pipeline.

## Running Kestra on Docker

Getting started with Kestra using Docker is a straightforward process. First, you'll need to install Docker on your machine, if you haven't already. Next, you can pull the Kestra official Docker image from the Docker registry and run it using the following command:

`docker run -d -p 8080:8080 kestra/kestra:latest `

This will start the Kestra server on your local machine, which you can access by navigating to [http://localhost:8080](http://localhost:8080/) in your web browser. From there, you can start creating workflows and automating your processes using Kestra's web interface.

![57c8376e-02ff-4e10-89e7-9fc358153409|690x290](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/80c3eb1bbc2de07a343bc56b1a5db24cf0569df7.png)


## Deploy a CrateDB Cloud Cluster

To deploy a new cluster on CrateDB Cloud, you need to sign up for a [CrateDB Cloud account](https://console.cratedb.cloud/). When creating a new organization, you are entitled to a [$200 free credit](https://crate.io/lp-free-trial) to spend on cluster deployment, scaling, and other operations as you see fit. Once you've signed up, you can create a new cluster by selecting the *Create Cluster* button and choosing your preferred cloud provider and region. You can then configure your cluster by selecting the number of nodes and the amount of storage you need. In this example, we used the 1-node cluster with 4GiB of storage which is enough for development environments and low-traffic applications.

![49d00261-bd03-4935-bdaf-15dee6f24a4e|558x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/5c4c24dde906df6004392356138637444844f57d.png)


Once your cluster is up and running, you can start using CrateDB's powerful distributed SQL database features via a web-based Admin UI.

## Move data between clusters with Kestra

There are several ways you can use to move data between CrateDB clusters and in the following example, we will illustrate how to simply do this with Kestra. The prerequisite for this use case is to have two running CrateDB clusters. The most straightforward way is to deploy both CrateDB clusters on CrateDB Cloud.

Now, let’s import some data on the first cluster. To do so, go back to the cluster overview page and click on *Learn how to import data* link. This will open a list of statements you need to execute to load NYC taxi data.

```sql
CREATE TABLE "nyc_taxi" (
  "congestion_surcharge" REAL, 
  "dolocationid" INTEGER, 
  "extra" REAL, 
  "fare_amount" REAL, 
  "improvement_surcharge" REAL, 
  "mta_tax" REAL, 
  "passenger_count" INTEGER, 
  "payment_type" INTEGER, 
  "pickup_datetime" TIMESTAMP WITH TIME ZONE, 
  "pulocationid" INTEGER, 
  "ratecodeid" INTEGER, 
  "store_and_fwd_flag" TEXT, 
  "tip_amount" REAL, 
  "tolls_amount" REAL, 
  "total_amount" REAL, 
  "trip_distance" REAL, 
  "vendorid" INTEGER) WITH ("column_policy" = 'dynamic', "number_of_replicas" = '0', "refresh_interval" = 10000);
```

```sql
COPY "nyc_taxi" FROM 'https://s3.amazonaws.com/crate.sampledata/nyc.yellowcab/yc.2019.07.gz' WITH (compression = 'gzip');
```

On the second cluster, create an empty `nyc_taxi` table. As a next step, we will create a new Kestra Flow to move data between clusters.

Flows in Kestra are used to implement workflows. Each flow is defined as a declarative model in the YAML file and it contains all the tasks and the order in which the tasks will be run. A flow must have an identifier (id), a namespace, and a list of tasks.

### Query CrateDB table

To query a PostgreSQL-compatible database, such as CrateDB, Kestra offers `io.kestra.plugin.jdbc.postgresql.Query` plugin. The *Query* task allows users to execute custom SQL queries against a database and use the results in their workflow. This task offers various parameters such as auto-committing SQL statements, specifying access-control rules, and storing fetch results.

The following snippet shows the declaration of our workflow and the specification of the first task that selects data from the `nyc_taxi` table and runs the query on the first CrateDB cluster:

```
id: cratedb-kestra
namespace: io.kestra.crate
tasks:
- id: query
  type: io.kestra.plugin.jdbc.postgresql.Query
  url: jdbc:postgresql://cratedb-kestra.aks1.westeurope.azure.cratedb.net:5432/
  username: admin
  password: my_super_secret_password
  sql: SELECT * FROM doc.nyc_taxi LIMIT 1000
  store: true
```


In this task, we set the `store` parameter is set to `true` to allow storing the results that will be used as input in the following task.

### Insert data into the second table

In Kestra, a batch task is a type of task that allows you to fetch rows from a table and bulk insert them into another one. We will use an instance of a batch task to fetch the results of the first task and to insert the results into the table on the second cluster.

The following snippet shows the Batch task declaration used for inserting data into the table on the second CrateDB cluster:

```
- id: update
  type: io.kestra.plugin.jdbc.postgresql.Batch
  from: "{{ outputs.query.uri }}"
  url: jdbc:postgresql://cratedb-kestra2.aks1.eastus2.azure.cratedb.net:5432/
  username: admin
  password: my_super_secret_password
  sql: |
    INSERT INTO doc.nyc_taxi VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
```

When a Kestra task is executed, it may create or modify a resource, such as a file, database record, or API endpoint. Kestra allows the output produced by the task to be stored in the execution flow context and used by subsequent tasks. The `output` object is used to capture information about the results of the task, including any resources that were created or modified.

In our example, the `output.query.uri` refers to the URI of the resource that was created by the previous task. Specifically, it refers to the URI of the database records returned by the `SELECT` statement.

Finally, once the data are imported to the second table, let’s create a new task that selects data from that table:

```
- id: select
  type: io.kestra.plugin.jdbc.postgresql.Query
  url: jdbc:postgresql://kestra-testing-cluster2.aks1.eastus2.azure.cratedb.net:5432/
  username: admin
  password: my_super_secret_password
  sql: SELECT MAX_BY(passenger_count, fare_amount) FROM doc.nyc_taxi
  store: false
```

In the last task, we select the `passenger_count` value for which the `fare_amount` is the highest and to achieve that we use the `MAX_BY` aggregation function. `MAX_BY` is one of the latest aggregation functions supported by CrateDB and to learn more about it, check out our [recent blog post](https://crate.io/blog/find-the-latest-reported-values-with-ease.-introducing-max_by-and-min_by-aggregations-in-cratedb-5.2).

### Execute the flow

To execute the flow click on the *New Execution* button below the Flow specification. To monitor the execution of your Flow, check the Logs view:

![8d50d548-710f-4496-b862-66eb1d166c0c|690x165](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/fd57f90eea19631daec9052dd8921fbce519d2a7.png)


The Logs view shows the execution status of each task, as well as the running times. There are other ways to monitor the execution of Flows in Kestra and we refer to the official Kestra documentation for a better overview of its full capabilities.

Finally, let’s check the data in the second cluster. As illustrated below, we can see that exactly 1000 records got inserted:

![4d84631b-ef55-4d90-a7ba-104046eb0300|690x133](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/c47fc7cdd3a91a007250c428a704f91962066e7b.png)


## Wrap up

If you need to automatically manage CrateDB data pipelines, [kestra.io](http://kestra.io/) can be a good choice. It allows you to specify workflows without requiring coding skills. Furthermore, it supports integrations with various systems including Postgres (and CrateDB), Kubernetes, Docker, Git, and many others.

In this tutorial, we have also shown how to deploy your CrateDB cluster in a few clicks. If you want to try it out and enjoy all of the CrateDB features, sign up for the [CrateDB Cloud](https://console.cratedb.cloud/?utm_campaign=2022-Q2-WS-Free-Trial&utm_source=website&utm_medium=free-trial-overhaul&hsCtaTracking=a7e2a487-cfb9-4a50-8e75-3029b9e176fb%7C7863166c-05e4-4334-9dd5-58dfdd6e78c1) trial.

To learn more about updates, features, and other questions you might have, join our [CrateDB](https://community.cratedb.com/) community.
