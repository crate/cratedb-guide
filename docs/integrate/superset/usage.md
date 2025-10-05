(superset-usage)=
# Set up Apache Superset with CrateDB

## Introduction
This walkthrough will guide you through the process to quickly set up a Python environment with [Apache Superset](https://superset.apache.org/), load data into [CrateDB](https://cratedb.com/product), and integrate both with each other.

It has been derived from a [corresponding recipe](https://github.com/crate/cratedb-examples/tree/main/application/apache-superset) we use on our CI systems to verify connectivity between Apache Superset and CrateDB.

## Prerequisites
You will need Bash, Docker, and Python to be installed on your workstation. All other prerequisites will be installed into your working tree.

## Install

Set up a Python environment, and install and configure Apache Superset. You can locate the installation within an arbitrary folder on your workstation, for example `~/dev/cratedb-superset`.
```shell
# Create and activate Python virtualenv.
python3 -m venv .venv
source .venv/bin/activate

# Install Apache Superset, CrateDB driver, and HTTPie http client.
pip install apache-superset sqlalchemy-cratedb httpie
```

You need to create a `superset_config.py` file, to configure an individual `SECRET_KEY` for your application.
```shell
echo "SECRET_KEY = '$(docker run --rm alpine/openssl rand -base64 42)'" > superset_config.py
```

This sequence of commands initializes the metadata database at `~/.superset/superset.db`, and provisions a superuser account.
```shell
# Configure and initialize Apache Superset.
export FLASK_APP=superset
export SUPERSET_CONFIG_PATH=superset_config.py
superset db upgrade
superset fab create-admin --username=admin --password=admin --firstname=admin --lastname=admin --email=admin@example.org
superset init
```

## Start services

Start CrateDB using Docker.
```shell
docker run --interactive --rm --pull=always \
  --publish=4200:4200 --publish=5432:5432 \
  --name=cratedb \
  --env CRATE_HEAP_SIZE=1g \
  crate:latest
```

Run Superset server.
```shell
superset run --port=9000 --with-threads
```


## Load data
Import six million records worth of data from the venerable NYC Yellowcab taxi ride dataset. Depending on the speed of the internet connection between the location of your database instance, and AWS S3, where data is loaded from, it may take about one minute of time.

This is a one-shot command using the [crash](https://cratedb.com/docs/crate/crash/) database shell running in a Docker container, which includes a relevant SQL DDL statement to create the database table schema, and a `COPY FROM` statement to import data from a compressed JSON file located on AWS S3.
```shell
docker run --interactive --rm --network=host crate:latest crash <<EOF
DROP TABLE IF EXISTS yellowcab;
CREATE TABLE yellowcab (
  "pickup" geo_point,
  "dropoff" geo_point,
  "congestion_surcharge" REAL,
  "dolocationid" INTEGER,
  "extra" REAL,
  "fare_amount" REAL,
  "improvement_surcharge" REAL,
  "mta_tax" REAL,
  "passenger_count" INTEGER,
  "payment_type" INTEGER,
  "pickup_datetime" TIMESTAMP WITH TIME ZONE,
  "pulocationid" INTEGER,
  "ratecodeid" INTEGER,
  "store_and_fwd_flag" TEXT,
  "tip_amount" REAL,
  "tolls_amount" REAL,
  "total_amount" REAL,
  "trip_distance" REAL,
  "vendorid" INTEGER,
  "month" AS date_format('%Y-%c', pickup_datetime)
) CLUSTERED INTO 12 SHARDS PARTITIONED BY (month);

COPY yellowcab 
  FROM 'https://s3.amazonaws.com/crate.sampledata/nyc.yellowcab/yc.2019.07.gz' 
  WITH ("compression"='gzip', "format"='json')
  RETURN SUMMARY;

REFRESH TABLE yellowcab;
SELECT COUNT(*) FROM yellowcab;

EOF
```


## Usage

You can operate CrateDB and Superset interactively, using the integrated web-based user interfaces. Alternatively, you can use their HTTP APIs.

### Web user interface
You should be ready to go. Now, you can explore the loaded data through user interfaces of CrateDB and Apache Superset.

- navigate to `http://localhost:4200/#!/console` for exploring the CrateDB Admin UI.
- navigate to `http://localhost:9000/sqllab/` for exploring your data in Apache Superset, log in with admin/admin.

In order to work with data in Apache Superset, before being able to create dashboards, you will need to establish connectivity between Apache Superset and CrateDB. To do that, you will [connect a database instance](https://superset.apache.org/docs/databases/db-connection-ui/) and [register a database table](https://superset.apache.org/docs/creating-charts-dashboards/creating-your-first-dashboard/#registering-a-new-table) as a dataset.


### HTTP API
Using [Apache Superset's HTTP API](https://superset.apache.org/docs/api), you can automate the provisioning process. The commands outlined below are using [HTTPie](https://httpie.io/docs/cli) for that purpose, saving a few clicks and keystrokes.

**Connect a database instance**
```shell
# Authenticate and acquire a JWT token.
AUTH_TOKEN=$(http --session=superset http://localhost:9000/api/v1/security/login username=admin password=admin provider=db | jq -r .access_token)

# Acquire a CSRF token.
CSRF_TOKEN=$(http --session=superset http://localhost:9000/api/v1/security/csrf_token/ Authorization:"Bearer ${AUTH_TOKEN}" | jq -r .result)

# Create a data source item / database connection.
http --session=superset http://localhost:9000/api/v1/database/ \
  database_name="CrateDB Testdrive" engine=crate \
  sqlalchemy_uri=crate://crate@localhost:4200 \
  Authorization:"Bearer ${AUTH_TOKEN}" \
  X-CSRFToken:"${CSRF_TOKEN}"
```

**Register a database table**
```shell
# Register database table as dataset.
http --session=superset http://localhost:9000/api/v1/dataset/ \
  Authorization:"Bearer ${AUTH_TOKEN}" \
  X-CSRFToken:"${CSRF_TOKEN}" \
  database=1 schema=doc table_name=yellowcab
```

Now, you can navigate to the Superset Web UI for exploring your newly created dataset, in order to create a dashboard.

- `http://localhost:9000/explore/?datasource_type=table&datasource_id=1` 

:::{note}
The command assumes `database=1`, which implies this is the first database
connection created. If you have already created other databases in your
Superset instance, this ID might be incorrect.
:::

## Clean up
1. The development web server of Apache Superset can be terminated by hitting `CTRL+C`.
2. The CrateDB database instance running in a container can be terminated by either hitting `CTRL+C`, or by invoking `docker rm cratedb --force`.
3. The metadata database of Apache Superset, where user accounts and database connections are stored, can be deleted by invoking `rm ~/.superset/superset.db`.
