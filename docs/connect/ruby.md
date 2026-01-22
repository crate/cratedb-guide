:::{include} /_include/links.md
:::

(connect-ruby)=

# Ruby

:::{div} sd-text-muted
How to connect to CrateDB using Ruby.
:::

:::{div}
An example implementation of Ruby client library for [CrateDB Cloud]:
:::

```ruby
require 'crate_ruby'


client = CrateRuby::Client.new(
  servers:   ["<name-of-your-cluster>.cratedb.net:4200"],
  username:  "admin",
  password:  "<PASSWORD>",
  ssl:       true
)
result = client.execute("SELECT name FROM sys.cluster")
p result.to_a
```

For additional information see [our GitHub documentation].

[our github documentation]: https://github.com/crate/crate_ruby/blob/main/README.rst
