(cfr)=
# CrateDB Flight Recorder (CFR)

:::{rubric} About
:::
In a similar spirit like the [](#jfr), CFR helps to collect information about
CrateDB clusters for support requests and self-service debugging.

CFR is a utility application to acquire and export diagnostic information from
CrateDB's [system tables](#systables) into an archive file. You can transmit
this file to support engineers, in order to optimally convey relevant
information about your cluster, mostly for debugging and troubleshooting
purposes.

:::{rubric} Details
:::
The CrateDB Flight Recorder (CFR) is an ETL application dumping all database
tables in the `sys` schema into a timestamped tarball archive file.
On the receiving end, the recording can be imported into another CrateDB
instance, in order to inspect and analyze it.

Flight recordings can be started against any running CrateDB cluster at runtime.
The utility connects to CrateDB like a regular client, talking SQL.
CFR is part of the CrateDB Toolkit (`ctk cfr`), and is also available as a
standalone application `cratedb-cfr(.exe)`.


## Synopsis

:Export:

    `cratedb-cfr sys-export` invokes the export operation.

:Import:

    `cratedb-cfr sys-import` invokes the import operation.


## Install

Select one of the standalone application bundles, matching the platform
and architecture of the corresponding system where you intend to run CFR.

::::{grid} 1 2 2 2

:::{grid-item-card} {material-outlined}`download_for_offline;1.4em` Linux x64
:link: https://github.com/crate/cratedb-toolkit/actions/runs/17050832642/artifacts/3792142004
:link-alt: CFR for Linux x64
:padding: 0
:class-title: sd-fs-5
+++
cratedb-cfr-linux-x64.zip
:::

:::{grid-item-card} {material-outlined}`download_for_offline;1.4em` macOS x64
:link: https://github.com/crate/cratedb-toolkit/actions/runs/17050832642/artifacts/3792153874
:link-alt: CFR for macOS x64
:padding: 0
:class-title: sd-fs-5
+++
cratedb-cfr-macos-x64.zip
:::

:::{grid-item-card} {material-outlined}`download_for_offline;1.4em` Windows x64
:link: https://github.com/crate/cratedb-toolkit/actions/runs/17050832642/artifacts/3792143556
:link-alt: CFR for Windows x64
:padding: 0
:class-title: sd-fs-5
+++
cratedb-cfr-windows-x64.zip
:::

:::{grid-item-card} {material-outlined}`download_for_offline;1.4em` macOS ARM64
:link: https://github.com/crate/cratedb-toolkit/actions/runs/17050832642/artifacts/3792135976
:link-alt: CFR for macOS ARM64
:padding: 0
:class-title: sd-fs-5
+++
cratedb-cfr-macos-arm64.zip
:::

::::



## Learn

:::{card} {material-outlined}`library_books;1.6em` CrateDB Cluster Flight Recorder (CFR)
:link: ctk:cfr
:link-type: ref
Learn about the concepts of CFR, and how to use it.
:::


[Java Flight Recorder]: https://en.wikipedia.org/wiki/JDK_Flight_Recorder
[jcmd]: https://docs.oracle.com/en/java/javase/17/docs/specs/man/jcmd.html
