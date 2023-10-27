.. _cratedb-kubernetes-operator:

====================================
Run CrateDB with Kubernetes Operator
====================================

The `CrateDB Kubernetes Operator`_ provides a convenient way to run `CrateDB`_
clusters inside Kubernetes.

Using the operator we can just deploy a ``CrateDB`` resource without having to
deal with services, persistent volumes, persistent volume claims, and stateful
sets. The only prerequisite is to have a suitable storage class.

Installation
============

`Helm`_ must be installed to install the Crate operator chart.
Once Helm is set up properly, add the repo as follows:

.. code-block:: console

    $ helm repo add crate-operator https://crate.github.io/crate-operator

Install the crate-operator chart:

.. code-block:: console

    $ kubectl create namespace crate-operator

    $ helm install crate-operator crate-operator/crate-operator --namespace crate-operator --set env.CRATEDB_OPERATOR_DEBUG_VOLUME_STORAGE_CLASS=<YOUR-STORAGE-CLASS>

.. NOTE::

    ``kubectl get storageclass`` gives you an list of the available StorageClasses
    on your setup. Be careful with what you choose!


.. NOTE::

    To be able to deploy the custom resource ``CrateDB`` to a Kubernetes cluster,
    the API needs to be extended with a `Custom Resource Definition`_ (CRD).
    It is installed as a dependency of the ``crate-operator`` chart, but it can be
    installed separately. See the `Crate Operator Chart documentation`_ for
    further details.

Run CrateDB
===========

A minimal custom resource for a three-node CrateDB cluster may look like this:

``dev-cluster.yaml``:

.. code-block:: yaml

   apiVersion: cloud.crate.io/v1
   kind: CrateDB
   metadata:
     name: my-cluster
     namespace: dev
   spec:
     cluster:
       imageRegistry: crate
       name: crate-dev
       version: 5.0.1
     nodes:
       data:
       - name: my-cluster
         replicas: 3
         resources:
           limits:
             cpu: 4
             memory: 4Gi
           disk:
             count: 1
             size: 128GiB
             storageClass: <YOUR-STORAGE-CLASS>
           heapRatio: 0.25

.. NOTE::

   The operator imposes an affinity constraint of 1 CrateDB node per Kubernetes node.
   To deploy a CrateDB cluster with multiple nodes on a single machine for
   testing purposes, :ref:`manually deploy a StatefulSet <cratedb-kubernetes>`.


.. WARNING::

    Specifying a `cpu` number under `limits` is mandatory.
    
.. code-block:: console

   $ kubectl create namespace dev

   $ kubectl --namespace dev create -f dev-cluster.yaml
   ...

   $ kubectl --namespace dev get cratedbs
   NAMESPACE   NAME         AGE
   dev         my-cluster   36s

We can check the status of the deployment by looking at the latest events:

.. code-block:: console

   $ kubectl get events --sort-by='.lastTimestamp' -n dev
   
and the status of the pods:
  
.. code-block:: console

   $ kubectl get pods --namespace dev 

Once we have a pod running for each CrateDB node, the cluster
is ready. Congratulations!

The operator created a user named ``system`` for you and a Loadbalancer
to access the cluster.

.. code-block:: console

   $ kubectl get secret user-system-my-cluster -o json | jq -r '.data.password' | base64 -d

   $ kubectl get service crate-my-cluster -o json | jq -r '.status.loadBalancer.ingress[0].ip'

As an alternative you can access the cluster via ``kubectl port-forwarding``
to port ``4200``. Which allows you to authenticate with the `crate` user.

.. NOTE::

    You can find the Crate Operator features in the ``Features`` section
    of `CrateDB Kubernetes Operator`_.


.. _CrateDB Kubernetes Operator: https://github.com/crate/crate-operator
.. _CrateDB: https://github.com/crate/crate
.. _Helm: https://helm.sh
.. _Custom Resource Definition: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
.. _Crate Operator Chart documentation: https://github.com/crate/crate-operator/blob/master/deploy/charts/crate-operator/README.md
