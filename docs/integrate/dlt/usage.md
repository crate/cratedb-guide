---
title: CrateDB
description: CrateDB `dlt` destination
keywords: [ cratedb, destination, data warehouse ]
---

(dlt-usage)=
# Load API data with dlt

:::{div} sd-text-muted
Exercise a canonical `dlt init` example with CrateDB.
:::

## Install the package

Install the dlt destination adapter for CrateDB.
```shell
pip install dlt-cratedb
```

## Initialize the dlt project

Start by initializing a new example `dlt` project.

```shell
export DESTINATION__CRATEDB__DESTINATION_TYPE=postgres
dlt init chess cratedb
```

The `dlt init` command will initialize your pipeline with `chess` [^chess-source]
as the source, and `cratedb` as the destination. It generates several files and directories.

## Edit the pipeline definition

The pipeline definition is stored in the Python file `chess_pipeline.py`.

- Because the dlt adapter currently only supports writing to the default `doc` schema
  of CrateDB [^create-schema], please replace `dataset_name="chess_players_games_data"`
  by `dataset_name="doc"` within the generated `chess_pipeline.py` file.

- To initialize the CrateDB destination adapter, insert the `import dlt_cratedb`
  statement at the top of the file. Otherwise, the destination will not be found,
  so you will receive a corresponding error [^not-initialized-error].

## Configure credentials

Next, set up the CrateDB credentials in the `.dlt/secrets.toml` file as shown below.
CrateDB is compatible with PostgreSQL and uses the `psycopg2` driver, like the
`postgres` destination.

```toml
[destination.cratedb.credentials]
host = "localhost"                       # CrateDB server host.
port = 5432                              # CrateDB PostgreSQL TCP protocol port, default is 5432.
username = "crate"                       # CrateDB username, default is usually "crate".
password = "crate"                       # CrateDB password, if any.
database = "crate"                       # CrateDB only knows a single database called `crate`.
connect_timeout = 15
```

Alternatively, you can pass a database connection string as shown below.
```toml
destination.cratedb.credentials="postgres://crate:crate@localhost:5432/"
```
Keep it at the top of your TOML file, before any section starts.
Because CrateDB uses `psycopg2`, using `postgres://` is the right choice.

## Start CrateDB

Use Docker or Podman to run an instance of CrateDB for evaluation purposes.
```shell
docker run --rm --name=cratedb --publish=4200:4200 --publish=5432:5432 crate:latest '-Cdiscovery.type=single-node'
```

## Run pipeline

```shell
python chess_pipeline.py
```

## Explore data
```shell
crash -c 'SELECT * FROM players_profiles LIMIT 10;'
crash -c 'SELECT * FROM players_online_status LIMIT 10;'
```


[^chess-source]: The `chess` dlt source pulls publicly available data from
  the [Chess.com Published-Data API].
[^create-schema]: CrateDB does not support `CREATE SCHEMA` yet, see [CRATEDB-14601].
  This means by default, unless any table exists within a schema, the schema appears
  not to exist at all. However, it also can't be created explicitly.
  currently implicitly created when tables exist in them.
[^not-initialized-error]: `UnknownDestinationModule: Destination "cratedb" is not one of the standard dlt destinations`

[Chess.com Published-Data API]: https://www.chess.com/news/view/published-data-api
[CRATEDB-14601]: https://github.com/crate/crate/issues/14601
