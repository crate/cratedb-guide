:::{include} /_include/logos.md
:::

(java-testing)=

# Software testing

```{div} .float-right
[![JUnit logo][JUnit logo]{height=60px loading=lazy}][JUnit home]
[![Testcontainers logo][Testcontainers logo]{height=60px loading=lazy}][Testcontainers for Java]
```
:::{div} sd-text-muted
Testing Java applications against CrateDB.
:::
```{div} .clearfix
```

(junit)=
(java-junit)=
## JUnit

The popular [JUnit] framework is supported by *CrateDB Java Testing Classes*.
The package includes `CrateTestServer` and `CrateTestCluster` classes for use
as [JUnit external resources]. Both classes download and start CrateDB before
test execution, and stop CrateDB afterward.

:::::{grid}
::::{grid-item}

:Package: `io.crate:crate-testing`
:Download: [io.crate:crate-testing] (Maven Central)
:Repository: [crate-java-testing]
::::
::::{grid-item}
:::{card} Using JUnit "crate-testing" with CrateDB
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/java-qa
This example project uses the `io.crate:crate-testing` package and includes a
corresponding project setup that you can use right away to get started.
:::
::::
:::::

(testcontainers-java)=
## Testcontainers

[Testcontainers] is an open-source framework for providing throwaway,
lightweight instances of databases, message brokers, web browsers, or
just about anything that can run in a Docker container.
CrateDB provides Testcontainers implementations for both Java and Python
which are using its {ref}`OCI container image <oci>`.

:::::{grid}
::::{grid-item}

:Package: `org.testcontainers:testcontainers-cratedb`
:Download: [org.testcontainers:testcontainers-cratedb] (Maven Central)
:Repository: [testcontainers-cratedb sources]
:Documentation: [Testcontainers CrateDB Module]
::::
::::{grid-item}
:::{card} Using "Testcontainers for Java" with CrateDB
:link: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/java
This example project uses the `testcontainers-cratedb` package and includes a
corresponding project setup that you can use right away to get started.
:::
::::
:::::


[crate-java-testing]: https://github.com/crate/crate-java-testing
[JUnit]: https://junit.org/
[JUnit external resources]: https://github.com/junit-team/junit4/wiki/Rules#externalresource-rules
[Testcontainers]: https://testcontainers.com/
[Testcontainers CrateDB Module]: https://java.testcontainers.org/modules/databases/cratedb/
[testcontainers-cratedb sources]: https://github.com/testcontainers/testcontainers-java/tree/main/modules/cratedb/src/main/java/org/testcontainers/cratedb

[io.crate:crate-testing]: https://repo1.maven.org/maven2/io/crate/crate-testing/
[org.testcontainers:testcontainers-cratedb]: https://repo1.maven.org/maven2/org/testcontainers/testcontainers-cratedb/
