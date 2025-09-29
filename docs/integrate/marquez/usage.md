(marquez-usage)=
# Use Marquez with CrateDB

This usage guide demonstrates how to run Airflow DAGs against a
CrateDB database and view lineage data.

## Setup

We will need Docker Compose v2. To install it, make it available to all users,
check the installed version, or upgrade from v1, refer to
[the Docker documentation](https://docs.docker.com/compose/migrate/).

Let's now start Marquez:

```bash
git clone https://github.com/MarquezProject/marquez && cd marquez
sudo ./docker/up.sh
```

While Marquez starts, let's open another terminal and proceed installing the Astro CLI for Airflow:

```bash
curl -sSL https://install.astronomer.io | sudo bash -s
```

Let's initialize a project folder:

```bash
mkdir datalineageeval
cd datalineageeval
astro dev init
```

We will use the PostgreSQL wire protocol to connect to CrateDB:

```bash
echo 'apache-airflow-providers-postgres' >> requirements.txt
```

Let's now configure Airflow to use Marquez as the lineage repository and connect to it via the Docker bridge interface:

```bash
cat <<EOF >>.env
# Linux (Docker bridge):
OPENLINEAGE_URL=http://172.17.0.1:5000
# macOS/Windows (Docker Desktop):
# OPENLINEAGE_URL=http://host.docker.internal:5000
OPENLINEAGE_NAMESPACE=example
EOF
```

We will use the Airflow web interface. If you are running headless (no local browser), enable port exposure:

```bash
astro config set airflow.expose_port true
``` 

Astro also needs an internal PostgreSQL instance, but port 5432 is taken by Marquez's own internal database, so we will configure Astro to use port 5435 for its internal database:

```bash
astro config set postgres.port 5435
astro dev start
```

And we will start a single-node local CrateDB instance using port 5436 for the PostgreSQL wire protocol interface:

```bash
sudo docker run -d --name cratedb --publish=4200:4200 --publish=5436:5432 --env CRATE_HEAP_SIZE=1g crate/crate:5.9.5 -Cdiscovery.type=single-node
```

(NB this will return immediately once the image is downloaded but CrateDB may take a few seconds to start)


Let's now use the CrateDB CLI to prepare the tables we will use for this example:

Install `crash` using `pip`.
```bash
sudo apt install -y python3-pip
sudo pip3 install --user crash
crash
```

Alternatively, install `crash` using `pipx`.
```bash
sudo apt install -y pipx
sudo pipx install crash
```

Connect using `crash`.
```bash
crash
```

```sql
CREATE TABLE public.Customers (
  CustomerID TEXT PRIMARY KEY NOT NULL DEFAULT gen_random_text_uuid(),
  CustomerName TEXT NOT NULL,
  Country TEXT
);

CREATE TABLE public.Invoices (
  InvoiceID TEXT PRIMARY KEY NOT NULL DEFAULT gen_random_text_uuid(),
  date TIMESTAMP DEFAULT now(),
  CustomerID TEXT
);

CREATE TABLE public.Products (
  ProductID TEXT PRIMARY KEY NOT NULL DEFAULT gen_random_text_uuid(),
  Description TEXT,
  applicable_tax_percentage REAL
);

CREATE TABLE public.Invoice_items (
  InvoiceID TEXT,
  ProductID TEXT,
  quantity SMALLINT,
  unit_price REAL,
  PRIMARY KEY (InvoiceID,ProductID)
);
```

Now press Ctrl+D to exit the CrateDB Shell.

## Usage

We are now going to configure Airflow to connect to CrateDB.

Open a web browser and navigate to port 8080 on the machine where you are running Astro, for instance `http://localhost:8080/`.
Login with username `admin` and password `admin`.

Under "Admin" select "Connections".
Click the blue plus sign button to create a new connection and enter the following details:

```text
Connection Id: cratedb_default
Connection Type: Postgres
Host: 172.17.0.1
Login: crate
Port: 5436
```

Click the Save button.

Now we will create a DAG. From the `datalineageeval` folder, run:
```bash
cp data_ingestion.py dags/
```

Then, restart Airflow.
```bash
sudo astro dev restart
```

Let's now go back to the Airflow web interface, navigate to "DAGs" on the top left corner, then identify the new `lineage-reporting-cratedb` DAG and use the "play" button to execute it.

When the DAG completes, "Recent Tasks" should show 7 successful tasks.

Now navigate to the Marquez web interface at <http://localhost:3000/> (replace localhost if this is not running locally).

In the upper right corner, select `example` instead of `default`.

You can now see all lineage graphs and events for this setup.

![Marquez lineage graph](/_assets/img/integrations/marquez/marquez-lineage.png){h=180px}
