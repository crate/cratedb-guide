(node-red-tutorial)=
# Ingesting MQTT messages into CrateDB using Node-RED

[Node-RED](https://nodered.org/) is a workflow automation tool that lets you orchestrate message flows and transformations through a web interface.
This tutorial shows how to read messages from an MQTT broker with Node-RED and insert them into CrateDB.

## Prerequisites

You need:
1. A running [Node-RED installation](https://nodered.org/#get-started).
2. The [node-red-contrib-postgresql](https://github.com/alexandrainst/node-red-contrib-postgresql) module installed.
3. A running MQTT broker. This tutorial uses [HiveMQ Cloud](https://www.hivemq.com/).

## Producing data

First, generate data to populate the MQTT topic with Node-RED. If you already have an MQTT topic with regular messages, you can skip this part.
![Screenshot 2021-09-13 at 14.58.42|690x134, 50%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/5722946039148ca6ce69702d963f9f842c4f972c.png){h=134px}

The `inject` node creates a JSON payload with three attributes:
![Screenshot 2021-09-13 at 14.56.42|690x293, 50%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/8084a53e544d681e79f85d780c621a340a7d0d30.png){h=293px}

In this example, two fields are static; only the timestamp changes.
Download the full workflow definition: [flows-producer.json](https://community.cratedb.com/uploads/short-url/eOvAk3XzDkRbNZjcZV0pZ0SnGu4.json) (1.3 KB)

## Consuming and ingesting data

First of all, we create the target table in CrateDB:
```sql
CREATE TABLE nodered_target (
   ts TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
   payload OBJECT(DYNAMIC)
);
```

Store the payload as CrateDB’s {ref}`OBJECT data type
<crate-reference:type-object>` to accommodate an evolving schema.
For production, also consider the {ref}`partitioning and sharding guide <sharding-partitioning>`.

To ingest efficiently, group messages into batches and use
{ref}`multi-value INSERT statements <inserts_multiple_values>`
to avoid generating one INSERT per message:
![Screenshot 2021-09-13 at 11.57.32|690x80](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/020164a15268330789c6f316e2092245014d3362.png)

1. HiveMQ Cloud: Consume messages from the configured MQTT topic.
2. `join`: Merge a given number of messages into one array. The array length determines the number of rows inserted into CrateDB in one multi-value statement.

   Configure the `join` node to forward a message to the subsequent `function` node when either a) the array reaches a target size, or b) a timeout elapses.
   Tune these values based on your message rate and acceptable end‑to‑end latency.
3. `function`: Reduce the array to a SQL VALUES string (`(p1), (p2), ...`) for the INSERT query.
4. `postgresql`: Execute the INSERT using the CrateDB connection, interpolating values from the payload.

+```{note}
Security: Prefer parameterized queries to avoid SQL injection. If you must
build a VALUES string, ensure proper escaping/encoding of all user-provided
content.
+```

Download the full workflow definition: [flows-consumer.json](https://community.cratedb.com/uploads/short-url/vWxIENgDPhYnoTZuQC7DKJoNdyY.json) (2.6 KB)

## Testing

To test the workflow, click the square to the left of the timestamp node
(![Screenshot 2021-09-13 at 14.24.50|70x68, 40%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/d3e06521d875fe2daa959b3adc9f5bf6a22453e7.png){w=30px})
to inject a message. In this configuration, an INSERT triggers after two
messages or after ten seconds if a second message does not arrive.

Then run a SELECT statement on your CrateDB cluster to see the inserted rows:
```sql
SELECT *
FROM nodered_target;
```
![Screenshot 2021-09-13 at 16.05.33|690x419, 75%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/37e20012ca132be3b1c810cc73340724640fb658.png){w=640px}
