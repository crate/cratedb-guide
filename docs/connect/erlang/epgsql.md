(erlang-epgsql)=

# Erlang epgsql

:::{div} sd-text-muted
Connect to CrateDB from Erlang using epgsql.
:::

:::{rubric} About
:::

[epgsql] is the designated Erlang PostgreSQL client library. 

:::{rubric} Synopsis
:::

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
[SSL application]: https://www.erlang.org/docs/28/apps/ssl/ssl_app.html
