(connect-configure)=
(connect-general)=
# General information

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
About connection properties for CrateDB.
:::

To connect to CrateDB properly, your application or driver needs to be
configured with corresponding connection properties. Please note that different
applications and drivers may obtain connection properties in different formats.

<style>
/* Code blocks need to be slimmer */
.driver-slim div.highlight-default {
  margin-top: 0.2em;
}
.driver-slim pre {
  padding: 0.4em;
}
.driver-slim p {
  margin-bottom: 0;
}
</style>

::::::{tab-set}

:::::{tab-item} CrateDB and CrateDB Cloud

::::{grid}
:margin: 0
:padding: 0

:::{grid-item}
:columns: 4
:margin: 0
:padding: 0

**Connection properties**

:Host: `<cluster>`.cratedb.net
:Port: 5432 (PostgreSQL) or<br>4200 (HTTP)
:User: `<user>`
:Pass: `<password>`

:::

:::{grid-item}
:columns: 8
:margin: 0
:padding: 0
:class: driver-slim

**Connection-string examples**
<br><br>

**Native PostgreSQL, psql**
```text
postgresql://<user>:<password>@<cluster>.cratedb.net:5432/doc
```

**JDBC: PostgreSQL pgJDBC**
```text
jdbc:postgresql://<cluster>.cratedb.net:5432/doc?user=<user>&password=<password>
```

**JDBC: CrateDB JDBC, e.g. Apache Flink**
```text
jdbc:crate://<cluster>.cratedb.net:5432/doc?user=<user>&password=<password>
```

**HTTP: Admin UI, CLI, CrateDB drivers**
```text
https://<user>:<password>@<cluster>.cratedb.net:4200/
```

**SQLAlchemy**
```text
crate://<user>:<password>@<cluster>.cratedb.net:4200/?schema=doc&ssl=true
```

:::

::::

:::::

:::::{tab-item} CrateDB on localhost

::::{grid}
:margin: 0
:padding: 0

:::{grid-item}
:columns: 4
:margin: 0
:padding: 0

**Connection properties**

:Host: localhost
:Port: 5432 (PostgreSQL) or<br>4200 (HTTP)
:User: `crate`
:Pass: (empty)

:::

:::{grid-item}
:columns: 8
:margin: 0
:padding: 0
:class: driver-slim

**Connection-string examples**
<br><br>

**Native PostgreSQL, psql**
```
postgresql://crate@localhost:5432/doc
```

**JDBC: PostgreSQL pgJDBC**
```text
jdbc:postgresql://localhost:5432/doc?user=crate
```

**JDBC: CrateDB JDBC, e.g. Apache Flink**
```text
jdbc:crate://localhost:5432/doc?user=<user>&password=<password>
```

**HTTP: Admin UI, CLI, CrateDB drivers**
```text
http://crate@localhost:4200/
```

**SQLAlchemy**
```text
crate://crate@localhost:4200/?schema=doc
```

:::

::::
:::::

::::::


:::{rubric} Notes
:::

:::{div}
- CrateDB's fixed catalog name is `crate`, the default schema name is `doc`.
- CrateDB does not implement the notion of a database,
  however tables can be created in different [schemas].
- When asked for a *database name*, specifying a schema name (any),
  or the fixed catalog name `crate` may be applicable.
- If a database-/schema-name is omitted while connecting,
  the PostgreSQL drivers may default to the "username".
- The predefined [superuser] on an unconfigured CrateDB cluster is
  called `crate`, defined without a password.
- For authenticating properly, please learn about the available
  [authentication] options.
:::


[authentication]: inv:crate-reference:*:label#admin_auth
[schemas]: inv:crate-reference:*:label#ddl-create-table-schemas
[superuser]: inv:crate-reference:*:label#administration_user_management
