(locust-tutorial)=
# Load testing CrateDB using Locust

## Introduction

As with every other database, users want to run performance tests to get a feel for the performance of their workload.

CrateDB offers a couple of tools that can be used for specific use cases. For example, the [nodeIngestBench][] allows you to run high-performance ingest benchmarks against a CrateDB cluster or use the [TimeIt][] function within the cr8 toolkit to measure the runtime of a given SQL statement on a cluster.

[nodeIngestBench]: https://github.com/proddata/nodeIngestBench
[TimeIt]: https://github.com/mfussenegger/cr8#timeit

We use Locust as the framework to run load tests with a customizable set of SQL statements. [Locust][] is a great, flexible, open-source (Python) framework that can swarm the database with users and get the RPS (request per second) for different queries. This small blog shows how to use Locust to load test CrateDB in your environment.

For this blog, I’m running a 3-node cluster created in a local docker environment as described in this [tutorial][].

[tutorial]: https://cratedb.com/docs/crate/tutorials/en/latest/containers/docker.html
[Locust]: https://locust.io

First, we must set up the data model and load some data. I’m using [DBeaver][] to connect in this case, but this can be done by either the [CrateDB CLI tools][] or the Admin UI that comes with either the self- or [fully-managed][] CrateDB solution. 

[DBeaver]: https://dbeaver.io
[CrateDB CLI tools]: https://cratedb.com/docs/crate/clients-tools/en/latest/connect/cli.html#cli
[fully-managed]: https://console.cratedb.cloud/

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

Create the user used further down the line.
```sql
CREATE USER locust with (password = 'load_test');
GRANT ALL PRIVILEGES ON table weather_data to locust;
GRANT ALL PRIVILEGES ON table weekly_aggr_weather_data to locust;
```

Load some data into the `weather_data` table by using the following statement. 

```sql
COPY weather_data
FROM 'https://github.com/crate/cratedb-datasets/raw/main/cloud-tutorials/data_weather.csv.gz'
WITH (format = 'csv', compression = 'gzip', empty_string_as_null = true);
```

The `weather_data` table should now have 70k rows of data.

```text
select count(*) from weather_data;

count(*)|
--------+
   70000|
```

We leave the other table empty as that one will be populated as part of the load test. 

## Install Locust

In this case, I installed Locust on my Mac, but in an acceptance environment, you probably want to run this Locust on one or more “driver” machines. Especially when you want to push the database, you will need enough firepower on the driver side to push the database.

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

Start with a simple test to ensure the connectivity is there and you can connect to the database. Copy the code below and write to a file named `locustfile.py`.
Besides the pure Locust execution, it also contains a CrateDB-specific implementation, connecting to CrateDB using our Python driver, instead of a plain HTTP client.

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

    def send_query(self, *args, **kwargs):
        cursor = self._connection.cursor()
        start_time = time.perf_counter()

        request_meta = {
            "request_type": "CrateDB",
            "name": args[1],
            "response_length": 0,
            "response": None,
            "context": {},
            "exception": None,
        }

        response = None
        try:
            cursor.execute(args[0])
            response = cursor.fetchall()
        except Exception as e:
            request_meta["exception"] = e

        request_meta["response_time"] = (time.perf_counter() - start_time) * 1000
        request_meta["response"] = response
        # Approximate length, we don't have the original HTTP response body any more
        request_meta["response_length"] = len(str(response))

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

In the actual Locust configuration, with the `wait_time = between (1, 5)`, you can control the number of queries and the randomization of the queries by using between. This will execute the different queries with a random interval between 1 and 5 sec. Another option that will give you more control over the amount of executed queries per second is using the `wait_time = constant_throughput(1.0)`, which will execute 1 of the queries per second for every user, or if you set it to `(2.0)`, will execute two queries every second.

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

Click “Start” to start the load test.

![swarm-query0|690x133](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/5/56615b02ec7a792326acb1d5dc086f5d7636bbdb.png)

As you can see, is 1 query being executed with an RPS of 1. The number of failures should be 0. If you stop the test and start a New test with ten users, you should get an RPS of 10.

![swarm-10users-query0|690x133](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/2/2ae79d623b440d1735df0285fd0bf85996623bd2.png)

Now that we have confirmed that Locust is running correctly, we can expand the number of queries we execute. For this blog, we are adding the following queries.

```sql
-- Avg Temperature per City
SELECT location, round(AVG(temperature)) AS avg_temp
FROM weather_data
WHERE location = 'CITY'
GROUP BY location
ORDER BY 2 DESC;

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
ORDER BY 1;

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

    def send_query(self, *args, **kwargs):
        cursor = self._connection.cursor()
        start_time = time.perf_counter()

        request_meta = {
            "request_type": "CrateDB",
            "name": args[1],
            "response_length": 0,
            "response": None,
            "context": {},
            "exception": None,
        }

        response = None
        try:
            cursor.execute(args[0])
            response = cursor.fetchall()
        except Exception as e:
            request_meta["exception"] = e

        request_meta["response_time"] = (time.perf_counter() - start_time) * 1000
        request_meta["response"] = response
        # Approximate length, we don't have the original HTTP response body any more
        request_meta["response_length"] = len(str(response))

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
        self.client.send_query(
            f"""
                SELECT location, ROUND(AVG(temperature)) AS avg_temp
                FROM weather_data
                WHERE location = '{random.choice(self.cities)}'
                GROUP BY location
                ORDER BY 2 DESC
            """,
            "Avg Temperature per City",
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
        self.client.send_query(
            f"""
                WITH minmax AS (
                    SELECT location,
                           MIN(timestamp) AS mintstamp,
                           MAX(timestamp) AS maxtstamp
                    FROM weather_data
                    WHERE location = '{random.choice(self.cities)}'
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
                ORDER BY 1;
            """,
            "Bridge the Gaps per City",
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

Note that the weight (of query01 and query04) is five compared to the rest, which has a weight of 1, which means that the likelihood that two queries will execute is five times higher than the others. This shows how you can influence the weight of the different queries. 

Let’s run this load test and see what happens. 

I started the run with 100 users.

![statistics-100users|690x206](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/a/aa31288ac528c7eaf3dec7657cc73bbac0bbf7b7.png)

You can see that 100 users running those five queries result in 100 requests per second (this is because we set the `wait_time = constant_throughput(1.0)`). The two “per City” queries are executed ~5x as much as the others. 

On the second tab in Locust, you see the Charts of the same data.

![charts-100users|595x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/c/c7a2119e8870e5c4c66571193afe66a186ffc6af.jpeg){w=800px}

If you want to download the locust data, you can do that on the last tab.

![download-stats-100users|638x221](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/b/b5a9a71f9db7275cd6c3465cdc1197eb4f54e41c.png)

## Conclusion

When you want to run a load test against a CrateDB Cluster with multiple queries, Locust is a great and flexible tool that lets you quickly define a load test and see what numbers regarding users and RPS are possible for that particular setup.
