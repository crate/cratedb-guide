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

$dbh = DBI->connect("dbi:Pg:host=localhost;port=5432;sslmode=disable", "crate", "crate")
  or die "Cannot connect: $DBI::errstr";
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

:::{rubric} SSL connection
:::

Use the `sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```perl
$dbh = DBI->connect("dbi:Pg:host=testcluster.cratedb.net;port=5432;sslmode=require", "admin", "password");
```


[DBD::Pg]: https://metacpan.org/pod/DBD::Pg
