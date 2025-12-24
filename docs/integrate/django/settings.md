# Django settings

CrateDB specific options for a django project `settings`.

## Specifying a database

The minimum needed to connect to a CrateDB instance in `localhost`.

```python
DATABASES = {
    "default": {
        "ENGINE": "cratedb_django",
        "SERVERS": ["localhost:4200"],
    }
}
```

The connector uses the [HTTP driver](https://github.com/crate/crate-python) therefore only the port `4200` is needed.

Several URIs can be specified in `SERVERS`, if there are more than one queries will be sent in a round-robin fashion,
this improves performance and availability. If there is a load balancer in front of the CrateDB cluster or the
cluster is deployed using [CrateDB Cloud](https://console.cratedb.cloud/) there is **no need** to specify several URIs,
only one (the load balancer's) is enough.

```python
DATABASES = {
    "default": {
        "ENGINE": "cratedb_django",
        "SERVERS": ["localhost:4200", "localhost:4201", "localhost:4203"],
    }
}
```

For authentication, `USER` and `PASSWORD` need to be set, additionally `OPTIONS` can be set with `crate-python` options.

```python
DATABASES = {
    "default": {
        "ENGINE": "cratedb_django",
        "SERVERS": ["https://<CLUSTER_NAME>.aks1.westeurope.azure.cratedb.net:4200"],
        "USER": "<USERNAME>",
        "PASSWORD": "<PASSWORD>",
        "OPTIONS": {
            'verify_ssl_cert': True
        },
    }
}
```

## Default auto field

It's recommended to set `DEFAULT_AUTO_FIELD = "cratedb_django.fields.AutoUUIDField"`, `AutoUUIDField` generates 
unique UUIDs for primary keys. `cratedb_django.fields.AutoField` can be used if an integer based primary key is needed.
