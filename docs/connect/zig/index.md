(connect-zig)=

# Zig

:::{div} sd-text-muted
Connect to CrateDB from Zig applications.
:::

:::{rubric} About
:::

[pg.zig] is a native PostgreSQL driver / client for Zig.

:::{rubric} Synopsis
:::

- `build.zig` will build the example program.
- `example.zig` is the program built by `build.zig`.

`build.zig`
```zig
const std = @import("std");

pub fn build(b: *std.Build) void {

    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const exe = b.addExecutable(.{
        .name = "example",
        .root_module = b.createModule(.{
            // `example.zig` is the program built by `build.zig`.
            .root_source_file = b.path("example.zig"),
            .target = b.graph.host,
        })
    });

    const pg = b.dependency("pg", .{
        .target = target,
        .optimize = optimize,
    });
    exe.root_module.addImport("pg", pg.module("pg"));

    b.installArtifact(exe);
}
```
`example.zig`
```zig
const std = @import("std");
const builtin = @import("builtin");

const pg = @import("pg");

pub fn main() !void {

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = if (builtin.mode == .Debug) gpa.allocator() else std.heap.c_allocator;

    const uri = try std.Uri.parse("postgresql://crate:crate@localhost/?sslmode=disable");
    var pool = try pg.Pool.initUri(allocator, uri, .{.size=5, .timeout=5_000});
    defer pool.deinit();

    var result = try pool.query("SELECT mountain, height FROM sys.summits ORDER BY height DESC LIMIT 3", .{});
    defer result.deinit();

    while (try result.next()) |row| {
        const mountain = row.get([]u8, 0);
        const height = row.get(i32, 1);
        std.debug.print("{s}: {d}\n", .{mountain, height});
    }

}
```

:::{include} ../_cratedb.md
:::
```shell
zig fetch --save git+https://github.com/karlseguin/pg.zig#master
zig build
./zig-out/bin/example
```

:::{rubric} SSL connection
:::

Use the `sslmode=require` parameter, and replace username, password,
and hostname with values matching your environment.
Also use this variant to connect to CrateDB Cloud.

```zig
const uri = try std.Uri.parse("postgresql://admin:password@testcluster.cratedb.net:5432/?sslmode=require");
```


[pg.zig]: https://github.com/karlseguin/pg.zig
