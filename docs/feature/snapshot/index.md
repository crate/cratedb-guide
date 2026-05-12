(snapshot)=

# Snapshots

:::{include} /_include/links.md
:::


:::::{grid}
:padding: 0

::::{grid-item}
:class: rubric-slim
:columns: auto 9 9 9

**CrateDB provides a backup mechanism based on snapshots.**

:::{rubric} Overview
:::
CrateDB, like Elasticsearch, uses snapshots to perform cluster-wide backups of
your data.

:::{rubric} About
:::
A snapshot is a backup of a running CrateDB cluster. You can use snapshots for
different purposes.

- Regularly back up a cluster with no downtime
- Recover data after deletion or a hardware failure
- Transfer data between clusters
- Reduce your storage costs by out-phasing partitions into cold and frozen
  data tier repositories and archives

:::{rubric} Details
:::
CrateDB stores snapshots in an off-cluster storage location called a snapshot repository.
Before you can take or restore snapshots, you must register a snapshot repository on the
cluster. CrateDB supports both local and remote storage, with the option to choose amongst
those repository types:

- AWS S3
- Google Cloud Storage (GCS)
- Microsoft Azure
- Local Filesystem
::::

::::{grid-item}
:class: rubric-slim
:columns: auto 3 3 3

:::{rubric} Reference Manual
:::
- {ref}`crate-reference:snapshot-restore`
:::{rubric} SQL Functions
:::
- {ref}`crate-reference:sql-create-repository`
- {ref}`crate-reference:sql-drop-repository`
- {ref}`crate-reference:sql-create-snapshot`
- {ref}`crate-reference:sql-restore-snapshot`
- {ref}`crate-reference:ref-drop-snapshot`
:::{rubric} System Tables
:::
- {ref}`sys.repositories <crate-reference:sys-repositories>`
- {ref}`sys.snapshots <crate-reference:sys-snapshots>`
- {ref}`sys.snapshots_restore <crate-reference:sys-snapshot-restore>`

{tags-primary}`Backup`
{tags-primary}`Restore`
{tags-primary}`Snapshot`
::::

:::::


## Synopsis

Create a repository and snapshot, inquire available snapshot, and restore it.

**Create Repository**
```sql
CREATE REPOSITORY backup
TYPE fs
WITH (location='<repository address>', compress=false);
```

**Create Snapshot**
```sql
CREATE SNAPSHOT backup.snapshot1 ALL
  WITH (wait_for_completion=true, ignore_unavailable=true);
```

**Inquire Snapshots**
```sql
SELECT repository, name, state
FROM sys.snapshots
ORDER BY repository, name;
```

**Restore Snapshot**
```sql
RESTORE SNAPSHOT backup.snapshot1
TABLE quotes
WITH (wait_for_completion=true);
```


## Usage

Please find more details about how to use snapshots in the reference documentation about
{ref}`snapshots <crate-reference:snapshot-restore>`.

Please also consider reading
the [Elasticsearch: Snapshot and restore] documentation section, because both CrateDB
and Elasticsearch use the same subsystem implementation.

Assuring your data is safe is both recommended and crucial for {ref}`upgrading`
your cluster to newer software releases.


## Other backup strategies

:::{warning}

   Filesystem-level backups (including cloud disk snapshots) are not
   cluster-consistent and must not be used as the primary backup method.
:::

Taking a snapshot using CrateDB’s built-in snapshot functionality is the
**only reliable and supported way** to back up a CrateDB cluster.

Backing up a cluster by copying the data directories of its nodes—whether via
filesystem-level backups, volume snapshots (e.g. Kubernetes CSI or cloud disk
snapshots), or other infrastructure-level mechanisms—is not guaranteed to 
produce a consistent or restorable backup.

CrateDB is a **distributed database** that stores data across multiple nodes
and shards. A backup created by copying node-local data directories does not
represent a consistent cluster-wide state at a single point in time. Even if
such copies are taken simultaneously, or nodes are stopped during the process,
important cluster-level consistency guarantees may still be violated.

Such approaches operate at the storage level and are not aware of CrateDB’s
distributed coordination, transaction visibility, and shard allocation
mechanisms.

In case infrastructure-level backups (e.g. cloud disk snapshots or Kubernetes volume
snapshots) are a requirement, we recommend you shut down the cluster before initiating
the backup.

:::{note}
{material-outlined}`construction;2em` This page is currently under construction.
It only includes the most basic essentials, and needs expansion. For example,
the "Learn" section is missing completely, referring to corresponding tutorials
and other educational material.
:::

[Elasticsearch: Snapshot and restore]: https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html
