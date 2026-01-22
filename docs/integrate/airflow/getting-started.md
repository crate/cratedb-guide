(airflow-getting-started)=
# Getting started with Apache Airflow

:::{div} sd-text-muted
Automate CrateDB queries with Apache Airflow.
:::

## Introduction

This guide shows how to use [Apache Airflow] with CrateDB to automate recurring queries.

You will:
- understand [Astronomer], a managed Apache Airflow platform,
- set up a local project with the [Astronomer CLI], and
- schedule and execute recurring queries with simple examples.

:::{rubric} Apache Airflow
:::
Apache Airflow programmatically creates, schedules, and monitors workflows
([Official documentation](https://airflow.apache.org/docs/)). A workflow
is a directed acyclic graph (DAG) where each node represents a task. Each
task runs independently; the DAG tracks dependencies. Run DAGs on demand
or on schedules (for example, twice a week).

:::{rubric} CrateDB
:::
CrateDB is an open-source, distributed database for storing and analyzing
large volumes of data. It offers high scalability, flexibility, and
availability, supports dynamic schemas and queryable objects, and provides
time series features and real-time full-text search over millions of
documents in seconds.

Because CrateDB powers large-scale data workloads, many deployments automate
recurring tasks. Apache Airflow’s resilient, scalable architecture makes it
a strong choice for orchestrating those tasks on CrateDB.

:::{rubric} Astronomer
:::
Since 2014, Apache Airflow and its ecosystem have grown significantly. To run Airflow in production, you need to understand both Airflow and the underlying deployment infrastructure.

To simplify operations, use a managed Apache Airflow provider such as Astronomer. Astronomer runs on Kubernetes, abstracts infrastructure details, and provides a clean interface for building and operating workflows.

::::::{stepper}
## Set up a local Airflow project

The examples use an 8‑core machine with 30 GB RAM on Ubuntu 22.04 LTS. Install the Astronomer CLI (requires [Docker](https://www.docker.com/) 18.09+). On Ubuntu:
```shell
curl -sSL install.astronomer.io | sudo bash -s
```

Verify the installation:
```shell
astro version
```

Example output:

`Astro CLI Version: 1.14.1`

For other operating systems, follow the [official documentation](https://www.astronomer.io/docs/astro/cli/install-cli).
After installing the Astronomer CLI, initialize a new project:

- Create a project directory:
  ```bash
  mkdir astro-project && cd astro-project
  ```
- Initialize the project with the following command:
   ```bash
   astro dev init
   ```
- This will create a skeleton project directory as follows:
   ```text
   ├── Dockerfile
   ├── README.md
   ├── airflow_settings.yaml
   ├── dags
   ├── include
   ├── packages.txt
   ├── plugins
   ├── requirements.txt
   └── tests
   ```

The astronomer project consists of four Docker containers:
- PostgreSQL server (for configuration/runtime data)
- Airflow scheduler
- Web server for rendering Airflow UI
- Triggerer (running an event loop for deferrable tasks)

The PostgreSQL server listens on port 5432. The web server listens on port 8080
and is available at `http://localhost:8080/` with `admin`/`admin`.

If these ports are already in use, change them in `.astro/config.yaml`. For
example, set the webserver to 8081 and PostgreSQL to 5435:
```yaml
project:
  name: astro-project
webserver:
  port: 8081
postgres:
  port: 5435
```

Start the project with `astro dev start`. After the containers start, access
the Airflow UI at `http://localhost:8081`:

![Airflow UI landing page](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/f298a4c609312133e388555a9eba51733bfd5645.png)

The landing page of Apache Airflow UI shows the list of all DAGs, their status, the time of the next and last run, and the metadata such as the owner and schedule. From the UI, you can manually trigger the DAG with the button in the Actions section, manually pause/unpause DAGs with the toggle button near the DAG name, and filter DAGs by tag. If you click on a specific DAG it will show the graph with tasks and dependencies between each task.

## Create a GitHub repository

To track the project with Git, execute from the `astro-project` directory: `git init`.

Go to [https://github.com](https://github.com) and create a new repository.
Add files that store sensitive information (for example, credentials and
environment variables) to `.gitignore`, such as:
```text
.env
airflow_settings.yaml
**/secrets.*
```

Then publish `astro-project` to GitHub:

```bash
git remote add origin https://github.com/username/new_repo
git push -u origin main
```
The initialized `astro-project` now has a home on GitHub.

## Add database credentials

To configure the CrateDB connection, set an environment variable. On
Astronomer, set it via the UI, `Dockerfile`, or the `.env` file
(generated during initialization).

In this guide, you will set up the necessary environment variables via a `.env`
file. To learn about alternative ways, please check the
[Astronomer Environment variables documentation].
The first variable to define is one for the CrateDB connection, as follows:

`AIRFLOW_CONN_CRATEDB_CONNECTION=postgresql://<user>:<password>@<host>/?sslmode=disable`

For TLS, set `sslmode=require`. To confirm that the variable is applied, start
the project and open a bash session in the scheduler container:
`docker exec -it <scheduler_container_name> /bin/bash`.

Run `env` to list the applied environment variables.

This will output some variables set by Astronomer by default including the variable for the CrateDB connection.
::::::

[Apache Airflow]: https://airflow.apache.org/
[Astronomer]: https://www.astronomer.io/
[Astronomer CLI]: https://docs.astronomer.io/astro/cli/overview
[Astronomer Environment variables documentation]: https://docs.astronomer.io/astro/environment-variables
