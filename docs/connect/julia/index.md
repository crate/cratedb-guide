(connect-julia)=

# Julia

:::{div} sd-text-muted
Connect to CrateDB from Julia applications.
:::

:::{rubric} About
:::

[LibPQ.jl] is a Julia wrapper for the PostgreSQL libpq C library.

:::{rubric} Synopsis
:::

`setup.jl`
```julia
using Pkg
Pkg.add("LibPQ")
Pkg.add("Tables")
```
`example.jl`
```julia
using LibPQ
using Tables

conn = LibPQ.Connection("postgresql://crate:crate@localhost:5432/?sslmode=disable");
result = LibPQ.execute(conn, "SELECT mountain, region, height FROM sys.summits ORDER BY height DESC LIMIT 3")
data = rowtable(result)
for row in data
    println(row)
end
```

:::{include} ../_cratedb.md
:::
```shell
julia setup.jl
julia example.jl
```

:::{rubric} SSL connection
:::

Use the `sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```julia
conn = LibPQ.Connection("postgresql://admin:password@testcluster.cratedb.net:5432/?sslmode=require");
```

:::{rubric} Learn
:::

- See also [Exploring the Power of PostgreSQL with Julia: A Beginners Guide]


[Exploring the Power of PostgreSQL with Julia: A Beginners Guide]: https://blog.stackademic.com/exploring-the-power-of-postgresql-with-julia-a-beginners-guide-88920ec9da3e?gi=231c51a85197
[LibPQ.jl]: https://github.com/JuliaDatabases/LibPQ.jl
