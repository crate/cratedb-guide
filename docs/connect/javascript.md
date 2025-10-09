(connect-javascript)=

# JavaScript

:::{div} sd-text-muted
Available Node.js modules and drivers for CrateDB and CrateDB Cloud.
:::

## node-postgres

node-postgres is a collection of Node.js modules (including pg and pg-cursor) for interfacing with a CrateDB
Cloud database.

Example implementation will look like this:

```javascript
import pg from "pg";
import Cursor from "pg-cursor";

const pool = new pg.Pool({
  host: "<name-of-your-cluster>.cratedb.net",
  port: 5432,
  user: "admin",
  password: "<PASSWORD>",
  ssl: true,
});
const conn = await pool.connect();

const stmt = "SELECT * FROM tbl";
const cursor = conn.query(new Cursor(stmt));
cursor.read(100, (err, rows) => {
  if (err) {
    console.error(err);
  } else {
    console.log(rows);
  }
  cursor.close(() => {
    conn.release();
    pool.end();
  });
});

```

For more information see [node-postgres documentation].

## node-crate

node-crate is an independent Node.js driver driver for CrateDB that communicates via
the `_sql` HTTP endpoint.

Example implementation will look like this:

```javascript
import { default as crate } from "node-crate";

crate.connect(`https://admin:${encodeURIComponent("<PASSWORD>")}@<name-of-your-cluster>.cratedb.net:4200`);

const result = await crate.execute("SELECT name FROM sys.cluster");
console.log(result.rows[0]);
```

For more information see [node-crate documentation].

[node-crate documentation]: https://www.npmjs.com/package/node-crate
[node-postgres documentation]: https://www.npmjs.com/package/pg
