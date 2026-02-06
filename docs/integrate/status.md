---
orphan: true
---

(build-status)=

# Build Status

The build status of relevant drivers, applications, and integrations
for CrateDB, on one page.

<style>
table td, table td * {
  vertical-align: top;
}
th, td {
  padding-right: 1em;
  padding-left: 1em;
}
/*
In `crate-docs-theme`, `src/crate/theme/rtd/crate/static/css/custom.css`
defines a style we don't want to apply here, specifically on `connect/index`.
*/
.wrapper-content-right .section img {
  margin-bottom: unset !important;
}
</style>


## Integrations

End-to-end QA integration tests against CrateDB Nightly,
on behalf of [cratedb-examples] and [academy-fundamentals-course].

<table>
<tbody>

<tr>
<td>
<b>Application</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-apache-superset.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-apache-superset.yml?branch=main&label=Apache Superset" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-cratedb-toolkit.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-cratedb-toolkit.yml?branch=main&label=CrateDB Toolkit" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-ingestr.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-ingestr.yml?branch=main&label=Ingestr" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/application-metabase.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/application-metabase.yml?branch=main&label=Metabase" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Dataframe</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/dataframe-dask.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-dask.yml?branch=main&label=Dask" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/dataframe-pandas.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-pandas.yml?branch=main&label=pandas" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/dataframe-polars.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/dataframe-polars.yml?branch=main&label=Polars" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Framework</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-flink-kafka-java.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-flink-kafka-java.yml?branch=main&label=Apache%20Kafka,%20Apache%20Flink" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-dbt.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-dbt.yml?branch=main&label=dbt" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-dlt.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-dlt.yml?branch=main&label=dlt" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-gradio.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-gradio.yml?branch=main&label=Gradio" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-mcp.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-mcp.yml?branch=main&label=MCP" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/framework-streamlit.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/framework-streamlit.yml?branch=main&label=Streamlit" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Language</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-npgsql.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-csharp-npgsql.yml?branch=main&label=C%23 Npgsql" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-csharp-efcore.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-csharp-efcore.yml?branch=main&label=C%23 EF Core" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-elixir-postgrex.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-elixir-postgrex.yml?branch=main&label=Elixir Postgrex" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-go-pgx.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-go-pgx.yml?branch=main&label=Go pgx" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-java-maven.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-java-maven.yml?branch=main&label=Java JDBC" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-java-jooq.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-java-jooq.yml?branch=main&label=Java jOOQ" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-php-amphp.yml?branch=main&label=PHP AMPHP" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-php-pdo.yml?branch=main&label=PHP PDO" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-python-dbapi.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-python-dbapi.yml?branch=main&label=Python DB API" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-python-sqlalchemy.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-python-sqlalchemy.yml?branch=main&label=Python SQLAlchemy" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-python-connectorx.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-python-connectorx.yml?branch=main&label=Python ConnectorX" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-python-turbodbc.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-python-turbodbc.yml?branch=main&label=Python turbodbc" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-r.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-r.yml?branch=main&label=R" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-ruby.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-ruby.yml?branch=main&label=Ruby" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/lang-rust-postgres.yml" target="_blank">
      <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/lang-rust-postgres.yml?branch=main&label=Rust postgres" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Testing</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/testing-testcontainers-java.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/testing-testcontainers-java.yml?branch=main&label=Testcontainers for Java" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/testing-testcontainers-python.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/testing-testcontainers-python.yml?branch=main&label=Testcontainers for Python" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/testing-native-python.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/testing-native-python.yml?branch=main&label=Native testing for Python" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Topic</b>
</td>
<td>
<div>
<b>Academy</b>
<br>
<a href="https://github.com/crate/academy-fundamentals-course/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/academy-fundamentals-course/tests.yml?branch=main&label=Fundamentals Course" loading="lazy"></a>
</div>
<div>
<b>Machine Learning</b>
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-langchain.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-langchain.yml?branch=main&label=LangChain" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-llamaindex.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-llamaindex.yml?branch=main&label=LlamaIndex" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-mlflow.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-mlflow.yml?branch=main&label=MLflow" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-pycaret.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-pycaret.yml?branch=main&label=PyCaret" loading="lazy"></a>
</div>
<div>
<b>Time Series</b>
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/timeseries.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/timeseries.yml?branch=main&label=Time%20Series" loading="lazy"></a>
</div>
</td>
</tr>

</tbody>
</table>


## Applications, Connectors, SDKs

CI outcomes for a range of applications, connectors, and libraries connecting
to CrateDB.

<table>
<tbody>

<tr>
<td>
<b>CLI / UI</b>
</td>
<td>
<a href="https://github.com/crate/crate-admin/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-admin/tests.yml?branch=main&label=CrateDB Admin UI" loading="lazy"></a>
<a href="https://github.com/crate/crash/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crash/main.yml?branch=master&label=Crash CLI" loading="lazy"></a>
<a href="https://github.com/crate/croud/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/croud/main.yml?branch=master&label=Croud CLI" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-mcp/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-mcp/tests.yml?branch=main&label=CrateDB MCP" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Connector</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-airflow-tutorial/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-airflow-tutorial/main.yml?branch=main&label=Airflow" loading="lazy"></a>
<a href="https://github.com/crate/dbt-cratedb2/actions/workflows/integration-tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/dbt-cratedb2/integration-tests.yml?branch=main&label=dbt" loading="lazy"></a>
<a href="https://github.com/surister/cratedb-django/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/surister/cratedb-django/tests.yml?branch=master&label=Django" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-estuary">
    <img src="https://img.shields.io/badge/Estuary-passing-success" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-fivetran-destination/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-fivetran-destination/tests.yml?branch=main&label=Fivetran" loading="lazy"></a>
