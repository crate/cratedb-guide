(airflow-getting-started)=
# Getting started with Apache Airflow

:::{div} sd-text-muted
Automate CrateDB queries with Apache Airflow.
:::

## Introduction

This first article shows how to use [Apache Airflow] with CrateDB to automate recurring queries.

Then, we cover [Astronomer], the managed Apache Airflow provider, followed
by instructions on how to set up the project with [Astronomer CLI].
Finally, we illustrate with relatively simple examples how to schedule and
execute recurring queries.

:::{rubric} Apache Airflow
:::
Apache Airflow is a platform for programmatically creating, scheduling, and monitoring workflows \[[Official documentation](https://airflow.apache.org/docs/)\]. Workflows are defined as directed acyclic graphs (DAGs) where each node in DAG represents an execution task. It is worth mentioning that each task is executed independently of other tasks and the purpose of DAG is to track the relationships between tasks. DAGs are designed to run on demand and in data intervals (e.g., twice a week).

:::{rubric} CrateDB
:::
CrateDB is an open-source distributed database that makes storage and analysis of massive amounts of data simple and efficient. CrateDB offers a high degree of scalability, flexibility, and availability. It supports dynamic schemas, queryable objects, time-series data support, and real-time full-text search over millions of documents in just a few seconds.

As CrateDB is designed to store and analyze massive amounts of data, continuous use of such data is a crucial task in many production applications of CrateDB. Needless to say, Apache Airflow is one of the most heavily used tools for the automation of big data pipelines. It has a very resilient architecture and scalable design. This makes Airflow an excellent tool for the automation of recurring tasks that run on CrateDB.

:::{rubric} Astronomer
:::
Since its inception in 2014, the complexity of Apache Airflow and its features has grown significantly. To run Airflow in production, it is no longer sufficient to know only Airflow, but also the underlying infrastructure used for Airflow deployment.

To help maintain complex environments, one can use managed Apache Airflow providers such as Astronomer. Astronomer is one of the main managed providers that allows users to easily run and monitor Apache Airflow deployments. It runs on Kubernetes, abstracts all underlying infrastructure details, and provides a clean interface for constructing and managing different workflows.

## Setting up an Airflow project
We set up a new Airflow project on an 8-core machine with 30GB RAM running Ubuntu 22.04 LTS. To initialize the project we use Astronomer CLI. The installation process requires [Docker](https://www.docker.com/) version 18.09 or higher. To install the latest version of the Astronomer CLI on Ubuntu, run:

`curl -sSL install.astronomer.io | sudo bash -s`

To make sure that you installed Astronomer CLI on your machine, run:

`astro version`

If the installation was successful, you will see the output similar to:

`Astro CLI Version: 1.14.1`

To install Astronomer CLI on another operating system, follow the [official documentation](https://www.astronomer.io/docs/astro/cli/install-cli).
After the successful installation of Astronomer CLI, create and initialize the new project as follows:

* Create project directory:
  ```bash
  mkdir astro-project && cd astro-project
  ```
* Initialize the project with the following command:  
   ```bash
   astro dev init
   ```
* This will create a skeleton project directory as follows:
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
*   PostgreSQL server (for configuration/runtime data)
*   Airflow scheduler
*   Web server for rendering Airflow UI
*  Triggerer (running an event loop for deferrable tasks)

The PostgreSQL server is configured to listen on port 5432. The web server is listening on port 8080 and can be accessed via http://localhost:8080/ with `admin` for both username and password.

In case these ports are already occupied you can change them in the file `.astro/config.yaml` inside the project folder. In our case we changed the web server port to 8081 and `postgres` port to 5435:
```yaml
project:
  name: astro-project
webserver:
  port: 8081
postgres:
  port: 5435
```

To start the project, run `astro dev start`. After Docker containers are spun up, access the Airflow UI at `http://localhost:8081` as illustrated:

![Screenshot 2021-11-10 at 14.05.15|690x242](https://us1.discourse-cdn.com/flex020/uploads/crate/original/1X/f298a4c609312133e388555a9eba51733bfd5645.png)

The landing page of Apache Airflow UI shows the list of all DAGs, their status, the time of the next and last run, and the metadata such as the owner and schedule. From the UI, you can manually trigger the DAG with the button in the Actions section, manually pause/unpause DAGs with the toggle button near the DAG name, and filter DAGs by tag. If you click on a specific DAG it will show the graph with tasks and dependencies between each task.

## Create a GitHub repository

To track the project with Git, execute from the `astro-project` directory: `git init`.

Go to [http://github.com](http://github.com) and create a new repository. The files that store sensitive information, such as credentials and environment variables should be added to `.gitignore`. Now, use the following instructions to publish `astro-project` to GitHub:

```bash
git remote add origin https://github.com/username/new_repo
git push -u origin main
```
The initialized `astro-project` now has a home on GitHub.

## Add database credentials

To configure the connection to CrateDB we need to set up a corresponding environment variable. On Astronomer the environment variable can be set up via the Astronomer UI, via `Dockerfile`, or via a `.env` file which is automatically generated during project initialization.

In this tutorial, we will set up the necessary environment variables via a `.env` file. To learn about alternative ways, please check the [Astronomer documentation](https://docs.astronomer.io/astro/environment-variables). The first variable we set is one for the CrateDB connection, as follows:

`AIRFLOW_CONN_CRATEDB_CONNECTION=postgresql://<CrateDB user name>:<CrateDB user password>@<CrateDB host>/doc?sslmode=disable`

In case a TLS connection is required, change `sslmode=require`. To confirm that a new variable is applied, first, start the Airflow project and then create a bash session in the scheduler container by running `docker exec -it <scheduler_container_name> /bin/bash`.

To check all environment variables that are applied, run `env`.

This will output some variables set by Astronomer by default including the variable for the CrateDB connection.


[Apache Airflow]: https://airflow.apache.org/
[Astronomer]: https://www.astronomer.io/
[Astronomer CLI]: https://docs.astronomer.io/astro/cli/overview
