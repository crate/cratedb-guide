(kestra-usage)=
# Data pipelines with CrateDB and Kestra

:::{div} sd-text-muted
[Kestra] provides open‑source workflow automation and orchestration.
:::

You can use it to automate and manage complex workflows
efficiently. It integrates with Postgres, Git, Docker, Kubernetes, and
more. The web UI lets you create, modify, and manage workflows
without writing code.

In this usage guide, we will show you how CrateDB integrates with Kestra using the PostgreSQL plugin to create an efficient and scalable data pipeline.

## Run Kestra on Docker

You can quickly start Kestra using Docker. First, install Docker on your machine if you haven't already.

```bash
docker run --rm --name=kestra --publish=8080:8080 docker.io/kestra/kestra:latest
```

This starts the Kestra server on your local machine. Access it by navigating to [http://localhost:8080](http://localhost:8080/) in your web browser.
From there, you can start creating workflows and automating your processes using Kestra's web interface.

![Kestra UI home screen](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/80c3eb1bbc2de07a343bc56b1a5db24cf0569df7.png){width=690px height=290px}


## Deploy CrateDB clusters

To deploy a new cluster on CrateDB Cloud, sign up for a
[CrateDB Cloud account](https://console.cratedb.cloud/).
New organizations receive a free trial credit for
cluster deployment, scaling, and other operations. After signing up,
create a cluster by selecting *Create Cluster* and choosing your preferred
cloud provider and region. In this example, we use a 1‑node cluster with
4 GiB of storage, sufficient for development and low‑traffic applications.

![CrateDB Cloud cluster configuration screen showing a 1-node cluster with 4 GiB storage option](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/5c4c24dde906df6004392356138637444844f57d.png){height=480px}


Once your cluster is up and running, use CrateDB's powerful distributed SQL database features via the web-based Admin UI.

## Provision databases

Let's import some data on the first cluster. Navigate to the cluster overview page and click the *Learn how to import data* link.

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

On the second cluster, create an empty `nyc_taxi` table.

## Transfer data

You can move data between CrateDB clusters in several ways. The following example shows how to do this with Kestra.

### Define workflow

As a next step, we will create a new Kestra Flow to move data between clusters.

Flows in Kestra implement workflows.
Each flow uses a declarative YAML model and contains all the tasks in the order they will run.
A flow must have an identifier (id), a namespace, and a list of tasks.

### Define source

To read from a PostgreSQL-compatible database, such as CrateDB,
Kestra offers the `io.kestra.plugin.jdbc.postgresql.Query` plugin.

The *Query* task allows users to execute custom SQL queries against
a database and use the results in their workflow.
It offers various parameters such as auto-committing SQL statements,
specifying access-control rules, and storing fetch results.

The following snippet shows the declaration of our workflow and the specification of the first task that selects data from the `nyc_taxi` table and runs the query on the first CrateDB cluster:

```yaml
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


In this task, we set the `store` parameter to `true` to store results for the next task.

### Define target

In Kestra, a batch task is a type of task that allows you to fetch rows from a table and bulk insert them into another one. We will use an instance of a batch task to fetch the results of the first task and to insert the results into the table on the second cluster.

The following snippet shows the Batch task declaration used for inserting data into the table on the second CrateDB cluster:

```yaml
- id: update
  type: io.kestra.plugin.jdbc.postgresql.Batch
  from: "{{ outputs.query.uri }}"
  url: jdbc:postgresql://cratedb-kestra2.aks1.eastus2.azure.cratedb.net:5432/
  username: admin
  password: my_super_secret_password
  sql: |
    INSERT INTO doc.nyc_taxi VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
```

When a Kestra task executes, it may create or modify a resource, such as a file, database record, or API endpoint.
Kestra allows the output produced by the task to be stored in the execution flow context and used by subsequent tasks.
The `output` object captures information about the task results, including any resources created or modified.

In our example, `output.query.uri` refers to the URI of the resource the previous task created.
Specifically, it refers to the URI of the database records returned by the `SELECT` statement.

### Define result

Finally, once the data are imported to the second table, let’s create a new task that selects data from that table:

```yaml
- id: select
  type: io.kestra.plugin.jdbc.postgresql.Query
  url: jdbc:postgresql://cratedb-kestra2.aks1.eastus2.azure.cratedb.net:5432/
  username: admin
  password: my_super_secret_password
  sql: SELECT MAX_BY(passenger_count, fare_amount) FROM doc.nyc_taxi
  store: false
```

In the last task, we select the `passenger_count` value with the highest `fare_amount` using the `MAX_BY` aggregation function. `MAX_BY` ranks among CrateDB's latest aggregation functions. Learn more in our [recent blog post](https://crate.io/blog/find-the-latest-reported-values-with-ease.-introducing-max_by-and-min_by-aggregations-in-cratedb-5.2).

### Execute the flow

To execute the flow click on the *New Execution* button below the Flow specification. To monitor the execution of your Flow, check the Logs view:

![Kestra Logs view showing execution status and running times for each task in the flow](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/fd57f90eea19631daec9052dd8921fbce519d2a7.png)


The Logs view shows the execution status of each task, as well as the running times. There are other ways to monitor the execution of Flows in Kestra and we refer to the official Kestra documentation for a better overview of its full capabilities.

Finally, let's check the data in the second cluster. As illustrated below, exactly 1000 records were inserted:

![CrateDB query result showing 1000 records inserted into the nyc_taxi table](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/c47fc7cdd3a91a007250c428a704f91962066e7b.png)


## Wrap up

If you need to automatically manage CrateDB data pipelines, [Kestra] provides a strong solution.
It lets you define workflows without writing code and integrates with PostgreSQL (and CrateDB), Kubernetes, Docker, Git, and more.

In this usage guide, we have also shown how to deploy your CrateDB cluster in a few clicks. If you want to try it out and enjoy all of the CrateDB features, sign up for the [CrateDB Cloud](https://console.cratedb.cloud/) trial.

To learn more about updates, features, and other questions you might have, join the [CrateDB community].


[CrateDB community]: https://community.cratedb.com/
[Kestra]: https://kestra.io/
