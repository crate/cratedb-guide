(connect-raku)=

# Raku

:::{div} .float-right .text-right
```{image} https://upload.wikimedia.org/wikipedia/commons/8/85/Camelia.svg
:height: 60px
```
:::
:::{div} .clearfix
:::

:::{div} sd-text-muted
Connect to CrateDB from Raku applications.
:::

:::{rubric} About
:::

[Protocol::Postgres] is a sans-io PostgreSQL client for Raku.

:::{rubric} Synopsis
:::

`example.raku`
```raku
use v6.d;
use Protocol::Postgres;

my $host = "localhost";
my $port = 5432;
my $user = "crate";
my $password = "crate";
my $database = "crate";

my $socket = await IO::Socket::Async.connect($host, $port);
my $client = Protocol::Postgres::Client.new;
$socket.Supply(:bin).act({ $client.incoming-data($^data) });
$client.outbound-data.act({ $socket.write($^data) });

await $client.startup($user, $database, $password);

my $resultset = await $client.query('SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3', []);
react {
    whenever $resultset.hash-rows -> (:$mountain, :$height) {
        say "$mountain: $height";
    }
}
```

:::{rubric} Example
:::

Create the file `example.raku` including the synopsis code shared above.

:::{include} ../_cratedb.md
:::
```shell
zef install Protocol::Postgres
raku example.raku
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, replace username, password, and
hostname with values matching your environment.

```raku
my $host = "testcluster.cratedb.net";
my $port = 5432;
my $user = "admin";
my $password = "password";
my $database = "crate";
```


[Protocol::Postgres]: https://raku.land/zef:leont/Protocol::Postgres
