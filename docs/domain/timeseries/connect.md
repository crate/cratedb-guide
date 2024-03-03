(timeseries-connect)=
(timeseries-io)=
(timeseries-import-export)=

# Database / Time Series Connectivity

CrateDB connectivity options for working with time series data.

{tags-primary}`Connect`
{tags-primary}`Import`
{tags-primary}`Export`
{tags-primary}`Extract`
{tags-primary}`Load`
{tags-primary}`ETL`


## Interfaces and Protocols

CrateDB supports both the [HTTP protocol] and the [PostgreSQL wire protocol],
which ensures that many clients that work with PostgreSQL, will also work with
CrateDB. Through corresponding drivers, CrateDB is compatible with [ODBC],
[JDBC], and other database API specifications.

By supporting [SQL], CrateDB is compatible with many standard database
environments out of the box.

- [CrateDB HTTP interface]
- [CrateDB PostgreSQL interface]
- [CrateDB SQL protocol]

## Drivers and Integrations

CrateDB provides plenty of connectivity options with database drivers,
applications, and frameworks, in order to get time series data in and
out of CrateDB, and to connect to other applications.

- [](inv:crate-clients-tools#connect)
- [](inv:crate-clients-tools#df)
- [](inv:crate-clients-tools#etl)
- [](inv:crate-clients-tools#metrics)

## Tutorials

Hands-on tutorials about CrateDB fundamentals about data I/O, as well as about
properly configuring and connecting relevant 3rd-party software components to
work optimally with CrateDB.

- [Fundamentals of the COPY FROM statement]
- [](#etl)
- [](#integrate-metrics)
- [](#performance)
- [Import weather data using Dask]


[CrateDB HTTP interface]: inv:crate-reference:*:label#interface-http
[CrateDB PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[CrateDB SQL protocol]: inv:crate-reference:*:label#sql
[Fundamentals of the COPY FROM statement]: https://community.cratedb.com/t/fundamentals-of-the-copy-from-statement/1178
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[Import weather data using Dask]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/dask-weather-data-import.ipynb
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[SQL]: https://en.wikipedia.org/wiki/Sql
