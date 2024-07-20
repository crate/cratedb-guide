(server-side-cursor)=
(server-side-cursors)=

# Server-Side Cursors

CrateDB implements the SQL Standard feature [F431 (read-only scrollable cursor)],
aka. server-side cursors, aka. portals.

A cursor is used to retrieve a small number of rows at a time from a query
with a large result set. Such a result set might not be suitable for other
ways of consumption, because its size might be larger than the system memory
of the machines that process it, both server- and client-side.

With F431, you {ref}`crate-reference:sql-declare` a server-side cursor,
and iterate it, fetching the rows progressively using
{ref}`crate-reference:sql-fetch`. 



:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
It includes not even the most basic essentials, and needs expansion. For example,
the "Usage" and "Learn" sections are missing completely, and it's also not in the
same shape like the other pages in this section.
:::


[F431 (read-only scrollable cursor)]: https://renenyffenegger.ch/notes/misc/ISO/9075/features/F431
