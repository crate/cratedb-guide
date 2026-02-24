(going-into-production)=

# Going into production

Running CrateDB in different environments requires different approaches. This
document outlines the basics you need to consider when going into production.

(prod-bootstrapping)=

## Configure bootstrapping

The process of forming a cluster is known as *bootstrapping*. Consult the
how-to guide on {ref}`CrateDB multi-node setups <multi-node-setup>` for an
overview of the two different ways to bootstrap a cluster.

If you have been using CrateDB for development on your local machine, there is
a good chance you have been using {ref}`single host auto-bootstrapping
<auto-bootstrapping>`.

For improved performance and resiliency, you should run production CrateDB
clusters with three or more nodes and one node per host machine. To do this,
you must manually configure the bootstrapping process by telling nodes how to:

1. {ref}`Discover other nodes <node-discovery>`, more details at
   {ref}`node discovery <crate-reference:concept-discovery>`.
2. {ref}`Elect a master node <master-node-election>`, more details at
   {ref}`master node election <crate-reference:concept-master-election>`.

This process is known as *manual bootstrapping*. See the {ref}`how-to guide
<manual-bootstrapping>` for more information about how to bootstrap a cluster
manually.

Switching to a manual bootstrapping configuration is the first step towards
going into production.

(prod-naming)=

## Naming

(prod-cluster-name)=

### Configure a logical cluster name

The {ref}`crate-reference:cluster.name` setting allows you to override the
default cluster name of `crate`. You should use this setting to give a
logical name to your cluster.

For example, add this to your [configuration] file:

```yaml
cluster.name: acme-prod
```

The `acme-prod` name suggests that this cluster is the production cluster for
the *Acme* organization. If *Acme* has a cluster running in a staging
environment, you might want to name it `acme-staging`. This way, you can
differentiate your clusters by name (visible in the {ref}`Admin UI
<crate-admin-ui:index>`).

:::{TIP}
A node will refuse to join a cluster if the respective cluster names
do not match
:::

:::{SEEALSO}
{ref}`Cluster names for multi-node setups <multi-node-cluster-name>`
:::

(prod-config-hostname)=

### Bind nodes to logical hostnames

By default, CrateDB binds to the loopback address (i.e., [localhost]). It
listens on port 4200-4299 for HTTP traffic and port 4300-4399 for node-to-node
communication. Because CrateDB uses a port range, if one port is busy, it will
automatically try the next port.

When using {ref}`multiple hosts <multi-node-setup>`, nodes must bind to a
non-loopback address.

:::{CAUTION}
Never expose an unprotected CrateDB node to the public internet
:::

You can bind to a non-loopback address with the [network.host] setting in your
[configuration] file, like so:

```yaml
network.host: node-01-md.acme-prod.internal.example.com
```

You must configure the `node-01-md.acme-prod.internal.example.com` hostname
using DNS. You must then set [network.host] to match the DNS name.

You should use the hostname to describe each node logically. To this end, the
example hostname (above) has four components:

- `example.com` -- The root domain name
- `internal` -- The internal private network
- `acme-prod` -- The cluster name
- `node-01-md` -- The {ref}`node label <prod-config-node-labels>`

When CrateDB is bound to a non-loopback address, CrateDB will enforce the
{ref}`bootstrap checks <bootstrap-checks>`. These checks may require changes to
your operating system configuration.

:::{SEEALSO}
{ref}`Host settings <crate-reference:conf_hosts>`
:::

(prod-config-node-labels)=

#### Logical node labels

CrateDB supports [multiple types of node], determined by the `node.master`
and `node.data` settings. You can use this information to give a logical DNS
label to each of your nodes.

(node-name-match)=

:::{TIP}
CrateDB {ref}`sets node names automatically <multi-node-node-name>`. If you
are happy with automatic node names, there is no need to set [node.name]
and hence you can use the same [configuration] on every node.

