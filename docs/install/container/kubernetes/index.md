# Run CrateDB on Kubernetes

CrateDB is ideal for containerized environments, creating and scaling a cluster
takes minutes and your valuable data is always in sync and available.

## Prerequisites

Both of following methods assume [familiarity with Kubernetes].

Before continuing you should already have a Kubernetes cluster up-and-running
with at least one master node and one worker node.

:::{SEEALSO}
You can use [kubeadm] to bootstrap a Kubernetes cluster by hand.

Alternatively, cloud services such as [Azure Kubernetes Service] or the
[Amazon Kubernetes Service] can do this for you.
:::

## Method 1 - Classic kubernetes

Install the resources to run your CrateDB.

## Method 2 - Kubernetes operator

You can also use the CrateDB custom resource and the Crate Operator to quickly
install your CrateDB.

```{rubric} Table of contents
```

```{toctree}
:maxdepth: 1

kubernetes
kubernetes-operator
```

[amazon kubernetes service]: https://aws.amazon.com/eks/
[azure kubernetes service]: https://azure.microsoft.com/en-us/services/kubernetes-service/
[familiarity with kubernetes]: https://kubernetes.io/docs/tutorials/kubernetes-basics/
[kubeadm]: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
