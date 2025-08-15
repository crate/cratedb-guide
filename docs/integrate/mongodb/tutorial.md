(mongodb-tutorial)=
# Load data from MongoDB into CrateDB

The tutorial will walk you through starting MongoDB and CrateDB,
inserting a record into a MongoDB collection, transferring the collection
into a CrateDB table, and validating that the data has
been stored successfully.
The data transfer is supported by the [CrateDB Toolkit MongoDB I/O] data
pipeline elements.

## Prerequisites

Docker is used for running all components. This approach works consistently
across Linux, macOS, and Windows. Alternatively, you can use Podman.

Create a shared network.
```shell
docker network create cratedb-demo
```

Start CrateDB.
```shell
docker run --rm --name=cratedb --network=cratedb-demo \
  --publish=4200:4200 --publish=5432:5432 \
  --env=CRATE_HEAP_SIZE=2g docker.io/crate -Cdiscovery.type=single-node
```

Start MongoDB.
```shell
docker run --rm --name=mongodb --network=cratedb-demo \
  --publish=27017:27017 \
  docker.io/mongo
```

Prepare shortcuts for the CrateDB shell, CrateDB Toolkit, and the MongoDB client
programs.

::::{tab-set}

:::{tab-item} Linux and macOS
To make the settings persistent, add them to your shell profile (e.g., `~/.profile` or `~/.zshrc`).
```shell
alias crash="docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash"
alias ctk="docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk"
alias mongosh="docker run --rm -it --network=cratedb-demo docker.io/mongo mongosh"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash @args }
function ctk { docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk @args }
function mongosh { docker run --rm -it --network=cratedb-demo docker.io/mongo mongosh @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash $*
doskey ctk=docker run --rm -i --network=cratedb-demo ghcr.io/crate/cratedb-toolkit ctk $*
doskey mongosh=docker run --rm -it --network=cratedb-demo docker.io/mongo mongosh $*
```
:::

::::

## Usage

Insert a record into a MongoDB collection; you can repeat this step as needed.
```shell
mongosh --host mongodb --db test --eval 'db.demo.insert({"temperature": 42.84, "humidity": 83.1})'
```

Invoke the data transfer pipeline.
```shell
ctk load table \
  "mongodb://mongodb/test/demo" \
  --cluster-url="crate://cratedb/doc/mongodb_demo"
```

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM doc.mongodb_demo"
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
