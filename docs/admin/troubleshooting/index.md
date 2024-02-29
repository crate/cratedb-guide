(troubleshooting)=

# Troubleshooting

A collection of guides and tools for troubleshooting CrateDB.

You will learn how to apply self-service measurements supporting you when
observing problems with your CrateDB database cluster.
If you need help from others, feel free to reach out to our community or
commercial [support channels][support] any time.

:::{tip}
Relevant suggestions will support you to optimally gather and convey
information about your database cluster, which helps others to get a
rough orientation about its size, and other technical characteristics.
Before [contacting support][support], you optimally have this information
ready.
:::

:::{note}
The guidelines may not exclusively be applicable for users of CrateDB Cloud,
or when running CrateDB on a commercial contract, where additional
communication channels apply.

Independently from support channels and status, significant parts
of the instructions outlined here will help our support engineers to discover
any sort of problem with your CrateDB cluster much faster than asking
individual questions, so we generally recommend to use
this guideline as a checklist in all situations.
:::


## Introduction

Many details about the status of your cluster is included within CrateDB's
[system tables]. The `sys` schema includes synthetic read-only tables which
can be queried to get statistical real-time information about the cluster's
metadata, like information about nodes and shards. The [](#systables) section
illustrates how to use them.

The sections below include instructions about how to use the [crate-node]
and [jcmd] utility and diagnosis programs, and information about
using the [Java Flight Recorder] for [monitoring Java applications].


## Instructions

:::{todo}
- 🚧 A concise step-by-step checklist could be provided here, with
  optional tool support.
- 🧹 The "table of contents" section below may be removed.
:::


:::{rubric} Table of contents
:::

:::{toctree}
:maxdepth: 2

using system tables <system-tables>
using crate-node <crate-node>
using jcmd on Docker <docker-jcmd>
:::




[crate-node]: inv:crate-reference#cli-crate-node
[Java Flight Recorder]: https://en.wikipedia.org/wiki/JDK_Flight_Recorder
[jcmd]: https://www.baeldung.com/running-jvm-diagnose
[monitoring Java applications]: https://www.baeldung.com/java-flight-recorder-monitoring
[support]: https://cratedb.com/support
[system tables]: inv:crate-reference#system-information
