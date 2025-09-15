(lineage)=
# Data Lineage

[Data lineage] refers to the process of tracking how data is generated,
transformed, transmitted and used across a system over time.

It documents data's origins, transformations and movements, providing
detailed visibility into its life cycle.
Processes implementing data lineage simplify the identification of errors
in data analytics workflows, by enabling users to trace issues back to their
root causes.

## Details
- Data lineage **information** includes technical metadata about data transformations.
  Enriched data lineage may include additional elements such as data quality test
  results, reference data, data models, business terminology, data stewardship
  information, program management details and enterprise systems associated with
  data points and transformations.

- Data lineage **visualization tools** often include masking features that allow users
  to focus on information relevant to specific use cases. To unify representations
  across disparate systems, metadata normalization or standardization may be required.

- **Data provenance** provides a historical record of data origins and
  transformations. It supports forensic activities such as data-dependency
  analysis, error/compromise detection, recovery, auditing and compliance
  analysis.

- Tapping into **data governance**, enhancing data lineage with data quality
  measures and master data management adds business value.

## Standards
[OpenLineage] is an open source industry standard framework for data lineage.
It standardizes the definition of data lineage, the metadata that makes up
lineage data, and the approach for collecting lineage data from external systems.


## Solutions
Data lineage solutions tested with CrateDB.

- {ref}`marquez`


[Data lineage]: https://en.wikipedia.org/wiki/Data_lineage
[OpenLineage]: https://openlineage.io/
