(recurrent-queries)=
# Automate recurrent CrateDB queries

Many database tasks run the same query repeatedly. Schedule them.
This article shows several scheduling options and how to integrate them with CrateDB.

As an example, we implement continuous aggregates: precompute results to speed up repeated aggregations.

## Use Case: Continuous Aggregates

Our base table contains simple periodic sensor readings:
```sql
CREATE TABLE sensor_readings_raw (
  ts TIMESTAMP NOT NULL,
  sensor_id INTEGER NOT NULL,
  "value" DOUBLE NOT NULL
);
```

Calculate an hourly average regularly with your analytics tool:
```sql
SELECT DATE_TRUNC('hour', ts),
       sensor_id,
       AVG(value)
FROM sensor_readings_raw;
```

In certain cases, it can make sense to precalculate the result, e.g. due to strict performance requirements or a high volume of identical queries.

We create a second table that stores the result set of the above query:
```sql
CREATE TABLE sensor_readings_aggregated (
  ts_hour TIMESTAMP NOT NULL,
  sensor_id INTEGER NOT NULL,
  value_avg DOUBLE PRECISION NOT NULL,
  last_updated GENERATED ALWAYS AS NOW(),
  PRIMARY KEY(ts_hour, sensor_id)
);
```

The INSERT query below will populate the target table. To update already aggregated data (e.g. for the latest hour which still changes or if data arrives late), we consider the raw readings of the last six hours and use the [ON CONFLICT DO UPDATE](https://crate.io/docs/crate/reference/en/4.6/sql/statements/insert.html#on-conflict-do-update-set) clause to override previously existing data:
```sql
INSERT INTO sensor_readings_aggregated (ts_hour, sensor_id, value_avg)
SELECT DATE_TRUNC('hour', ts),
       sensor_id,
       AVG(value)
FROM sensor_readings_raw
WHERE ts >= DATE_TRUNC('hour', ts - '6 hours'::INTERVAL)
GROUP BY 1, 2
ON CONFLICT (ts_hour, sensor_id) DO UPDATE SET value_avg = excluded.value_avg;
```

Schedule this INSERT to refresh the aggregates regularly.


## Scheduling Methods

We will now go through several scheduling methods and how to use them for the given use case.

### cron
On Unix-based systems, use cron to schedule jobs.

:::{rubric} Prerequisites
:::
The CrateDB CLI client [crash](https://crate.io/docs/crate/crash/en/latest/) is installed.

:::{rubric} Setup
:::
1. Create a script ~/update_continuous_aggregates.sh with the following content (replace `<placeholders>` for CrateDB connection information accordingly):
   ```bash
   #!/bin/bash

   UPDATE_QUERY=$(cat << QUERY
     INSERT INTO sensor_readings_aggregated (ts_hour, sensor_id, value_avg)
     SELECT DATE_TRUNC('hour', ts),
            sensor_id,
            AVG(value)
     FROM sensor_readings_raw
     WHERE ts >= DATE_TRUNC('hour', ts - '6 hours'::INTERVAL)
     GROUP BY 1, 2
     ON CONFLICT (ts_hour, sensor_id) DO UPDATE SET value_avg = excluded.value_avg;
   QUERY
   )

   CRATEPW=<CrateDB user password> crash -U <CrateDB user name> -c "${UPDATE_QUERY}" --hosts https://<CrateDB host>:4200 > /dev/null
   ```
2. Make the script executable: `chmod +x ~/update_continuous_aggregates.sh`
3. On the Unix command line, run `crontab -e` to edit the cron jobs of the current user. Add the following line to update aggregated data every five minutes:
`*/5 * * * * ~/update_continuous_aggregates.sh`

:::{rubric} Caveats
:::
Monitor your cron jobs. By default, the cron daemon delivers output (including errors) to the user’s mailbox if configured.

You can also use third‑party cron monitoring services for deeper visibility.

### Apache Airflow
[Airflow](https://airflow.apache.org/) programmatically schedules and controls complex workflows. See our [crate-airflow-tutorial](https://github.com/crate/crate-airflow-tutorial) repository for examples.

(node-red-recurrent-queries)=
### Node-RED
[Node-RED](https://nodered.org) is a low‑code tool that also offers scheduling.

:::{rubric} Prerequisites
:::
The [node-red-contrib-postgresql](https://flows.nodered.org/node/node-red-contrib-postgresql) package is installed.

:::{rubric} Setup
:::
![Node-RED flow editor](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/ea6c64ac6c2330cade043d56c53808b8c231941c.png)
1. Import the workflow definition and replace the `<placeholders>` for CrateDB connection information:
    <details>
    <summary>Workflow definition</summary>

    ```json
     [{
      "id": "97faa38a7298a42f",
      "type": "tab",
      "label": "Continuous Aggregates",
      "disabled": false,
      "info": ""
    }, {
      "id": "198292c29380b198",
      "type": "inject",
      "z": "97faa38a7298a42f",
      "d": true,
      "name": "Every 5 minutes",
      "props": [{
        "p": "payload"
      }, {
        "p": "topic",
        "vt": "str"
      }],
      "repeat": "300",
      "crontab": "",
      "once": false,
      "onceDelay": 0.1,
      "topic": "",
      "payloadType": "date",
      "x": 250,
      "y": 280,
      "wires": [["de0833a8befa9217"]]
    }, {
      "id": "de0833a8befa9217",
      "type": "postgresql",
      "z": "97faa38a7298a42f",
      "name": "Update Continuous Aggregates",
      "query": "INSERT INTO sensor_readings_aggregated (ts_hour, sensor_id, value_avg)\nSELECT DATE_TRUNC('hour', ts),\n       sensor_id,\n       AVG(value)\nFROM sensor_readings_raw\nWHERE ts >= DATE_TRUNC('hour', ts - '6 hours'::INTERVAL)\nGROUP BY 1, 2\nON CONFLICT (ts_hour, sensor_id) DO UPDATE SET value_avg = excluded.value_avg\nRETURNING _id, sensor_id, value_avg;",
      "postgreSQLConfig": "79bc378b4e65b06e",
      "split": false,
      "rowsPerMsg": 1,
      "outputs": 1,
      "x": 530,
      "y": 280,
      "wires": [[]]
    }, {
      "id": "79bc378b4e65b06e",
      "type": "postgreSQLConfig",
      "name": "CrateDB",
      "host": "<CrateDB host>",
      "hostFieldType": "str",
      "port": "5432",
      "portFieldType": "num",
      "database": "doc",
      "databaseFieldType": "str",
      "ssl": "true",
      "sslFieldType": "bool",
      "max": "10",
      "maxFieldType": "num",
      "min": "1",
      "minFieldType": "num",
      "idle": "1000",
      "idleFieldType": "num",
      "connectionTimeout": "10000",
      "connectionTimeoutFieldType": "num",
      "user": "<CrateDB user name>",
      "userFieldType": "str",
      "password": "<CrateDB user password>",
      "passwordFieldType": "str"
    }]
    ```
   </details>


### CrateDB Cloud - SQL Job Scheduler

Specifically for CrateDB Cloud deployments, there is the SQL Job Scheduler option. As the name says, it allows you to schedule jobs in the Cloud platform to run in a defined interval through a centralized user interface. Whether you're looking to move data between tables or schedule regular data exports, the SQL Job Scheduler equips you with the necessary tools.

Use the Cloud Console Automation menu to create a new job. Define the name, interval, and the exact query to run. You can activate/deactivate the job and review its execution history.

![Screenshot 2024-06-19 at 10.09.35|690x287](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/4/4b40ad5c25d287bbcad25b2d18f8000c78961f10.png)

:::{rubric} API access
:::

Besides the web interface, you can use `croud` to configure new jobs. Check the [documentation](https://cratedb.com/docs/cloud/cli/en/latest/commands/scheduled-jobs.html) for further details on how to achieve that. For instance, to have the same result as the web UI, you can use the following command, assuming you have `croud` already configured in your environment:

```bash
croud clusters scheduled-jobs create \
    --name update-continuous-aggregates \
    --cluster-id 8d6a7c3c-61d5-11e9-a639-34e12d2331a1 \
    --cron "5 * * * *" \
    --sql "INSERT INTO sensor_readings_aggregated (ts_hour, sensor_id, value_avg)
           SELECT DATE_TRUNC('hour', ts),
                  sensor_id,
                  AVG(value)
           FROM sensor_readings_raw
           WHERE ts >= DATE_TRUNC('hour', ts - '6 hours'::INTERVAL)
           GROUP BY 1, 2
           ON CONFLICT (ts_hour, sensor_id) DO UPDATE SET value_avg = excluded.value_avg;" \
    --enabled True 
```
