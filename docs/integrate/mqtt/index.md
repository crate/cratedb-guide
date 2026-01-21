(mqtt)=
# MQTT

```{div} .float-right
[![MQTT logo](https://mqtt.org/assets/img/mqtt-logo.svg){width=180px loading=lazy}][MQTT]
```
```{div} .clearfix
```

:::{rubric} About
:::

[MQTT] is an OASIS standard messaging protocol for the Internet of Things (IoT).

It is designed as an extremely lightweight publish/subscribe messaging transport
that is ideal for connecting remote devices with a small code footprint and minimal
network bandwidth.

MQTT today is used in a wide variety of industries, such as automotive, manufacturing,
telecommunications, and oil and gas. It enables efficient, reliable messaging between
devices and backends over constrained networks.

Through CrateDB's MQTT integration you can use any MQTT broker such as Coreflux,
Eclipse Mosquitto, EMQX, HiveMQ, VerneMQ, or RabbitMQ. Azure IoT Hub speaks MQTT
as well, but with protocol and authentication specifics; please adjust settings
accordingly.

:::{rubric} Synopsis
:::

[LorryStream] is a lightweight and polyglot stream-processing library, used as a
data backplane, message relay, or pipeline subsystem.
Use LorryStream to receive JSON data from an MQTT topic, continuously loading
records into CrateDB.
```shell
uvx --from=lorrystream lorry relay \
    "mqtt://localhost/testdrive/%23?content-type=json" \
    "crate://localhost/?table=testdrive"
```

:::{rubric} Learn
:::

Follow up with detailed tutorials about integrations with different MQTT brokers.

::::{grid}

:::{grid-item-card} HiveMQ
:link: hivemq
:link-type: ref
:::

:::{grid-item-card} Mosquitto
:link: mosquitto
:link-type: ref
:::

::::


[LorryStream]: https://lorrystream.readthedocs.io/
[MQTT]: https://mqtt.org/
