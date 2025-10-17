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

```julia
using Pkg
Pkg.add("LibPQ")
Pkg.add("Tables")
```
```julia
using LibPQ
using Tables

conn = LibPQ.Connection("postgres://crate:crate@localhost:5432/?sslmode=disable");
result = LibPQ.execute(conn, "SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3")
data = rowtable(result)
println(data)
```

:::{rubric} Learn
:::

- See also [Exploring the Power of PostgreSQL with Julia: A Beginners Guide]


[Exploring the Power of PostgreSQL with Julia: A Beginners Guide]: https://blog.stackademic.com/exploring-the-power-of-postgresql-with-julia-a-beginners-guide-88920ec9da3e?gi=231c51a85197
[LibPQ.jl]: https://github.com/JuliaDatabases/LibPQ.jl
