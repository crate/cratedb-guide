(use)=
(getting-started)=

# Getting Started


{#introduction}
## Introduction

Once CrateDB is [installed and running](#install), you can start to interact
with the database for the first time.


{#use-admin-ui}
### The Admin UI

CrateDB ships with a browser-based administration interface called
[Admin UI](inv:crate-admin-ui:*:label#index).
It is enabled on each CrateDB node, you can use it to inspect and
interact with the whole CrateDB cluster in a number of ways.

If CrateDB is running on your workstation, access the Admin UI using
`http://localhost:4200/`. Otherwise, replace `localhost` with the
hostname CrateDB is running on.

When using CrateDB Cloud, the URL will look like
`https://testdrive.aks1.westeurope.azure.cratedb.net:4200/`.

![image](https://cratedb.com/docs/crate/admin-ui/en/latest/_images/console-query.png){width=320px}
![image](/_assets/img/getting-started/first-use/admin-ui.png){width=320px}

:::{note}
If you are running CrateDB on a remote machine, you will have to create
a dedicated user account for accessing the Admin UI. See [](#create-user).
:::


{#use-crash}
### The CrateDB Shell

The CrateDB Shell, called `crash`, is an interactive command-line interface
(CLI) program for working with CrateDB on your favorite terminal. To learn more
about it, please refer to its documentation at [](inv:crate-crash:*:label#index).

![image](https://cratedb.com/docs/crate/crash/en/latest/_images/query.png){width=320px}


{#use-dive-in}
{#use-start-building}
## How to Connect
There is a dedicated page which enumerates all the connectivity options.

- {ref}`connect`


:::{tip}
To learn more about all the details of CrateDB features, operations, and
its SQL dialect, please also visit the [CrateDB Reference Manual].
:::


[CrateDB Cloud]: inv:cloud:*:label#index
[CrateDB Reference Manual]: inv:crate-reference:*:label#index
