# Models

`CrateDBModels` is a Django model that enables CrateDB-specific features. While
`django.models.Model` can be used,
it's recommended to use the model provided by `cratedb_django`.

```python
from cratedb_django import CrateModel
from cratedb_django import fields


class Metrics(CrateModel):
    timestamp = fields.DateTimeField()
    labels_hash = fields.CharField(max_length=255)
    labels = fields.ObjectField()
    value = fields.FloatField(null=True)
    valueRaw = fields.BigIntegerField(null=True)
    day_generated = fields.GeneratedField(
        expression=RawSQL("date_trunc('day', %s)", [F("timestamp")]),
        output_field=fields.DateTimeField(),
        editable=False,
    )
    pk = fields.CompositePrimaryKey("timestamp", "labels_hash", "day_generated")

    class Meta:
        app_label = "_crate_test"
        partition_by = "day_generated"
```

## Meta options

In the class `Meta` you can specify table wide options, some will affect how the
table will be created (DLL) others
will be tunable parameters.

CrateDB specific meta options:

Any value that is `None` means that the default value is set by CrateDB, see
[docs](https://cratedb.com/docs/crate/reference/en/latest/sql/statements/create-table.html)

| name             | example             | Default | descriptions                                       |
|------------------|---------------------|---------|----------------------------------------------------|
| auto_refresh     | True                | False   | Automatically refresh the table on inserts.        |
| clustered        | ('col1', 'col2'...) | None    | The columns that the table will be clustered in.   |
| partitioned      | ('col1', 'col2'...) | None    | The columns that the table will be partitioned by. |
| number_of_shards | 4                   | None    | The number of shards per partitions.               |

## Refresh

Due to
the [eventual consistency model](https://cratedb.com/docs/crate/reference/en/latest/concepts/storage-consistency.html#consistency)
of CrateDB, `select`, `update` and `delete` will not see newly modified data
until a refresh operation is triggered. CrateDB triggers this refresh operation
every 1s if the table is not idle. You should avoid refreshing a lot due to
performance reasons.

To trigger a manual refresh on a model, call `refresh()`.

```python
Metrics.refresh()
```

To trigger a refresh automatically after every `insert` set `auto_refresh=True`
in the Meta class. This will **not** trigger on deletes or updates.

```python
class SomeModel(CrateModel):
    ...

    class Meta:
        auto_refresh = True
```

### Composite primary keys

To have several primary keys in a table, use `fields.CompositePrimaryKey`.

For example, this model will generate:

```python
class Metrics(CrateModel):
    timestamp = fields.DateTimeField()
    some_value = fields.IntegerField()
    day_generated = fields.GeneratedField(
        expression=RawSQL("date_trunc('day', %s)", [F("timestamp")]),
        output_field=fields.DateTimeField(),
        editable=False,
    )
    pk = fields.CompositePrimaryKey("timestamp", "some_value", "day_generated")
```

```sql
CREATE TABLE "_crate_test_metrics"
(
    "timestamp"     timestamp with time zone NOT NULL,
    "some_value"    integer                  NOT NULL,
    "day_generated" timestamp with time zone GENERATED ALWAYS AS ((date_trunc('day', % s))),
    PRIMARY KEY ("timestamp", "some_value", "day_generated")
)
```