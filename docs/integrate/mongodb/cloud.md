# Cloud to Cloud

The procedure for importing data from [MongoDB Atlas] into [CrateDB Cloud] is
similar to the {ref}`standalone variant <mongodb-usage>`, with a few small
adjustments.

First, helpful aliases:
```shell
alias crash="docker run --rm -it ghcr.io/crate-workbench/cratedb-toolkit crash"
alias ctk="docker run --rm -i ghcr.io/crate/cratedb-toolkit ctk"
```

You will need credentials for both CrateDB and MongoDB.
These are, with examples:

**CrateDB Cloud**
* Host: `<CRATEDB_CLOUD_HOST>`
* Username: `<CRATEDB_USER>`
* Password: `<CRATEDB_PASSWORD>`

**MongoDB Atlas**
* Host: `<MONGODB_ATLAS_HOST>`
* User: `<MONGODB_USER>`
* Password: `<MONGODB_PASSWORD>`

For CrateDB, the credentials are displayed at time of cluster creation.
For MongoDB, they can be found in the [cloud platform] itself.

Now, same as before, import data from MongoDB database/collection into 
CrateDB schema/table.
```shell
ctk load table "mongodb+srv://admin:a..1@cluster0.nttj7.mongodb.net/testdrive/demo" --cluster-url='crate://admin:-..n@gray-wicket.aks1.westeurope.azure.cratedb.net:4200/testdrive/demo?ssl=true'
```

:::{note}
CrateDB Cloud requires `ssl=true` in the cluster URL. For MongoDB Atlas SRV URIs
(`mongodb+srv://`), TLS is implied and no extra parameter is needed.
:::

Verify that relevant data has been transferred to CrateDB.
```shell
crash --hosts 'https://admin:-..n@gray-wicket.aks1.westeurope.azure.cratedb.net:4200' --command 'SELECT * FROM testdrive.demo;'
```


[cloud platform]: https://cloud.mongodb.com
[CrateDB Cloud]: https://console.cratedb.cloud/
[MongoDB Atlas]: https://www.mongodb.com/cloud/atlas
