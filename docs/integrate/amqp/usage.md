(amqp-usage)=

# Load data from an AMQP queue into CrateDB

The usage guide will walk you through starting the [RabbitMQ] AMQP broker
and CrateDB, publishing JSON data to an AMQP queue, consuming and relaying
it into a CrateDB table continuously, and validating that the data has
been stored successfully.
The data transfer is supported by the [LorryStream AMQP source] data
pipeline element.

## Prerequisites

Use Docker or Podman to run all components. This approach works consistently
across Linux, macOS, and Windows.

### Files

First, download and save all required files to your machine.
- {download}`compose.yaml`

### Services

Start services using Docker Compose or Podman Compose.
If you use Podman, replace `docker` with `podman` (or enable the podman‑docker
compatibility shim) and run `podman compose up`.

You can also use a different AMQP broker such as
Apache Qpid, Apache ActiveMQ, IBM MQ, or Solace. Azure Event Hubs and Azure Service
Bus speak AMQP as well, but with protocol and authentication specifics; adjust
settings accordingly.

```shell
docker compose up
```

:::{note}
The AMQP broker configuration used here allows anonymous access for
demonstration purposes only. Do not expose it to untrusted networks. For
production, configure authentication/TLS.
:::

## Submit data

Invoke the data transfer pipeline.
```shell
docker compose run --rm --no-TTY lorrystream lorry relay \
  "amqp://guest:guest@rabbitmq:5672/%2F?exchange=default&queue=default&routing-key=testdrive&setup=exchange,queue,bind&content-type=json" \
  "crate://cratedb/?table=amqp_demo"
```

Publish a JSON message to AMQP.
```shell
echo '{"temperature": 42.84, "humidity": 83.1}' | \
  docker compose run --rm --no-TTY amqpcat amqpcat --producer --uri='amqp://guest:guest@rabbitmq:5672/%2F' \
    --exchange=default --queue=default --routing-key=testdrive
```

## Explore data

Inspect data stored in CrateDB.
```shell
docker compose exec cratedb crash -c "SELECT * FROM doc.amqp_demo"
```
```psql
+-------------+----------+
| temperature | humidity |
+-------------+----------+
|       42.84 |     83.1 |
+-------------+----------+
SELECT 1 row in set (0.023 sec)
```


[LorryStream AMQP source]: https://lorrystream.readthedocs.io/source/amqp.html
[RabbitMQ]: https://www.rabbitmq.com/
