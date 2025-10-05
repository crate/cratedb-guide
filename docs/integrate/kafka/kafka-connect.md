(kafka-connect)=
# Using Confluent Kafka Connect

This guide describes a dockerized procedure for integrating CrateDB with Kafka
Connect. By following these steps, you will set up a pipeline to ingest data 
from Kafka topics into CrateDB seamlessly.

## Abstract

Kafka is a popular stream processing software used for building scalable data
processing pipelines and applications. Many use cases might involve ingesting 
data from a Kafka topic (or several topics) into CrateDB for further 
enrichment, analysis, or visualization. This can be done using the 
supplementary component [Kafka Connect], which provides a set of connectors
that can stream data to and from Kafka.

Thanks to their compatibility [Kafka Connect JDBC connector] with the [
PostgreSQL driver] allow to designate CrateDB as a sink target, with the 
following example connector definition:

```json
{
  "name": "crate-jdbc-sink",
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
    "tasks.max": "1",
    "topics": "sensor-data-topic",
    "connection.url": "jdbc:postgresql://cratedb:5432/crate?user=crate&sslmode=disable",
    "dialect.name": "PostgreSqlDatabaseDialect",
    "auto.create": "true",
    "auto.evolve": "true",
    "insert.mode": "insert",
    "pk.mode": "none",
    "value.converter": "io.confluent.connect.avro.AvroConverter",
    "value.converter.schemas.enable": "true",
    "value.converter.schema.registry.url": "http://schema-registry:8081",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "key.converter.schemas.enable": "false",
    "table.name.format": "sensortable",
    "schema.pattern": "doc"
  }
}
```

This results in the following architecture:


![image](/_assets/img/integrations/kafka-connect.png){width=650px}

## Setup
To illustrate how this architecture can be used, let's create a scenario 
where machine sensor data from a series of weather stations is 
ingested into a Kafka topic. This data could be used in a reactive sense: for 
example, a micro-controller could consume from this topic to turn on air 
conditioning if the temperature were to rise above a certain threshold. Aside
this use of the data, it should be stored into CrateDB. This allows 
to do long term data analytics, like predicting the weather trends for 
example. Payload from each sensor may look like this:

```json
{
   "sensor_id":101,
   "timestamp":"2022-06-12T19:00:00Z",
   "temperature":22.5,
   "humidity":60,
}
```

The fields in the payload are:

* `sensor_id` - The unique identifier for the individual sensor.
* `timestamp` - The timestamp of when this payload was recorded.
* `temperature` - The ambient temperature measured by the sensor.
* `humidity` - The relative humidity level measured by the sensor.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Docker]
- [Docker Compose]
- CrateDB version of at least 4.7

## Set Up the Project Directory

Create a dedicated directory for the Kafka-CrateDB integration and navigate
into it:

```bash
mkdir kafka-cratedb-integration
cd kafka-cratedb-integration
```

Within this directory, create subdirectories for Kafka Connect plugins and 
JDBC drivers:

```bash
mkdir kafka-connect-plugins
mkdir jdbc-drivers
```

## Pull Kafka Connect Components

Use Docker to pull the necessary Kafka Connect components. These are connector 
plugins that provide predefined functionality for integrating Kafka with 
various systems. This command downloads the plugin into a local directory.

```bash
docker run --rm \
  -v "$(pwd)/kafka-connect-plugins:/usr/share/confluent-hub-components" \
  confluentinc/cp-kafka-connect:7.4.0 \
  bash -c "confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:latest"
```

## Obtain the PostgreSQL JDBC Driver

Download the PostgreSQL JDBC `.jar` file from the [PostgreSQL website]. Once 
downloaded, move the `.jar` file to the `jdbc-drivers` directory:

```bash
mv path/to/downloaded/postgresql-*.jar jdbc-drivers/
```

## Configure Docker Compose

Create a `docker-compose.yml` file with the following content to define the 
services required for the integration:

