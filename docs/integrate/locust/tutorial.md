(locust-tutorial)=
# Load testing CrateDB using Locust

:::{article-info}
---
avatar: https://sea2.discourse-cdn.com/flex020/user_avatar/community.cratedb.com/wierd/288/1080_2.png
avatar-link: https://github.com/wierdvanderhaar
avatar-outline: muted
author: Wierd van der Haar
date: August 14, 2024
read-time: 12 min read
class-container: sd-p-2 sd-outline-muted sd-rounded-1
---
:::

## Introduction

Like with any database, you’ll want to run performance tests to understand
your workload’s behavior.

CrateDB offers a couple of tools that can be used for specific use cases. For example, the [nodeIngestBench][] allows you to run high-performance ingest benchmarks against a CrateDB cluster or use the [TimeIt][] function within the cr8 toolkit to measure the runtime of a given SQL statement on a cluster.

Use Locust to run load tests with a customizable set of SQL statements. [Locust][] is a flexible, open‑source Python framework that can swarm the database with users and report RPS (requests per second) per query. This tutorial shows how to use Locust to load test CrateDB in your environment.

For this tutorial, we use a 3‑node local Docker cluster (see this [tutorial][]).

First, set up the data model and load data. This example uses [DBeaver][], but you can also use the [CrateDB CLI tools][] or the Admin UI in self‑managed or [fully-managed][] CrateDB. 

Create the following tables:

```sql
CREATE TABLE "weather_data" (
       "timestamp" TIMESTAMP,
       "location" VARCHAR,
       "temperature" DOUBLE,
       "humidity" DOUBLE,
       "wind_speed" DOUBLE
);

CREATE TABLE IF NOT EXISTS "weekly_aggr_weather_data"(
       "week" TIMESTAMP,
       "location" VARCHAR,     
       "avgtemp" DOUBLE,
       "maxhumid" DOUBLE,
       "minwind" DOUBLE,
       "lastupdated" TIMESTAMP,
       PRIMARY KEY (week, location)
);
```

Create the user for the load test.
```sql
CREATE USER locust WITH (password = 'load_test');
GRANT ALL PRIVILEGES ON table weather_data TO locust;
GRANT ALL PRIVILEGES ON table weekly_aggr_weather_data TO locust;
```

Load some data into the `weather_data` table by using the following statement. 

```sql
COPY weather_data
FROM 'https://github.com/crate/cratedb-datasets/raw/main/cloud-tutorials/data_weather.csv.gz'
WITH (format = 'csv', compression = 'gzip', empty_string_as_null = true);
```

The `weather_data` table now contains roughly 70k rows.

```text
select count(*) from weather_data;

count(*)|
--------+
   70000|
```

Leave `weekly_aggr_weather_data` empty; the load test populates it.

## Install Locust

Install Locust locally for a quick start. In staging or production‑like testing, run Locust on one or more driver machines to generate sufficient load.

On Python (3.9 or later), install Locust as well as the CrateDB driver:
```bash
pip3 install -U locust crate
```

Validate your installation:
```bash
locust -V
# locust 2.29.1 from [...]
```

## Run Locust

Start with a simple connectivity check.
Copy the code below into a file named `locustfile.py`.
It uses a CrateDB-specific client built on the Python driver rather than
a generic HTTP client.

