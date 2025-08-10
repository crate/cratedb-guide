(aws-dynamodb)=
(cdc-dynamodb)=
# Amazon DynamoDB

:::{include} /_include/links.md
:::

```{div} .float-right .text-right
[![DynamoDB logo](https://upload.wikimedia.org/wikipedia/commons/f/fd/DynamoDB.png){height=60px loading=lazy}][DynamoDB]
<br>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/dynamodb.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/dynamodb.yml?branch=main&label=CTK%2BDynamoDB" loading="lazy"></a>
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
[DynamoDB] is a fully managed NoSQL database service provided by Amazon Web Services (AWS).
It is designed for high-performance, scalable applications and offers key-value and
document data structures. DynamoDB is serverless, meaning users don't need to manage
servers or infrastructure.
:::

::::

::::{grid-item}
:columns: auto 3 3 3

:::{rubric} Related
:::
- [Amazon DynamoDB Streams]
- {ref}`aws-kinesis`
- [Amazon Kinesis Data Streams]
::::

:::::


:::{rubric} Synopsis
:::

```shell
uvx 'cratedb-toolkit[kinesis]' load table \
  "kinesis+dynamodb+cdc://${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}@aws/cdc-stream?region=eu-central-1" \
  --cluster-url="crate://crate:crate@localhost:4200/testdrive/demo"
```

:::{rubric} Learn
:::

It is common practice to forward DynamoDB table change stream events to a
Kinesis Stream, and consume that from an adapter to write into an analytical
or long-term storage consolidation database like CrateDB.

::::{grid}

:::{grid-item-card} DynamoDB Table Loader
:link: ctk:dynamodb-loader
:link-type: ref
Load DynamoDB tables into CrateDB (`full-load`).
:::

:::{grid-item-card} DynamoDB CDC Relay
:link: ctk:dynamodb-cdc
:link-type: ref
Relay table change stream CDC events from a DynamoDB table into CrateDB (`cdc`).
:::

:::{grid-item-card} DynamoDB CDC Relay using AWS Lambda
:link: ctk:io/dynamodb/cdc-lambda
:link-type: doc
Use serverless replication based on AWS Lambda to
relay CDC events into CrateDB (`cdc`).
:::

::::

:::{seealso}
**Blog:** [Replicating CDC events from DynamoDB to CrateDB]
:::