When {ref}`configuring cluster bootstrapping <prod-bootstrapping>`, you can
{ref}`specify the list of master-eligible nodes <master-node-election>`
using hostnames. This allows you to configure logical hostnames with DNS node
labels that differ from the node name set by CrateDB.

If you would prefer your node names to match your DNS node labels, you will
have to configure [node.name] manually on each host.
:::

:::{SEEALSO}
{ref}`Node names for multi-node setups <multi-node-node-name>`
:::

(prod-node-md)=

##### Multi-purpose nodes

You can [configure] a master-eligible node that also handles query execution
loads like this:

```yaml
node.master: true
node.data: true
```

A good DNS label for this node might be `node-01-md`.

Here, `node` is used as base label with a sequence number of `01`. Every
node in the cluster should have a unique sequence number, independent of the
node type. The letters `md` indicate that this node has `node.master` and
`node.data` set to `true`.

If you optionally want your node name to match ({ref}`see above
<node-name-match>`), configure the [node.name] setting in your
[configuration] file, like so:

```yaml
node.name: node-01-md
```

Alternatively, you can configure this setting at startup with a command-line
option:

```console
sh$ bin/crate \
        -Cnode.name=node-01-md
```

(prod-node-d)=

##### Request handling and query execution nodes

You can [configure] a node that only handles client requests and query
execution (i.e., is not master-eligible) like this:

```yaml
node.master: false
node.data: true
```

A good DNS label for this node might be `node-02-d`.

Here, `node` is used as base label with a sequence number of `02`. Every
node in the cluster should have a unique sequence number, independent of the
node type. The letter `d` indicates that this node has `node.data` set to
`true`.

If you optionally want your node name to match ({ref}`see above
<node-name-match>`), configure the [node.name] setting in your
[configuration] file, like so:

```yaml
node.name: node-02-d
```

Alternatively, you can configure this setting at startup with a command-line
option:

```console
sh$ bin/crate \
        -Cnode.name=node-02-d
```

(prod-node-m)=

##### Cluster management nodes

You can [configure] a node that handles cluster management (i.e., is
master-eligible) but does not handle query execution loads like this:

```yaml
node.master: true
node.data: false
```

A good DNS label for this node might be `node-03-m`.

Here, `node` is used as base label with a sequence number of `03`. Every
node in the cluster should have a unique sequence number, independent of the
node type. The letter `m` indicates that this node has `node.master` set to
`true`.

If you optionally want your node name to match ({ref}`see above
<node-name-match>`), configure the [node.name] setting in your
[configuration] file, like so:

```yaml
node.name: node-03-m
```

Alternatively, you can configure this setting at startup with a command-line
option:

```console
sh$ bin/crate \
        -Cnode.name=node-03-m
```

(prod-node)=

##### Request handling nodes

You can [configure] a node that handles client requests but does not handle query
execution loads or cluster management (i.e., is not master-eligible) like this:

```yaml
node.master: false
node.data: false
```

A good DNS label for this node might be `node-04`.

Here, `node` is used as base label with a sequence number of `04`. Every
node in the cluster should have a unique sequence number, independent of the
node type. The absence of any additional letters indicates that `node.master`
and `node.data` are `false`.

If you optionally want your node name to match ({ref}`see above
<node-name-match>`), configure the [node.name] setting in your
[configuration] file, like so:

```yaml
node.name: node-04
```

Alternatively, you can configure this setting at startup with a command-line
option:

```console
sh$ bin/crate \
        -Cnode.name=node-04
```

(prod-config-paths)=

## Configure persistent data paths

By default, CrateDB keeps data under the [CRATE_HOME] directory (which
defaults to the installation directory). When you upgrade CrateDB, you will
have to switch to a new installation directory.

Instead of migrating data by hand each time, you should move the data
directories off to a persistent location. You can do this using the
[CRATE_HOME] environment variable and the [path settings] in your
[configuration] file.

:::{SEEALSO}
[Path settings]
:::

