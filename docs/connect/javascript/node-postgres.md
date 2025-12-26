(node-postgres)=

# node-postgres

node-postgres is a collection of Node.js modules (including pg and
pg-cursor) for interfacing with a CrateDB Cloud database.

:::{rubric} Install
:::

```shell
npm install pg pg-cursor
```

:::{rubric} Synopsis
:::

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

const stmt = "SELECT * FROM sys.summits LIMIT 3";
const cursor = conn.query(new Cursor(stmt));
cursor.read(100, (err, rows) => {
  if (err) {
    console.error(err);
  } else {
    console.log(rows);
  }
  cursor.close(async () => {
    conn.release();
    await pool.end();
  });
});
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`package;1.75em;sd-text-info` &nbsp; pg
:link: https://www.npmjs.com/package/pg
:link-type: url
:link-alt: node-postgres documentation
The full documentation for node-postgres.
::::

:::::
