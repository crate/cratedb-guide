# Scalar functions

Support for [Scalar functions] is tracked in [scalar issue].

[Scalar functions]: https://cratedb.com/docs/crate/reference/en/latest/general/builtins/scalar-functions.html
[scalar issue]: https://github.com/crate/cratedb-django/issues/32

Scalar functions can be used in both `db_default` and `expressions` in 
`GeneratedFields`. It is recommended to use the ones provided by 
`cratedb_django.models.functions`, alternatively if the needed function
is not implemented, `RawSQL` can be used.

## Using functions

```python
from cratedb_django.models import CrateDBModel, functions
from cratedb_django import fields

from django.db.models.expressions import Value, RawSQL

class SomeModel(CrateDBModel):
    f_format = fields.GeneratedField(
        expression=functions.Format(Value("%tY"), functions.CURRENT_DATE()),
        output_field=fields.CharField(max_length=100),
    )
```

The same function could be implemented by using `RawSQL`.

```python
from cratedb_django.models import CrateDBModel, functions
from cratedb_django import fields

from django.db.models.expressions import Value, RawSQL

class SomeModel(CrateDBModel):
    f_raw = fields.GeneratedField(
        expression=RawSQL('format(%s, CURRENT_DATE)', [Value("%tY")]),
        output_field=fields.CharField(max_length=100)
    )
```