```python
import time
import random
from locust import task, User, between, constant_throughput
from crate import client

# If a host is provided through the Locust UI, that host will be used.
# Otherwise, there is a fallback to the host provided here.
CRATEDB_HOST = "http://localhost:4200"

# Credentials are always used from here to not have them leak into the UI as
# part of the connection URL.
CRATEDB_USERNAME = "crate"
CRATEDB_PASSWORD = ""


# CrateDBClient wraps the CrateDB client and returns results in a
# Locust-compatible data structure with additional metadata
class CrateDBClient:
    def __init__(self, host, request_event):
        self._connection = client.connect(
            servers=host or CRATEDB_HOST,
            username=CRATEDB_USERNAME,
            password=CRATEDB_PASSWORD,
        )
        self._request_event = request_event

    def send_query(self, sql, name, params=None):
        cursor = self._connection.cursor()
        start_time = time.perf_counter()

        request_meta = {
            "request_type": "CrateDB",
            "name": name,
            "response_length": 0,
            "response": None,
            "context": {},
            "exception": None,
        }

        response = None
        try:
            cursor.execute(sql, params or ())
            response = cursor.fetchall()
        except Exception as e:
            request_meta["exception"] = e

        request_meta["response_time"] = (time.perf_counter() - start_time) * 1000
        request_meta["response"] = response
        # Approximate length, we don't have the original HTTP response body any more
        request_meta["response_length"] = len(response) if response is not None else 0

        # This is what makes the request actually get logged in Locust
        self._request_event.fire(**request_meta)

        return response


class CrateDBUser(User):
    abstract = True

    def __init__(self, environment):
        super().__init__(environment)
        self.client = CrateDBClient(self.host, request_event=environment.events.request)


class QuickstartUser(CrateDBUser):
    # wait_time = between(1, 50)
    # Using constant_throughput in combination with the number of users to start with gives the option to control the pace.
    # Using a constant_throughput of 1 will ensure that a task runs at least 1x per sec.
    # https://docs.locust.io/en/stable/writing-a-locustfile.html#wait-time-attribute
    # Starting with 200 users will end up in 200 queries/sec.
    wait_time = constant_throughput(1.0)

    # Start with the queries you want to execute
    @task(1)
    def query0(self):
        self.client.send_query(
            "SELECT * FROM weather_data LIMIT 100",
            "query0",
        )
```
Some explanation on some of the code above ☝️

The class `CrateDBClient` implements how to connect to CrateDB and details on how to measure requests. `CrateDBUser` represents a Locust-generated user based on the `CrateDBClient`.

In Locust, `wait_time = between(1, 5)` randomizes task execution between 1 and 5 seconds. To control throughput more precisely, use `wait_time = constant_throughput(1.0)`, which runs one task per second per user (set to `2.0` for two tasks per second).

For every query you want to include in your test, you will need to create a block like this:

```python
    # Start with the queries you want to execute
    @task(1)
    def query0(self):
        self.client.send_query(
            "SELECT * FROM weather_data LIMIT 100",
            "query0",
        )
```
With `@task`, you give weight to the queries. If you have two questions and want to execute one of the statements twice as often, you can control this by changing `@task(2)`. The last parameter in the `send_query` call is what will be visible on the Locust report.

Let's see how to run Locust. Run the following command to start the Locust application. 

```bash
locust
```

Open a browser and navigate to the web interface (at `http://localhost:8089`). This will take you to the “Start new load test” page.

Define the number of users and the spawn rate. As this is an initial test, we leave the numbers as they are. The CrateDB connection will default to localhost.

![Start new load test|272x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/d/d61218208d3f11d27d398e87c3954cb4327c9910.png){h=320px}

Click "Start" to launch the load test.

![swarm-query0|690x133](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/5/56615b02ec7a792326acb1d5dc086f5d7636bbdb.png)

Locust executes one query at ~1 RPS (requests per second) with zero failures. If you stop and start a new test with 10 users, you’ll see ~10 RPS.

![swarm-10users-query0|690x133](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/2/2ae79d623b440d1735df0285fd0bf85996623bd2.png)

Now that we have confirmed that Locust is running correctly, we can expand the number of queries we execute. For this blog, we are adding the following queries.

