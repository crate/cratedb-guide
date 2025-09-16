(nifi)=
# NiFi

```{div} .float-right
[![Apache NiFi logo](https://nifi.apache.org/images/apache-nifi-drop-logo.svg){height=60px loading=lazy}][Apache NiFi]
```
```{div} .clearfix
```

:::{rubric} About
:::

[Apache NiFi] is an easy to use, powerful, and reliable system to process and
distribute data. NiFi automates cybersecurity, observability, event streams,
and generative AI data pipelines and distribution for thousands of companies
worldwide across every industry.

:::{dropdown} **Details**

- **Data provenance tracking**: Complete lineage of information from beginning to end.
- **Extensive configuration**: Loss-tolerant and guaranteed delivery, low latency and
  high throughput, Dynamic prioritization, Runtime modification of flow configuration,
  Back pressure control.
- **Browser-based user interface**: Seamless experience for design, control, feedback,
  and monitoring
- **Secure communication**: HTTPS with configurable authentication strategies,
  multi-tenant authorization and policy management, standard protocols for encrypted
  communication including TLS and SSH.

![NiFi flow canvas screenshot 1](https://github.com/crate/crate-clients-tools/assets/453543/ba6973dd-2eec-4f1f-a436-96aac7eb9892){height=120px loading=lazy}
![NiFi flow canvas screenshot 2](https://github.com/crate/crate-clients-tools/assets/453543/7fd4d2e7-98bc-44ee-b441-e1835016ab4d){height=120px loading=lazy}
![NiFi processors screenshot](https://github.com/crate/crate-clients-tools/assets/453543/ccfa4ac7-0d60-432f-b952-2b50789cd325){height=120px loading=lazy}

:::

:::{rubric} Learn
:::

::::{grid} 2

:::{grid-item-card} Connect Apache NiFi and CrateDB
:link: nifi-tutorial
:link-type: ref
Connect Apache NiFi to CrateDB and ingest data.
:::

::::

```{seealso}
[CrateDB and Apache NiFi]
```

:::{toctree}
:maxdepth: 1
:hidden:
Tutorial <tutorial>
:::


[Apache NiFi]: https://nifi.apache.org/
[CrateDB and Apache NiFi]: https://cratedb.com/integrations/cratedb-and-apache-nifi
