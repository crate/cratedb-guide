(connect)=

# Connect

You have a variety of options to connect your custom applications to CrateDB,
and to integrate it with 3rd-party applications, mostly using [CrateDB's
PostgreSQL interface].

This documentation section lists client drivers, libraries, and frameworks,
which can be used together with CrateDB, and outlines how to use them optimally.

- [Drivers and Integrations]
- [Integration Tutorials]

About specific topics, there are code examples for database drivers,
dataframe-, and ORM-libraries.

- [Database Driver Code Examples]
- SQLAlchemy
  - [SQLAlchemy Support], [SQLAlchemy by Example], [SQLAlchemy Code Examples]
- pandas and Dask
  - [Importing Parquet files into CrateDB using Apache Arrow and SQLAlchemy]
  - [Guide to efficient data ingestion to CrateDB with pandas]
  - [Guide to efficient data ingestion to CrateDB with pandas and Dask]
  - [Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]
  - [pandas code examples]
  - [Dask code examples]
- Polars
  - [Polars code examples]




[CrateDB's PostgreSQL interface]: inv:crate-reference:*:label#interface-postgresql
[Dask code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/dask
[Database Driver Code Examples]: inv:crate-clients-tools:*:label#connect
[Drivers and Integrations]: inv:crate-clients-tools:*:label#index
[Efficient batch/bulk INSERT operations with pandas, Dask, and SQLAlchemy]: https://cratedb.com/docs/python/en/latest/by-example/sqlalchemy/dataframe.html
[Guide to efficient data ingestion to CrateDB with pandas]: https://community.crate.io/t/guide-to-efficient-data-ingestion-to-cratedb-with-pandas/1541
[Guide to efficient data ingestion to CrateDB with pandas and Dask]: https://community.crate.io/t/guide-to-efficient-data-ingestion-to-cratedb-with-pandas-and-dask/1482
[Importing Parquet files into CrateDB using Apache Arrow and SQLAlchemy]: https://community.crate.io/t/importing-parquet-files-into-cratedb-using-apache-arrow-and-sqlalchemy/1161
[Integration Tutorials]: https://community.crate.io/t/overview-of-cratedb-integration-tutorials/1015
[pandas code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/pandas
[Polars code examples]: https://github.com/crate/cratedb-examples/tree/main/by-dataframe/polars
[SQLAlchemy by Example]: https://cratedb.com/docs/python/en/latest/by-example/index.html#sqlalchemy-by-example
[SQLAlchemy Code Examples]: https://github.com/crate/cratedb-examples/tree/main/by-language/python-sqlalchemy
[SQLAlchemy Support]: https://cratedb.com/docs/python/en/latest/sqlalchemy.html
