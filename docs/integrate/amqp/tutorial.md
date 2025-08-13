(amqp-tutorial)=

# Load data from an AMQP queue into CrateDB

The tutorial will walk you through starting the [RabbitMQ] AMQP broker
and CrateDB, publishing JSON data to an AMQP queue, consuming and relaying
it into a CrateDB table continuously, and validating that the data has
been stored successfully.
The data transfer is supported by the [LorryStream AMQP source] data
pipeline element.

## Prerequisites

Docker is used for running all components. This approach works consistently
across Linux, macOS, and Windows.

Alternatively, you can use Podman. You can also use a different AMQP broker such as
Apache Qpid, Apache ActiveMQ, IBM MQ, or Solace. Azure Event Hubs and Azure Service
Bus speak AMQP as well, but with protocol and authentication specifics; adjust
settings accordingly.

Create a shared network.
```shell
docker network create cratedb-demo
```

Start CrateDB.
```shell
docker run --name=cratedb --rm --network=cratedb-demo \
  --publish=4200:4200 --publish=5432:5432 \
  --env=CRATE_HEAP_SIZE=2g docker.io/crate -Cdiscovery.type=single-node
```

Start RabbitMQ.
```shell
docker run --name=rabbitmq --rm --network=cratedb-demo \
  --publish=5672:5672 docker.io/rabbitmq:3
```
> Note: This broker configuration allows anonymous access for demonstration purposes only.
> Do not expose it to untrusted networks. For production, configure authentication/TLS.

Prepare shortcuts for the CrateDB shell, LorryStream, and the AMQP client
programs.

::::{tab-set}

:::{tab-item} Linux and macOS
To make the settings persistent, add them to your shell profile (e.g., `~/.profile` or `~/.zshrc`).
```shell
alias crash="docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash"
alias lorry="docker run --rm -i --network=cratedb-demo ghcr.io/daq-tools/lorrystream lorry"
alias amqpcat="docker run --rm -i --network=cratedb-demo docker.io/cloudamqp/amqpcat amqpcat"
```
:::
:::{tab-item} Windows PowerShell
To make the settings persistent, add them to your PowerShell profile (`$PROFILE`).
```powershell
function crash { docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash @args }
function lorry { docker run --rm -i --network=cratedb-demo ghcr.io/daq-tools/lorrystream lorry @args }
function amqpcat { docker run --rm -i --network=cratedb-demo docker.io/cloudamqp/amqpcat amqpcat @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker run --rm -it --network=cratedb-demo ghcr.io/crate/cratedb-toolkit crash $*
doskey lorry=docker run --rm -i --network=cratedb-demo ghcr.io/daq-tools/lorrystream lorry $*
doskey amqpcat=docker run --rm -i --network=cratedb-demo docker.io/cloudamqp/amqpcat amqpcat $*
```
:::

::::

## Usage

Invoke the data transfer pipeline.
```shell
lorry relay \
  "amqp://guest:guest@rabbitmq:5672/%2F?exchange=default&queue=default&routing-key=testdrive&setup=exchange,queue,bind&content-type=json" \
  "crate://cratedb/?table=testdrive"
```

Publish a JSON message to AMQP.
```shell
echo '{"temperature": 42.84, "humidity": 83.1}' | \
  amqpcat --producer --uri='amqp://guest:guest@rabbitmq:5672/%2F' \
    --exchange=default --queue=default --routing-key=testdrive
```

Inspect data stored in CrateDB.
```shell
crash --hosts cratedb -c "SELECT * FROM testdrive"
```


[LorryStream AMQP source]: https://lorrystream.readthedocs.io/source/amqp.html
[RabbitMQ]: https://www.rabbitmq.com/
