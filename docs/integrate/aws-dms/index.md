(aws-dms)=
(cdc-dms)=
# AWS Database Migration Service

:::{include} /_include/links.md
:::

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

:::{rubric} Learn
:::

:::{div}
The [AWS DMS Integration with CrateDB] uses Amazon Kinesis Data Streams as
a DMS target, combined with a CrateDB-specific downstream processor element.

CrateDB supports two ways to run AWS DMS migrations:
Either standalone/on‑premises, or fully managed with AWS and CrateDB Cloud.

AWS DMS supports both `full-load` and `cdc` operation modes, which are often
combined (`full-load-and-cdc`).
:::
