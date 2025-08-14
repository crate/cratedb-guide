# Data Model

InfluxDB stores time series data in buckets and measurements. CrateDB stores
data in schemas and tables.

- A **bucket** is a named location with a retention policy where time series data is stored.
- A **series** is a logical grouping of data defined by shared measurement, tag, and field.
- A **measurement** is similar to an SQL database table.
- A **tag** is similar to an indexed column in an SQL database.
- A **field** is similar to an un-indexed column in an SQL database.
- A **point** is similar to an SQL row.

> via: [What are series and bucket in InfluxDB]


[What are series and bucket in InfluxDB]: https://stackoverflow.com/questions/58190272/what-are-series-and-bucket-in-influxdb/69951376#69951376
