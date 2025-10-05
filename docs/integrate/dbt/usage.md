(dbt-usage)=
# Using dbt with CrateDB

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Setup instructions and guidelines for transforming data using dbt and CrateDB.
:::

:::{div}
For running the following steps, you will need connectivity to a CrateDB
cluster, and a Python installation on your workstation. You can use
[CrateDB Self-Managed] or [CrateDB Cloud].
:::

## Setup

To start a CrateDB instance for evaluation purposes, use Docker or Podman.
```shell
docker run --rm --publish=4200:4200 --publish=5432:5432 --env=CRATE_HEAP_SIZE=2g crate:latest
```

Install the most recent version of the [dbt-cratedb2] Python package.
```shell
pip install --upgrade 'dbt-cratedb2'
```
:::{note}
dbt-cratedb2 is based on dbt-postgres, which uses [psycopg2] to connect to
the database server.
:::

## Configure
A minimal set of **dbt profile configuration** options, for example within a
[`profiles.yml`] file at `~/.dbt/profiles.yml`.
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
Please note the values for `dbname`, `schema`, and `search_path` in this example.

## Project
When working with dbt, you are working on behalf of a dbt project.
A dbt project has a [specific structure][dbt-project-structure], and contains a
combination of SQL, Jinja, YAML, and Markdown files.
In your project folder, alongside the `models` folder that most projects have,
a folder called `macros` can include macro override files.

At [cratedb-examples » framework/dbt], you can explore a few ready-to-run dbt
projects that demonstrate usage with CrateDB.

## Appendix

A few notes about advanced configuration options and general usage
information.

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

### Full Connection Options
CrateDB targets should be set up using the following **dbt profile configuration** in
your [`profiles.yml`] file, which is identical to the [setup options of dbt-postgres].
```yaml
cratedb_analytics:
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
      [keepalives_idle]: 0 # default 0, indicating the system default.
      connect_timeout: 10 # default 10 seconds
      [retries]: 1  # default 1 retry on error/timeout when opening connections
      [search_path]: # optional, override the default postgres `search_path`
      [role]: # optional, set the role dbt assumes when executing queries
      [sslmode]: # optional, set the `sslmode` used to connect to the database
      [sslcert]: # optional, set the `sslcert` to control the certificate file location
      [sslkey]: # optional, set the `sslkey` to control the location of the private key
      [sslrootcert]: # optional, set the `sslrootcert` config value to a new file path
                     # in order to customize the file location that contain root certificates
```


## Notes

### CrateDB's Differences
- CrateDB’s fixed catalog name is `crate`, the default schema name is `doc`.
- CrateDB does not implement the notion of a database, however tables can be created in different [schemas](https://cratedb.com/docs/crate/reference/en/latest/general/ddl/create-table.html#ddl-create-table-schemas).
- When asked for a database name, specifying a schema name (any), or the fixed catalog name `crate` may be applicable.
- If a database/schema name is omitted while connecting, the PostgreSQL drivers may default to the “username”.
- The predefined [superuser](https://cratedb.com/docs/crate/reference/en/latest/admin/user-management.html#administration-user-management) on an unconfigured CrateDB cluster is called `crate`, defined without a password.
- For authenticating properly, please learn about the available [authentication](https://cratedb.com/docs/crate/reference/en/latest/admin/auth/index.html#admin-auth) options.

### Feature Coverage
Those dbt features have been tested successfully with CrateDB.

* [Model materializations](https://docs.getdbt.com/docs/build/materializations):
  table, view, incremental, ephemeral
* [Incremental models](https://docs.getdbt.com/docs/build/incremental-models-overview)
* [Source data freshness](https://docs.getdbt.com/docs/build/sources#source-data-freshness)
* [CSV seeds](https://docs.getdbt.com/docs/build/seeds)
* [Data tests](https://docs.getdbt.com/docs/build/tests)

### Caveats
- Model materializations using the "materialized view" strategy are
  not supported yet.
- Incremental materializations with CrateDB currently only support the
  `delete+insert` strategy.
- Incremental materializations do not support columns using the
  {ref}`OBJECT <crate-reference:data-types-objects>` data type yet.


:::{note}
CrateDB is continuously adding new features and we will endeavor to come
back and update this article if there are any updates or improvements.
We are tracking interoperability issues per [Tool: dbt], and appreciate
any contributions and reports.
:::


[cratedb-examples » framework/dbt]: https://github.com/crate/cratedb-examples/tree/main/framework/dbt/
[custom schemas with dbt]: https://docs.getdbt.com/docs/build/custom-schemas
[dbt]: https://www.getdbt.com/
[dbt-cratedb2]: https://pypi.org/project/dbt-cratedb2/
[dbt-project-structure]: https://docs.getdbt.com/guides/best-practices/how-we-structure/1-guide-overview
[`profiles.yml`]: https://docs.getdbt.com/docs/core/connect-data-platform/profiles.yml
[psycopg2]: https://pypi.org/project/psycopg2/
[setup options of dbt-postgres]: https://docs.getdbt.com/docs/core/connect-data-platform/postgres-setup
[Tool: dbt]: https://github.com/crate/crate/labels/tool%3A%20dbt
