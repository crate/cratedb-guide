# Cloud to Cloud

The procedure for importing data from [InfluxDB Cloud] into [CrateDB Cloud] is
similar to the {ref}`standalone variant <influxdb-tutorial>`, with a few small
adjustments.

First, helpful aliases:
```shell
alias ctk="docker run --rm -it ghcr.io/crate/cratedb-toolkit:latest ctk"
alias crash="docker run --rm -it ghcr.io/crate/cratedb-toolkit:latest crash"
```

You will need credentials for both CrateDB and InfluxDB.
Use placeholders and/or environment variables (recommended) to avoid leaking
secrets in shell history.

:::{rubric} CrateDB Cloud
:::
- Host: `<CRATEDB_HOST>` (e.g., `cluster-id.eks1.eu-west-1.aws.cratedb.net`)
- Username: `<CRATEDB_USER>` (e.g., `admin`)
- Password: `<CRATEDB_PASSWORD>`

:::{rubric} InfluxDB Cloud
:::
- Host: `<INFLUXDB_HOST>` (e.g., `eu-central-1-1.aws.cloud2.influxdata.com`)
- Organization ID: `<INFLUXDB_ORG_ID>`
- All-Access API token: `<INFLUXDB_TOKEN>`

For CrateDB, the credentials are displayed at time of cluster creation.
For InfluxDB, they can be found in the [cloud platform] itself.

Now, same as before, import data from InfluxDB bucket/measurement into 
CrateDB schema/table.
```shell
ctk load table \
  "influxdb2://${INFLUX_ORG}:${INFLUX_TOKEN}@${INFLUX_HOST}/testdrive/demo?ssl=true" \
  --cluster-url="crate://${CRATEDB_USER}:${CRATEDB_PASSWORD}@${CRATEDB_HOST}:4200/testdrive/demo?ssl=true"
```

:::{note}
Note the **necessary** `ssl=true` query parameter at the end of both database connection URLs
when working on Cloud-to-Cloud transfers.
:::

Verify that relevant data has been transferred to CrateDB.
```shell
crash --hosts "https://${CRATEDB_USER}:${CRATEDB_PASSWORD}@${CRATEDB_HOST}:4200" --command 'SELECT * FROM testdrive.demo;'
```


[cloud platform]: https://docs.influxdata.com/influxdb/cloud/admin
[CrateDB Cloud]: https://console.cratedb.cloud/
[InfluxDB Cloud]: https://cloud2.influxdata.com/
