# Developer Guide

The documentation below guides you through the process setting up a development
sandbox suitable for convenient editing with live reloading, i.e. just type
`make dev`.


## Prerequisites

You will need an installation of Python on your workstation.


## Setup

In order to spin up a development environment for live editing, based on
[crate-docs], in turn using [sphinx-autobuild], acquire the sources, and
invoke `make dev`.

```shell
git clone https://github.com/crate/cratedb-guide
cd cratedb-guide/docs
```


## Sandbox Operations

### Live Reloading
When invoking the live editing mode, the documentation will be compiled and
served by a development web server.
```shell
make dev
```
When connecting to it using a browser, and editing the files using the editor
of your choice, filesystem changes will be detected, documentation will be
recompiled, and a refresh event will be propagated to the browser.

### Link Checker
To invoke the link checker, which is also part of the PR validation on CI.
```shell
make check
```

### Rendering
To render the documentation, one-shot, without live editing.
```shell
make html
```

### Reset
Reset the embedded `docs/.crate-docs` directory, in order to fetch a new
version next time.
```shell
make reset
```


## Publishing

This project uses [Read the Docs] for publishing, thanks to their team for
the excellent service.

If you submit a pull request to the project on GitHub, a corresponding CI job
will provide you a rendered preview version to inspect your changes like they
would be published after integrating your patch.


[sphinx-autobuild]: https://pypi.org/project/sphinx-autobuild/
[crate-docs]: https://github.com/crate/crate-docs
[Read the Docs]: https://about.readthedocs.com/