If you are following the [shared-nothing] approach to deployment, the best way
to handle persistent data is to keep it on an external volume. This allows you
to persist data beyond the lifespan of an individual virtual machine or
container.

:::{CAUTION}
This is required if you are using Docker, which is stateless by design.
Failing to persist data to a mounted volume will result in data loss when
the container is stopped.
:::

:::{TIP}
Using an external volume for persistence also allows you to optimize the
underlying storage mechanism for performance.

You should take care to size your data storage volumes according to your
needs. You should also use storage with high [IOPS] when possible to
improve CrateDB performance.
:::

On a [Unix-like] system, you might mount an external volume to a path like
`/opt/cratedb`. If you are installing CrateDB by hand, you can then set
[CRATE_HOME] to `/opt/cratedb`. Make sure to set `CRATE_HOME` before
running {ref}`bin/crate <crate-reference:cli-crate>`.

Then, you could configure your [data paths] like this:

```yaml
path.conf: /opt/cratedb/config
path.data: /opt/cratedb/data
path.logs: /opt/cratedb/logs
path.repo: /opt/cratedb/snapshots
```

Here, the values given for `path.conf`, `path.data`, and `path.logs`
reflect the default paths when `CRATE_HOME` is set to `/opt/cratedb`. The
example above configures them for illustrative purposes. You do not have to
configure these settings if you are happy with the defaults.

:::{NOTE}
Normally, configuration files, data files, log files, and so on would be
kept under specialized directories such as `/etc`, `/var/lib`, and
`/var/log` (see the [Linux Filesystem Hierarchy] for more information).

However, if you want to customize your installation to make use of a single
external volume, it is necessary to bring these directories together under
a single mount point. You can do this by relocating all data directories
under your mount point (`/opt/cratedb` in the example above). Other
approaches are possible (for example, using [symbolic links]).

If you have installed CrateDB using a system package for {ref}`Debian
<debian>`, {ref}`Ubuntu <ubuntu>`, or {ref}`Red Hat <red-hat>`, the
[CRATE_HOME] variable (as well as some data paths) are configured for by
the [systemd] *service file*. You can view the `crate` service file,
like so:

```console
sh$ systemctl cat crate
```
:::

(prod-jvm)=

## Tune the JVM

(prod-config-heap)=

### Heap

CrateDB is a Java application running on top of a Java Virtual Machine (JVM).
The JVM uses a heap for memory allocations. For optimal performance, you must
pay special attention to your {ref}`heap configuration <memory>`.

By default, CrateDB configures the JVM to dump out-of-memory exceptions to the
file or directory specified by [CRATE_HEAP_DUMP_PATH]. You must make sure
there is enough disk space available for heap dumps at this location.

:::{SEEALSO}
{ref}`JVM environment variables <crate-reference:conf-env-java>`
:::

(prod-config-gc)=

### Garbage collection

CrateDB logs JVM garbage collection times using the built-in *garbage
collection* (GC) logging provided by the JVM. You can configure this process
with the {ref}`GC logging environment variables <conf-logging-gc>`.

You must ensure that the log directory is on a fast-enough disk and has enough
space. When using Docker, use a path on a mounted volume.

If garbage collection takes too long, CrateDB will log this. You can adjust the
[timeout settings] to suit your needs. However, the default settings should
work in most instances.

If you are running CrateDB on Docker, you should configure the container to
send debug logs to [STDERR] so that the container orchestrator handles the
output.

(prod-wire-encryption)=

## Configure wire encryption

For security reasons, most production clusters should use wire encryption for
network traffic between nodes and clients. Check out the reference manual on
{ref}`secured communications <crate-reference:admin_ssl>` for more information.

(prod-monitoring)=

## Operational readiness

Going into production is not a one-time step. Operating CrateDB reliably
requires continuous monitoring, maintenance, and lifecycle management.
The following checklist highlights important aspects to consider for production clusters.

