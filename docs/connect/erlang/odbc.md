(erlang-odbc)=

# Erlang ODBC

:::{div} sd-text-muted
Connect to CrateDB from Erlang using ODBC.
:::

:::{rubric} About
:::

Erlang includes an [ODBC application] out of the box that provides an
interface to communicate with relational SQL-databases, see also
[Erlang ODBC examples].

::::{todo}
Enable this include with the [ODBC patch](https://github.com/crate/cratedb-guide/pull/411).
```md
:::{include} _odbc-setup-widget.md
:::
```
::::

:::{rubric} Synopsis
:::

Before running the example, ensure the PostgreSQL ODBC driver is
installed on your system.

`odbc_example.erl`
```erlang
-module(odbc_example).

main(_) ->
    odbc:start(),
    {ok, Ref} = odbc:connect("Driver={PostgreSQL ODBC};Server=localhost;Port=5432;Uid=crate;Pwd=crate", []),
    io:fwrite("~p~n", [odbc:sql_query(Ref, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")]),
    init:stop().
```

:::{include} ../_cratedb.md
:::
```shell
escript odbc_example.erl
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, start the Erlang [SSL application],
add `sslmode=require`, and replace `Server`, `Uid`, and `Pwd` with
values matching your environment.

`odbc_example.erl`
```erlang
-module(odbc_example).

main(_) ->
    ssl:start(),
    odbc:start(),
    {ok, Ref} = odbc:connect("Driver={PostgreSQL};Server=testcluster.cratedb.net;Port=5432;sslmode=require;Uid=admin;Pwd=password", []),
    io:fwrite("~p~n", [odbc:sql_query(Ref, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")]),
    init:stop().
```


[Erlang ODBC examples]: https://www.erlang.org/doc/apps/odbc/getting_started.html
[ODBC application]: https://www.erlang.org/docs/28/apps/odbc/odbc.html
