# Settings

CrateDB-specific options for a django project `settings`.

## Warnings

`cratedb_django` emits certain warnings to notify about compatability issues.

* `unique=True`. CrateDB only supports unique constraints on primary keys, any
  model field with unique=true will emit a warning to stdout.

### Environment variables

| name                                 | value            | default | description                                                             |
|--------------------------------------|------------------|---------|-------------------------------------------------------------------------|
| `SUPPRESS_UNIQUE_CONSTRAINT_WARNING` | [`true`/`false`] | false   | Suppresses warning when a model is created with unique=True constraint. |

## Specifying a database

The minimum needed to connect to a CrateDB instance in `localhost` is
`ENGINE` and `SERVERS`.

```python
DATABASES = {
    "default": {
        "ENGINE": "cratedb_django",
        "SERVERS": ["localhost:4200"],
    }
}
```

The connector uses the [HTTP driver](https://github.com/crate/crate-python)
therefore only the port `4200`
is needed.

Several URIs can be specified in `SERVERS`, if several servers are provided
queries will be sent in a round-robin fashion, this improves performance
and availability. If there is a load balancer in front of the CrateDB
cluster or the cluster is deployed
using [CrateDB Cloud](https://console.cratedb.cloud/) there is
**no need** to specify several URIs, only one (the load balancer's) is enough.

```python
DATABASES = {
    "default": {
        "ENGINE": "cratedb_django",
        "SERVERS": ["localhost:4200", "localhost:4201", "localhost:4203"],
    }
}
```

## Valid URIs

`http://localhost:4200`<br>
`https://localhost:4200`<br>
`localhost:4200`

## Authentication

For authentication, `USER` and `PASSWORD` need to be set, additional options
can be set with `OPTIONS` to pass `crate-python` options.

```python
DATABASES = {
    "default": {
        "ENGINE": "cratedb_django",
        "SERVERS": [
            "https://<CLUSTER_NAME>.aks1.westeurope.azure.cratedb.net:4200"],
        "USER": "<USERNAME>",
        "PASSWORD": "<PASSWORD>",
        "OPTIONS": {
            'verify_ssl_cert': True
        },
    }
}
```

## Default auto field

`DEFAULT_AUTO_FIELD` specifies the type of auto-created primary key fields,
it's recommended to set it to `AutoUUIDField`.

```python
DEFAULT_AUTO_FIELD = "cratedb_django.fields.AutoUUIDField"
```

`AutoUUIDField` generates unique UUIDs for primary keys.
`cratedb_django.fields.AutoField` can be used if an integer-based primary
key is needed.
