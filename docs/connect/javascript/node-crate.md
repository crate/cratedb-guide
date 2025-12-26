(node-crate)=

# node-crate

node-crate is an independent Node.js driver for CrateDB
that communicates via the `_sql` HTTP endpoint.

:::{rubric} Install
:::

```shell
npm install node-crate
```

:::{rubric} Synopsis
:::

```javascript
import { default as crate } from "node-crate";

crate.connect(`https://admin:<PASSWORD>@<name-of-your-cluster>.cratedb.net:4200`);

const result = await crate.execute("SELECT * FROM sys.summits LIMIT 3");
console.log(result.rows[0]);
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`package;1.75em;sd-text-info` &nbsp; node-crate
:link: https://www.npmjs.com/package/node-crate
:link-type: url
:link-alt: node-crate documentation
The full documentation for node-crate.
::::

:::::
