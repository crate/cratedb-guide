---
myst_ref_domains: ["std:ref"] 
---

(troubleshooting)=
# Troubleshooting

A collection of guides, procedures, and utilities for troubleshooting CrateDB
clusters.

You will learn how to apply self-service measures supporting you when
observing problems with your CrateDB database cluster.
If you need help from others, feel free to reach out to our community or
commercial [support channels][support] any time.

:::{rubric} General Recommendations
:::
Relevant suggestions will support you to optimally gather and convey
information about your database cluster, which helps others to get a
good orientation about its technical details like cluster size, or data
volumes. Before [contacting support][support], you optimally have this
information ready.

We recommend to use those guidelines as a checklist in all situations, in order
to help our support engineers to discover any sort of problem with your CrateDB
clusters much faster than needing to ask individual questions.

**Note:** Additional communication channels apply for users of CrateDB Cloud, or
when running CrateDB on a commercial contract.


:::{rubric} System Tables
:::
Many details about the status of your cluster is included within CrateDB's
[system tables]. The `sys` schema includes synthetic read-only tables which
can be queried to get real-time information about the cluster's metadata,
like information about nodes and shards.

:::{card} {material-outlined}`wysiwyg;1.6em` Troubleshooting with system tables
:link: systables
:link-type: ref
How to use CrateDB's system tables to investigate the database cluster status,
and debug issues.
:::


:::{rubric} Diagnostic Utilities
:::
Instructions about how to use relevant utility and diagnosis programs.

:::{card} {material-outlined}`wysiwyg;1.6em` About CFR
:link: cfr
:link-type: ref
The CrateDB Flight Recorder (CFR) collects information from CrateDB's system tables,
and bundles it into an archive file ready to share with our support engineers.
:::

:::{card} {material-outlined}`wysiwyg;1.6em` About `jcmd`
:link: jcmd
:link-type: ref
The jcmd utility is the traditional application to inquire diagnostics information
from software running on the JVM. It also includes the Java Flight Recorder (JFR).
:::

:::{card} {material-outlined}`wysiwyg;1.6em` About `crate-node`
:link: use-crate-node
:link-type: ref
A utility program to interact with a CrateDB cluster for conducting
infrastructure operations. For example:
- Control the master node election process.
- Repurpose nodes: Detach and move between clusters.
- Clean up stale node data.
:::

:::{note}
You can find a lot of troubleshooting guides that explain how to perform
diagnostics on Java applications.

Because CrateDB is written in Java, any of those tools can be used to troubleshoot
CrateDB instances. Above, we are focusing on canonical and traditional utilities,
for example jcmd.
:::

:::{toctree}
:hidden:

System Tables <system-tables>
cfr
jcmd/jfr
The jcmd Utility <jcmd/index>
crate-node
:::


[support]: https://cratedb.com/support
[system tables]: inv:crate-reference#system-information