<a href="https://github.com/crate/langchain-cratedb/actions/workflows/ci.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/langchain-cratedb/ci.yml?branch=main&label=LangChain" loading="lazy"></a>
<a href="https://github.com/crate/mlflow-cratedb/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/mlflow-cratedb/main.yml?branch=main&label=MLflow" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-tableau-connector/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-tableau-connector/main.yml?branch=main&label=Tableau" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Documentation</b>
</td>
<td>
<a href="https://github.com/crate/about/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/about/tests.yml?branch=main&label=About CrateDB" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Metrics</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-prometheus-adapter/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-prometheus-adapter/tests.yml?branch=main&label=CrateDB Prometheus Adapter" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Operations</b>
</td>
<td>
<a href="https://github.com/crate/crate-operator/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-operator/main.yaml?branch=master&label=CrateDB Kubernetes Operator" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>SDK</b>
</td>
<td>
<a href="https://github.com/crate/cratedb-sqlparse/actions/workflows/python.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-sqlparse/python.yml?branch=main&label=cratedb-sqlparse (python)" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-sqlparse/actions/workflows/javascript.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-sqlparse/javascript.yml?branch=main&label=cratedb-sqlparse (javascript)" loading="lazy"></a>
<br>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/main.yml?branch=main&label=CrateDB Toolkit" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/dynamodb.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/dynamodb.yml?branch=main&label=CTK%2BDynamoDB" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/influxdb.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/influxdb.yml?branch=main&label=CTK%2BInfluxDB" loading="lazy"></a>
<a href="https://github.com/crate/cratedb-toolkit/actions/workflows/mongodb.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-toolkit/mongodb.yml?branch=main&label=CTK%2BMongoDB" loading="lazy"></a>
</td>
</tr>

<tr>
<td>
<b>Testing</b>
</td>
<td>
<a href="https://github.com/crate/crate-java-testing/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-java-testing/tests.yml?branch=master&label=crate-java-testing" loading="lazy"></a>
<a href="https://github.com/crate/pytest-cratedb/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/pytest-cratedb/tests.yml?branch=main&label=pytest-cratedb" loading="lazy"></a>
</td>
</tr>

</tbody>
</table>


## Drivers

CI outcomes for a range of client drivers connecting your applications to CrateDB.

### CrateDB
Adapters, drivers, dialects, and support utilities maintained by CrateDB.

<a href="https://github.com/crate/crate-python/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-python/tests.yml?branch=main&label=crate-python" loading="lazy"></a>
<a href="https://github.com/crate/sqlalchemy-cratedb/actions/workflows/nightly.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/sqlalchemy-cratedb/nightly.yml?branch=main&label=sqlalchemy-cratedb" loading="lazy"></a>
<a href="https://github.com/crate/micropython-cratedb/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/micropython-cratedb/tests.yml?branch=main&label=micropython-cratedb" loading="lazy"></a>
<br>
<a href="https://github.com/crate/crate-pdo/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-pdo/tests.yml?branch=main&label=crate-pdo" loading="lazy"></a>
<a href="https://github.com/crate/crate-dbal/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate-dbal/tests.yml?branch=main&label=crate-dbal" loading="lazy"></a>
<a href="https://github.com/crate/crate_ruby/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/crate_ruby/tests.yml?branch=main&label=crate_ruby" loading="lazy"></a>
<a href="https://github.com/crate/activerecord-crate-adapter/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/activerecord-crate-adapter/tests.yml?branch=main&label=activerecord-crate-adapter" loading="lazy"></a>

<br>
<br>

### PostgreSQL
Standard PostgreSQL drivers for different languages.

<a href="https://github.com/pgjdbc/pgjdbc/actions/workflows/main.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/pgjdbc/pgjdbc/main.yml?branch=master&label=pgjdbc" loading="lazy"></a>
<a href="https://github.com/npgsql/npgsql/actions/workflows/build.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/npgsql/npgsql/build.yml?branch=main&label=npgsql" loading="lazy"></a>
<a href="https://github.com/psycopg/psycopg2/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/psycopg/psycopg2/tests.yml?branch=master&label=psycopg2" loading="lazy"></a>
<a href="https://github.com/psycopg/psycopg/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/psycopg/psycopg/tests.yml?branch=master&label=psycopg3" loading="lazy"></a>
<a href="https://github.com/MagicStack/asyncpg/actions/workflows/tests.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/MagicStack/asyncpg/tests.yml?branch=master&label=asyncpg" loading="lazy"></a>
<a href="https://github.com/brianc/node-postgres/actions/workflows/ci.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/brianc/node-postgres/ci.yml?branch=master&label=node-postgres" loading="lazy"></a>

<br><br>


```{note}
Please note that the designated status of drivers maintained by community
authors and other maintainers reflect the build status of the development
head. It does not mean integration with GA releases isn't stable. This is
reflected within the topmost section of this page.
```


[academy-fundamentals-course]: https://github.com/crate/academy-fundamentals-course
[cratedb-examples]: https://github.com/crate/cratedb-examples