```sql
-- Avg Temperature per City
SELECT location, round(AVG(temperature)) AS avg_temp
FROM weather_data
WHERE location = 'CITY'
GROUP BY location
ORDER BY avg_temp DESC;

-- When was Max Temp 
SELECT location,
       MAX(temperature) AS highest_temp,
       MAX_BY(timestamp, temperature) AS time_of_highest_temp
FROM weather_data
GROUP BY location;

-- Bridge the gaps (not all readings have values and with LAG and LEAD we can calculate the missing values). 
WITH OrderedData AS (
    SELECT timestamp,
           location,
           temperature,
           LAG(temperature, 1) IGNORE NULLS OVER (ORDER BY timestamp) AS prev_temp,
           LEAD(temperature, 1) IGNORE NULLS OVER (ORDER BY timestamp) AS next_temp
    FROM weather_data
)
SELECT timestamp,
       location,
       temperature,
       (prev_temp + next_temp) / 2 AS interpolated_temperature
FROM OrderedData
ORDER BY location, timestamp
LIMIT 1000;

-- Bridge the Gaps per City 
WITH minmax AS (
    SELECT location,
           MIN(timestamp) AS mintstamp,
           MAX(timestamp) AS maxtstamp
    FROM weather_data
    WHERE location = 'CITY'
    GROUP BY location
)
SELECT a.timestamp,
       a.location,
       a.temperature,
       LAG(a.temperature, 1) IGNORE NULLS OVER (ORDER BY timestamp) AS prev_temp,
       LEAD(a.temperature, 1) IGNORE NULLS OVER (ORDER BY timestamp) AS next_temp
FROM weather_data a, minmax b
WHERE a.location = b.location
  AND a.timestamp BETWEEN b.mintstamp AND b.maxtstamp
ORDER BY a.timestamp;

-- Upsert the Aggr per week
INSERT INTO weekly_aggr_weather_data (week, location, avgtemp, maxhumid, minwind, lastupdated)
(
    SELECT DISTINCT(DATE_TRUNC('week', timestamp)) AS week,
           location,
           AVG(temperature),
           MAX(humidity),
           MIN(wind_speed),
           NOW()
    FROM weather_data
    GROUP BY 1, 2
) ON CONFLICT (week, location) DO UPDATE SET avgtemp = excluded.avgtemp, maxhumid = excluded.maxhumid, minwind = excluded.minwind, lastupdated = excluded.lastupdated;
```

We create an array of different cities to randomize the city used. In the execution of the queries, we randomly choose one of those to execute.

```python
cities = ["Berlin", "Dornbirn", "Redwood City", "Vienna", "Zurich"]
```

This will be used in queries 01 and 04. 

These queries in a `locustfile.py` will look like this:

