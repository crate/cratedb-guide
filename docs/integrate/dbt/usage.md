(dbt-usage)=

# Using dbt with CrateDB

_Guidelines for transforming data using dbt and CrateDB._

## Introduction

### dbt's Features
The data abstraction layer provided by [dbt][dbt-core] allows the decoupling of
the models on which reports and dashboards rely from the source data. When
business rules or source systems change, you can still maintain the same models
as a stable interface.

Some of the things that dbt can do include:

* Import reference data from CSV files
* Track changes in source data with different strategies so that downstream
  models do not need to be built every time from scratch.
* Run tests on data, to confirm assumptions remain valid, and to validate
  any changes made to the models' logic.

### CrateDB's Benefits
Due to its unique capabilities, CrateDB is an excellent warehouse choice for
data transformation projects. It offers automatic indexing, fast aggregations,
easy partitioning, and the ability to scale horizontally.


## Setup

For running the following steps, you will need connectivity to a CrateDB
cluster, and a Python installation on your workstation. The starting point
will be a fresh installation of `dbt-cratedb2`.

```bash
pip install --upgrade 'dbt-cratedb2'
```

To start a CrateDB instance for evaluation purposes, use Docker or Podman.
```shell
docker run --rm \
  --publish=4200:4200 --publish=5432:5432 \
  --env=CRATE_HEAP_SIZE=2g crate:latest
```

**dbt Profile Configuration:** CrateDB targets should be set up using the
following configuration in your connection profile, e.g. within a
[`profiles.yml`] file at `~/.dbt/profiles.yml`.

Now, create a connection profile `profiles.yaml` file including your
connection details, for example at `~/.dbt/profiles.yml`.
```bash
cd ~
mkdir -p .dbt
cat << EOF > .dbt/profiles.yml
cratedb_analytics:
  target: dev
  outputs:
    dev:
      type: cratedb
      host: localhost
      port: 5432
      user: crate
      pass: crate
      dbname: crate
      schema: doc
      search_path: doc
EOF
```
(please note the values for `database`, `schema`, and `search_path` in this example)

A dbt project has a [specific structure][dbt-project-structure], and contains a combination of SQL, Jinja, YAML, and Markdown files.
In your project folder, alongside the `models` folder that most projects have,
a folder called `macros` can include macro override files.


Those dbt features have been tested successfully:

* models with [view, table, and ephemeral materializations](https://docs.getdbt.com/docs/build/materializations)
* [dbt source freshness](https://docs.getdbt.com/docs/deploy/source-freshness)
* [dbt test](https://docs.getdbt.com/docs/build/tests)
* [dbt seed](https://docs.getdbt.com/docs/build/seeds)
* [Incremental materializations](https://docs.getdbt.com/docs/build/incremental-models) (with `incremental_strategy='delete+insert'` and without involving [OBJECT](https://crate.io/docs/crate/reference/en/5.4/general/ddl/data-types.html#objects) columns)

We hope you find this useful. CrateDB is continuously adding new features and we will endeavor to come back and update this article if there are any developments and some of these overrides require changes or become obsolete.


## Appendix

A few notes about advanced configuration options and general usage
information.

### CrateDB's Differences
- CrateDB’s fixed catalog name is `crate`, the default schema name is `doc`.
- CrateDB does not implement the notion of a database, however tables can be created in different [schemas](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/create-table.html#ddl-create-table-schemas).
- When asked for a database name, specifying a schema name (any), or the fixed catalog name `crate` may be applicable.
- If a database-/schema-name is omitted while connecting, the PostgreSQL drivers may default to the “username”.
- The predefined [superuser](https://cratedb.com/docs/crate/reference/en/latest/admin/user-management.html#administration-user-management) on an unconfigured CrateDB cluster is called `crate`, defined without a password.
- For authenticating properly, please learn about the available [authentication](https://cratedb.com/docs/crate/reference/en/latest/admin/auth/index.html#admin-auth) options.

-- https://cratedb.com/docs/crate/clients-tools/en/latest/connect/#configure

### Connection Options
**dbt Profile Configuration:** CrateDB targets should be set up using the
following configuration in your [`profiles.yml`] file.
```yaml
company-name:
  target: dev
  outputs:
    dev:
      type: cratedb
      host: [clustername].aks1.westeurope.azure.cratedb.net
      user: [username]
      password: [password]
      port: 5432
      dbname: crate  # CrateDB's only catalog is `crate`.
      schema: doc    # You can define any schema. `doc` is the default.
      threads: [optional, 1 or more]
      [keepalives_idle](#keepalives_idle): 0 # default 0, indicating the system default. See below
      connect_timeout: 10 # default 10 seconds
      [retries](#retries): 1  # default 1 retry on error/timeout when opening connections
      [search_path](#search_path): [optional, override the default postgres search_path]
      [role](#role): [optional, set the role dbt assumes when executing queries]
      [sslmode](#sslmode): [optional, set the sslmode used to connect to the database]
      [sslcert](#sslcert): [optional, set the sslcert to control the certifcate file location]
      [sslkey](#sslkey): [optional, set the sslkey to control the location of the private key]
      [sslrootcert](#sslrootcert): [optional, set the sslrootcert config value to a new file path in order to customize the file location that contain root certificates]
```

### Search Path
The `search_path` config controls the CrateDB "search path" that dbt configures
when opening new connections to the database. By default, the CrateDB search
path is `"doc"`, meaning that unqualified <Term id="table" /> names will be
searched for in the `doc` schema.

### Custom Schemas
By default, dbt writes the models into the schema you configured in your
profile, but in some dbt projects you may need to write data into different
target schemas. You can adjust the target schema using [custom schemas with
dbt].

If your dbt project has a custom macro called `generate_schema_name`, dbt
will use it instead of the default macro. This allows you to customize
the name generation according to your needs.

```jinja
{% macro generate_schema_name(custom_schema_name, node) -%}
  {%- set default_schema = target.schema -%}
  {%- if custom_schema_name is none -%}
    {{ default_schema }}
  {%- else -%}
    {{ custom_schema_name | trim }}
  {%- endif -%}
{%- endmacro %}
```


[dbt]: https://www.getdbt.com/
[dbt-core]: https://github.com/dbt-labs/dbt-core
[dbt-project-structure]: https://docs.getdbt.com/guides/best-practices/how-we-structure/1-guide-overview
