(start-connect)=
# Connect to CrateDB

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Start to interact with the database for the first time.
:::


(use-admin-ui)=
## Admin UI
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


(use-drivers)=
## Adapters and drivers
:::{div}
- To learn how to connect to CrateDB using software drivers, see {ref}`connect`.

- To learn more about all the details of CrateDB features, operations, and
  its SQL dialect, please also visit the [CrateDB Reference Manual].
:::