```python
import time
import random
from locust import task, User, between, constant_throughput
from crate import client

# If a host is provided through the Locust UI, that host will be used.
# Otherwise, there is a fallback to the host provided here.
CRATEDB_HOST = "http://localhost:4200"

# Credentials are always used from here to not have them leak into the UI as
# part of the connection URL.
CRATEDB_USERNAME = "crate"
CRATEDB_PASSWORD = ""


# CrateDBClient wraps the CrateDB client and returns results in a
# Locust-compatible data structure with additional metadata
class CrateDBClient:
    def __init__(self, host, request_event):
        self._connection = client.connect(
            servers=host or CRATEDB_HOST,
            username=CRATEDB_USERNAME,
            password=CRATEDB_PASSWORD,
        )
        self._request_event = request_event

    def send_query(self, sql, name, params=None):
        cursor = self._connection.cursor()
        start_time = time.perf_counter()

        request_meta = {
            "request_type": "CrateDB",
            "name": name,
            "response_length": 0,
            "response": None,
            "context": {},
            "exception": None,
        }

        response = None
        try:
            cursor.execute(sql, params or ())
            response = cursor.fetchall()
        except Exception as e:
            request_meta["exception"] = e

        request_meta["response_time"] = (time.perf_counter() - start_time) * 1000
        request_meta["response"] = response
        # Approximate length, we don't have the original HTTP response body any more
        request_meta["response_length"] = len(response) if response is not None else 0

        # This is what makes the request actually get logged in Locust
        self._request_event.fire(**request_meta)

        return response


class CrateDBUser(User):
    abstract = True

    def __init__(self, environment):
        super().__init__(environment)
        self.client = CrateDBClient(self.host, request_event=environment.events.request)


class QuickstartUser(CrateDBUser):
    # wait_time = between(1, 50)
    # Using constant_throughput in combination with the number of users to start with gives the option to control the pace.
    # Using a constant_throughput of 1 will ensure that a task runs at least 1x per sec.
    # https://docs.locust.io/en/stable/writing-a-locustfile.html#wait-time-attribute
    # Starting with 200 users will end up in 200 queries/sec.
    wait_time = constant_throughput(1.0)

    cities = ["Berlin", "Dornbirn", "Redwood City", "Vienna", "Zurich"]

    @task(5)
    def query01(self):
        city = random.choice(self.cities)
        self.client.send_query(
            """
                SELECT location, ROUND(AVG(temperature)) AS avg_temp
                FROM weather_data
                WHERE location = ?
                GROUP BY location
                ORDER BY avg_temp DESC
            """,
            "Avg Temperature per City",
            params=(city,),
        )

    @task(1)
    def query02(self):
        self.client.send_query(
            """
                SELECT location,
                       MAX(temperature) AS highest_temp,
                       MAX_BY(timestamp, temperature) AS time_of_highest_temp
                FROM weather_data
                GROUP BY location
            """,
            "Max Temperature date",
        )

    @task(1)
    def query03(self):
        self.client.send_query(
            """
                WITH OrderedData AS (
                    SELECT timestamp,
                           location,
                           temperature,
                           LAG(temperature, 1) IGNORE NULLS OVER (ORDER BY timestamp) AS prev_temp,
                           LEAD(temperature, 1) IGNORE NULLS OVER (ORDER BY timestamp) AS next_temp
                    FROM weather_data
                )
                SELECT timestamp,
                       location,
                       temperature,
                       (prev_temp + next_temp) / 2 AS interpolated_temperature
                FROM OrderedData
                ORDER BY location, timestamp
                LIMIT 1000;
            """,
            "Bridge the gaps",
        )

    @task(5)
    def query04(self):
        city = random.choice(self.cities)
        self.client.send_query(
            """
                WITH minmax AS (
                    SELECT location,
                           MIN(timestamp) AS mintstamp,
                           MAX(timestamp) AS maxtstamp
                    FROM weather_data
                    WHERE location = ?
                    GROUP BY location
                )
                SELECT a.timestamp,
                       a.location,
                       a.temperature,
                       LAG(a.temperature, 1) IGNORE NULLS OVER (ORDER BY timestamp) AS prev_temp,
                       LEAD(a.temperature, 1) IGNORE NULLS OVER (ORDER BY timestamp) AS next_temp
                FROM weather_data a, minmax b
                WHERE a.location = b.location
                AND a.timestamp BETWEEN b.mintstamp AND b.maxtstamp
                ORDER BY a.timestamp;
            """,
            "Bridge the Gaps per City",
            params=(city,),
        )

    @task(1)
    def query05(self):
        self.client.send_query(
            """
                INSERT INTO weekly_aggr_weather_data (week, location, avgtemp, maxhumid, minwind, lastupdated)
                (
                    SELECT DISTINCT(DATE_TRUNC('week', timestamp)) AS week,
                           location,
                           AVG(temperature),
                           MAX(humidity),
                           MIN(wind_speed),
                           NOW()
                    FROM weather_data
                    GROUP BY 1, 2
                ) ON CONFLICT (week, location) DO UPDATE SET avgtemp = excluded.avgtemp, maxhumid = excluded.maxhumid, minwind = excluded.minwind, lastupdated = excluded.lastupdated;
            """,
            "Upsert aggregation",
        )

```

Queries 01 and 04 have weight 5; Locust schedules them ~5× as often as the others (weight 1). Use weights to shape your query mix.

Let’s run this load test and see what happens. The following run was started with 100 users.

![statistics-100users|690x206](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/a/aa31288ac528c7eaf3dec7657cc73bbac0bbf7b7.png)

You can see that 100 users running those five queries result in 100 requests per second (this is because we set the `wait_time = constant_throughput(1.0)`). The two “per City” queries are executed ~5x as much as the others. 

On the second tab in Locust, you see the Charts of the same data.

![charts-100users|595x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/c/c7a2119e8870e5c4c66571193afe66a186ffc6af.jpeg){w=800px}

If you want to download the locust data, you can do that on the last tab.

![download-stats-100users|638x221](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/b/b5a9a71f9db7275cd6c3465cdc1197eb4f54e41c.png)

## Conclusion

When you want to run a load test against a CrateDB Cluster with multiple queries, Locust is a great and flexible tool that lets you quickly define a load test and see what numbers regarding users and RPS are possible for that particular setup.


[CrateDB CLI tools]: project:#cli
[DBeaver]: https://dbeaver.io
[fully-managed]: https://console.cratedb.cloud/
[Locust]: https://locust.io
[nodeIngestBench]: https://github.com/proddata/nodeIngestBench
[TimeIt]: https://github.com/mfussenegger/cr8#timeit
[tutorial]: https://cratedb.com/docs/crate/tutorials/en/latest/containers/docker.html
