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

AWS DMS supports migration between 20-plus database and analytics engines, either
on-premises, or per EC2 instance databases. Supported data migration sources are:
Amazon Aurora, Amazon DocumentDB, Amazon S3, IBM DB2, MariaDB, Azure SQL Database,
Microsoft SQL Server, MongoDB, MySQL, Oracle, PostgreSQL, SAP ASE.
:::

:::{rubric} Learn
:::

:::{div}
The [AWS DMS Integration with CrateDB] uses Amazon Kinesis Data Streams as
a DMS target, combined with a CrateDB-specific downstream processor element.

CrateDB provides two variants how to conduct data migrations using AWS DMS.
Either use it standalone / on your own premises, or use it in a completely
managed environment with services of AWS and CrateDB Cloud.

AWS DMS supports both `full-load` and `cdc` operation modes, often used in
combination with each other (`full-load-and-cdc`).
:::
