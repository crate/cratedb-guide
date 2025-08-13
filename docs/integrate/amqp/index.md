(amqp)=
# AMQP

```{div} .float-right
[![AMQP logo](https://www.cleo.com/sites/default/files/styles/desktop_664_270_scale/public/2023-12/amqp-logo.png.webp){width=180px loading=lazy}][AMQP]
```
```{div} .clearfix
```

:::{rubric} About
:::

The [AMQP] protocol is an open standard application layer protocol for
message-oriented middleware. The defining features of AMQP are message
orientation, queuing, routing (including point-to-point and
publish-and-subscribe), reliability, and security.

:::{rubric} Synopsis
:::

Use LorryStream to receive JSON data from an AMQP queue, continuously loading
records into CrateDB.
```shell
uvx --from=lorrystream lorry relay \
    "amqp://guest:guest@localhost:5672/%2F?queue=testdrive&content-type=json" \
    "crate://localhost/?table=testdrive"
```

:::{rubric} Learn
:::

[LorryStream] is a lightweight and polyglot stream-processing library, used as a
data backplane, message relay, or pipeline subsystem.

::::{grid}

:::{grid-item-card} Tutorial: Use LorryStream
:link: amqp-tutorial
:link-type: ref
How to load data from AMQP into CrateDB using LorryStream.
:::

::::

:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
:::


[LorryStream]: https://lorrystream.readthedocs.io/
[AMQP]: https://www.amqp.org/
