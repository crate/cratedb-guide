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

The CrateDB team develops and supports a custom-built driver, [cratedb_django](https://github.com/crate/cratedb-django)

:::{rubric} Getting started
:::

Installing the library:
```shell
pip install cratedb_django
```

Once the library is installed, set it in the project's `settings`

```python
DATABASES = {
    "default": {
        "ENGINE": "cratedb_django",
        "SERVERS": ["localhost:4200"],
    }
}
```

For a model to be compatible with CrateDB, import and use `CrateDBModel`:

```python
from django.db import models
from cratedb_django.models import CrateModel

class Metrics(CrateModel):
    value = models.IntegerField()
```

Django migrations can be run in CrateDB, default django migrations are tested.
In spite of that, we recommend that you run anything transactional in a transactional database, 
like PostgresSQL and use CrateDB as your analytical database.

## What's supported?

Django ORM has many features, see [feature-list](https://github.com/crate/cratedb-django/issues/50) for a comprehensive list of supported features.
Feel free to open a new issue if you need a new feature.

### Table of Contents