```yaml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.4.0
    hostname: zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

  kafka:
    image: confluentinc/cp-kafka:7.4.0
    hostname: kafka
    container_name: kafka
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: 'zookeeper:2181'
      KAFKA_ADVERTISED_LISTENERS: 'PLAINTEXT://kafka:9092'
      KAFKA_LISTENERS: 'PLAINTEXT://0.0.0.0:9092'
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

  schema-registry:
    image: confluentinc/cp-schema-registry:7.4.0
    hostname: schema-registry
    container_name: schema-registry
    depends_on:
      - kafka
    ports:
      - "8081:8081"
    environment:
      SCHEMA_REGISTRY_KAFKASTORE_BOOTSTRAP_SERVERS: 'kafka:9092'
      SCHEMA_REGISTRY_HOST_NAME: 'schema-registry'
      SCHEMA_REGISTRY_LISTENERS: 'http://0.0.0.0:8081'

  kafka-connect:
    image: confluentinc/cp-kafka-connect:7.4.0
    hostname: connect
    container_name: kafka-connect
    depends_on:
      - kafka
      - schema-registry
    ports:
      - "8083:8083"
    environment:
      CONNECT_BOOTSTRAP_SERVERS: 'kafka:9092'
      CONNECT_REST_ADVERTISED_HOST_NAME: 'connect'
      CONNECT_REST_PORT: 8083
      CONNECT_GROUP_ID: 'compose-connect-group'
      CONNECT_CONFIG_STORAGE_TOPIC: 'docker-connect-configs'
      CONNECT_CONFIG_STORAGE_REPLICATION_FACTOR: 1
      CONNECT_OFFSET_STORAGE_TOPIC: 'docker-connect-offsets'
      CONNECT_OFFSET_STORAGE_REPLICATION_FACTOR: 1
      CONNECT_STATUS_STORAGE_TOPIC: 'docker-connect-status'
      CONNECT_STATUS_STORAGE_REPLICATION_FACTOR: 1
      CONNECT_KEY_CONVERTER: 'org.apache.kafka.connect.storage.StringConverter'
      CONNECT_KEY_CONVERTER_SCHEMAS_ENABLE: 'false'
      CONNECT_VALUE_CONVERTER: 'io.confluent.connect.avro.AvroConverter'
      CONNECT_VALUE_CONVERTER_SCHEMAS_ENABLE: 'true'
      CONNECT_VALUE_CONVERTER_SCHEMA_REGISTRY_URL: 'http://schema-registry:8081'
      CONNECT_PLUGIN_PATH: '/usr/share/java,/usr/share/confluent-hub-components,/etc/kafka-connect/jars'
    volumes:
      - ./kafka-connect-plugins:/usr/share/confluent-hub-components
      - ./jdbc-drivers:/etc/kafka-connect/jars

  cratedb:
    image: crate:latest
    hostname: cratedb
    container_name: cratedb
    ports:
      - "4200:4200"
      - "5432:5432"
    environment:
      CRATE_HEAP_SIZE: 1g
```

Each tool in this stack plays an integral role for proper functioning of the 
data transfer:

* `CrateDB` Is the destination database that stores the sensor data 
  from Kafka and allows further enrichment or manipulation of the data.

* `Zookeeper` Zookeeper acts as a centralized service to manage Kafka brokers
  and their metadata.

* `Kafka`: Is a distributed message broker that handles the production and 
  consumption of messages.

* `Schema Registry`: Manages Avro schemas for Kafka messages. It ensures that 
  all messages conform to predefined schemas, enabling compatibility and 
  proper deserialization.

* `Kafka Connect` Is responsible for integrating Kafka with 
  external systems. It provides a reliable mechanism to stream data 
  between Kafka and various databases, like CrateDB.

## Start Up the Containers

Launch all the services defined in the `docker-compose.yml` file:

```bash
docker compose up -d
```

## Verify the Running Containers

Ensure that all services are up and running by listing the active containers:

```bash
docker compose ps
```

You should see the following containers:

- cratedb
- zookeeper
- kafka
- schema-registry
- kafka-connect

## Configure the Sink Connector

Create a `sink-connector.json` file with the following configuration to define 
the JDBC sink connector for CrateDB:

```json
{
  "name": "crate-jdbc-sink",
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
    "tasks.max": "1",
    "topics": "sensor-data-topic",
    "connection.url": "jdbc:postgresql://cratedb:5432/crate?user=crate&sslmode=disable",
    "dialect.name": "PostgreSqlDatabaseDialect",
    "auto.create": "true",
    "auto.evolve": "true",
    "insert.mode": "insert",
    "pk.mode": "none",
    "value.converter": "io.confluent.connect.avro.AvroConverter",
    "value.converter.schemas.enable": "true",
    "value.converter.schema.registry.url": "http://schema-registry:8081",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "key.converter.schemas.enable": "false",
    "table.name.format": "sensortable",
    "schema.pattern": "doc"
  }
}
```

