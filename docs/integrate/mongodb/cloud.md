# Cloud to Cloud

The procedure for importing data from [MongoDB Atlas] into [CrateDB Cloud] is
similar, with a few small adjustments.

First, helpful aliases again:
:::{code} shell
alias ctk="docker run --rm -it ghcr.io/crate/cratedb-toolkit ctk"
alias crash="docker run --rm -it ghcr.io/crate-workbench/cratedb-toolkit crash"
:::

You will need your credentials for both CrateDB and MongoDB. 
These are, with examples:

**CrateDB Cloud**
* Host: ```gray-wicket.aks1.westeurope.azure.cratedb.net```
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
  --cluster-url='crate://admin:-..n@gray-wicket.aks1.westeurope.azure.cratedb.net:4200/testdrive/demo?ssl=true'
:::

::: {note}
Note the **necessary** `ssl=true` query parameter at the end of both database connection URLs
when working on Cloud-to-Cloud transfers.
:::

Verify that relevant data has been transferred to CrateDB.
:::{code} shell
crash --hosts 'https://admin:-..n@gray-wicket.aks1.westeurope.azure.cratedb.net:4200' --command 'SELECT * FROM testdrive.demo;'
:::



[cloud platform]: https://cloud.mongodb.com
[CrateDB Cloud]: https://console.cratedb.cloud/
[MongoDB Atlas]: https://www.mongodb.com/cloud/atlas
