(psycopg2)=

# psycopg2

Psycopg is a popular PostgreSQL database adapter for Python. Its main features
are the complete implementation of the Python DB API 2.0 specification and the
thread safety (several threads can share the same connection).
For more information, see the [psycopg2 documentation].

```python
import psycopg2

conn = psycopg2.connect(host="<name-of-your-cluster>.cratedb.net", port=5432, user="admin", password="<PASSWORD>", sslmode="require")

with conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM sys.summits")
        result = cursor.fetchone()
        print(result)
```


[psycopg2 documentation]: https://www.psycopg.org/docs/
