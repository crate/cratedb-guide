(fdw)=

# Foreign data wrappers

:::{div} sd-text-muted
Access PostgreSQL database tables on remote servers as if they were stored
within CrateDB.
:::

## Limitations

- **Read-only** – only SELECT (DQL) is supported on foreign tables.
- **PostgreSQL support** – currently CrateDB only supports FDW for PostgreSQL.
- **Filter push-down is best-effort** – use `EXPLAIN` to see what is pushed.
- **Security guard-rail** – by default only the `crate` user may connect to
  *localhost* targets. Override via `fdw.allow_local = true` if you must.

## Prerequisites

Before configuring a Foreign Data Wrapper (FDW), you should have CrateDB and
PostgreSQL instances up and running, or other services that speak the PostgreSQL wire protocol.

:::{note}
To have access to FDW in CrateDB, make sure you have a cluster running
version 5.7 or above.
:::

## Set up

Ensure outbound firewall rules allow CrateDB → remote DB traffic before
proceeding with the following steps.

::::{stepper}
### Create a server in CrateDB

```sql
CREATE SERVER my_postgresql FOREIGN DATA WRAPPER jdbc
OPTIONS (url 'jdbc:postgresql://example.com:5432/');
```

:::{note}
By default only the `crate` user can use server definitions that connect to
localhost. Other users are not allowed to connect to instances running on the
same host as CrateDB. This is a security measure to prevent users from
bypassing [Host-Based Authentication (HBA)] restrictions.
See [fdw.allow_local].

[Host-Based Authentication (HBA)]: inv:crate-reference:*:label#admin_hba
[fdw.allow_local]: inv:crate-reference:*:label#fdw.allow_local
:::

### Create a user mapping

Use a DDL statement to map a CrateDB user to another user on a
foreign server. If not set, your session details will be used instead.

```sql
CREATE USER MAPPING
FOR mylocaluser
SERVER my_postgresql
OPTIONS ("user" 'myremoteuser', password '*****');
```

### Create foreign tables

Establish a view onto data in the foreign system:

```sql
CREATE FOREIGN TABLE remote_readings (
  ts      timestamp,
  device  text,
  value   double
) SERVER my_postgresql
  OPTIONS (
    schema_name 'public',  -- remote schema
    table_name  'readings'
  );
```

::::

## Usage

### Query and debug

You can query these foreign tables like regular user tables:

```sql
SELECT ts, value
FROM   remote_readings
WHERE  device = 'sensor-42';
```

Query clauses like `GROUP BY`, `HAVING`, `LIMIT` or `ORDER BY` are executed
within CrateDB, not within the foreign system. `WHERE` clauses can in some
circumstances be pushed to the foreign system, but that depends on the
concrete foreign data wrapper implementation. You can check if this is the
case by using the {ref}`crate-reference:ref-explain` statement.

For example, in the following explain output there is a dedicated `Filter`
node, indicating that the filter is executed within CrateDB:

```sql
EXPLAIN SELECT ts, value FROM remote_readings WHERE device = 'sensor-42';
```

```text
+--------------------------------------------------------------------------+
| QUERY PLAN                                                               |
+--------------------------------------------------------------------------+
| Filter[(device = 'sensor-42')] (rows=0)                                  |
|   └ ForeignCollect[doc.remote_readings | [device] | true] (rows=unknown) |
+--------------------------------------------------------------------------+
```

### Drop server

```sql
DROP SERVER my_postgresql;
```

You can drop the server once it is no longer used. The clauses available are:

- **IF EXISTS** – the statement won't raise an error if any servers listed
  don't exist.
- **RESTRICT** – raises an error if any foreign table or user mappings for the
  given servers exist. This is the default.
- **CASCADE** – causes `DROP SERVER` to also delete all foreign tables and
  mapped users using the given servers.

:::{seealso}
{ref}`Reference manual <crate-reference:administration-fdw>`

**SQL Functions:**
- {ref}`crate-reference:ref-create-server`
- {ref}`crate-reference:ref-drop-server`
- {ref}`crate-reference:ref-create-foreign-table`
- {ref}`crate-reference:ref-drop-foreign-table`

**System Tables:**
- {ref}`crate-reference:foreign_servers`
- {ref}`crate-reference:foreign_server_options`
- {ref}`crate-reference:foreign_tables`
- {ref}`crate-reference:foreign_table_options`
- {ref}`crate-reference:user_mappings`
- {ref}`crate-reference:user_mapping_options`
:::
