(langchain)=

# LangChain

:::{include} /_include/links.md
:::

```{div} .float-right
:style: "font-size: 4em; margin-left: 0.3em"
🦜️🔗
```

:::{rubric} About
:::

[LangChain] is a framework for developing applications powered by language models,
written in Python, and with a strong focus on composability. As a language model
integration framework, LangChain's use-cases largely overlap with those of language
models in general, including document analysis and summarization, chatbots, and
code analysis.

The [LangChain adapter for CrateDB] provides support to use CrateDB as a vector store
database, to load documents using LangChain's DocumentLoader, and also supports
LangChain's conversational memory subsystem.

:::{rubric} RAG
:::
LangChain supports retrieval-augmented generation (RAG), which is a technique for
augmenting LLM knowledge with additional, often private or real-time, data, and mixing
in "prompt engineering" as the process of structuring text that can be interpreted and
understood by a generative AI model. A prompt is natural language text describing the
task that an AI should perform.

:::{rubric} Use case examples
:::
LangChain has a number of components designed to help build Q&A applications,
and RAG applications more generally. Those are typical applications you can
build using LLMs:

  - [LangChain: Retrieval augmented generation]
  - [LangChain: Analyzing structured data]
  - [LangChain: Chatbots]
  - [LangChain: Q&A with SQL]

```{div} .clearfix
```


## Install
```shell
pip install --upgrade langchain-cratedb
```


## Learn

Tutorials and Notebooks about using [LangChain] together with CrateDB.

:::{rubric} Tutorials
:::

::::{info-card}
:::{grid-item}
:columns: 9
**Tutorial: Set up LangChain with CrateDB**

LangChain is a framework for developing applications powered by language models.
For this tutorial, we are going to use it to interact with CrateDB using only
natural language without writing any SQL.

To achieve that, you will need a CrateDB instance running, an OpenAI API key,
and some Python knowledge.

[![Navigate to Tutorial](https://img.shields.io/badge/Navigate%20to-Tutorial-darkblue?logo=Markdown)][How to set up LangChain with CrateDB]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`LLM` \
{tags-secondary}`RAG`
:::
::::


::::{info-card}
:::{grid-item}
:columns: 9
**Notebook: Vector Similarity Search**

CrateDB's `FLOAT_VECTOR` type and its `KNN_MATCH` function can be used
for storing and retrieving embeddings, and for conducting similarity
searches.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][LangChain and CrateDB: Code Examples]
[![Notebook on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkgreen?logo=GitHub)][langchain-similarity-github]
[![Notebook on Colab](https://img.shields.io/badge/Open%20on-Colab-blue?logo=Google%20Colab)][langchain-similarity-colab]
[![Notebook on Binder](https://img.shields.io/badge/Open%20on-Binder-lightblue?logo=binder)][langchain-similarity-binder]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`LLM` \
{tags-secondary}`RAG`
:::
::::


::::{info-card}
:::{grid-item}
:columns: 9
**Notebook: SQLAlchemy Document Loader**

Database tables in CrateDB can be used as a source provider for
LangChain documents.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][LangChain and CrateDB: Code Examples]
[![Notebook on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkgreen?logo=GitHub)][langchain-document-loader-github]
[![Notebook on Colab](https://img.shields.io/badge/Open%20on-Colab-blue?logo=Google%20Colab)][langchain-document-loader-colab]
[![Notebook on Binder](https://img.shields.io/badge/Open%20on-Binder-lightblue?logo=binder)][langchain-document-loader-binder]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`Data I/O`
:::
::::


::::{info-card}
:::{grid-item}
:columns: 9
**Notebook: Conversational History**

CrateDB supports managing LangChain's conversation history.

[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][LangChain and CrateDB: Code Examples]
[![Notebook on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkgreen?logo=GitHub)][langchain-conversational-history-github]
[![Notebook on Colab](https://img.shields.io/badge/Open%20on-Colab-blue?logo=Google%20Colab)][langchain-conversational-history-colab]
[![Notebook on Binder](https://img.shields.io/badge/Open%20on-Binder-lightblue?logo=binder)][langchain-conversational-history-binder]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`Vector Store` \
{tags-secondary}`History`
:::
::::


:::{rubric} Webinars
:::

::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**LangChain Cookbook**

The LangChain Cookbook is based off the [LangChain Conceptual Documentation].

Its goal is to provide an introductory understanding of the components,
use cases, and concepts of LangChain via ELI5 examples and code snippets.
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/2xxziIWmaSA?list=PLqZXAkvF1bPNQER9mLmDbntNfSpzdDIU5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Webinar`
{tags-secondary}`Fundamentals`
:::

::::

::::{info-card}

:::{grid-item}
:columns: auto auto 8 8
**How to Use Private Data in Generative AI**

In this video recorded at FOSDEM 2024, we explain how to leverage private data
in generative AI on behalf of an end-to-end Retrieval Augmented Generation (RAG)
solution.

- [How to Use Private Data in Generative AI] (Video)
- [End-to-End RAG with CrateDB and LangChain] (Slides)
:::

:::{grid-item}
:columns: auto auto 4 4

<iframe width="240" src="https://www.youtube-nocookie.com/embed/icquKckM4o0?si=J0w5yG56Ld4fIXfm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
&nbsp;

{tags-primary}`Webinar`
{tags-secondary}`Integrations`
:::

::::



[End-to-End RAG with CrateDB and LangChain]: https://speakerdeck.com/cratedb/how-to-use-private-data-in-generative-ai-end-to-end-solution-for-rag-with-cratedb-and-langchain
[How to set up LangChain with CrateDB]: https://community.cratedb.com/t/how-to-set-up-langchain-with-cratedb/1576
[How to Use Private Data in Generative AI]: https://youtu.be/icquKckM4o0?feature=shared
[LangChain]: https://python.langchain.com/
[LangChain: Analyzing structured data]: https://python.langchain.com/docs/how_to/#extraction
[LangChain: Chatbots]: https://python.langchain.com/docs/how_to/#chatbots
[LangChain: Q&A with SQL]: https://python.langchain.com/docs/how_to/#qa-over-sql--csv
[LangChain: Retrieval augmented generation]: https://python.langchain.com/docs/tutorials/sql_qa/
[LangChain adapter for CrateDB]: https://pypi.org/project/langchain-cratedb/
[LangChain Conceptual Documentation]: https://python.langchain.com/docs/introduction/
[langchain-conversational-history-binder]: https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Flangchain%2Fconversational_memory.ipynb
[langchain-conversational-history-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/langchain/conversational_memory.ipynb
[langchain-conversational-history-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/langchain/conversational_memory.ipynb
[langchain-document-loader-binder]: https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Flangchain%2Fdocument_loader.ipynb
[langchain-document-loader-colab]: https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/langchain/document_loader.ipynb
[langchain-document-loader-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/langchain/document_loader.ipynb
