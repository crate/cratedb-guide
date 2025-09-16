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

[LlamaIndex] is a data framework for Large Language Models (LLMs). It integrates
with providers and models such as GPT‑4 or Llama 3/4, and provides interfaces to
external data sources for natural‑language querying of your private data.

Azure OpenAI Service runs on the Azure global infrastructure and lets you
integrate OpenAI models into your applications. The Azure OpenAI API provides
scalable access to a wide range of models.

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

:::{grid-item-card} Demo: Using LlamaIndex with OpenAI/Azure OpenAI and CrateDB
:link: llamaindex-tutorial
:link-type: ref
- Connect CrateDB to an LLM via OpenAI or Azure OpenAI.
- Text‑to‑SQL: Query CrateDB in natural language.

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
