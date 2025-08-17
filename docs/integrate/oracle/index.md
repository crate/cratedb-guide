(oracle)=
# Oracle

```{div} .float-right
[![oracle-logo](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Oracle_logo.svg/500px-Oracle_logo.svg.png){height=60px loading=lazy}][Oracle Database]
```
```{div} .clearfix
```

:::{rubric} About
:::

[Oracle Database] (Oracle DBMS, or simply as Oracle) is a proprietary multi-model
database management system produced and marketed by Oracle Corporation.

It is commonly used for running online transaction processing (OLTP), data
warehousing (DW) and mixed (OLTP & DW) database workloads.

:::{rubric} Synopsis
:::

```shell
uvx 'cratedb-toolkit[io-ingestr]' load table \
  "oracle://sys:secret@localhost:1521/?table=sys.demo&mode=SYSDBA" \
  --cluster-url="crate://crate:crate@localhost:4200/doc/oracle_demo"
```

:::{rubric} Learn
:::

::::{grid}

:::{grid-item-card} Tutorial: Use CrateDB Toolkit
:link: oracle-tutorial
:link-type: ref
Load data from Oracle Database into CrateDB using CrateDB Toolkit.
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
:::


[Oracle Database]: https://www.oracle.com/database/
