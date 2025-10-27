(expiration)=
(retention)=

# Automatic retention and expiration

When operating a system storing and processing large amounts of data,
it is crucial to manage data flows and life-cycles well, which includes
handling concerns of data expiry, size reduction, and archival.

Optimally, corresponding tasks are automated rather than manually
performed. CrateDB provides relevant integrations and standalone
applications for automatic data retention purposes.

:::{rubric} Apache Airflow
:::

{ref}`Build a hot/cold storage data retention policy <airflow-data-retention-hot-cold>`
describes how to manage aging data by leveraging CrateDB cluster
features to mix nodes with different hardware setups, i.e. hot
nodes using the latest generation of NVMe drives for responding
to analytics queries quickly, and cold nodes that have access to
cheap mass storage for retaining historic data.

:::{rubric} CrateDB Toolkit
:::

[CrateDB Toolkit Retention and Expiration] is a data retention and
expiration policy management system for CrateDB, providing multiple
retention strategies.

The system derives its concepts from [InfluxDB data retention] ideas and
from the {ref}`Airflow-based data retention tasks for CrateDB <airflow-data-retention-policy>`,
but aims to be usable as a standalone system in different software environments.
Effectively, it is a Python library and CLI around a policy management
table defined per [retention-policy-ddl.sql].


[CrateDB Toolkit Retention and Expiration]: https://cratedb-toolkit.readthedocs.io/retention.html
[InfluxDB data retention]: https://docs.influxdata.com/influxdb/v1/guides/downsample_and_retain/
[retention-policy-ddl.sql]: https://github.com/crate/cratedb-toolkit/blob/main/cratedb_toolkit/retention/setup/schema.sql
