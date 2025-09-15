(aws-lambda)=
# AWS Lambda

:::{include} /_include/links.md
:::

```{div} .float-right
[![AWS Lambda logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Amazon_Lambda_architecture_logo.svg/281px-Amazon_Lambda_architecture_logo.svg.png){height=60px loading=lazy}][AWS Lambda]
```
```{div} .clearfix
```

:::{rubric} About
:::

:::{div}
[AWS Lambda] is a serverless compute service that runs your code in response to
events and automatically manages the underlying compute resources for you.
Events can include state changes and updates.
:::

:::{rubric} Learn
:::

It is common practice to forward DynamoDB table change stream events to a
Kinesis stream, and to consume that from an adapter to write into an analytical
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
