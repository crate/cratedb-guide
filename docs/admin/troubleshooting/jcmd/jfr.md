(jfr)=
# Java Flight Recorder (JFR)

:::{rubric} About
:::
The jcmd utility is the traditional application to inquire diagnostic information
from applications running on the JVM, also including the [Java Flight Recorder] (JFR).

:::{rubric} Details
:::
The Java Flight Recorder (JFR) is a profiling and event collection framework to
gather detailed low-level information about how the Java Virtual Machine (JVM)
and Java applications are behaving during execution.

Flight recordings can be started when the application is started or while the
application is running. The data is recorded as time-stamped data points called
events.

JFR is part of the JDK distribution, and it is integrated into the JVM.

:Events:

    JFR collects events that occur in the JVM when the Java application runs. The
    events are related to the state of the JVM itself or the state of the program.
    An event has a name, a timestamp, and additional information, like thread
    information, execution stack, and state of the heap.

:Recording Types:

    A _time fixed recording_, also known as a _profiling recording_, runs for a set
    amount of time, and then stops. A _continuous recording_ is a recording that is
    always on and saves, for example, the last six hours of data into a circular
    buffer, discarding old data when the buffer fills up.

:Performance:

    The events that JFR collects contain a huge amount of data. For this reason,
    JFR is designed to affect the performance of a running application as little
    as possible.

    JFR saves data about the events into a single output file.
    Because disk I/O operations are expensive, JFR uses various buffers to store
    collected data before flushing blocks of data to disk.


## Synopsis
:::{code} console
jcmd 1 JFR.start duration=60s filename=/data/recording1.jfr
jcmd 1 JFR.start duration=300s filename=/data/recording2.jfr settings=profile
:::


## Learn

:::{rubric} Fundamentals
:::

:::{card} {material-outlined}`article;1.6em` Java Flight Recorder » Basic Concepts and Usage
:link: https://www.baeldung.com/java-flight-recorder-monitoring#java-flight-recorder
This tutorial examines Java Flight Recorder, its concepts, its basic commands, and how to use it.
:::

:::{card} {material-outlined}`receipt_long;1.6em` Diagnose a Running JVM » JFR Command Options
:link: https://www.baeldung.com/running-jvm-diagnose#7-jfr-command-options
A concise example how to generate a JFR file using the jcmd command.
:::

:::{card} {material-outlined}`library_books;1.6em` Java SE Diagnostic Tools » Flight Recorder
:link: https://docs.oracle.com/en/java/javase/11/troubleshoot/diagnostic-tools.html#GUID-D38849B6-61C7-4ED6-A395-EA4BC32A9FD6
The official documentation about JFR outlines its advantages, its event types grouped
by recording templates, and its types of recordings. It also describes in detail how
to produce flight recordings, what's inside, and how to analyze them.
:::

:::{rubric} CrateDB
:::

:::{card} {octicon}`container;1.6em` Use JFR with CrateDB on Docker
:link: jfr-docker
:link-type: ref
Learn why the standard way to run `jcmd` does not work when running CrateDB
inside a container, for example when using Docker, and how to resolve that
problem.
:::



[Java Flight Recorder]: https://en.wikipedia.org/wiki/JDK_Flight_Recorder
[jcmd]: https://docs.oracle.com/en/java/javase/17/docs/specs/man/jcmd.html
