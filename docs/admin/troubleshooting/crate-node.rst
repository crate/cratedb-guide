.. highlight:: console

.. _use-crate-node:

==========================
The ``crate-node`` command
==========================

Use the `crate-node`_ command to troubleshoot CrateDB cluster nodes.
Using this command, you can:

* Repurpose nodes and clean up their old data.
* Force the election of a master node (and the creation of a new cluster) in
  the event that you lose too many nodes to be able to form a quorum.
* Detach nodes from an old cluster so they can be moved to a new cluster.


.. _crate-node-repurpose:

Repurpose a node
================

.. rubric:: About

In a situation where you have irrecoverably lost the majority of the
master-eligible nodes in a cluster, you may need to form a new cluster.
When forming a new cluster, you may have to change the `role`_ of one or more
nodes. Changing the role of a node is referred to as *repurposing* a node.

Each node checks the contents of its :ref:`data path <crate-reference:conf-env>`
at startup. If CrateDB discovers unexpected data, it will refuse to start.
The specific rules are:

- Nodes configured with `node.data`_ set to ``false`` will refuse to start if
  they find any shard data at startup.

- Nodes configured with both `node.master`_ set to ``false`` and `node.data`_
  set to ``false`` will refuse to start if they have any index metadata at
  startup.

The `crate-node`_ :ref:`repurpose command <crate-reference:cli-crate-node-commands>`
can help you clean up the necessary node data, so that CrateDB can be restarted
with a new role.

.. rubric:: Procedure

To repurpose a node, first of all, you must stop the node.
Then, update the settings `node.data`_ and `node.master`_ in the ``crate.yml``
:ref:`configuration file <crate-reference:config>` as needed.
The ``node.data`` and ``node.master`` settings can be configured in four
different ways, each corresponding to a different type of node.

+-------------------+------------------------+-----------------------------+
| Role              | Configuration          | After repurposing           |
+                   +                        +------------+----------------+
|                   |                        | Shard data | Index metadata |
+===================+========================+============+================+
| Master-eligible   | .. code-block:: yaml   | —          | —              |
|                   |                        |            |                |
|                   |     node.data: true    |            |                |
|                   |     node.master: true  |            |                |
+-------------------+------------------------+------------+----------------+
| Master-only       | .. code-block:: yaml   | Deleted    | —              |
|                   |                        |            |                |
|                   |     node.master: true  |            |                |
|                   |     node.data: false   |            |                |
+-------------------+------------------------+------------+----------------+
| Data-only         | .. code-block:: yaml   | —          | Deleted        |
|                   |                        |            |                |
|                   |     node.data: true    |            |                |
|                   |     node.master: false |            |                |
+-------------------+------------------------+------------+----------------+
| Coordination-only | .. code-block:: yaml   | Deleted    | Deleted        |
|                   |                        |            |                |
|                   |     node.data: false   |            |                |
|                   |     node.master: false |            |                |
+-------------------+------------------------+------------+----------------+

The final column in the above table indicates what data (if any) will be
deleted (i.e., "cleaned up") after repurposing the node to that configuration.

.. WARNING::

    Before running the ``repurpose`` command, make sure that any data you want
    to keep is available on other nodes in the cluster.

Then, invoke the ``repurpose`` command.

.. code-block:: console

    sh$ ./bin/crate-node repurpose

    Found 2 shards in 2 tables to clean up.
    Use -v to see a list of paths and tables affected.
    Node is being repurposed as master and no-data. Clean-up of shard data will
    be performed.

    Do you want to proceed?

    Confirm [y/N] y
    Node successfully repurposed to master and no data.

As mentioned in the command output, you can pass in ``-v`` to get a more
verbose output.

.. code-block:: console

    sh$ ./bin/crate-node repurpose -v

Finally, start the node again. After that, the node has been successfully
repurposed.


.. _crate-node-unsafe-bootstrap:

Perform an unsafe cluster bootstrap
===================================

.. rubric:: About

When communication is lost between one or more nodes in a cluster (e.g., during
a `network partition`_), the situation is assumed to be temporary and safeguards
exist to prevent the election of a master node unless a `quorum`_ can be
established.

However, if the situation is permanent (i.e., you have irrecoverably lost a
majority of the nodes in your cluster), also known as a `split-brain`_ situation,
you will need to force the election of
a master. Forcing a master election without quorum is referred to as an *unsafe
cluster bootstrap*.

The :ref:`unsafe-bootstrap command <crate-reference:cli-crate-node-commands>`
can support you to choose a new master
node and subsequently perform an unsafe cluster bootstrap.

.. WARNING::

    An unsafe bootstrap should be your last resort.

    When you perform an unsafe bootstrap, you are effectively abandoning the
    data on any unreachable nodes. This may result in arbitrary data loss and
    inconsistencies.

    Before you attempt this, we recommend you try one or both of the following:

    1. Build a new cluster from a recent :ref:`snapshot <crate-reference:snapshot-restore>`
       and then re-import any
       data that was ingested since the snapshot was taken.

    2. Recreate lost nodes using a copy of the data kept in the
       :ref:`CRATE_HOME <crate-reference:conf-env>` directory, if you still
       have access to the file system.


