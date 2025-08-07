# Create table schema

In CrateDB you can create a table within a schema like
```sql
CREATE TABLE schema_name.table_name;
```

Also, you can grant rights like so on a schema (even if it doesn’t explicitly exist yet):
```sql
GRANT DQL ON SCHEMA schema_name TO user_name;
```

In CrateDB, schemas are just namespaces that are created and dropped implicitly.
Therefore, when `GRANT`, `DENY` or `REVOKE` are invoked on a schema level,
CrateDB takes the schema name provided without further validation.


:::{note}
🚧 _Please note this page is a work in progress._ 🚧
:::
