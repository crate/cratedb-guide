(testing)=
# Software Testing

Java and Python based test frameworks and libraries that support software
integration testing with CrateDB.


(java-junit)=
## Java JUnit

The popular [JUnit] framework is supported by *CrateDB Java Testing Classes*,
provided per [io.crate:crate-testing] package available on Maven Central.
Its source code is maintained within the [crate-java-testing] repository on GitHub.

The package includes `CrateTestServer` and `CrateTestCluster` classes for use
as [JUnit external resources]. Both classes download and start CrateDB before
test execution, and stop CrateDB afterwards.

This example project includes a corresponding setup that you can use right away
to get started.

- [Using "crate-testing" with CrateDB and JUnit]


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

CrateDB provides Testcontainers implementations for both Java and Python.

- [Using "Testcontainers for Java" with CrateDB]
- [Using "Testcontainers for Python" with CrateDB and pytest]
- [Using "Testcontainers for Python" with CrateDB and unittest]


[cr8]: https://pypi.org/project/cr8/
[crate-java-testing]: https://github.com/crate/crate-java-testing
[io.crate:crate-testing]: https://repo1.maven.org/maven2/io/crate/crate-testing/
[JUnit]: https://en.wikipedia.org/wiki/JUnit
[JUnit external resources]: https://github.com/junit-team/junit4/wiki/Rules#externalresource-rules
[pytest]: https://docs.pytest.org/
[pytest-cratedb]: https://pypi.org/project/pytest-cratedb/
[run-crate]: https://pypi.org/project/cr8/#run-crate
[Testcontainers]: https://testcontainers.com/
[unittest]: https://docs.python.org/3/library/unittest.html
[Using "cr8" test layers with CrateDB and unittest]: https://github.com/crate/cratedb-examples/tree/main/testing/native/python-unittest
[Using "crate-testing" with CrateDB and JUnit]: https://github.com/crate/cratedb-examples/tree/main/by-language/java-qa
[Using "pytest-cratedb" with CrateDB and pytest]: https://github.com/crate/cratedb-examples/tree/main/testing/native/python-pytest
[Using "Testcontainers for Java" with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/java
[Using "Testcontainers for Python" with CrateDB and pytest]: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/python-pytest
[Using "Testcontainers for Python" with CrateDB and unittest]: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/python-unittest
