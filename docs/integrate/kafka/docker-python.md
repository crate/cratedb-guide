(kafka-docker-python)=
# Using Kafka with Python

This walkthrough demonstrates how to load data from a Kafka topic into a
CrateDB table, using a Python consumer and CrateDB's HTTP interface.

## Start services

Start Kafka and CrateDB using Docker Compose.
```yaml
# docker-compose.yml
services:
  kafka:
    image: bitnami/kafka:latest
    container_name: kafka
    environment:
      - KAFKA_CFG_NODE_ID=1
      - KAFKA_CFG_PROCESS_ROLES=broker,controller
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093
      - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT
      - KAFKA_ENABLE_KRAFT=yes
      - ALLOW_PLAINTEXT_LISTENER=yes
    ports:
      - "9092:9092"
    networks: [ demo ]

  cratedb:
    image: crate:latest
    container_name: cratedb
    command: ["crate", "-Ccluster.name=crate-demo", "-Chttp.cors.enabled=true", "-Chttp.cors.allow-origin=*"]
    ports:
      - "4200:4200"   # HTTP API / Admin UI
      - "5432:5432"   # PostgreSQL wire protocol
    networks: [ demo ]

networks:
  demo: {}
```

```shell
docker compose up -d
```

## Provision CrateDB and Kafka

* CrateDB Admin UI: `http://localhost:4200`
* Kafka broker (inside-compose hostname): kafka:9092

### Create a demo table in CrateDB

The easiest way to do this is through the CrateDB Admin UI at `http://localhost:4200` and execute this using the console:

```sql
CREATE TABLE IF NOT EXISTS sensor_readings (
    device_id TEXT, ts TIMESTAMPTZ,
    temperature DOUBLE PRECISION,
    humidity DOUBLE PRECISION,
    PRIMARY KEY (device_id, ts)
);
```

But this can also be done using `curl`:

```bash
curl -sS -H 'Content-Type: application/json' -X POST http://localhost:4200/_sql -d '{"stmt":"CREATE TABLE IF NOT EXISTS sensor_readings (device_id TEXT, ts TIMESTAMPTZ, temperature DOUBLE PRECISION, humidity DOUBLE PRECISION, PRIMARY KEY (device_id, ts))"}'
```

### Create a Kafka topic and send a couple of messages

Creating a Kafka topic can be done in several ways, we are selecting to use
`docker exec` in this way:
```bash
docker exec -it kafka kafka-topics.sh --create --topic sensors --bootstrap-server kafka:9092 --partitions 3 --replication-factor 1
```

## Process events

```bash
docker exec -it kafka kafka-console-producer.sh --bootstrap-server kafka:9092 --topic sensors <<'EOF'
{"device_id":"alpha","ts":"2025-08-19T12:00:00Z","temperature":21.4,"humidity":48.0}
{"device_id":"alpha","ts":"2025-08-19T12:01:00Z","temperature":21.5,"humidity":47.6}
{"device_id":"beta","ts":"2025-08-19T12:00:00Z","temperature":19.8,"humidity":55.1}
EOF
```

Messages are newline-delimited JSON for simplicity.


Create a simple consumer using Python.

```python
# quick_consumer.py
import json, requests
from confluent_kafka import Consumer

c = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "demo",
    "auto.offset.reset": "earliest",
})
c.subscribe(["sensors"])

SQL_ENDPOINT = "http://localhost:4200/_bulk"

def insert_batch(rows):
    # Bulk insert via HTTP; one statement, many parameter sets
    body = {
      "stmt": "INSERT INTO sensor_readings (device_id, ts, temperature, humidity) VALUES (?, ?, ?, ?) ON CONFLICT (device_id, ts) DO UPDATE SET temperature = EXCLUDED.temperature, humidity = EXCLUDED.humidity",
      "bulk_args": rows
    }
    r = requests.post(SQL_ENDPOINT, json=body, timeout=10)
    r.raise_for_status()

batch = []
try:
    while True:
        msg = c.poll(1.0)
        if msg is None: 
            if batch: insert_batch(batch); batch.clear()
            continue
        if msg.error(): 
            print("Kafka error:", msg.error()); 
            continue

        rec = json.loads(msg.value())
        batch.append([rec["device_id"], rec["ts"], rec["temperature"], rec["humidity"]])

        if len(batch) >= 500:
            insert_batch(batch)
            batch.clear()
finally:
    if batch: insert_batch(batch)
    c.close()
```

Run this with:

```bash
pip install confluent-kafka requests
python quick_consumer.py
```

:::{tip}
This shows the custom client path: transform/filter as you like, do idempotent upserts on (device_id, ts), and batch writes for speed.
:::

## Explore data

Use `curl` to submit a `SELECT` statement that verifies data has been stored in CrateDB.
```bash
curl -sS -H 'Content-Type: application/json' -X POST http://localhost:4200/_sql -d '{"stmt":"SELECT device_id, ts, temperature, humidity FROM sensor_readings ORDER BY ts LIMIT 10"}' | jq
```
