(connect-go)=

# Go

:::{include} /_include/links.md
:::

:::{div} sd-text-muted
Connect to CrateDB from Go applications.
:::

The `pgx` and `pq` packages have been validated with CrateDB.
`pq` is in maintenance mode, so their authors recommend using
`pgx` which is under active development.

:::{toctree}
:hidden:
pgx
pq
ksql
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`package;2em;sd-text-info` &nbsp; pgx
:link: go-pgx
:link-type: ref
:link-alt: pgx for Go
pgx is a pure Go driver and toolkit for PostgreSQL.
::::

::::{grid-item-card} {octicon}`package;2em;sd-text-info` &nbsp; pq
:link: go-pq
:link-type: ref
:link-alt: pq for Go
pq is a pure Go PostgreSQL driver for Go's database/sql package.
::::

::::{grid-item-card} {octicon}`package;2em;sd-text-info` &nbsp; KSQL
:link: go-ksql
:link-type: ref
:link-alt: KSQL for Go
KSQL, the _Keep it Simple_ SQL library.
::::

:::::
