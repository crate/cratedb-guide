.. _cratedb-kubernetes:

======================
CrateDB and Kubernetes
======================

CrateDB and `Docker`_ are a great match thanks to CrateDB’s `horizontally
scalable`_ `shared-nothing architecture`_ that lends itself well to
`containerization`_.

`Kubernetes`_ is an open-source container orchestration system for the
management, deployment, and scaling of containerized systems.

Together, Docker and Kubernetes are a fantastic way to deploy and scale CrateDB.

.. NOTE::

   While Kubernetes works with a variety of container technologies, this
   document only covers its use with Docker.

.. SEEALSO::

    A complimentary blog post miniseries that walks you through the process of
    `setting up your first CrateDB cluster on Kubernetes`_.

    A lower-level introduction to :ref:`running CrateDB on Docker <cratedb-docker>`.

    A guide to :ref:`scaling CrateDB on Kubernetes <scaling-kube>`.

    The official `CrateDB Docker image`_.


Managing Kubernetes
===================

Kubernetes deployments can be `managed`_ in many different ways. Which one
makes sense for you will depend on your situation.

This section shows you three basic commands you can use to create and update a
resource.

You can create a resource like so:

.. code-block:: console

     sh$ kubectl create -f crate-controller.yaml --namespace crate
     statefulset.apps/crate-controller created

Here, we are creating a `StatefulSet`_ controller in the ``crate`` namespace
using a configuration file named ``crate-controller.yaml``.

You can update the resource after editing the configuration file, like so:

.. code-block:: console

    sh$ kubectl replace -f crate-controller.yaml --namespace crate
    statefulset.apps/crate replaced

If your StatefulSet uses the default `rolling update strategy`_, this command will
restart your pods with the new configuration one-by-one.

.. WARNING::

    If you use a regular ``replace`` command, pods are restarted, and any
    `persistent volumes`_ will still be intact.

    If, however, you pass the ``--force`` option to the ``replace`` command,
    resources are deleted and recreated, and the pods will come back up with no
    data.


Configuration
=============

This section provides four Kubernetes `configuration`_ snippets that can be
used to create a three-node CrateDB cluster.


Services
--------

A Kubernetes pod is ephemeral and so are its network addresses. Typically, this
means that it is inadvisable to connect to pods directly.

A Kubernetes `service`_ allows you to define a network access policy for a set
of pods. You can then use the network address of the service to communicate
with the pods. The network address of the service remains static even though the
constituent pods may come and go.

For our purposes, we define two services: an `internal service`_ and an
`external service`_.


Internal service
................

CrateDB uses the internal service for :ref:`node discovery via DNS
<crate-reference:conf_dns_discovery>` and :ref:`inter-node communication
<inter-node-comms>`.

Here's an example configuration snippet:

.. code-block:: yaml

    kind: Service
    apiVersion: v1
    metadata:
      name: crate-internal-service
      labels:
        app: crate
    spec:
      # A static IP address is assigned to this service. This IP address is
      # only reachable from within the Kubernetes cluster.
      type: ClusterIP
      ports:
        # Port 4300 for inter-node communication.
      - port: 4300
        name: crate-internal
      selector:
        # Apply this to all nodes with the `app:crate` label.
        app: crate


External service
................

The external service provides a stable network address for external clients.

Here's an example configuration snippet:

.. code-block:: yaml

    kind: Service
    apiVersion: v1
    metadata:
      name: crate-external-service
      labels:
        app: crate
    spec:
      # Create an externally reachable load balancer.
      type: LoadBalancer
      ports:
        # Port 4200 for HTTP clients.
      - port: 4200
        name: crate-web
        # Port 5432 for PostgreSQL wire protocol clients.
      - port: 5432
        name: postgres
      selector:
        # Apply this to all nodes with the `app:crate` label.
        app: crate

.. NOTE::

   In production, a `LoadBalancer`_ service type is typically only available on
   hosted cloud platforms that provide externally managed load balancers.
   However, an `ingress`_ resource can be used to provide internally managed
   load balancers.

   For local development, `Minikube`_ provides a LoadBalancer service.


Controller
----------

A Kubernetes `pod`_ is a group of one or more containers. Pods are designed to
provide discrete units of functionality.

CrateDB nodes are self-contained, so we don't need to use more than one
container in a pod. We can configure our pods as a single container running
CrateDB.

Pods are designed to be fungible computing units, meaning they can be created or
destroyed at will. This, in turn, means that:

- A cluster can be scaled in or out by destroying or creating pods

- A cluster can be healed by replacing pods

- A cluster can be rebalanced by rescheduling pods (i.e., destroying the pod on
  one Kubernetes node and recreating it on a new node)

However, CrateDB nodes that leave and then want to rejoin a cluster must retain
their state. That is, they must continue to use the same name and must continue
to use the same data on disk.

For this reason, we use the `StatefulSet`_ controller to define our cluster,
which ensures that CrateDB nodes retain state across restarts or rescheduling.

The following configuration snippet defines a controller for a three-node
CrateDB 5.1.1 cluster:

.. code-block:: yaml

    kind: StatefulSet
    apiVersion: "apps/v1"
    metadata:
      # This is the name used as a prefix for all pods in the set.
      name: crate
    spec:
      serviceName: "crate-set"
      # Our cluster has three nodes.
      replicas: 3
      selector:
        matchLabels:
          # The pods in this cluster have the `app:crate` app label.
          app: crate
      template:
        metadata:
          labels:
            app: crate
        spec:
          # InitContainers run before the main containers of a pod are
          # started, and they must terminate before the primary containers
          # are initialized. Here, we use one to set the correct memory
          # map limit.
          initContainers:
          - name: init-sysctl
            image: busybox
            imagePullPolicy: IfNotPresent
            command: ["sysctl", "-w", "vm.max_map_count=262144"]
            securityContext:
              privileged: true
          # This final section is the core of the StatefulSet configuration.
          # It defines the container to run in each pod.
          containers:
          - name: crate
            # Use the CrateDB 5.1.1 Docker image.
            image: crate:5.1.1
            # Pass in configuration to CrateDB via command-line options.
            # We are setting the name of the node's explicitly, which is
            # needed to determine the initial master nodes. These are set to
            # the name of the pod.
            # We are using the SRV records provided by Kubernetes to discover
            # nodes within the cluster.
            args:
              - -Cnode.name=${POD_NAME}
              - -Ccluster.name=${CLUSTER_NAME}
              - -Ccluster.initial_master_nodes=crate-0,crate-1,crate-2
              - -Cdiscovery.seed_providers=srv
              - -Cdiscovery.srv.query=_crate-internal._tcp.crate-internal-service.${NAMESPACE}.svc.cluster.local
              - -Cgateway.recover_after_data_nodes=2
              - -Cgateway.expected_data_nodes=${EXPECTED_NODES}
              - -Cpath.data=/data
            volumeMounts:
                  # Mount the `/data` directory as a volume named `data`.
                - mountPath: /data
                  name: data
            resources:
              limits:
                # How much memory each pod gets.
                memory: 512Mi
            ports:
              # Port 4300 for inter-node communication.
            - containerPort: 4300
              name: crate-internal
              # Port 4200 for HTTP clients.
            - containerPort: 4200
              name: crate-web
              # Port 5432 for PostgreSQL wire protocol clients.
            - containerPort: 5432
              name: postgres
            # Environment variables passed through to the container.
            env:
              # This is variable is detected by CrateDB.
            - name: CRATE_HEAP_SIZE
              value: "256m"
              # The rest of these variables are used in the command-line
              # options.
            - name: EXPECTED_NODES
              value: "3"
            - name: CLUSTER_NAME
              value: "my-crate"
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
      volumeClaimTemplates:
        # Use persistent storage.
        - metadata:
            name: data
          spec:
            accessModes:
            - ReadWriteOnce
            resources:
              requests:
                storage: 1Gi

.. CAUTION::

   If you are not running CrateDB 5.1.1, you must adapt this example
   configuration to your specific CrateDB version.

.. SEEALSO::

   CrateDB supports :ref:`configuration via command-line options
   <crate-reference:config>` and :ref:`node discovery via DNS
   <crate-reference:conf_dns_discovery>`.

   Explicitly :ref:`configure heap memory <memory>` for optimum performance.

   You must set memory map limits correctly. Consult the :ref:`bootstrap checks
   <bootstrap-checks>` documentation for more information.


Persistent volume
-----------------

As mentioned in the `Controller`_ section, CrateDB containers must be able to
retain state between restarts and rescheduling. Stateful containers can be
achieved with `persistent volumes`_.

Persistent volumes can be provisioned in many different ways, so the specific
configuration will depend on your setup.


Microsoft Azure
...............

You can create a `StorageClass`_ for `Azure Managed Disks`_ with a
configuration snippet like this:

.. code-block:: yaml

    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      labels:
        addonmanager.kubernetes.io/mode: Reconcile
        app.kubernetes.io/managed-by: kube-addon-manager
        app.kubernetes.io/name: crate-premium
        app.kubernetes.io/part-of: infrastructure
        app.kubernetes.io/version: "0.1"
        storage-tier: premium
        volume-type: ssd
      name: crate-premium
    parameters:
      kind: Managed
      storageaccounttype: Premium_LRS
    provisioner: kubernetes.io/azure-disk
    reclaimPolicy: Delete
    volumeBindingMode: Immediate

You can then use this in your controller configuration with something like this:

.. code-block:: yaml

    [...]
      volumeClaimTemplates:
        - metadata:
            name: persistant-data
          spec:
            # This will create one 100GB read-write Azure Managed Disks volume
            # for every CrateDB pod.
            accessModes: [ "ReadWriteOnce" ]
            storageClassName: crate-premium
            resources:
              requests:
                storage: 100g

.. _Azure Managed Disks: https://azure.microsoft.com/en-us/pricing/details/managed-disks/
.. _configuration: https://kubernetes.io/docs/concepts/configuration/overview/
.. _containerization: https://www.docker.com/resources/what-container
.. _CrateDB Docker image: https://hub.docker.com/_/crate/
.. _Docker: https://www.docker.com/
.. _horizontally scalable: https://en.wikipedia.org/wiki/Scalability#Horizontal_(scale_out)_and_vertical_scaling_(scale_up)
.. _Ingress: https://kubernetes.io/docs/concepts/services-networking/ingress/
.. _Kubernetes: https://kubernetes.io/
.. _LoadBalancer: https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer
.. _managed: https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/
.. _Minikube: https://kubernetes.io/docs/setup/minikube/
.. _persistent volume: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
.. _persistent volumes: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
.. _pod: https://kubernetes.io/docs/concepts/workloads/pods/
.. _rolling update strategy: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#rolling-updates
.. _service: https://kubernetes.io/docs/concepts/services-networking/service/
.. _services: https://kubernetes.io/docs/concepts/services-networking/service/
.. _setting up your first CrateDB cluster on Kubernetes: https://cratedb.com/blog/run-your-first-cratedb-cluster-on-kubernetes-part-one
.. _shared-nothing architecture : https://en.wikipedia.org/wiki/Shared-nothing_architecture
.. _StatefulSet: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
.. _StorageClass: https://kubernetes.io/docs/concepts/storage/storage-classes/