.. rubric:: Procedure

Before you continue, you must stop all master-eligible nodes in the cluster.

.. CAUTION::

    The ``unsafe-bootstrap`` command will return an error message if the node
    you issue it from is still running. However, it does not check the running
    status of any other nodes in the cluster. You must verify the cluster state
    for yourself before proceeding.

Once all master-eligible nodes in the cluster have been stopped, you can
manually select a new master.

To support you selecting a new master node, the ``unsafe-bootstrap`` command
returns information about the node cluster state as a pair of values in the
form *(term, version)*.
You can gather this information (safely) by issuing the ``unsafe-bootstrap``
command and answering "no" (``n``) at the confirmation prompt.

.. code-block:: console

   sh$ ./bin/crate-node unsafe-bootstrap

   WARNING: CrateDB MUST be stopped before running this tool.

   Current node cluster state (term, version) pair is (4, 12)

   Do you want to proceed?

   Confirm [y/N] n

Here, the node cluster state has a term value of ``4`` and a version value of
``12``.

Run this command on every master-eligible node in the cluster (making sure to
answer "no" each time) and make a note of each respective value pair.

Once you're done, select the node with the highest term value. If multiple
nodes share the highest term value, select the one with the highest version
value. If multiple nodes share the highest term value and the highest version
value, select any one of them.

.. NOTE::

    Selecting the node with the highest state values (per the above) ensures
    that you elect a master node with the freshest state data. This, in turn,
    minimizes the potential for data loss and inconsistency.

Once you have selected a node to elect to master, invoke the ``unsafe-bootstrap``
command on that node and answer yes (``y``) at the confirmation prompt.

.. code-block:: console

    sh$ ./bin/crate-node unsafe-bootstrap

    WARNING: CrateDB MUST be stopped before running this tool.

    Current node cluster state (term, version) pair is (4, 12)

    Do you want to proceed?

    Confirm [y/N] y

If the operation was successful, the program will acknowledge it.
**Note:** This success message indicates that the operation was completed.
You may still experience data loss and inconsistencies.

.. code-block:: console

    Master node was successfully bootstrapped

Now, start the bootstrapped node and verify that it has started a new cluster with
one node and elected itself as the master.

Before you can add the rest of the nodes to the new cluster, you must detach
them from the old cluster (see the :ref:`next section
<crate-node-detach-cluster>`).

After that's done, start the nodes and verify that they join the new cluster.

.. NOTE::

    Once the new cluster is up-and-running and all recoveries are complete, you
    are advised to assess the database for data loss and inconsistencies.


.. _crate-node-detach-cluster:

Detach a node from its cluster
==============================

.. rubric:: About

To protect nodes from inadvertently rejoining the wrong cluster (e.g., in the
event of a network partition), each node binds to the first cluster it joins.

However, if a cluster has permanently failed (see the :ref:`previous section
<crate-node-unsafe-bootstrap>`) you must detach nodes before you can move them
to a a new cluster.

The :ref:`detach-cluster command <crate-reference:cli-crate-node-commands>`
supports you moving a node to a new
cluster by resetting the cluster it is bound to (i.e., *detaching* it from its
existing cluster).

.. WARNING::

    Do not attempt to move a node from one logical cluster to another. You
    cannot merge two clusters in this fashion.

    You should only detach a node subsequent to performing an :ref:`unsafe
    cluster bootstrap <crate-node-unsafe-bootstrap>`.


.. rubric:: Procedure

To detach a node, run:

.. code-block:: console

   sh$ ./bin/crate-node detach-cluster

   WARNING: CrateDB MUST be stopped before running this tool.

   Do you want to proceed?

   Confirm [y/N] y

A corresponding message confirms success.

.. code-block:: console

   Node was successfully detached from the cluster.

When the node is started again, it will be able to join a new cluster.

.. NOTE::

    You may also have to update the :ref:`discovery configuration
    <crate-reference:conf_discovery>`, so that
    nodes are able to find the new cluster.


.. _crate-node: https://cratedb.com/docs/crate/reference/en/latest/cli-tools.html#cli-crate-node
.. _data path: https://cratedb.com/docs/crate/reference/en/latest/config/environment.html#application-variables
.. _network partition: https://en.wikipedia.org/wiki/Network_partition
.. _node.data: https://cratedb.com/docs/crate/reference/en/latest/config/node.html#node-types
.. _node.master: https://cratedb.com/docs/crate/reference/en/latest/config/node.html#node-types
.. _quorum: https://cratedb.com/docs/crate/reference/en/latest/concepts/clustering.html#master-node-election
.. _role: https://cratedb.com/docs/crate/reference/en/latest/config/node.html#node-types
.. _split-brain: https://en.wikipedia.org/wiki/Split-brain_(computing)
.. _UUID: https://en.wikipedia.org/wiki/Universally_unique_identifier
