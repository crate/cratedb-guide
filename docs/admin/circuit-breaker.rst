.. _circuit-breaker:

===============
Circuit Breaker
===============
CrateDB's circuit breakers prevent queries and background processes from exhausting node memory and destabilizing the cluster.
This works by estimating the memory each operation will require and aborting the operation before the JVM heap space is exhausted.

What is a Circuit Breaker
==========================
A **circuit breaker** is a safeguard that halts work when resource usage crosses a dangerous threshold.
Think of the miniature breakers inside a household fuse box: if too many appliances pull current on the same line, the breaker
trips and cuts power to prevent the wires from melting. The same principle applies in software, only the resource under pressure
is memory, CPU, file descriptors, or an external service.

In CrateDB, the critical resource is **RAM**. Queries run in parallel across many shards; a single
oversize aggregation or JOIN can allocate gigabytes in milliseconds. The breaker detects this and aborts the query with a
``CircuitBreakingException`` instead of letting the JVM run out of heap and crash the node.

How Circuit Breakers Work in CrateDB
====================================
A query executes as an ordered set of operations. Before running each stage, CrateDB estimates the extra memory that step will need.
If the projected total would exceed the breaker limit, the system aborts the query and returns a ``CircuitBreakingException``.
This pre-emptive trip prevents the JVM's garbage collector from reaching an unrecoverable out-of-memory state.

It is important to understand CrateDB doesn’t aspire to do a fully accurate memory accounting, but instead opts for a best-effort approach,
since a precise estimate is tricky to achieve.

Types of Circuit Breakers
=========================
There are six different Circuit Breaker types which are described in detail in the `cluster settings`_ documentation page: ``query``,
``request``, ``jobs_log``, ``operations_log``, ``total`` and ``accounting``, which was deprecated and will be removed soon. The ``total`` Circuit Breaker, also
known as ``parent``, accounts for all others, meaning that it controls the general use of memory, tripping an operation if a
combination of the circuit breakers threatens the cluster.

Monitoring & Observability
==========================

To monitor the Circuit Breaker usage, follow the `JMX monitoring`_ guide. In particular,
consult the `CircuitBreakers MXBean`_ section.

For hosted deployments, see `Cloud monitoring`_ and for self-managed clusters, the `on-prem monitoring`_ guide. Both describe the complete path from cluster
deployment to collecting metrics and displaying them on a Grafana dashboard.

Exception Handling
==================
.. code-block:: console

  CircuitBreakingException[Allocating 2mb for 'query: mergeOnHandler' failed, breaker would use 976.4mb in total. Limit is 972.7mb. Either increase memory and limit, change the query or reduce concurrent query load]

* **Understanding the error**

  The memory estimate for **mergeOnHandler** exceeded the ``indices.breaker.query.limit``, so the query was aborted and the
  exception returned.


* **Immediate actions**

  * **Optimize the query** - see :ref:`Query Optimization 101 <performance-optimization>` for detailed guidance.
  * **Identify memory-hungry queries** - run:

    .. code-block:: psql

      SELECT  js.id,
              stmt,
              username,
              sum(used_bytes) sum_bytes
      FROM sys.operations op
      JOIN sys.jobs js ON op.job_id = js.id
      GROUP BY js.id, stmt, username
      ORDER BY sum_bytes DESC;


    The query above will return all jobs that are currently being executed in the cluster. To check completed jobs and operations, query
    the corresponding system tables ``sys.jobs_log`` and ``sys.operations_log``. Access to these tables are subject to `table permissions`_.

  * **Scale the cluster** - if breakers trip frequently even after query tuning, evaluate scaling your cluster to get more resources.


Similar exceptions exist for the other breaker types ``[request]``, ``[parent]``, ``[jobs_log]``, etc.
If you experience a ``CircuitBreakingException [parent]`` it is because other queries/tasks were running simultaneously and their summed estimate
exceeded ``indices.breaker.total.limit``.

Further Reading
===============
`The Circuit Breaker Mechanism in CrateDB`_



.. _cluster settings: https://cratedb.com/docs/crate/reference/en/master/config/cluster.html#query-circuit-breaker
.. _table permissions: https://cratedb.com/docs/crate/reference/en/master/admin/system-information.html#jobs-table-permissions
.. _The Circuit Breaker Mechanism in CrateDB: https://zignar.net/2021/06/17/the-circuit-breaker-mechanism-in-cratedb/
.. _JMX monitoring: https://cratedb.com/docs/crate/reference/en/master/admin/monitoring.html#jmx-monitoring
.. _CircuitBreakers MXBean: https://cratedb.com/docs/crate/reference/en/master/admin/monitoring.html#circuitbreakers-mxbean
.. _Cloud monitoring: https://community.cratedb.com/t/monitoring-cratedb-cloud-clusters/1397
.. _on-prem monitoring: https://community.cratedb.com/t/monitoring-a-self-managed-cratedb-cluster-with-prometheus-and-grafana/1236
