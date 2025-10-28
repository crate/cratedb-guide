(odbc-erlang)=

# ODBC with Erlang

:::{rubric} About
:::

The [Erlang ODBC application] provides an interface to communicate
with relational SQL-databases out of the box.

:::{rubric} Synopsis
:::

`example.erl`
```erlang
odbc:start(),
{ok, Ref} = odbc:connect("Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Uid=crate;Pwd=crate", []),
io:fwrite("~p~n", [odbc:sql_query(Ref, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")]),
```

:::{rubric} Example
:::

:::{todo}
Enable with the [Erlang patch](https://github.com/crate/cratedb-guide/pull/420).
```
- {ref}`connect-erlang`
```
:::


[Erlang ODBC application]: https://www.erlang.org/docs/28/apps/odbc/odbc.html
