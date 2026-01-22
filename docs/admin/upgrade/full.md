```{highlight} sh
```

(full-restart-upgrade)=

# Full Restart Upgrade

## Introduction

The preferred way to upgrade a running CrateDB cluster is via the
{ref}`rolling-upgrade` method. But this is not always an option (for example,
when you are upgrading from one feature version to the next and minor versions
difference is greater than 1).

When a {ref}`rolling-upgrade` is not possible, a full restart upgrade must be
done if you want to update CrateDB.

:::{CAUTION}
These instructions work for most ways of {ref}`installing <install>` and
running CrateDB.
However, if you are using Docker, take note that `docker service update`
performs a {ref}`rolling-upgrade`.

To do a full restart upgrade with Docker, you must remove the CrateDB
service and then recreate it.
:::

## Upgrade process

::::::{stepper}

### Backup

:::{WARNING}
Before upgrading, you should {ref}`back up your data
<crate-reference:snapshot-restore>`.
:::



### Stop every node

Once you have backed up your data and made the necessary preparations for
downtime, stop the `crate` daemon on every node in the cluster, using
whatever method is appropriate to your setup.

### Upgrade every node

:::{WARNING}
Make sure that every `crate` daemon has been stopped before you continue
or you risk data corruption or data loss.
:::

Once the cluster has been stopped, upgrade the CrateDB software on every node
in the cluster, using whatever method is appropriate to your setup.

### Start every node

Once the CrateDB software on node in the cluster has been updated, start the
`crate` daemon on every node in the cluster, using whatever method is
appropriate to your setup.

::::::

[arch linux aur package]: https://aur.archlinux.org/packages/crate/
[release directory]: https://cdn.crate.io/downloads/releases/
