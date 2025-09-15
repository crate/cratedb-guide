(influxdb-data-model)=
# Data Model

InfluxDB stores time-series data in buckets and measurements; CrateDB stores
data in schemas and tables.

- A **bucket** is a named location with a retention policy where time series data is stored.
- A **series** is a logical grouping of data defined by a shared measurement and tag set (fields do not define series).
- A **measurement** is similar to an SQL database table.
- A **tag** is similar to an indexed column in an SQL database.
- A **field** is similar to a non-indexed column in an SQL database.
- A **point** is similar to an SQL row.

> Source: [What are series and bucket in InfluxDB]


[What are series and bucket in InfluxDB]: https://stackoverflow.com/questions/58190272/what-are-series-and-bucket-in-influxdb/69951376#69951376
