<div align="center">

# The CrateDB Guide

📖 _Guidelines and tutorials about [CrateDB]._ 📖

🔗 Handbook:
[Install](https://cratedb.com/docs/guide/install/) •
[Getting Started](https://cratedb.com/docs/guide/getting-started.html) •
[Administration](https://cratedb.com/docs/guide/admin/) •
[Performance](https://cratedb.com/docs/guide/performance/)

🔗 Ecosystem:
[Application Domains](https://cratedb.com/docs/guide/domain/) •
[Integrations](https://cratedb.com/docs/guide/integrate/) •
[Reference Architectures](https://cratedb.com/docs/guide/reference-architectures/)

📖 More information:
[Drivers and Integrations](https://cratedb.com/docs/clients/) •
[Integration Tutorials](https://community.cratedb.com/t/overview-of-cratedb-integration-tutorials/1015) •
[Reference Documentation](https://cratedb.com/docs/crate/reference/)

✅ CI Status:
[![](https://github.com/crate/cratedb-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/crate/cratedb-guide/actions/workflows/docs.yml)
[![](https://readthedocs.org/projects/cratedb-guide/badge/?version=latest)](https://readthedocs.org/projects/cratedb-guide)
[![](https://img.shields.io/endpoint.svg?color=blue&url=https%3A%2F%2Fraw.githubusercontent.com%2Fcrate%2Fcratedb-guide%2Fmain%2Fdocs%2Fbuild.json)](https://github.com/crate/cratedb-guide/blob/main/docs/build.json)

</div>

## 👨‍💻 About

- This repository contains the sources for the documentation pages rendered
  to https://cratedb.com/docs/guide/. The content is optimally consumed
  from there.

- You can use the content and code snippets for educational and knowledge base
  purposes, or as blueprints for your own projects.

## 🧐 What's Inside

The main content tree of the CrateDB Guide includes a wide array of topics.

If you are looking for something specific, please use the search feature on
GitHub, for example, [searching for "flink"], or clone the repository and
use a local search tool like `ripgrep` or the Silver Searcher.

### ℹ️ General information

- Sources for statically rendered documentation about CrateDB are written in
  [Markdown] and/or [reStructuredText]. Please prefer using Markdown going forward.
- The documentation system is based on [Sphinx], [MyST], [sphinx-design],
  [sphinx-design-elements], and many other Sphinx addons and plugins.
- The documentation theme is [crate-docs-theme].
- The project uses [Read the Docs] for publishing.

### 📁 Directory layout

The folder structure follows a few conventions and ideas. The order of the items
enumerated below is the order how they are currently enumerated within the primary
navigation element (left-hand menu).

- `start` The canonical "Getting Started" section, providing an easy user journey.
- `install` The canonical "How to install CrateDB" section.
- `connect` The canonical "How to connect to CrateDB" section.
- `feature` A backbone section about all features at a glance, using a flat layout.
- `ingest` A category section bundling all ingest methods.
- `topic` A category section bundling different topics [sic!] and application domains.
- `use` A category section bundling different successful customer scenarios.
- `integrate` A backbone section about all the integration items, using a flat layout.
- `admin` A potpourri of operational guidelines.
- `performance` A potpourri of performance tuning guidelines.

## 💁 Contributing

Interested in contributing to this project? Thank you so much!

As an open-source project, we are always looking for improvements in form of
contributions, whether it be in the form of a new feature, improved
infrastructure, or better documentation.

Your bug reports, feature requests, and patches are highly appreciated.

See also the [developer docs] to learn how to set up a development sandbox, in
order to start editing. The [contribution docs] include general information
about how to contribute to CrateDB repositories.
Please also refer to the [CrateDB Authoring Guide] for more information.


## 🌟 Contributors

[![Contributors to CrateDB Examples](https://contrib.rocks/image?repo=crate/cratedb-guide)](https://github.com/crate/cratedb-guide/graphs/contributors)



[contribution docs]: https://github.com/crate/crate/blob/master/CONTRIBUTING.rst
[CrateDB]: https://github.com/crate/crate
[CrateDB Authoring Guide]: https://crate-docs-theme.readthedocs.io/en/latest/authoring.html
[crate-docs-theme]: https://crate-docs-theme.readthedocs.io/
[developer docs]: DEVELOP.md
[Markdown]: https://daringfireball.net/projects/markdown/
[MyST]: https://myst-parser.readthedocs.io/
[Read the Docs]: https://about.readthedocs.com/
[reStructuredText]: https://docutils.sourceforge.io/rst.html
[searching for "flink"]: https://cratedb.com/docs/guide/search.html?q=flink
[Sphinx]: https://www.sphinx-doc.org/
[sphinx-design]: https://sphinx-design.readthedocs.io/
[sphinx-design-elements]: https://sphinx-design-elements.readthedocs.io/
