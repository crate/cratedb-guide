(connect-erlang)=

# Erlang

:::{div} sd-text-muted
Connect to CrateDB from Erlang applications.
:::

## ODBC

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


## epgsql

[epgsql] is the designated Erlang PostgreSQL client library. 

`rebar.config`
```erlang
{deps,
 [
  {epgsql, ".*", {git, "https://github.com/epgsql/epgsql.git", {tag, "4.8.0"}}}
 ]}.
```
`epgsql_example.erl`
```erlang
-module(epgsql_example).
-export([start/0]).

start() ->
    {ok, C} = epgsql:connect(#{
        host => "localhost",
        username => "crate",
        password => "crate",
        database => "doc",
        port => 5432,
        timeout => 4000
    }),
    {ok, _, Result} = epgsql:squery(C, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3"),
    io:fwrite("~p~n", [Result]),
    ok = epgsql:close(C),
    init:stop().
```

:::{include} ../_cratedb.md
:::
```shell
rebar3 compile
erlc epgsql_example.erl
rebar3 shell --eval 'epgsql_example:start().'
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, start the Erlang [SSL application] first,
use the `ssl` and `ssl_opts` arguments on `epgsql:connect`, and
replace username, password, and hostname with values matching
your environment.
```erlang
start() ->
    ssl:start(),
    {ok, C} = epgsql:connect(#{
        host => "testcluster.cratedb.net",
        username => "admin",
        password => "password",
        database => "doc",
        port => 5432,
        ssl => true,
        ssl_opts => [{verify, verify_none}],
        timeout => 4000
    }),
```


[epgsql]: https://github.com/epgsql/epgsql
[Erlang ODBC examples]: https://www.erlang.org/doc/apps/odbc/getting_started.html
[ODBC application]: https://www.erlang.org/docs/28/apps/odbc/odbc.html
[SSL application]: https://www.erlang.org/docs/28/apps/ssl/ssl_app.html
