.. _scaling-kube:

===========================
Scale CrateDB on Kubernetes
===========================

CrateDB and `Docker`_ are a great match thanks to CrateDB’s `horizontally
scalable`_ `shared-nothing architecture`_ that lends itself well to
`containerization`_.

`Kubernetes`_ is an open-source container orchestration system for the
management, deployment, and scaling of containerized systems.

Together, Docker and Kubernetes are a fantastic way to deploy and scale CrateDB.

.. NOTE::

    This guide assumes you have already deployed CrateDB on Kubernetes.

    Consult the :ref:`Kubernetes deployment guide <cratedb-kubernetes>`
    for more help.

.. SEEALSO::

    A guide to :ref:`deploying CrateDB on Kubernetes <cratedb-kubernetes>`.

    The official `CrateDB Docker image`_.


.. _scaling-kube-kube:

Kubernetes reconfiguration
==========================

You can scale your CrateDB cluster by increasing or decreasing the configured
number of replica `pods`_ in your `StatefulSet`_ controller to the desired
number of CrateDB nodes.


.. _scaling-kube-command:

Using an imperative command
---------------------------

You can issue an `imperative command`_ to make the configuration change, like
so:

.. code-block:: console

    sh$ kubectl scale statefulsets crate --replicas=4

.. NOTE::

    This makes it easy to scale quickly, but your cluster configuration is not
    reflected in your `version control`_ system.


.. _scaling-kube-vc:

Using version control
---------------------

If you want to version control your cluster configuration, you can edit the
StatefulSet controller configuration file directly.

Take this example configuration snippet:

.. code-block:: yaml

    kind: StatefulSet
    apiVersion: "apps/v1"
    metadata:
      # This is the name used as a prefix for all pods in the set.
      name: crate
    spec:
      serviceName: "crate-set"
      # Our cluster has three nodes.
      replicas: 4
    [...]

The only thing you need to change here is the ``replicas`` value.

You can then save your edits and update Kubernetes, like so:

.. code-block:: console

    sh$ kubectl replace -f crate-controller.yaml --namespace crate
    statefulset.apps/crate replaced

Here, we're assuming a configuration file named ``crate-controller.yaml`` and a
deployment that uses the ``crate`` `namespace`_.

If your StatefulSet uses the default `rolling update strategy`_, this command will
restart your pods with the new configuration one-by-one.

.. NOTE::

    If you are making changes this way, you probably want to update the CrateDB
    configuration at the same time. Consult the next section for details.

.. WARNING::

    If you use a regular ``replace`` command, pods are restarted, and any
    `persistent volumes`_ will still be intact.

    If, however, you pass the ``--force`` option to the ``replace`` command,
    resources are deleted and recreated, and the pods will come back up with no
    data.


.. _scaling-kube-cratedb:

CrateDB reconfiguration
=======================

CrateDB needs to be configured appropriately for the number of nodes in the
CrateDB cluster.

.. WARNING::

    Failing to update CrateDB configuration after a rescale operation can
    result in data loss.

    You should take particular care if you are reducing the size of the cluster
    because CrateDB must recover and rebalance shards as the nodes drop out.


.. _scaling-kube-clustering:

Clustering behavior
-------------------

.. NOTE::

   The following only applies to CrateDB versions 3.x and below.

   The ``discovery.zen.minimum_master_nodes`` setting is :ref:`no longer used
   <node-discovery>` in CrateDB versions 4.x and above.

The `discovery.zen.minimum_master_nodes`_ setting affects :ref:`metadata
master <crate-reference:concept-clusters>` election.

This setting can be changed while CrateDB is running, like so:

.. code-block:: psql

    SET GLOBAL PERSISTENT discovery.zen.minimum_master_nodes = 5

If you are using a controller configuration like the example given in the
:ref:`Kubernetes deployment guide <cratedb-kubernetes>`, you can make this
reconfiguration by altering the ``discovery.zen.minimum_master_nodes`` command
option.

Changes to the Kubernetes controller configuration can then be deployed using
``kubectl replace`` as shown in the previous subsection, `Using Version
Control`_.

.. CAUTION::

    If ``discovery.zen.minimum_master_nodes`` is set to more than the current
    number of nodes in the cluster, the cluster will disband. On the other
    hand, a number that is too small might lead to a `split-brain`_ scenario.

    Accordingly, it is important to `adjust this number carefully`_ when
    scaling CrateDB.


.. _scaling-kube-recovery:

Recovery behavior
-----------------

CrateDB has two settings that depend on cluster size and determine how cluster
`metadata`_ is recovered during startup:

- `gateway.expected_data_nodes`_
- `gateway.recover_after_data_nodes`_

The values of these settings must be changed via Kubernetes. Unlike with
clustering behavior reconfiguration, you cannot change these values using
CrateDB's :ref:`runtime configuration <crate-reference:administration-runtime-config>`
capabilities.

If you are using a controller configuration like the example given in the
:ref:`Kubernetes deployment guide <cratedb-kubernetes>`, you can make this
reconfiguration by altering the ``EXPECTED_NODES`` environment variable and the
``recover_after_data_nodes`` command option.

Changes to the Kubernetes controller configuration can then be deployed using
``kubectl replace`` as shown in the previous subsection, `Using Version
Control`_.

.. NOTE::

    You can scale a CrateDB cluster without updating these values, but the
    :ref:`CrateDB Admin UI <crate-admin-ui:index>` will display
    :ref:`node check <crate-reference:sys-node-checks-settings>` failures.

    However, you should only do this on a production cluster if you need to
    scale to handle a load spike quickly.


.. _adjust this number carefully: https://cratedb.com/docs/crate/reference/en/3.3/config/cluster.html#discovery-zen-minimum-master-nodes
.. _containerization: https://www.docker.com/resources/what-container
.. _CrateDB Docker image: https://hub.docker.com/_/crate/
.. _deleted and recreated: https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#disruptive-updates
.. _discovery.zen.minimum_master_nodes: https://cratedb.com/docs/crate/reference/en/3.3/config/cluster.html#discovery-zen-minimum-master-nodes
.. _Docker: https://www.docker.com/
.. _gateway.expected_data_nodes: https://cratedb.com/docs/crate/reference/en/latest/admin/system-information.html#recovery-expected-data-nodes
.. _gateway.recover_after_data_nodes: https://cratedb.com/docs/crate/reference/en/latest/admin/system-information.html#recovery-after-data-nodes
.. _horizontally scalable: https://en.wikipedia.org/wiki/Scalability#Horizontal_(scale_out)_and_vertical_scaling_(scale_up)
.. _imperative command: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/#imperative-commands
.. _kubectl: https://kubernetes.io/docs/reference/kubectl/overview/
.. _Kubernetes: https://kubernetes.io/
.. _metadata: https://cratedb.com/docs/crate/reference/en/latest/config/cluster.html#metadata
.. _namespace: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
.. _persistent volumes: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
.. _pods: https://kubernetes.io/docs/concepts/workloads/pods/
.. _rolling update strategy: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#rolling-updates
.. _shared-nothing architecture : https://en.wikipedia.org/wiki/Shared-nothing_architecture
.. _split-brain: https://en.wikipedia.org/wiki/Split-brain
.. _StatefulSet: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
.. _version control: https://en.wikipedia.org/wiki/Version_control
