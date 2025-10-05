(mongodb-usage)=
# Load data from MongoDB into CrateDB

The usage guide will walk you through starting MongoDB and CrateDB,
inserting a record into a MongoDB collection, transferring the collection
into a CrateDB table, and validating that the data has
been stored successfully.
The data transfer is supported by the [CrateDB Toolkit MongoDB I/O] data
pipeline elements.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

## Submit data

Insert a record into a MongoDB collection; you can repeat this step as needed.
```shell
docker compose run --rm --no-TTY mongosh mongosh --host mongodb --db test --eval 'db.demo.insert({"temperature": 42.84, "humidity": 83.1})'
```

Invoke the data transfer pipeline.
```shell
docker compose run --rm --no-TTY ctk ctk load table "mongodb://mongodb/test/demo" --cluster-url="crate://cratedb/doc/mongodb_demo"
```

## Explore data

Inspect data stored in CrateDB.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.mongodb_demo"
```
```psql
+--------------------------+-----------------------------------------------------------------------------+
| oid                      | data                                                                        |
+--------------------------+-----------------------------------------------------------------------------+
| 68e1cf2a1d9d9d28b1ce5f47 | {"_id": "68e1cf2a1d9d9d28b1ce5f47", "humidity": 83.1, "temperature": 42.84} |
+--------------------------+-----------------------------------------------------------------------------+
SELECT 1 row in set (0.027 sec)
```


:::{tip}
To bulk import example data into the same database and collection used above:
```shell
mongoimport --db test --collection demo --file demodata.json --jsonArray
```
Note: `mongoimport` is part of the [MongoDB Database tools].
:::


[CrateDB Toolkit MongoDB I/O]: https://cratedb-toolkit.readthedocs.io/io/mongodb/loader.html
[MongoDB Database tools]: https://www.mongodb.com/docs/database-tools/installation/installation-linux/
