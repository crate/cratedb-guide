<div align="center">

# The CrateDB Handbook

📖 _How-to guides, tutorials, explanations, and extended reference material about [CrateDB]._ 📖

🔗 Learning path:
[Getting Started](https://cratedb.com/docs/guide/start/) •
[Install](https://cratedb.com/docs/guide/install/) •
[How-to guides](https://cratedb.com/docs/guide/howto/) •
[Tutorials](https://cratedb.com/docs/guide/tutorial/) •
[Administration](https://cratedb.com/docs/guide/admin/) •
[Performance](https://cratedb.com/docs/guide/performance/)

🔗 Reference material:
[All features](https://cratedb.com/docs/guide/feature/) •
[Ingestion](https://cratedb.com/docs/guide/ingest/) •
[Topics](https://cratedb.com/docs/guide/topic/) •
[Solutions](https://cratedb.com/docs/guide/solution/) •
[Integrations](https://cratedb.com/docs/guide/integrate/)

📖 More information:
[Reference Manual](https://cratedb.com/docs/crate/reference/)

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

The main content tree of the CrateDB Handbook includes an array of topics,
roughly based on two approaches to convey information: A "learning path"
style documentation serving newcomers, and a "reference lookup" style
documentation serving experienced users.

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

**Learning path**
- `start` The canonical "Getting Started" section, providing an easy user journey.
- `install` The canonical "How to install CrateDB" section.
- `connect` The canonical "How to connect to CrateDB" section.
- `howto` How-to guides about CrateDB.
- `tutorial` Tutorials about CrateDB.
- `admin` A potpourri of operational guidelines.
- `performance` A potpourri of performance tuning guidelines.

**Reference material**
- `feature` A backbone section about all features at a glance, using a flat layout.
- `ingest` A category section bundling all ingest methods.
- `topic` A category section bundling different topics [sic!] and application domains.
- `solution` A category section bundling different successful customer scenarios.
- `integrate` A backbone section about all the integration items, using a flat layout.

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
[CrateDB Authoring Guide]: https://crate-docs-theme.readthedocs.io/en/latest/authoring/
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
