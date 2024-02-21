(testing)=
# Software Testing

Java and Python based test frameworks and libraries that support software
integration testing with CrateDB.


(python-pytest)=
## Python pytest

The popular [pytest] framework makes it easy to write small tests, but it
also supports complex functional testing for applications and libraries.
The [pytest-crate] package manages CrateDB instances for running integration
tests against them.

It is based on [cr8](#cr8) for the heavy lifting, and additionally provides
the `crate`, `crate_execute`, and `crate_cursor` pytest fixtures for
developer convenience.

- [Using "pytest-crate" with CrateDB and pytest]


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
[pytest]: https://docs.pytest.org/
[pytest-crate]: https://pypi.org/project/pytest-crate/
[run-crate]: https://pypi.org/project/cr8/#run-crate
[Testcontainers]: https://testcontainers.com/
[unittest]: https://docs.python.org/3/library/unittest.html
[Using "cr8" test layers with CrateDB and unittest]: https://github.com/crate/cratedb-examples/tree/main/testing/native/python-unittest
[Using "pytest-crate" with CrateDB and pytest]: https://github.com/crate/cratedb-examples/tree/main/testing/native/python-pytest
[Using "Testcontainers for Java" with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/java
[Using "Testcontainers for Python" with CrateDB and pytest]: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/python-pytest
[Using "Testcontainers for Python" with CrateDB and unittest]: https://github.com/crate/cratedb-examples/tree/main/testing/testcontainers/python-unittest
