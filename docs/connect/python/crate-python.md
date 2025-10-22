(crate-python)=
# crate-python

:::{div} .float-right .text-right
[![Python DB API CI](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-dbapi.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-python-dbapi.yml)
:::
:::{div} .clearfix
:::

The `crate` Python package offers a database client implementation compatible
with the Python Database API 2.0 specification, and also includes the CrateDB
SQLAlchemy dialect. See the full documentation {ref}`here <crate-python:index>`.
The package can be installed using `pip install crate`.

```python
from crate import client

conn = client.connect("https://<name-of-your-cluster>.cratedb.net:4200", username="admin", password="<PASSWORD>", verify_ssl_cert=True)

with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sys.summits")
    result = cursor.fetchone()
    print(result)
```

- [Connect to CrateDB using the Python DB API]


[Connect to CrateDB using the Python DB API]: https://github.com/crate/cratedb-examples/tree/main/by-language/python-dbapi
