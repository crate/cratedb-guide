(mqtt-usage)=
# Load data from an MQTT topic into CrateDB

The usage guide will walk you through starting the [Eclipse Mosquitto] broker and CrateDB,
publishing JSON data to an MQTT topic, subscribing to the topic to relay
data into a CrateDB table continuously, and validating that the data has
been stored successfully.
The data transfer is supported by the [LorryStream MQTT source] data
pipeline element.

## Prerequisites

Docker is used for running all components. This approach works consistently
across Linux, macOS, and Windows.

Alternatively, you can use Podman. You can also use a different MQTT broker such as
EMQX, HiveMQ, VerneMQ, or RabbitMQ. Azure IoT Hub speaks MQTT as well, but with
protocol and authentication specifics; adjust settings accordingly.

Create a shared network.
```shell
docker network create cratedb-demo
```

Start CrateDB.
```shell
docker run --name=cratedb --rm -it --network=cratedb-demo \
  --publish=4200:4200 --publish=5432:5432 \
  --env=CRATE_HEAP_SIZE=2g docker.io/crate -Cdiscovery.type=single-node
```

Start Mosquitto.
```shell
docker run --name=mosquitto --rm -it --network=cratedb-demo \
  --publish=1883:1883 docker.io/eclipse-mosquitto \
  mosquitto -c /mosquitto-no-auth.conf
```
> Note: This broker configuration allows anonymous access for demonstration purposes only.
> Do not expose it to untrusted networks. For production, configure authentication/TLS.

Prepare shortcuts for the CrateDB shell, LorryStream, and the Mosquitto client
programs.

::::{tab-set}

:::{tab-item} Linux and macOS
To make the settings persistent, add them to your shell profile (`~/.profile`).
```shell
alias crash="docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash"
alias lorry="docker run --rm -i --network=cratedb-demo ghcr.io/daq-tools/lorrystream lorry"
alias mosquitto_pub="docker run --rm -i --network=cratedb-demo docker.io/eclipse-mosquitto mosquitto_pub"
alias mosquitto_sub="docker run --rm -i --network=cratedb-demo docker.io/eclipse-mosquitto mosquitto_sub"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash @args }
function lorry { docker run --rm -i --network=cratedb-demo ghcr.io/daq-tools/lorrystream lorry @args }
function mosquitto_pub { docker run --rm -i --network=cratedb-demo docker.io/eclipse-mosquitto mosquitto_pub @args }
function mosquitto_sub { docker run --rm -i --network=cratedb-demo docker.io/eclipse-mosquitto mosquitto_sub @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash $*
doskey lorry=docker run --rm -i --network=cratedb-demo ghcr.io/daq-tools/lorrystream lorry $*
doskey mosquitto_pub=docker run --rm -i --network=cratedb-demo docker.io/eclipse-mosquitto mosquitto_pub $*
doskey mosquitto_sub=docker run --rm -i --network=cratedb-demo docker.io/eclipse-mosquitto mosquitto_sub $*
```
:::

::::

## Usage

Subscribe to all MQTT topics on the broker to monitor any traffic.
```shell
mosquitto_sub -h mosquitto -t "#" -v
```

Invoke the data transfer pipeline.
```shell
lorry relay \
  "mqtt://mosquitto/testdrive/%23?content-type=json" \
  "crate://cratedb/?table=testdrive"
```

Publish a JSON message to an MQTT topic.
```shell
echo '{"temperature": 42.84, "humidity": 83.1}' | \
  mosquitto_pub -h mosquitto -t testdrive/channel1 -s
```

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM testdrive"
```


[Eclipse Mosquitto]: https://mosquitto.org/
[LorryStream MQTT source]: https://lorrystream.readthedocs.io/source/mqtt.html
