(influxdb)=
(integrate-influxdb)=
(integrate-influxdb-quickstart)=
# InfluxDB

:::{include} /_include/links.md
:::

```{div} .float-right .text-right
[![InfluxDB logo](https://upload.wikimedia.org/wikipedia/commons/c/c6/Influxdb_logo.svg){height=60px loading=lazy}][InfluxDB]
<br>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/influxdb.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/influxdb.yml?branch=main&label=CTK%2BInfluxDB" loading="lazy" alt="CI status: InfluxDB"></a>
```
```{div} .clearfix
```

:::{rubric} About
:::

:::{div}
[InfluxDB] is a scalable datastore for metrics, events, and real-time analytics. 
InfluxDB Core is a database built to collect, process, transform, and store event
and time series data. It is ideal for use cases that require real-time ingest and
fast query response times to build user interfaces, monitoring, and automation solutions.
:::


:::{rubric} Synopsis
:::

```shell
ctk load table \
  "influxdb2://example:token@influxdb.example.org:8086/testdrive/demo" \
  --cratedb-sqlalchemy-url="crate://user:password@cratedb.example.org:4200/testdrive/demo"
```

That's the blueprint for the InfluxDB URI:
```text
"influxdb2://{org}:{token}@influxdb.example.org:8086/{bucket}/{measurement}"
```

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Tutorial: Import data from InfluxDB
:link: influxdb-learn
:link-type: ref
How to load data from InfluxDB Server and files in InfluxDB line protocol
format (ILP) into CrateDB.
:::

:::{grid-item-card} InfluxDB Table Loader
:link: ctk:influxdb-loader
:link-type: ref
Load InfluxDB collections into CrateDB.
:::

::::

:::{toctree}
:maxdepth: 1
:hidden:
learn
:::
