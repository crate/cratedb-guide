# Cloud to Cloud

The procedure for importing data from [InfluxDB Cloud] into [CrateDB Cloud] is
similar, with a few small adjustments.

First, helpful aliases again:
:::{code} shell
alias ctk="docker run --rm -it ghcr.io/crate/cratedb-toolkit:latest ctk"
alias crash="docker run --rm -it ghcr.io/crate/cratedb-toolkit:latest crash"
:::

You will need your credentials for both CrateDB and InfluxDB. 
These are, with examples:

:::{rubric} CrateDB Cloud
:::
- Host: `purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net`
- Username: `admin`
- Password: `dZ..qB`

:::{rubric} InfluxDB Cloud
:::
- Host: `eu-central-1-1.aws.cloud2.influxdata.com`
- Organization ID: `9fafc869a91a3406`
- All-Access API token: `T2..==`

For CrateDB, the credentials are displayed at time of cluster creation.
For InfluxDB, they can be found in the [cloud platform] itself.

Now, same as before, import data from InfluxDB bucket/measurement into 
CrateDB schema/table.
```shell
export CRATEPW='dZ..qB'
ctk load table \
  "influxdb2://9f..06:T2..==@eu-central-1-1.aws.cloud2.influxdata.com/testdrive/demo?ssl=true" \
  --cratedb-sqlalchemy-url="crate://admin:${CRATEPW}@purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net:4200/testdrive/demo?ssl=true"
```

:::{note}
Note the **necessary** `ssl=true` query parameter at the end of both database connection URLs
when working on Cloud-to-Cloud transfers.
:::

Verify that relevant data has been transferred to CrateDB.
```shell
export CRATEPW='dZ..qB'
crash --hosts 'https://admin:${CRATEPW}@purple-shaak-ti.eks1.eu-west-1.aws.cratedb.net:4200' --command 'SELECT * FROM testdrive.demo;'
```


[cloud platform]: https://docs.influxdata.com/influxdb/cloud/admin
[CrateDB Cloud]: https://console.cratedb.cloud/
[InfluxDB Cloud]: https://cloud2.influxdata.com/
