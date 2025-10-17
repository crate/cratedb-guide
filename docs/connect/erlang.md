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

:::{rubric} Synopsis
:::

`odbcinst.ini`
```ini
[PostgreSQL]
Description     = PostgreSQL ODBC driver
Driver          = /usr/local/lib/psqlodbcw.so
```
```shell
odbcinst -i -d -f odbcinst.ini
```
`odbc_demo.erl`
```erlang
-module(odbc_demo).
-export([start/0]).

start() ->
    odbc:start(),
    {ok, Ref} = odbc:connect("Driver={PostgreSQL};Servername=localhost;Portnumber=5432;Uid=crate;Pwd=crate", []),
    io:fwrite("~p", [odbc:sql_query(Ref, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")]).
```
```shell
erlc odbc_demo.erl && erl -s odbc_demo
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
```shell
rebar3 compile
```
`epgsql_demo.erl`
```erlang
-module(epgsql_demo).
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
    io:fwrite("~p", [Result]),
    ok = epgsql:close(C).
```
```shell
erlc epgsql_demo.erl
erl -pa ebin ./_build/default/lib/epgsql/ebin ./_build/default/lib/epgsql/include -s epgsql_demo
```


[epgsql]: https://github.com/epgsql/epgsql
[Erlang ODBC examples]: https://www.erlang.org/doc/apps/odbc/getting_started.html
[ODBC application]: https://www.erlang.org/doc/apps/odbc/odbc.html
