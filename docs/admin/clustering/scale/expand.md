(scale-expand)=

# How to expand an existing CrateDB cluster

## Introduction

A significant feature in CrateDB is that it can scale horizontally, which means that instead of adding more RAM, CPU, and disk resources to our existing nodes we can add more nodes to our CrateDB cluster.

This allows the handling of volumes of data that simply could not fit on a single node, but it is also very useful in scenarios where hosting everything in a single node, or a small number of nodes, would still be possible, this is because smaller nodes are often easier to manage infrastructure-wise.

More nodes also mean more resiliency to issues, on a scenario where we have for instance 5 nodes, and configure our tables with 2 replicas, we could lose 2 nodes and still serve our production workloads. This means we can carry out maintenance on the nodes one at a time and still be able to withstand an unplanned issue on another node without downtime.

Today we want to review how to add a new node to an existing on-premises cluster.

## Related reading

- [CrateDB multi-node setup — CrateDB: How-Tos](https://crate.io/docs/crate/howtos/en/latest/clustering/multi-node-setup.html)

- [Clustering — CrateDB: Reference](https://crate.io/docs/crate/reference/en/latest/concepts/clustering.html)

- [Storage and consistency — CrateDB: Reference](https://crate.io/docs/crate/reference/en/latest/concepts/storage-consistency.html)

## Discovery

When a CrateDB node starts it needs a mechanism to get a list of the nodes that make up the cluster, this is called discovery.
At the time of writing, there are 3 ways for a node to get this list:

* The list of nodes can be defined in the `discovery.seed_hosts` setting in the configuration file (typically in `/etc/crate/crate.yml`)
* The list can be retrieved with a DNS query, see https://crate.io/docs/crate/reference/en/5.4/config/cluster.html#discovery-via-dns
* In AWS environments, the list of nodes can be looked up via the EC2 API, filtering on specific security groups, availability zones, and tags, see https://crate.io/docs/crate/reference/en/5.4/config/cluster.html#discovery-on-amazon-ec2

For the purpose of this post, we will work with the `discovery.seed_hosts` list.

## Scaling from a single-node deployment

If a node is started without specifying the `initial_master_nodes` setting (the default configuration), or with `discovery_type` set to `single-node`, it will be started as a standalone instance and it cannot later be scaled into a cluster. Single-node deployments are great for development and testing, but for production setups we recommend using a cluster with at least 3 nodes.

If you are going for a single-node deployment initially, but plan to scale to a multi-node cluster in the future, there are some settings to configure before the very first run of the CrateDB node so that it bootstraps as a 1-node cluster instead of a standalone instance.
The settings that we need are:

* `discovery.seed_hosts` set to the hostname or the `node.name` of the node
* `initial_master_nodes` set to the hostname or the `node.name` of the node
* optionally we can set a `cluster.name`

If you are using containers you would pass these settings with lines in the `args` section of your YAML file, otherwise you could create `/etc/crate/crate.yml` before deploying the package for your distribution (refer to https://github.com/crate/crate/blob/master/app/src/main/dist/config/crate.yml for the template), or you could prevent the package installation from auto-starting the daemon by using a mechanism such as `policy-rcd-declarative`, then edit the configuration file (`crate.yml`), and start the `crate` daemon once all settings are ready.

## Networking considerations

Nodes need to be able to resolve each other's hostnames at DNS level, and they need to be able to reach each other on a TCP port which is 4300 by default.

For security reasons you should configure your network so that CrateDB cluster nodes are only reachable on port 4300 from other CrateDB nodes in the cluster.
In a Kubernetes environment this can be achieved with a `Service` resource with a `ClusterIP`.
In a non-containerized environment one way to do this is to use firewall software directly on each node, for instance:

```bash
#Enable ufw - all incoming connections blocked by default
sudo ufw enable

#Allow SSH if you are using it to manage your server
sudo ufw allow 22

#Allow 4200 for clients to connect to CrateDB via the http endpoint
sudo ufw allow 4200

#Allow 5432 if you have PostgreSQL clients
sudo ufw allow 5432

#Allow 4300 from 192.168.0.202 (another cluster node in this example)
sudo ufw allow proto tcp from 192.168.0.202 to any port 4300
```

You may also want to consider network access control and/or a separate network adapter for intra-cluster communications.

## Deploying the new node

Make sure the new node does not auto-bootstrap as a single-node instance, you may want to either create `/etc/crate/crate.yml` in advance or use a mechanism as `policy-rcd-declarative` as mentioned earlier.
On the configuration file for the new node:

* Set `discovery.seed_hosts` to the full list of nodes, including the new one you are adding.
* Optionally set a `node.name` , if not done the node get assigned a random name from the `sys.summits` table. You may wonder what those default names are about, they are the names of mountains in the area around our main office, we love mountains at [Crate.io](http://crate.io/).
* Set `cluster.name` to a value that matches the other nodes in the cluster, if not specified the default cluster name is `crate`.
* Consider if you want to set the [cluster-wide settings](https://crate.io/docs/crate/reference/en/latest/config/cluster.html#metadata-gateway) `gateway.expected_data_nodes`, `gateway.recover_after_data_nodes`, and/or `gateway.recover_after_time` to prevent the unnecessary creation of new replicas and the rebalancing of shards when a node takes a little bit longer to start, or in case of transient issues, when the cluster is starting up from a situation where all nodes are shutdown. Please note these settings are used when the cluster is starting up from being offline, if you want to delay the allocation of replicas when a node becomes unavailable on a cluster that stays online there is [a different setting at table level](https://crate.io/docs/crate/reference/en/5.4/sql/statements/create-table.html#unassigned-node-left-delayed-timeout).

Now we can start the `crate` daemon, you will see the node joining the cluster and CrateDB will start using it for shards allocation.

Remember to add the new nodes alongside the old ones in any monitoring system and load balancer configuration you may have in your environment.

## Updating settings on the old nodes

Now we need to align a number of settings in the other nodes, these are typically in the `/etc/crate/crate.yml` file:

* Update `discovery.seed_hosts` adding the new node
* If you have configured `gateway.` settings, update them to have the same values on all nodes

These settings only play a role during restart, not at runtime, so you do not need to restart the nodes after making these changes, but if the `gateway.` settings need updating you may see a warning in the Admin UI which can be acknowledged.

Please also note there is no need to update the `initial_master_nodes` list, this is only considered during the initial cluster bootstrapping.

And that is it, we have scaled out our cluster and we are ready to work with larger volumes of data. I hope you find this useful and, as usual, please do not hesitate to raise any thoughts or questions in the [CrateDB Community](https://community.cratedb.com/).
