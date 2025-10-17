(connect-perl)=

# Perl

:::{div} sd-text-muted
Connect to CrateDB from Perl applications.
:::

:::{rubric} About
:::

[DBD::Pg] is the PostgreSQL database driver for the Perl DBI module.

:::{rubric} Synopsis
:::

`example.pl`
```perl
use DBI;
use DBD::Pg qw(:pg_types);

$dbh = DBI->connect("dbi:Pg:host=localhost;port=5432;dbname=doc", "crate", "crate", {AutoCommit => 0});
$sth = $dbh->prepare("SELECT region, mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3");
$sth->execute();

$rows = $sth->dump_results();
print($rows);
```

:::{include} ../_cratedb.md
:::
```shell
cpan install DBD::Pg
perl example.pl
```

:::{rubric} CrateDB Cloud
:::

For connecting to CrateDB Cloud, replace username, password, and
hostname with values matching your environment.

```perl
$dbh = DBI->connect("dbi:Pg:host=testcluster.cratedb.net;port=5432;dbname=doc", "admin", "password", {AutoCommit => 0});
```


[DBD::Pg]: https://metacpan.org/pod/DBD::Pg
