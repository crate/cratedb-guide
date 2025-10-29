(psycopg3)=

# psycopg3

[Psycopg 3] is a newly designed PostgreSQL database adapter for the Python
programming language. Psycopg 3 presents a familiar interface for everyone who
has used Psycopg 2 or any other DB-API 2.0 database adapter, but allows to use
more modern PostgreSQL and Python features, such as:

- Asynchronous support
- COPY support from Python objects
- A redesigned connection pool
- Support for static typing
- Server-side parameters binding
- Prepared statements
- Statements pipeline
- Binary communication
- Direct access to the libpq functionalities

```python
import psycopg

with psycopg.connect("postgres://crate@localhost:5432/doc") as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM sys.summits")
        for record in cursor:
            print(record)
```


[psycopg 3]: https://www.psycopg.org/psycopg3/docs/
