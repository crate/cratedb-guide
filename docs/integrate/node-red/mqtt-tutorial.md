(node-red-tutorial)=
# Ingesting MQTT messages into CrateDB using Node-RED

[Node-RED](https://nodered.org/) is a workflow automation tool allowing to orchestrate message flows and transformations via a comfortable web interface.
In this article, we will demonstrate the usage of Node-RED with CrateDB at the example of reading messages from an MQTT broker and inserting them into CrateDB.

## Prerequisites
To follow this article, you will need:
1. A running [Node-RED installation](https://nodered.org/#get-started)
2. An installed [node-red-contrib-postgresql](https://github.com/alexandrainst/node-red-contrib-postgresql) module
3. A running MQTT broker. We are using [HiveMQ Cloud](https://www.hivemq.com/) for this test setup.

## Producing data

First, we will generate data that populates the MQTT topic using Node-RED. If you already have an MQTT topic with regular messages, you can skip this part.
![Screenshot 2021-09-13 at 14.58.42|690x134, 50%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/5722946039148ca6ce69702d963f9f842c4f972c.png){h=134px}

The inject node is creating a JSON payload with three different attributes:
![Screenshot 2021-09-13 at 14.56.42|690x293, 50%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/8084a53e544d681e79f85d780c621a340a7d0d30.png){h=293px}

For the sake of this example, two of them are static and only the timestamp will change.
Here is the full workflow definition: [flows-producer.json](https://community.cratedb.com/uploads/short-url/eOvAk3XzDkRbNZjcZV0pZ0SnGu4.json) (1.3 KB)


## Consuming and ingesting data
First of all, we create the target table in CrateDB:
```sql
CREATE TABLE nodered_target (
   ts TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
   payload OBJECT(DYNAMIC)
);
```

The payload makes use of CrateDB’s [OBJECT data type](https://crate.io/docs/crate/reference/en/4.6/general/ddl/data-types.html#object) that is a perfect fit for payloads with a schema that will likely evolve over time. For productive usage, [partitioning and sharding](https://community.cratedb.com/t/sharding-and-partitioning-guide-for-time-series-data/737) should be considered as well.

To deal with high amounts of data in an efficient manner, messages retrieved from the MQTT topic are grouped into batches before ingestion. Batching messages into [multi-value INSERT statements](https://crate.io/docs/crate/howtos/en/latest/performance/inserts/methods.html#inserts-multiple-values) will reduce the overhead of generating single INSERT statements for each MQTT message and is set up as follows:
![Screenshot 2021-09-13 at 11.57.32|690x80](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/020164a15268330789c6f316e2092245014d3362.png)

1. HiveMQ Cloud: Consumes messages from the configured MQTT topic
2. join: Merges a given number of messages into one array. The length of the array equals the number of rows that will later be inserted into CrateDB in one multi-value statement.

   The join node is configured to send a message to the subsequent function node if a) the array has reached a specific size or b) no new messages have been received for a given period.

   The optimal values for those two parameters depend on your individual setup, e.g. the frequency of messages or the acceptable delay until messages reach the database.
3. function: This node receives a message with an array of payloads from the join node and performs a `reduce` operation. That operation transforms the array into a list of values represented as a string (`(p1), (p2), ...`). The aim is to produce a string that is already in a proper SQL-compatible syntax for usage as part of an INSERT query.
4. postgresql: As a final step, the postgresql node contains the connection information to the CrateDB cluster and the INSERT SQL query. The values are interpolated from the payload provided by the function node.

Here is the full workflow definition: [flows-consumer.json](https://community.cratedb.com/uploads/short-url/vWxIENgDPhYnoTZuQC7DKJoNdyY.json) (2.6 KB)

## Testing
To test the workflow, you can click on the rectangle left to the timestamp node (![Screenshot 2021-09-13 at 14.24.50|70x68, 40%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/d3e06521d875fe2daa959b3adc9f5bf6a22453e7.png){w=30px}) to inject a message. In the provided configuration, an INSERT statement will be triggered after two messages have been injected or ten seconds after the first message, if no second message follows.

Run a SELECT statement on your CrateDB cluster to see the inserted rows:
```sql
SELECT *
FROM nodered_target;
```
![Screenshot 2021-09-13 at 16.05.33|690x419, 75%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/37e20012ca132be3b1c810cc73340724640fb658.png){w=640px}
