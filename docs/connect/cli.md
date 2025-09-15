(cli)=
(connect-cli)=
# Using command-line programs with CrateDB

This section provides a quick overview about a few CLI programs, and how to
use them for connecting to CrateDB clusters. We recommend to use crash,
psql, http ([HTTPie]), or curl.

You can use them to quickly validate HTTP and PostgreSQL connectivity to your
database cluster, or to conduct basic scripting.

Before running the command-line snippets outlined below, please use the correct
settings instead of the placeholder tokens `<hostname>`, `<username>` and
`<password>`.

When using CrateDB Cloud, `<hostname>` will be something like
`<clustername>.{aks1,eks1}.region.{azure,aws}.cratedb.net`.


(crash)=
## crash

```{div}
:style: "float: right"
![image](https://cratedb.com/docs/crate/crash/en/latest/_images/query.png){w=240px}
```

The **CrateDB Shell** is an interactive command-line interface (CLI) tool for
working with CrateDB. For more information, see the documentation about [crash].

```{div}
:style: "clear: both"
```

::::{tab-set}

:::{tab-item} CrateDB and CrateDB Cloud
:sync: server

```{code-block} shell
CRATEPW=<password> \
    crash --hosts 'https://<hostname>:4200' --username '<username>' \
    --command "SELECT 42.42;"
```
:::

:::{tab-item} CrateDB on localhost
:sync: localhost

```{code-block} shell
# No authentication. 
crash --command "SELECT 42.42;"
 
```
:::

::::


(psql)=
## psql

```{div}
:style: "float: right"
![image](https://github.com/crate/crate-clients-tools/assets/453543/8f0a0e06-87f6-467f-be2d-b38121afbafa){w=240px}
```

**psql** is a terminal-based front-end to PostgreSQL. It enables you to type in
queries interactively, issue them to PostgreSQL, and see the query results.
For more information, see the documentation about [psql].

```{div}
:style: "clear: both"
```

::::{tab-set}

:::{tab-item} CrateDB and CrateDB Cloud
:sync: server

```{code-block} shell
PGUSER=<username> PGPASSWORD=<password> \
    psql postgresql://<hostname>/crate --command "SELECT 42.42;"
```
:::

:::{tab-item} CrateDB on localhost
:sync: localhost

```{code-block} shell
# No authentication.
psql postgresql://crate@localhost:5432/crate --command "SELECT 42.42;"
```
:::

::::


(httpie)=
## HTTPie

```{div}
:style: "float: right"
![image](https://github.com/crate/crate-clients-tools/assets/453543/f5a2916d-3730-4901-99cf-b88b9af03329){w=240px}
```

The **HTTPie CLI** is a modern, user-friendly command-line HTTP client with
JSON support, colors, sessions, downloads, plugins & more. 
For more information, see the documentation about [HTTPie].

```{div}
:style: "clear: both"
```

::::{tab-set}

:::{tab-item} CrateDB and CrateDB Cloud
:sync: server

```{code-block} shell
http "https://<username>:<password>@<hostname>:4200/_sql?pretty" \
    stmt="SELECT 42.42;"
```
:::

:::{tab-item} CrateDB on localhost
:sync: localhost

```{code-block} shell
http "localhost:4200/_sql?pretty" \
    stmt="SELECT 42.42;"
```
:::

::::


(curl)=
## curl

```{div}
:style: "float: right"
![image](https://github.com/crate/crate-clients-tools/assets/453543/318b0819-a0d4-4112-a320-23852263362c){w=240px}
```

The venerable **curl** is the ubiquitous command line tool and library for transferring
data with URLs. For more information, see the documentation about [curl].

This example combines it with [jq], a lightweight and flexible command-line JSON processor.

```{div}
:style: "clear: both"
```

::::{tab-set}

:::{tab-item} CrateDB and CrateDB Cloud
:sync: server

```{code-block} shell
echo '{"stmt": "SELECT 42.42;"}' \
    | curl "https://<username>:<password>@<hostname>:4200/_sql?pretty" --silent --data @- | jq
```
:::

:::{tab-item} CrateDB on localhost
:sync: localhost

```{code-block} shell
echo '{"stmt": "SELECT 42.42;"}' \
    | curl "localhost:4200/_sql?pretty" --silent --data @- | jq
```
:::

::::



[curl]: https://curl.se/
[crash]: inv:crate-crash:*:label#index
[HTTPie]: https://httpie.io/
[jq]: https://jqlang.github.io/jq/
[psql]: https://www.postgresql.org/docs/current/app-psql.html