- **Cluster health and capacity management**
  - **Shard sizes:** Monitor your shard sizes to remain around 50 GB ({ref}`sharding-partitioning`). Especially for partitioned tables, observe how your data volume changes over time.
  - **Disk usage:** If the {ref}`low watermark threshold <cluster.routing.allocation.disk.watermark.low>` is exceeded, CrateDB will no longer allocate new shards on affected nodes. Monitor your disk usage to guarantee seamless shard allocation.
  - **Shard count per node:** The number of open shards per node is limited. Monitor your shard count to prevent exceeding {ref}`cluster.max_shards_per_node`.
  - **Cluster and node health:** Several system tables expose the status of various health checks. Regularly check {ref}`sys-node-checks`, {ref}`sys-health`, and {ref}`sys-cluster_health`.
- **Lifecycle and maintenance management**
  - **Keep CrateDB up-to-date:** Regularly upgrade CrateDB to stay within supported versions. Consult the [Support Terms] regarding end-of-life policies.
  - **Keep your ecosystem up-to-date:** Keep drivers, frameworks, and other tools within versions that are supported by their respective providers.
  - **Data hygiene:** Delete data you no longer need, such as old partitions, columns, or deprecated tables.
- **Disaster scenarios and planning**
  - **Plan scenarios:** Actively think about failure scenarios you want to be protected against and their implications on your setup, such as {ref}`replication <ddl-replication>`, number of nodes, {ref}`multi-zone setup <multi-zone-setup>`, etc.
  - **Practice recovery:** Test your contingency plans, observe how CrateDB and other components in your stack behave and ensure you have error logging, retries, the ability to replay ingestion payloads, and similar mechanisms in place.
- **Self-managed: additional requirements** (if you are not using CrateDB Cloud)
  - **Monitoring:** Have both operating system/container-level metrics such as CPU, I/O, memory, and network-related metrics available, as well as CrateDB's own {ref}`jmx_monitoring`.
  - **Snapshots:** Regular {ref}`snapshots <snapshot-restore>` enable point-in-time recovery.
  - **Infrastructure lifecycle:** Apply regular updates to your operating system, container runtime, etc. as well. If you are running in the cloud, switch to recent VM and storage generations.
  - **TLS certificates:** When using wire encryption, renew your certificates in time to prevent communication breakdowns.
- **Support readiness**
  - When engaging with CrateDB support, have logs and monitoring metrics ready to share. In certain situations, CrateDB support may also ask for a {ref}`jfr`, {ref}`heap dump <jcmd>`, or [system table export].

[configuration]: inv:crate-reference#config
[configure]: inv:crate-reference#config
[crate_heap_dump_path]: inv:crate-reference#conf-env-dump-path
[crate_home]: inv:crate-reference#conf-env-crate-home
[data paths]: https://cratedb.com/docs/crate/reference/en/latest/config/node.html#paths
[iops]: https://en.wikipedia.org/wiki/IOPS
[linux filesystem hierarchy]: https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/
[localhost]: https://en.wikipedia.org/wiki/Localhost
[multiple types of node]: https://cratedb.com/docs/crate/reference/en/latest/config/node.html#node-types
[network.host]: inv:crate-reference#network.host
[node.name]: inv:crate-reference#node.name
[path settings]: https://cratedb.com/docs/crate/reference/en/latest/config/node.html#paths
[shared-nothing]: https://en.wikipedia.org/wiki/Shared-nothing_architecture
[stderr]: https://en.wikipedia.org/wiki/Standard_streams
[symbolic links]: https://en.wikipedia.org/wiki/Symbolic_link
[systemd]: https://github.com/systemd/systemd
[timeout settings]: https://cratedb.com/docs/crate/reference/en/latest/config/node.html#garbage-collection
[unix-like]: https://en.wikipedia.org/wiki/Unix-like
[support terms]: https://cratedb.com/legal/support-terms
[system table export]: https://cratedb-toolkit.readthedocs.io/cfr/systable.html
