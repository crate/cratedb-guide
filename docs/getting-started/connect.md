(connect)=
(connectivity)=
(io)=
(import-export)=


# Database Connectivity

CrateDB connectivity options.

You have a variety of options to connect to CrateDB, and to integrate it with
off-the-shelve, 3rd-party, open-source, and proprietary applications.

{tags-primary}`Connect`
{tags-primary}`Import`
{tags-primary}`Export`
{tags-primary}`Extract`
{tags-primary}`Load`
{tags-primary}`ETL`


## Interfaces and Protocols

CrateDB supports both the [HTTP protocol] and the [PostgreSQL wire protocol],
which ensures that many clients that work with PostgreSQL, will also work with
CrateDB.

Through corresponding drivers, CrateDB is compatible with [ODBC],
[JDBC], and other database API specifications.
By supporting [SQL], CrateDB is compatible with many standard database
environments out of the box.

- [CrateDB HTTP interface]
- [CrateDB PostgreSQL interface]
- [CrateDB SQL protocol]

To learn more, please refer to the documentation sections about supported
client drivers, libraries, and frameworks, and corresponding tutorials.


## Drivers and Integrations

CrateDB provides plenty of connectivity options with database drivers,
applications, and frameworks, in order to get time series data in and
out of CrateDB, and to connect to other applications.

- [Drivers and Integrations]
- [](inv:crate-clients-tools#connect)
- [](inv:crate-clients-tools#df)
- [](inv:crate-clients-tools#etl)
- [](inv:crate-clients-tools#metrics)

## Tutorials

Hands-on tutorials about CrateDB fundamentals about data I/O, as well as about
properly configuring and connecting relevant 3rd-party software components to
work optimally with CrateDB.

:::{rubric} Overview
:::
- [](#integrate)
- [More integration tutorials]
- [](#etl)
- [](#integrate-metrics)
- [](#performance)

:::{rubric} Specific Information
:::
- [Fundamentals of the COPY FROM statement]
- [Import weather data using Dask]


[CrateDB HTTP interface]: inv:crate-reference:*:label#interface-http
[CrateDB PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[CrateDB SQL protocol]: inv:crate-reference:*:label#sql
[Drivers and Integrations]: inv:crate-clients-tools:*:label#index
[Fundamentals of the COPY FROM statement]: https://community.cratedb.com/t/fundamentals-of-the-copy-from-statement/1178
[HTTP protocol]: https://en.wikipedia.org/wiki/HTTP
[Import weather data using Dask]: https://github.com/crate/cratedb-examples/blob/main/topic/timeseries/dask-weather-data-import.ipynb
[JDBC]: https://en.wikipedia.org/wiki/Java_Database_Connectivity
[More integration tutorials]: https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015
[ODBC]: https://en.wikipedia.org/wiki/Open_Database_Connectivity
[PostgreSQL wire protocol]: https://www.postgresql.org/docs/current/protocol.html
[SQL]: https://en.wikipedia.org/wiki/Sql
