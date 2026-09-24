(connect-crystal)=

# Crystal

:::{div} sd-text-muted
Connect to CrateDB from Crystal applications.
:::

:::{rubric} About
:::

[crystal-pg] is a native, non-blocking Postgres driver for Crystal,
building upon [crystal-db].

:::{rubric} Synopsis
:::

`shard.yml`
```yaml
name: cratedb_demo
version: 0.0.0
dependencies:
  pg:
    github: will/crystal-pg
```
`example.cr`
```crystal
require "db"
require "pg"

DB.open("postgres://crate:crate@localhost:5432/?sslmode=disable") do |db|

  db.query "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3" do |rs|
    puts "#{rs.column_name(0)} #{rs.column_name(1)}"
    rs.each do
      puts "#{rs.read(String)}: #{rs.read(Int32)}"
    end
  end

end
```

:::{include} ../_cratedb.md
:::
```shell
shards install
```
```shell
crystal example.cr
```

:::{rubric} SSL connection
:::

Use the `sslmode=require&auth_methods=cleartext` parameters,
and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```crystal
DB.open("postgres://admin:password@testcluster.cratedb.net:5432/?sslmode=require&auth_methods=cleartext")
```


[crystal-db]: https://github.com/crystal-lang/crystal-db
[crystal-pg]: https://github.com/will/crystal-pg
