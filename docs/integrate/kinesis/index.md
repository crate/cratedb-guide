(aws-kinesis)=
# Kinesis

:::{include} /_include/links.md
:::

```{div} .float-right
[![Kinesis logo](https://icon.icepanel.io/AWS/svg/Analytics/Kinesis-Data-Streams.svg){height=60px loading=lazy}][Amazon Kinesis Data Streams]
```
```{div} .clearfix
```

:::::{grid}
:padding: 0

::::{grid-item}
:columns: auto 9 9 9

:::{rubric} About
:::
:::{div}
[Amazon Kinesis Data Streams] is a serverless streaming data service that
simplifies the capture, processing, and storage of data streams at any
scale, such as application logs, website clickstreams, and IoT telemetry
data, for machine learning (ML), analytics, and other applications.

You can use Amazon Kinesis Data Streams to collect and process large data
streams in real time. A typical application reads data from the stream as
records.
:::
::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Related
:::
- {ref}`aws-dynamodb`
- [Amazon DynamoDB Streams]
::::

:::::

:::{rubric} Synopsis
:::

```shell
uvx 'cratedb-toolkit[io-ingestr]' load table \
  "kinesis://?aws_access_key_id=${AWS_ACCESS_KEY_ID}&aws_secret_access_key=${AWS_SECRET_ACCESS_KEY}&region_name=eu-central-1&table=arn:aws:kinesis:eu-central-1:831394476016:stream/testdrive" \
  --cluster-url="crate://crate:crate@localhost:4200/testdrive/kinesis_demo"
```

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Ingestr Table Loader
:link: https://cratedb-toolkit.readthedocs.io/io/ingestr/#amazon-kinesis-to-cratedb
:link-type: url
Relay Kinesis stream into CrateDB.
:::

:::{grid-item-card} DynamoDB CDC Relay
:link: ctk:dynamodb-cdc
:link-type: ref
Relay table change stream CDC events from DynamoDB into CrateDB, using Kinesis.
:::

::::


:::{seealso}
**Blog:** [Replicating CDC events from DynamoDB to CrateDB]
:::
