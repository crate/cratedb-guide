(memory)=

# Memory Configuration

## Introduction

CrateDB is a Java application running on top of a Java Virtual Machine (JVM).

For optimal performance, you must configure the amount of memory that is
available to the JVM for **heap** allocations. The **heap** is a memory region
used for allocations of objects. For example, if you invoke a `SELECT`
statement, parts of the result set are temporarily allocated on the **heap**
memory.

The amount of memory that CrateDB can use for heap allocations is configured
using the [CRATE_HEAP_SIZE] environment variable.

The right memory configuration depends on your workloads.

## Recommendation

A good starting point for the heap space is 25% of the system memory.

Be careful when configuring this, as making the heap too large may lead to OutOfMemory errors,
if the operating system cannot allocate memory for other needs, and on the other hand, making
the heap too small may lead to OutOfMemory errors when new Java objects cannot be allocated
inside the heap.

In any case, it shouldn't be set below 1GB and not above 30.5GB,
See the limits section below.

## Considerations

Consider the following when determining the right value:

- The JVM has automatic memory management and frees up memory using [Garbage
  Collection][garbage collection] (GC). CrateDB, as of version 4.1, defaults to use a garbage
  collection implementation called [G1GC]. This implementation performs well
  for heap sizes ranging from several GB to ten or more. It tries to provide
  the best balance between latency and throughput. Still, the garbage
  collection times **increase** with a bigger heap, leading to **increased**
  latency. Therefore, your heap size shouldn't be too large.
- The optimal heap size is workload dependent. Be sure to test carefully
  if you want to change the default, as wrong values may cause CrateDB to crash
  with OutOfMemory errors.
- CrateDB needs to be able to hold all the structures required to process
  queries in memory. The biggest offender are intermediate or final result
  sets. Therefore, the heap region must be large enough to hold the biggest
  result sets in memory. The size of the intermediate and final result sets
  depend entirely on the type of queries you are running.
- CrateDB uses [Memory mapped files] via [Lucene]. This reduces the
  amount of heap space required and benefits from the file system cache.
- Both to keep latency down, and to enable use of heap sizes above 32 GB,
  it is also possible to use one of the newer garbage collectors, such as ZGC.
  These are known to have worked, but aren't officially tested nor supported.

(swap)=

## Swap

CrateDB performs sub-optimally when the JVM starts swapping. To ensure that
CrateDB never swaps, set the [bootstrap.memory_lock] property to `true` to
lock the memory. You can configure this setting in your [configuration] file,
like so:

```yaml
bootstrap.memory_lock: true
```

(memory-limits)=

## Memory Limits

### About Compressed Oops

On [x64 architectures], the [HotSpot Java Virtual Machine] (JVM) uses a
performance optimization technique called [Compressed Oops]. This technique
allows the JVM to use 4 bytes instead of 8 bytes for object references. This
saves a lot of memory.

Unfortunately, the JVM can only address up to about 32 GB of memory with
`Compressed Oops`, and the optimization is disabled if a heap size of more
than 32 GB is configured.

If `Compressed Oops` is disabled, the object overhead will increase compared to
having it enabled. Because of this, a cluster that is configured to use 30 GB
heap memory may have more real memory available for objects than a cluster that
uses only slightly more than 32GB of heap memory.

### Considerations

On some JVMs, this value is as low as 30.5 gigabytes. To verify that
*Compressed Oops* is enabled you can use the `jcmd` program:

```console
sh$ jcmd 624140 VM.info | grep "Compressed Oops"

Heap address: 0x0000000414200000, size: 16062 MB, Compressed Oops mode: Zero
based, Oop shift amount: 3
```

Here, 624140 is the PID of the CrateDB progress. If the output is empty,
*Compressed Oops* are not in use.

### Recommendation

For this reason, you should aim to stay below 30.5 GB.

If you want to use more than 30.5 GB, you should configure the total amount to
offset the memory lost due to the lack of *Compressed Oops*.

:::{TIP}
When configuring the heap size via [CRATE_HEAP_SIZE], you can specify 30.5
gigabytes with the value `30500m`.
:::

[bootstrap.memory_lock]: https://cratedb.com/docs/crate/reference/en/latest/config/node.html#memory
[compressed oops]: https://wiki.openjdk.java.net/display/HotSpot/CompressedOops
[configuration]: inv:crate-reference#config
[configurations]: inv:crate-reference#config
[crate_heap_size]: inv:crate-reference#conf-env-heap-size
[g1gc]: https://docs.oracle.com/javase/10/gctuning/garbage-first-garbage-collector.htm
[garbage collection]: https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)
[hotspot java virtual machine]: https://www.oracle.com/java/technologies/javase/javase-core-technologies-apis.html
[lucene]: https://lucene.apache.org/
[memory mapped files]: https://en.wikipedia.org/wiki/Memory-mapped_file
[x64 architectures]: https://en.wikipedia.org/wiki/X86-64
