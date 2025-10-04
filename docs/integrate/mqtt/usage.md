(mqtt-usage)=
# Load data from an MQTT topic into CrateDB

The usage guide will walk you through starting the [Eclipse Mosquitto] broker and CrateDB,
publishing JSON data to an MQTT topic, subscribing to the topic to relay
data into a CrateDB table continuously, and validating that the data has
been stored successfully.
The data transfer is supported by the [LorryStream MQTT source] data
pipeline element.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

You can also use a different MQTT broker such as
EMQX, HiveMQ, VerneMQ, or RabbitMQ. Azure IoT Hub speaks MQTT as well, but with
protocol and authentication specifics; adjust settings accordingly.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

```shell
docker compose up
```

:::{note}
The MQTT broker configuration used here allows anonymous access for
demonstration purposes only. Do not expose it to untrusted networks. For
production, configure authentication/TLS.
:::

## Submit data

Subscribe to all MQTT topics on the broker to monitor any traffic.
```shell
docker compose exec --no-tty mosquitto mosquitto_sub -h mosquitto -t "#" -v
```

Invoke the data transfer pipeline.
```shell
docker compose run --rm lorrystream lorry relay "mqtt://mosquitto/testdrive/%23?content-type=json" "crate://cratedb/?table=mqtt_demo"
```

Publish a JSON message to an MQTT topic.
```shell
echo '{"temperature": 42.84, "humidity": 83.1}' | docker compose exec --no-tty mosquitto mosquitto_pub -h mosquitto -t testdrive/channel1 -s
```

## Explore data

Inspect data stored in CrateDB.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.mqtt_demo"
```
```psql
+-------------+----------+
| temperature | humidity |
+-------------+----------+
|       42.84 |     83.1 |
+-------------+----------+
SELECT 1 row in set (0.004 sec)
```


[Eclipse Mosquitto]: https://mosquitto.org/
[LorryStream]: https://lorrystream.readthedocs.io/
[LorryStream MQTT source]: https://lorrystream.readthedocs.io/source/mqtt.html
