(aws-dynamodb)=
(cdc-dynamodb)=
# Amazon DynamoDB

:::{include} /_include/links.md
:::

:::{rubric} About
:::

:::{div}
The [DynamoDB Table Loader] supports loading DynamoDB tables into CrateDB (full-load),
while the [DynamoDB CDC Relay] pipeline uses [Amazon DynamoDB Streams] or [Amazon Kinesis
Data Streams] to relay table change stream CDC events from a DynamoDB table into CrateDB.

:::{rubric} Learn
:::

:::{div}
It is a common application to relay DynamoDB table change stream events to a
Kinesis Stream, and consume that from an adapter to write into an analytical
or long-term storage consolidation database.

If you are looking into serverless replication using AWS Lambda:
- [DynamoDB CDC Relay with AWS Lambda]
- Blog: [Replicating CDC events from DynamoDB to CrateDB]
:::
