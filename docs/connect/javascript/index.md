(connect-javascript)=
(connect-typescript)=

# JavaScript

:::{div} sd-text-muted
Connect to CrateDB and CrateDB Cloud from Node.js.
:::

:::{rubric} Driver options
:::
Choose one of two JavaScript (Node.js) drivers:

- {ref}`node-postgres` - using PG Wire Protocol
- {ref}`node-crate` - using HTTP/HTTPS

Prefer `node-postgres` first for PostgreSQL-wire compatibility. If you need
HTTP/REST features or run into PG-wire limitations, use `node-crate`.
:::

:::{toctree}
:maxdepth: 1
:hidden:
node-postgres
node-crate
:::
