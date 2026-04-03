(fdw)=

# Foreign data wrappers

:::{div} sd-text-muted
Access PostgreSQL database tables on remote servers as if they were stored
within CrateDB and perform read-only queries on the data.
:::

## Prerequisites

This guide walks you through setting up and querying foreign data wrappers.
Before configuring a foreign data wrapper (FDW), you should have CrateDB and
PostgreSQL instances up and running, or other services that speak the
PostgreSQL wire protocol.
Please note that FDW in CrateDB is available with version 5.7 and above.

## Set up

::::{stepper}

### Set firewall rules

Ensure outbound firewall rules allow CrateDB → remote DB traffic before
proceeding with the following steps. The default PostgreSQL port is 5432.

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

### Create foreign table

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

## Example

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/application/roapi
:link-type: url
{material-regular}`play_arrow;2em`
Integrating ROAPI data sources with CrateDB.
+++
Demonstrates how to mount ROAPI data sources as tables in CrateDB
using the PostgreSQL foreign data wrapper.
:::

:::{seealso}
**Reference manual:** {ref}`Foreign data wrappers <crate-reference:administration-fdw>`
<br>
**SQL Functions:**
{ref}`crate-reference:ref-create-server`
• {ref}`crate-reference:ref-drop-server`
• {ref}`crate-reference:ref-create-foreign-table`
• {ref}`crate-reference:ref-drop-foreign-table`
<br>
**System Tables:**
{ref}`crate-reference:foreign_servers`
• {ref}`crate-reference:foreign_server_options`
• {ref}`crate-reference:foreign_tables`
• {ref}`crate-reference:foreign_table_options`
• {ref}`crate-reference:user_mappings`
• {ref}`crate-reference:user_mapping_options`
:::
