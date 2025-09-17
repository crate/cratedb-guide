(rill-tutorial)=
# Introducing Rill and BI as Code with CrateDB Cloud

In the world of data analytics, Rill represents a revolutionary approach to Business Intelligence (BI), championing the concept of BI as code. This methodology allows for the versioning, tracking, and collaboration on BI projects using code, which can be more efficient and scalable than traditional BI tools. By leveraging Rill in conjunction with CrateDB Cloud, you can harness the power of distributed SQL database technology for real-time analytics at scale.

## Create a free-tier cluster

To begin setting up your CrateDB Cloud free-tier cluster, follow these steps:

1. Navigate to the CrateDB Cloud Console at [https://console.cratedb.cloud](https://console.cratedb.cloud).
2. Click on "Deploy Cluster."
3. Choose your desired region from the list provided.
4. Select the "CRFEE" plan for the Free tier option.
5. Enter a unique name for your cluster, such as "rilldata."
6. Click on "Deploy Cluster" to initiate the setup.

After initiating the cluster deployment, you will be directed to a screen where you can copy your username and password. Please ensure you save these credentials securely. The cluster setup usually completes in less than 5 minutes.

![Cluster setup|600x440](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/f/f8860d7873923990307a3f43112fae66898787c9.png){width=800px}

**Connecting to Your Cluster:**

Once your cluster is ready, the next step involves connecting to it:

- Go to the "Connecting to your cluster" section and scroll down to find the "psycopg3-sync" part.
- Copy the Postgres formatted DB-URI provided, which looks similar to this:

```
postgres://admin:<PASSWORD>@rilldata.aks1.westeurope.azure.cratedb.net:5432
```

- Replace `<PASSWORD>` with the password you saved earlier, resulting in a connection string like:

```
postgres://admin:Yl3dnY666YlPyVkHKdIYjtqk@rilldata.aks1.westeurope.azure.cratedb.net:5432
```

## Set up Rill

To integrate Rill with your CrateDB Cloud cluster:

1. Install Rill by executing the shell install script:

```shell
curl https://rill.sh | sh
```

2. Navigate to the directory where you wish to create your Rill project:

```shell
cd ~/my-rill-projects/
```

3. Initiate a new Rill project named `my-cratedb-rill-project`:

```shell
rill start my-cratedb-rill-project
```

This action should open a browser window at `http://localhost:9009/welcome`, allowing you to begin adding data.

![Rill setup|600x400](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/3/3596a5edc5560ede38f8683d1092fb3fbbcb0435.jpeg){width=800px}

When adding data, select PostgreSQL as your data source.

![Select PostgreSQL|380x400](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/a/aff8ddc9f63840a330e8bf735de3cfd1179ef354.png){height=480px}

Enter the following details:

**SQL Query** (or your own query): 
```sql
SELECT classification, country, first_ascent, height, mountain, prominence, region FROM sys.summits
```

**Name**: 
```
summits_table
```

**Postgres Connection String** (Use the connection string you formed earlier)
```
postgres://admin:Yl3dnY666YlPyVkHKdIYjtqk@rilldata.aks1.westeurope.azure.cratedb.net:5432
```

![image|690x323](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/0/050718f5eb81abfc06db1f040984a53bfd95e296.png){width=800px}


Congratulations! You're now ready to explore Rill with your CrateDB Cloud cluster.
