(dapr-usage)=
# Connecting to CrateDB from Dapr

## Introduction
This article describes how to connect from [Dapr](https://dapr.io) (a cloud-native application runtime environment) to CrateDB. At the time of writing, the steps are identical to a regular PostgreSQL setup. If you are already familiar with setting up an output binding in Dapr with PostgreSQL, you can skip this article.

Dapr supports connecting to PostgreSQL (and therefore CrateDB) as an [output binding](https://docs.dapr.io/reference/components-reference/supported-bindings/) and as a [state store](https://docs.dapr.io/reference/components-reference/supported-state-stores/setup-postgresql-v2/). Using CrateDB as a state store is currently not supported, this article will concentrate on defining an output binding:

> Output bindings allow you to invoke external resources. An optional payload and metadata can be sent with the invocation request.
> In order to invoke an output binding:
> 1. Define the component YAML that describes the type of binding and its metadata (connection info, etc.)
> 2. Use the HTTP endpoint or gRPC method to invoke the binding with an optional payload

## Prerequisites
Before configuring the CrateDB connection, it is assumed that:
1. you have a running Dapr environment. If this is not the case yet, please follow Dapr's [Getting Started](https://docs.dapr.io/getting-started/) guide.
2. you have a running CrateDB cluster.

## Configuring the Dapr application
To configure the output binding of your application:
1. Navigate to your application folder. We will be using one of Dapr's sample applications: `git clone https://github.com/dapr/samples.git && cd samples/hello-dapr-slim`
2. Create a `components` folder if not already present: `mkdir -p components`
3. Create the file `components/crate.yaml`:

      ```yaml
   ---
   apiVersion: dapr.io/v1alpha1
   kind: Component
   metadata:
        name: crate
   spec:
        type: bindings.postgres
        version: v1
        metadata:
          - name: url
            value: "postgres://crate:crate@testcluster.cratedb.net/?ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory"
      ```

4. Start the application. In case of the sample application via `dapr run --app-id nodeapp --app-port 3000 --dapr-http-port 3500 --components-path=./components node app.js`.
5. Watch for a log message similar to `INFO[0000] component loaded. name: crate, type: bindings.postgres/v1` to verify the binding was loaded correctly.

## Usage of the output binding
There are now two services running, the actual application (port 3000) and a web service with the so-called Dapr sidecar (port 3500). Below are some examples of how to interact with the PostgreSQL binding via the Dapr sidecar (see the PostgreSQL binding specification for reference):

```bash
# Submit SELECT statements via the query operation.
curl -X POST http://localhost:3500/v1.0/bindings/crate \
  -H "Content-Type: application/json" \
  -d '{
  "operation": "query",
  "metadata": {
    "sql": "SELECT * FROM <schema name>.<table name>"
  }
}'

# Submit DDL or DML statements via the exec operation.
curl -X POST http://localhost:3500/v1.0/bindings/crate \
  -H "Content-Type: application/json" \
  -d '{
  "operation": "exec",
  "metadata": {
    "sql": "INSERT INTO <schema name>.<table name> VALUES (NOW(), 123, '"'"'some string...'"'"')"
  }
}'

# Close the connection pool, no further queries will be possible.
curl -X POST http://localhost:3500/v1.0/bindings/crate \
  -H "Content-Type: application/json" \
  -d '{
  "operation": "close"
}'
```
