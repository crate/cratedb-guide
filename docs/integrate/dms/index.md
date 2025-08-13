(aws-dms)=
(cdc-dms)=
# DMS (AWS Database Migration Service)

:::{include} /_include/links.md
:::

```{div} .float-right
[![AWS DMS logo](https://icon.icepanel.io/AWS/svg/Database/Database-Migration-Service.svg){height=60px loading=lazy}][AWS Database Migration Service (AWS DMS)]
```
```{div} .clearfix
```

:::{rubric} About
:::

:::{div}
[AWS Database Migration Service (AWS DMS)] is a managed migration and replication
service that helps move your database and analytics workloads between different
kinds of databases quickly, securely, and with minimal downtime and zero data
loss.

AWS DMS supports migration between 20+ database and analytics engines, either
on-premises or on EC2-hosted databases. Supported data migration sources include:
Amazon Aurora, Amazon DocumentDB, Amazon S3, IBM DB2, MariaDB, Azure SQL Database,
Microsoft SQL Server, MongoDB, MySQL, Oracle, PostgreSQL, SAP ASE.
:::

:::{rubric} Synopsis
:::

```shell
uvx 'cratedb-toolkit[kinesis]' load table \
  "kinesis+dms:///arn:aws:kinesis:eu-central-1:831394476016:stream/testdrive" \
  --cluster-url="crate://crate:crate@localhost:4200/testdrive"
```

:::{rubric} Learn
:::

::::{grid} 2

:::{grid-item-card} AWS DMS Processor
:link: ctk:io/dms/index
:link-type: doc
A full-load-and-cdc pipeline using AWS DMS and CrateDB, where an Amazon Kinesis Data
Stream is selected as a DMS target, combined with a CrateDB-specific downstream
processor element.
+++
AWS DMS supports both `full-load` and continuous replication `cdc` operation modes,
which are often combined (`full-load-and-cdc`).
CrateDB supports two ways to run AWS DMS migrations:
Either standalone/on‑premises, or fully managed with AWS and CrateDB Cloud.
:::

::::


:::{seealso}
**Blog:** [Replicating CDC events to CrateDB using AWS DMS]
:::
