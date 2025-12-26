(django)=
# Django

```{div} .float-right
[![Django logo](https://static.djangoproject.com/img/logos/django-logo-positive.svg){height=60px loading=lazy}][Django]
<br>
<a href="https://github.com/surister/cratedb-django/actions/workflows/tests.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/surister/cratedb-django/tests.yml?branch=master&label=Django" loading="lazy" alt="CI status: CrateDB Django connector"></a>
```
```{div} .clearfix
```

The CrateDB team develops and supports a custom-built driver, [cratedb-django](https://github.com/crate/cratedb-django)

:::{rubric} Getting started
:::

Installing the library:
```shell
pip install cratedb-django
```

Once the library is installed, set the appropiate `settings.py`

```python
DATABASES = {
    "default": {
        "ENGINE": "cratedb_django",
        "SERVERS": ["localhost:4200"],
    }
}

DEFAULT_AUTO_FIELD = "cratedb_django.fields.AutoUUIDField"
```

For a model to be compatible with CrateDB, import and use `CrateDBModel`:

```python
from cratedb_django.models import fields
from cratedb_django.models import CrateModel

class Metrics(CrateModel):
    value = fields.IntegerField()
```

Django migrations can be run in CrateDB, all migrations for the default applications (contrib, auth, admin...) are
tested and work. In spite of that it's recommended that you run anything transactional in a transactional database, 
like PostgresSQL and use CrateDB as your analytical database.

CrateDB has certain constraints that makes migration management different.

## What's supported?

Django ORM has many features, see [feature-list](https://github.com/crate/cratedb-django/issues/50) for a comprehensive list of supported features.
Feel free to open a new issue if you need a new feature.

## Table of Contents

:::{toctree}
:maxdepth: 1
settings
models
fields
:::
