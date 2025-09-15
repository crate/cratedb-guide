"""
Airflow example DAG for reporting lineage to Marquez/OpenLineage while ingesting sample data into CrateDB.
"""
from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.providers.postgres.operators.postgres import SQLExecuteQueryOperator

with DAG(
    "lineage-reporting-cratedb",
    start_date=datetime(2024, 6, 28),
    max_active_runs=1,
    schedule="@daily",
    default_args={"retries": 1, "retry_delay": timedelta(minutes=1)},
    catchup=False,
):

    ingest_customers = SQLExecuteQueryOperator(
        task_id="ingest_customers",
        conn_id="cratedb_default",
        sql="""
            INSERT INTO public.Customers (CustomerName,Country)
            SELECT CONCAT(mountain,' Corp.'), country
            FROM sys.summits
            LIMIT 100;
        """,
		inlets=[{'namespace': 'example', 'name': 'sampledata'}],
		outlets=[{'namespace': 'example', 'name': 'customers_table'}]
    )

    ingest_invoices = SQLExecuteQueryOperator(
        task_id="ingest_invoices",
        conn_id="cratedb_default",
        sql="""
            INSERT INTO public.Invoices(date,CustomerID)
            SELECT
                ('2022-01-01'::TIMESTAMP)+concat(floor(random()*1000),' DAYS')::INTERVAL,
                (SELECT CustomerID FROM public.Customers ORDER BY random()+a.b LIMIT 1)
            FROM GENERATE_SERIES(1,1000) a(b);
        """,
		inlets=[{'namespace': 'example', 'name': 'customers_table'}],
		outlets=[{'namespace': 'example', 'name': 'invoices_table'}]
    )

    ingest_products = SQLExecuteQueryOperator(
        task_id="ingest_products",
        conn_id="cratedb_default",
        sql="""
            INSERT INTO public.Products(Description,applicable_tax_percentage)
            SELECT
                CONCAT('Product ',a.b),
                (floor(random()*10)+15)/100.0
            FROM GENERATE_SERIES(1,10) a(b);
        """,
		inlets=[{'namespace': 'example', 'name': 'more_sample_data'}],
		outlets=[{'namespace': 'example', 'name': 'products_table'}]
    )

    ingest_invoice_items = SQLExecuteQueryOperator(
        task_id="ingest_invoice_items",
        conn_id="cratedb_default",
        sql="""
            INSERT INTO public.Invoice_items(InvoiceID,ProductID,quantity,unit_price)
            SELECT InvoiceID, ProductID, 1+ceil(random()*4), random()*1000
            FROM public.Invoices
            INNER JOIN public.Products ON random()>0.5;
        """,
		inlets=[{'namespace': 'example', 'name': 'invoices_table'},{'namespace': 'example', 'name': 'products_table'}],
		outlets=[{'namespace': 'example', 'name': 'invoice_items_table'}]
    )

    refresh_customer_table = SQLExecuteQueryOperator(
        task_id="refresh_customer_table",
        conn_id="cratedb_default",
        sql="REFRESH TABLE public.Customers;",
    )

    refresh_invoices_table = SQLExecuteQueryOperator(
        task_id="refresh_invoices_table",
        conn_id="cratedb_default",
        sql="REFRESH TABLE public.Invoices;",
    )

    refresh_products_table = SQLExecuteQueryOperator(
        task_id="refresh_products_table",
        conn_id="cratedb_default",
        sql="REFRESH TABLE public.Products;",
    )

    ingest_customers >> refresh_customer_table >> ingest_invoices >> refresh_invoices_table
    refresh_invoices_table >> ingest_invoice_items
    ingest_products >> refresh_products_table >> ingest_invoice_items
