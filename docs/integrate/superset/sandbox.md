(superset-sandbox)=
# Set up an Apache Superset development sandbox with CrateDB

## Introduction
This is a little walkthrough about how to quickly spawn a development sandbox with Apache Superset, in order to work on the CrateDB SQLAlchemy dialect with live code reloading.

## Prerequisites
You will need Bash, Docker, Git, and Python to be installed on your workstation. All other prerequisites will be installed into your working tree.

## Setup

::::::{stepper}
:::::{step} Start CrateDB
Start CrateDB using Docker.
```shell
docker run --rm --publish=4200:4200 --publish=5432:5432 --name=cratedb --env CRATE_HEAP_SIZE=1g crate:latest '-Cdiscovery.type=single-node'
```

Create an example table and insert a single record.
```shell
docker run --interactive --rm --network=host crate:latest crash <<EOF
CREATE TABLE IF NOT EXISTS testdrive (
    ts TIMESTAMP,
    tstz TIMESTAMPTZ,
    val INTEGER CHECK (val >= 0),
    str TEXT NOT NULL,
    str2 TEXT,
    PRIMARY KEY(val, str, str2)
);
INSERT INTO testdrive (ts, tstz, val, str, str2) VALUES (now(), now(), 42, 'foobar', 'bazqux');
EOF
```

If you need more data to explore, follow [how to load 2.6M records from the NYC Yellowcab dataset into CrateDB](https://community.cratedb.com/t/quickly-starting-cratedb-with-2-5m-records-of-the-nyc-yellowcab-dataset/1162) instead.
:::::

:::::{step} Install Apache Superset from source
You can copy this whole section verbatim into your terminal.
```shell
# Acquire sources.
git clone https://github.com/apache/superset --depth=1
cd superset

# Create Python virtualenv.
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/local.txt

# Setup Node.js 16 with NPM 7.
export NODEJS_VERSION=20.19.5
export NPM_VERSION=10
source /dev/stdin <<<"$(curl -s https://raw.githubusercontent.com/cicerops/supernode/main/supernode)"

# Run provisioning steps for Apache Superset.
superset db upgrade
superset fab create-admin --username=admin --password=admin --firstname=admin --lastname=admin --email=admin@example.org
superset init
```
:::::

:::::{step} Link the SQLAlchemy dialect for CrateDB
In order to link the filesystem location of the Python driver into the sandbox environment, install the package in ["editable" mode](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs).
```shell
pip install --editable=/path/to/sqlalchemy-cratedb
```
If you don't have the sources yet, you can obtain them from the Git repository using `git clone https://github.com/crate/sqlalchemy-cratedb`.
:::::

:::::{step} Start backend
By using the `--reload` option, changes on the Python code will be automatically picked up.
```shell
# Invoke development web server with code reload machinery.
FLASK_ENV=development superset run -p 8088 --with-threads --reload --debugger
```
:::::

:::::{step} Build and start frontend
In another console, but also within the same virtualenv, you will need to build the frontend and run its development web server.
```shell
source .venv/bin/activate
cd superset-frontend
npm install
npm run dev-server
```
:::::

:::::{step} Usage
You should be ready to go. Now,

- navigate to `http://localhost:4200/#!/console` for exploring the CrateDB Admin UI.
- navigate to `http://localhost:8088/superset/sqllab/` for exploring your data in Apache Superset, log in with admin/admin.

**Create a database connection**

For creating a database connection to CrateDB in Apache Superset, you can either use the user interface, or the HTTP API. Those steps will create the connection using the HTTP API, saving a few clicks and keystrokes.
```shell
# Authenticate and acquire a JWT token.
AUTH_TOKEN=$(http --session=superset http://localhost:8088/api/v1/security/login username=admin password=admin provider=db | jq -r .access_token)

# Acquire a CSRF token.
CSRF_TOKEN=$(http --session=superset http://localhost:8088/api/v1/security/csrf_token/ Authorization:"Bearer ${AUTH_TOKEN}" | jq -r .result)

# Create a data source item / database connection.
http --session=superset http://localhost:8088/api/v1/database/ database_name="CrateDB Testdrive" engine=crate sqlalchemy_uri=crate://crate@localhost:4200 Authorization:"Bearer ${AUTH_TOKEN}" X-CSRFToken:"${CSRF_TOKEN}"
```

**Hacking**

Now, you can just go ahead and edit code on the CrateDB Python driver located on your workstation. The application will notice your changes and pick them up by reloading the daemon environment. Please make sure to watch the output on the first console, where `superset run` has been invoked, for any anomalies or stacktraces.
:::::

:::::{step} Clean up
1. Both development web servers of Apache Superset (backend and frontend) can be terminated by hitting `CTRL+C`.
2. The CrateDB database instance running in a container can be terminated by invoking `docker rm cratedb --force`.
3. The metadata database of Apache Superset, where user accounts and database connections are stored, can be deleted by invoking `rm ~/.superset/superset.db`.
:::::
::::::
