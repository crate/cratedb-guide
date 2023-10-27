=========================
Run CrateDB on Kubernetes
=========================

CrateDB is ideal for containerized environments, creating and scaling a cluster
takes minutes and your valuable data is always in sync and available.

Prerequisites
-------------

Both of following methods assume `familiarity with Kubernetes`_.

Before continuing you should already have a Kubernetes cluster up-and-running
with at least one master node and one worker node.

.. SEEALSO::

   You can use `kubeadm`_ to bootstrap a Kubernetes cluster by hand.

   Alternatively, cloud services such as `Azure Kubernetes Service`_ or the
   `Amazon Kubernetes Service`_ can do this for you.

Method 1 - Classic kubernetes
-----------------------------

Install the resources to run your CrateDB.

Method 2 - Kubernetes operator
------------------------------

You can also use the CrateDB custom resource and the Crate Operator to quickly
install your CrateDB.

.. rubric:: Table of contents

.. toctree::
   :maxdepth: 1

   kubernetes
   kubernetes-operator

.. _familiarity with Kubernetes: https://kubernetes.io/docs/tutorials/kubernetes-basics/
.. _kubeadm: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
.. _Azure Kubernetes Service: https://azure.microsoft.com/en-us/services/kubernetes-service/
.. _Amazon Kubernetes Service: https://aws.amazon.com/eks/