These and more JDBC Sink Connector settings, like batch inserting or 
parallelization, can be found in [Confluent Documentation]. 

## Deploy the Sink Connector

Use `curl` to deploy the sink connector to Kafka Connect:

```bash
curl -X POST -H "Content-Type: application/json" --data '@sink-connector.json' http://localhost:8083/connectors
```

## Validate the Connector Deployment

Check that the connector has been successfully deployed and is running:

- **List all connectors:**

  ```bash
  curl -X GET http://localhost:8083/connectors/
  ```

- **Check the status of the specific connector:**

  ```bash
  curl -X GET http://localhost:8083/connectors/crate-jdbc-sink/status
  ```

:::{note}
If you ever need to delete a connector, for example to test changes made to 
`.json` file, you can do it with following command:

  ```bash
  curl -X DELETE http://localhost:8083/connectors/crate-jdbc-sink
  ```
To test changes, simply delete it and then use the deployment `curl` again.
:::

## Access the Kafka Connect Container

To interact directly with Kafka Connect, access its container:

```bash
docker exec -it kafka-connect /bin/bash
```

## Produce Sample Avro Data

Once in the kafka-connect container, send sample sensor data to the 
`sensor-data-topic` using the Avro console  producer. In this sample we 
combine the schema definition and sending the data into single step.

```bash
echo '{"sensor_id":101,"timestamp":"2022-06-12T19:00:00Z","temperature":22.5,"humidity":60}
{"sensor_id":102,"timestamp":"2022-06-12T19:05:00Z","temperature":23.0,"humidity":58}
{"sensor_id":103,"timestamp":"2022-06-12T19:10:00Z","temperature":21.8,"humidity":65}
{"sensor_id":104,"timestamp":"2022-06-12T19:15:00Z","temperature":24.1,"humidity":55}
{"sensor_id":105,"timestamp":"2022-06-12T19:20:00Z","temperature":20.9,"humidity":68}' | kafka-avro-console-producer \
  --broker-list kafka:9092 \
  --topic sensor-data-topic \
  --property schema.registry.url=http://schema-registry:8081 \
  --property value.schema='{
    "type": "record",
    "name": "SensorData",
    "fields": [
      {"name": "sensor_id", "type": "int"},
      {"name": "timestamp", "type": "string"},
      {"name": "temperature", "type": "float"},
      {"name": "humidity", "type": "int"}
    ]
  }'
```

## Query Data in CrateDB

Last thing to do is verify that data was successfully sent. You can do so 
via the {ref}`Admin UI <crate-admin-ui:index>`, in this case accessible at 
`http://localhost:4200` or by {ref}`Crash <crate-crash:index>`, our CLI tool.

::::{tab-set}
:::{tab-item} Admin UI
:sync: tab1
```sql
SELECT *
FROM "crate"."sensortable"
LIMIT 100;
```
:::
:::{tab-item} Crash
:sync: tab2
``` bash
cr> SELECT * FROM crate.sensortable LIMIT 5;
+-----------+----------------------+-------------+----------+
| sensor_id | timestamp            | temperature | humidity |
+-----------+----------------------+-------------+----------+
|       103 | 2022-06-12T19:10:00Z |        21.8 |       65 |
|       105 | 2022-06-12T19:20:00Z |        20.9 |       68 |
|       101 | 2022-06-12T19:00:00Z |        22.5 |       60 |
|       102 | 2022-06-12T19:05:00Z |        23.0 |       58 |
|       104 | 2022-06-12T19:15:00Z |        24.1 |       55 |
+-----------+----------------------+-------------+----------+
SELECT 5 rows in set (0.015 sec)
```
:::
::::

[Confluent Documentation]: https://docs.confluent.io/kafka-connectors/jdbc/current/sink-connector/sink_config_options.html
[Docker]: https://docs.docker.com/get-docker
[Docker Compose]: https://docs.docker.com/compose/install
[Kafka Connect]: https://docs.confluent.io/platform/current/connect/index.html
[Kafka Connect JDBC connector]: https://docs.confluent.io/kafka-connectors/jdbc/current/sink-connector/overview.html
[PostgreSQL driver]: https://jdbc.postgresql.org/download
[PostgreSQL website]: https://jdbc.postgresql.org/download
