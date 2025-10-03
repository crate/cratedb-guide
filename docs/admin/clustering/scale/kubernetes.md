(scaling-kube)=

# Scale CrateDB on Kubernetes

CrateDB and [Docker] are a great match thanks to CrateDB’s [horizontally
scalable][horizontally scalable] [shared-nothing architecture] that lends itself well to
[containerization].

[Kubernetes] is an open-source container orchestration system for the
management, deployment, and scaling of containerized systems.

Together, Docker and Kubernetes are a fantastic way to deploy and scale CrateDB.

:::{NOTE}
This guide assumes you have already deployed CrateDB on Kubernetes.

Consult the {ref}`Kubernetes deployment guide <cratedb-kubernetes>`
for more help.
:::

:::{SEEALSO}
A guide to {ref}`deploying CrateDB on Kubernetes <cratedb-kubernetes>`.

The official [CrateDB Docker image].
:::

(scaling-kube-kube)=

## Kubernetes reconfiguration

You can scale your CrateDB cluster by increasing or decreasing the configured
number of replica [pods] in your [StatefulSet] controller to the desired
number of CrateDB nodes.

(scaling-kube-command)=

### Using an imperative command

You can issue an [imperative command] to make the configuration change, like
so:

```console
sh$ kubectl scale statefulsets crate --replicas=4
```

:::{NOTE}
This makes it easy to scale quickly, but your cluster configuration is not
reflected in your [version control] system.
:::

(scaling-kube-vc)=

### Using version control

If you want to version control your cluster configuration, you can edit the
StatefulSet controller configuration file directly.

Take this example configuration snippet:

```yaml
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
```

The only thing you need to change here is the `replicas` value.

You can then save your edits and update Kubernetes, like so:

```console
sh$ kubectl replace -f crate-controller.yaml --namespace crate
statefulset.apps/crate replaced
```

Here, we're assuming a configuration file named `crate-controller.yaml` and a
deployment that uses the `crate` [namespace].

If your StatefulSet uses the default [rolling update strategy], this command will
restart your pods with the new configuration one-by-one.

:::{NOTE}
If you are making changes this way, you probably want to update the CrateDB
configuration at the same time. Consult the next section for details.
:::

:::{WARNING}
If you use a regular `replace` command, pods are restarted, and any
[persistent volumes] will still be intact.

If, however, you pass the `--force` option to the `replace` command,
resources are deleted and recreated, and the pods will come back up with no
data.
:::

(scaling-kube-cratedb)=

## CrateDB reconfiguration

CrateDB needs to be configured appropriately for the number of nodes in the
CrateDB cluster.

:::{WARNING}
Failing to update CrateDB configuration after a rescale operation can
result in data loss.

You should take particular care if you are reducing the size of the cluster
because CrateDB must recover and rebalance shards as the nodes drop out.
:::

(scaling-kube-clustering)=

### Clustering behavior

:::{NOTE}
The following only applies to CrateDB versions 3.x and below.

The [discovery.zen.minimum_master_nodes] setting is no longer used in CrateDB
versions 4.x and above. Please refer to the current documentation section
about {ref}`crate-reference:conf_discovery`.
:::

The [discovery.zen.minimum_master_nodes] setting affects {ref}`metadata
master <crate-reference:concept-clusters>` election with previous versions
of CrateDB.

This setting can be changed while CrateDB is running, like so:

```psql
SET GLOBAL PERSISTENT discovery.zen.minimum_master_nodes = 5
```

If you are using a controller configuration like the example given in the
{ref}`Kubernetes deployment guide <cratedb-kubernetes>`, you can make this
reconfiguration by altering the `discovery.zen.minimum_master_nodes` command
option.

Changes to the Kubernetes controller configuration can then be deployed using
`kubectl replace` as shown in the previous subsection, [Using Version
Control][using version control].

:::{CAUTION}
If [discovery.zen.minimum_master_nodes] is set to more than the current
number of nodes in the cluster, the cluster will disband. On the other
hand, a number that is too small might lead to a [split-brain] scenario.

Accordingly, it is important to adjust this number carefully when
scaling CrateDB.
:::

(scaling-kube-recovery)=

### Recovery behavior

CrateDB has two settings that depend on cluster size and determine how cluster
[metadata] is recovered during startup:

- [gateway.expected_data_nodes]
- [gateway.recover_after_data_nodes]

The values of these settings must be changed via Kubernetes. Unlike with
clustering behavior reconfiguration, you cannot change these values using
CrateDB's {ref}`runtime configuration <crate-reference:administration-runtime-config>`
capabilities.

If you are using a controller configuration like the example given in the
{ref}`Kubernetes deployment guide <cratedb-kubernetes>`, you can make this
reconfiguration by altering the `EXPECTED_NODES` environment variable and the
`recover_after_data_nodes` command option.

Changes to the Kubernetes controller configuration can then be deployed using
`kubectl replace` as shown in the previous subsection, [Using Version
Control][using version control].

:::{NOTE}
You can scale a CrateDB cluster without updating these values, but the
{ref}`CrateDB Admin UI <crate-admin-ui:index>` will display
{ref}`node check <crate-reference:sys-node-checks-settings>` failures.

However, you should only do this on a production cluster if you need to
scale to handle a load spike quickly.
:::


[containerization]: https://www.docker.com/resources/what-container
[cratedb docker image]: https://hub.docker.com/_/crate/
[deleted and recreated]: https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#disruptive-updates
[discovery.zen.minimum_master_nodes]: https://github.com/crate/crate/blob/3.3/blackbox/docs/config/cluster.rst#discovery
[docker]: https://www.docker.com/
[gateway.expected_data_nodes]: https://cratedb.com/docs/crate/reference/en/latest/admin/system-information.html#recovery-expected-data-nodes
[gateway.recover_after_data_nodes]: https://cratedb.com/docs/crate/reference/en/latest/admin/system-information.html#recovery-after-data-nodes
[horizontally scalable]: https://en.wikipedia.org/wiki/Scalability#Horizontal_(scale_out)_and_vertical_scaling_(scale_up)
[imperative command]: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/#imperative-commands
[kubectl]: https://kubernetes.io/docs/reference/kubectl/overview/
[kubernetes]: https://kubernetes.io/
[metadata]: https://cratedb.com/docs/crate/reference/en/latest/config/cluster.html#metadata
[namespace]: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
[persistent volumes]: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
[pods]: https://kubernetes.io/docs/concepts/workloads/pods/
[rolling update strategy]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#rolling-updates
[shared-nothing architecture]: https://en.wikipedia.org/wiki/Shared-nothing_architecture
[split-brain]: https://en.wikipedia.org/wiki/Split-brain
[statefulset]: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
[version control]: https://en.wikipedia.org/wiki/Version_control
