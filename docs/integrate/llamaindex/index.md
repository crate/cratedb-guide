(llamaindex)=
# LlamaIndex

:::{include} /_include/links.md
:::

```{div} .float-right .text-right
[![LlamaIndex logo](https://www.llamaindex.ai/llamaindex.svg){height=60px loading=lazy}][LlamaIndex]
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-llamaindex.yml" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-llamaindex.yml?branch=main&label=LlamaIndex" loading="lazy" alt="CI status: LlamaIndex"></a>
```
```{div} .clearfix
```

:::{rubric} About
:::

[LlamaIndex] is a data framework for Large Language Models (LLMs). It comes with
pre-trained models on massive public datasets such as GPT-4 or Llama 2, and
provides an interface to external data sources allowing for natural language
querying on your private data.

Azure Open AI Service is a fully managed service that runs on the Azure global
infrastructure and allows developers to integrate OpenAI models into their
applications. Through Azure Open AI API one can easily access a wide range of
AI models in a scalable and reliable way.

:::{rubric} Use case examples
:::
What can you do with LlamaIndex?

- [LlamaIndex: Building a RAG pipeline]
- [LlamaIndex: Building an Agent]
- [LlamaIndex: Using Workflows]

:::{rubric} Learn
:::

::::{grid} 2
:gutter: 2

:::{grid-item-card} Synopsis: Using LlamaIndex for Text-to-SQL
:link: llamaindex-synopsis
:link-type: ref
Text-to-SQL: Talk to your data using human language and
contemporary large language models, optionally offline.

{tags-primary}`Fundamentals`
{tags-secondary}`LLM`
{tags-secondary}`NLP`
{tags-secondary}`RAG`
:::

:::{grid-item-card} Demo: Using LlamaIndex with OpenAI and CrateDB
:link: llamaindex-tutorial
:link-type: ref
- Connect your CrateDB data to an LLM using OpenAI or Azure OpenAI.
- Text-to-SQL / Talk to your data: Query the database in human language; query CrateDB in plain English.

{tags-primary}`Cloud LLM`
{tags-secondary}`LLM`
{tags-secondary}`NLP`
{tags-secondary}`RAG`
:::

:::{grid-item-card} LlamaIndex and CrateDB: Code Examples
:link: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llama-index
:link-type: url
NL2SQL with LlamaIndex: Querying CrateDB using natural language.

{tags-primary}`Runnable example`
:::

::::


:::{toctree}
:maxdepth: 1
:hidden:
Text-to-SQL synopsis <synopsis>
Text-to-SQL tutorial <tutorial>
:::


[LlamaIndex]: https://www.llamaindex.ai/framework
[LlamaIndex: Building a RAG pipeline]: https://docs.llamaindex.ai/en/stable/understanding/rag/
[LlamaIndex: Building an Agent]: https://docs.llamaindex.ai/en/stable/understanding/agent/
[LlamaIndex: Using Workflows]: https://docs.llamaindex.ai/en/stable/understanding/workflows/
[LlamaIndex and CrateDB: Code Examples]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llama-index
[llamaindex-nlquery-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llama-index/demo_nlsql.py
