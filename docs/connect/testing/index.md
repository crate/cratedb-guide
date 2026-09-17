(testing)=
# Software Testing

:::{include} /_include/logos.md
:::

:::{div} sd-text-muted
Test frameworks and libraries that support software
integration testing with CrateDB.
:::

## Java

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} ![JUnit logo][JUnit logo]{height=40px loading=lazy} &nbsp; JUnit
:link: junit
:link-type: ref
:link-alt: Use JUnit with CrateDB
Use JUnit with CrateDB.
::::

::::{grid-item-card} ![Testcontainers logo][Testcontainers logo]{height=40px loading=lazy} &nbsp; Testcontainers for Java
:link: testcontainers-java
:link-type: ref
:link-alt: Use Testcontainers for Java with CrateDB
Use Testcontainers for Java with CrateDB.
::::

:::::

(python-pytest)=
## Python pytest

The popular [pytest] framework makes it easy to write small tests, but it
also supports complex functional testing for applications and libraries.
The [pytest-cratedb] package manages CrateDB instances for running integration
tests against them.

It is based on [cr8](#cr8) for the heavy lifting, and additionally provides
the `crate`, `crate_execute`, and `crate_cursor` pytest fixtures for
developer convenience.

- [Using "pytest-cratedb" with CrateDB and pytest]


(cr8)=
(python-unittest)=
## Python unittest

[cr8], a collection of tools for CrateDB developers, provides primitive
elements to manage CrateDB single-node and multi-node instances through
its [run-crate] subsystem, that can be used to create test layers for
Python's built-in [unittest] framework.

- [Using "cr8" test layers with CrateDB and unittest]


(testcontainers)=
## Testcontainers

[Testcontainers] is an open source framework for providing throwaway,
lightweight instances of databases, message brokers, web browsers, or
just about anything that can run in a Docker container.

Testcontainers provides CrateDB modules for {ref}`Java <testcontainers-java>`,
Python, and Rust.

(testcontainers-python)=
### Python

The CrateDB module of [Testcontainers for Python] starts a single-node
CrateDB, and provides a connection URL for the SQLAlchemy dialect.

:Package: `testcontainers[cratedb]`, version 4.15.0 or later
:Repository: [Testcontainers for Python CrateDB module sources]
:CI status: [![Testcontainers for Python](https://github.com/crate/cratedb-examples/actions/workflows/testing-testcontainers-python.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/testing-testcontainers-python.yml)

- [Using "Testcontainers for Python" with CrateDB and pytest]
- [Using "Testcontainers for Python" with CrateDB and unittest]

(testcontainers-rust)=
### Rust

The CrateDB module of [Testcontainers for Rust] is part of its community
modules.

:Package: `testcontainers-modules`, with the `cratedb` feature
:Documentation: [Testcontainers for Rust CrateDB module]


[cr8]: https://pypi.org/project/cr8/
[pytest]: https://docs.pytest.org/
[pytest-cratedb]: https://pypi.org/project/pytest-cratedb/
[run-crate]: https://pypi.org/project/cr8/#run-crate
[Testcontainers]: https://testcontainers.com/
[Testcontainers for Python]: https://testcontainers-python.readthedocs.io/
[Testcontainers for Python CrateDB module sources]: https://github.com/testcontainers/testcontainers-python/tree/main/src/testcontainers/community/cratedb
[Testcontainers for Rust]: https://rust.testcontainers.org/
[Testcontainers for Rust CrateDB module]: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/cratedb/
[unittest]: https://docs.python.org/3/library/unittest.html
[Using "cr8" test layers with CrateDB and unittest]: https://github.com/crate/cratedb-examples/tree/main/testing/native/python-unittest
[Using "pytest-cratedb" with CrateDB and pytest]: https://github.com/crate/cratedb-examples/tree/main/testing/native/python-pytest
[Using "Testcontainers for Python" with CrateDB and pytest]: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/python-pytest
[Using "Testcontainers for Python" with CrateDB and unittest]: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/python-unittest
