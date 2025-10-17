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

```shell
cpan install DBD::Pg
```
```perl
use DBI;
use DBD::Pg qw(:pg_types);

$dbh = DBI->connect("dbi:Pg:host=localhost;port=5432;dbname=doc", "crate", "crate", {AutoCommit => 0});
$sth = $dbh->prepare("SELECT region, mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3");
$sth->execute();

$rows = $sth->dump_results();
print($rows);
```


[DBD::Pg]: https://metacpan.org/pod/DBD::Pg
