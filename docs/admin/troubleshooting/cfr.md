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
The CrateDB Flight Recorder (CFR) is part of the CrateDB Toolkit. It is an
ETL application dumping all database tables in the `sys` schema into a
timestamped tarball archive file.

On the receiving end, the recording can be imported into another CrateDB
instance to inspect and analyze it.
Flight recordings can be started against any running CrateDB cluster at runtime.
The utility connects to CrateDB like a regular client, talking SQL.

## Install

```shell
uv tool install 'cratedb-toolkit[cfr]'
```

## Synopsis

:Export:

  Invoke the export operation.
  ```shell
  ctk cfr sys-export
  ```

:Import:

  Invoke the import operation.
  ```shell
  ctk cfr sys-import
  ```

## Learn

:::{card} {material-outlined}`library_books;1.6em` CrateDB Cluster Flight Recorder (CFR)
:link: ctk:cfr
:link-type: ref
Learn about the concepts of CFR, and how to use it.
:::


[Java Flight Recorder]: https://en.wikipedia.org/wiki/JDK_Flight_Recorder
[jcmd]: https://docs.oracle.com/en/java/javase/17/docs/specs/man/jcmd.html
