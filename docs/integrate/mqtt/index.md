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

:::{rubric} Synopsis
:::

Use LorryStream to receive JSON data from an MQTT topic, continuously loading
records into CrateDB.
```shell
uvx --from=lorrystream lorry relay \
    "mqtt://localhost/testdrive/%23?content-type=json" \
    "crate://localhost/?table=testdrive"
```

:::{rubric} Learn
:::

[LorryStream] is a lightweight and polyglot stream-processing library, used as a
data backplane, message relay, or pipeline subsystem.
[Node-RED] is a workflow automation tool that allows you to orchestrate message flows
and transformations via a comfortable web interface.

::::{grid}

:::{grid-item-card} Load data from MQTT using LorryStream
:link: mqtt-usage
:link-type: ref
How to load data from an MQTT topic into CrateDB using LorryStream.
:::

:::{grid-item-card} Load data from MQTT using Node-RED
:link: https://community.cratedb.com/t/ingesting-mqtt-messages-into-cratedb-using-node-red/803
:link-type: url
Ingesting MQTT messages into CrateDB using Node-RED.
:::

::::

:::{toctree}
:maxdepth: 1
:hidden:
Usage <usage>
:::


[LorryStream]: https://lorrystream.readthedocs.io/
[MQTT]: https://mqtt.org/
[Node-RED]: https://nodered.org/
