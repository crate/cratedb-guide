(start-connect)=
(connect-applications)=
# Applications

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Connect to CrateDB from database shells and IDEs.
:::


(use-admin-ui)=
## CrateDB Admin UI
:::{div}
CrateDB ships with a browser-based administration interface called
[Admin UI].
:::
The Admin UI is enabled on each CrateDB node. You can use it to inspect and
interact with the whole CrateDB cluster in various ways.

If CrateDB is running on your workstation, access the Admin UI using
`http://localhost:4200/`. Otherwise, replace `localhost` with the
hostname CrateDB is running on.

When using CrateDB Cloud, open the Admin UI from the Cloud Console
using the link shown there (port 4200). The URL typically looks like
`https://<cluster-name>.<region>.<provider>.cratedb.net:4200/`, e.g.
`https://testdrive.aks1.westeurope.azure.cratedb.net:4200/`.

![Admin UI SQL console showing a sample SELECT statement](https://cratedb.com/docs/crate/admin-ui/en/latest/_images/console-query.png){width=320px}
![Admin UI navigation and overview panel](/_assets/img/getting-started/first-use/admin-ui.png){width=320px}

:::{note}
If you are running CrateDB on a remote machine, you will have to create
a dedicated user account for accessing the Admin UI. See {ref}`create-user`.
:::


(use-crash)=
## CrateDB Shell

The CrateDB Shell, called `crash`, is an interactive command-line interface
(CLI) program for working with CrateDB on your favorite terminal. To learn more
about it, please refer to its documentation at {ref}`crate-crash:index`.

![crash default screen after executing a query](https://cratedb.com/docs/crate/crash/en/latest/_images/query.png){width=320px}


(cli)=
(connect-cli)=
## Command-line programs

A quick overview about a few CLI programs, and how to
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
### crash

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
### psql

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
### HTTPie

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
### curl

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


(ide)=
(connect-ide)=
## Database IDEs

Mostly through its PostgreSQL interface, CrateDB supports working with popular
database IDE (Integrated Development Environment) applications.

### DataGrip

- {ref}`datagrip`

### DBeaver

- {ref}`dbeaver`



[curl]: https://curl.se/
[crash]: inv:crate-crash:*:label#index
[HTTPie]: https://httpie.io/
[jq]: https://jqlang.github.io/jq/
[psql]: https://www.postgresql.org/docs/current/app-psql.html
