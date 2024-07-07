(jcmd)=

# Using `jcmd` with CrateDB

:::{rubric} Introduction
:::
Since JDK 8, `jcmd` is the designated successor of different tools used before
(`jstack`, `jinfo`, `jmap`). It can be used to perform various diagnostic tasks
on a running Java application, such as performing a heap dump, thread dump, and
so on.

> The [jcmd] utility is used to send diagnostic command requests to the JVM,
where these requests are useful for controlling Java Flight Recordings,
troubleshoot, and diagnose JVM and Java Applications. It must be used on
the same machine where the JVM is running, and have the same effective user
and group identifiers that were used to launch the JVM.

:::{code} console
$ /crate/jdk/bin/jcmd -h
Usage: jcmd <pid | main class> <command ...|PerfCounter.print|-f file>
   or: jcmd -l
   or: jcmd -h

  command must be a valid jcmd command for the selected jvm.
  Use the command "help" to see which commands are available.
  If the pid is 0, commands will be sent to all Java processes.
  The main class argument will be used to match (either partially
  or fully) the class used to start Java.
  If no options are given, lists Java processes (same as -l).

  PerfCounter.print display the counters exposed by this process
  -f  read and execute commands from the file
  -l  list JVM processes on the local machine
  -? -h --help print this help message
:::


:::{rubric} Help
:::
`jcmd <PID> help` lists all available commands that you can use to troubleshoot
CrateDB.
:::{code} console
/crate/jdk/bin/jcmd 1 help
:::
For more information about a specific command, use `help <command>`.


:::::{grid} 1 1 2 2
:padding: 0

::::{grid-item}
:class: rubric-slimmer

:::{rubric} Troubleshooting Commands
:::
:::{code} console
# Java Version
/crate/jdk/bin/jcmd 1 VM.version
   1:
   OpenJDK 64-Bit Server VM version 13.0.1+9
   JDK 13.0.1

# Heap Information
/crate/jdk/bin/jcmd 1 GC.heap_info

# Heap Dump
/crate/jdk/bin/jcmd 1 GC.heap_dump /data/crate.hprof

# Thread Dump
/crate/jdk/bin/jcmd 1 Thread.print
:::
::::

::::{grid-item}
:class: rubric-slimmer

:::{rubric} Java Flight Recorder (JFR)
:::
:::{code} console
/crate/jdk/bin/jcmd 1 JFR.start duration=60s filename=/data/recording1.jfr
/crate/jdk/bin/jcmd 1 JFR.start duration=300s filename=/data/recording2.jfr settings=profile
:::
:::{card} {material-outlined}`receipt_long;2em` Java Flight Recorder (JFR)
:link: jfr
:link-type: ref
A monitoring tool that collects information about the events in a Java Virtual
Machine (JVM) during the execution of a Java application. JFR is part of the
JDK distribution, and it is integrated into the JVM.
:::
::::

:::::



## Learn

:::{rubric} Fundamentals
:::

:::{card} {material-outlined}`receipt_long;1.6em` Diagnosing a Running JVM
:link: https://www.baeldung.com/running-jvm-diagnose#7-jfr-command-options
This tutorial examines the jcmd utility, its commands, command options, and
and how to use it.
:::

:::{card} {material-outlined}`library_books;1.6em` Java SE Diagnostic Tools » The jcmd Utility
:link: https://docs.oracle.com/en/java/javase/11/troubleshoot/diagnostic-tools.html#GUID-42A18B29-B4AD-4831-B846-2CDBA55F2254
The official documentation about jcmd outlines its advantages, useful commands, and
troubleshooting guidelines.
:::

:::{rubric} CrateDB
:::

:::{card} {octicon}`container;1.6em` Use jcmd with CrateDB on Docker
:link: jcmd-docker
:link-type: ref
Learn why the standard way to run `jcmd` does not work when running CrateDB
inside a container, for example when using Docker, and how to resolve that
problem.
:::



:::{toctree}
:hidden:

docker
jfr
:::


[jcmd]: https://docs.oracle.com/en/java/javase/17/docs/specs/man/jcmd.html
