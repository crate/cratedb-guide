(llamaindex)=
# LlamaIndex

:::{include} /_include/links.md
:::

```{div}
:style: "float: right; text-align: right"
[![LlamaIndex logo](https://www.llamaindex.ai/llamaindex.svg){h=60px}][LlamaIndex]
<br>
<a href="https://github.com/crate/cratedb-examples/actions/workflows/ml-llamaindex.yml" target="_blank">
    <img src="https://img.shields.io/github/actions/workflow/status/crate/cratedb-examples/ml-llamaindex.yml?branch=main&label=LlamaIndex" loading="lazy"></a>
```
```{div}
:style: "clear: both"
```

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


## Install
Project dependencies. For example, use them in a `requirements.txt` file.
```shell
langchain-openai<0.3
llama-index-embeddings-langchain<0.4
llama-index-embeddings-openai<0.4
llama-index-llms-azure-openai<0.4
llama-index-llms-openai<0.4
sqlalchemy-cratedb
```

## Synopsis

:::{dropdown} Code example using the LlamaIndex package
```python
import os
import sqlalchemy as sa

from llama_index.core.utilities.sql_wrapper import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core import Settings

engine = sa.create_engine("crate://localhost:4200/")
engine.connect()

sql_database = SQLDatabase(
    engine, 
    include_tables=["testdrive"]
)

query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=[os.getenv("CRATEDB_TABLE_NAME")],
    llm=Settings.llm
)

query_str = "What is the average value for sensor 1?"
answer = query_engine.query(query_str)
print(answer.get_formatted_sources())
print("Query was:", query_str)
print("Answer was:", answer)

# query was: What is the average value for sensor 1?
# answer was: The average value for sensor 1 is 17.03.
```
:::


## Learn

:::{rubric} Tutorials
:::

::::{info-card}
:::{grid-item}
:columns: 9
**Demo: Using LlamaIndex with OpenAI and CrateDB**

- Connect your CrateDB data to an LLM using OpenAI or Azure OpenAI.
- Text-to-SQL / Talk to your data:
  Query the database in human language, i.e. query CrateDB in plain English.

{hyper-tutorial}`[LlamaIndex and CrateDB: Tutorial]`
[![README](https://img.shields.io/badge/Open-README-darkblue?logo=GitHub)][LlamaIndex and CrateDB: Code Examples]
[![Program on GitHub](https://img.shields.io/badge/Open%20on-GitHub-darkgreen?logo=GitHub)][llamaindex-nlquery-github]
:::
:::{grid-item}
:columns: 3
{tags-primary}`Fundamentals` \
{tags-secondary}`LLM` \
{tags-secondary}`NLP` \
{tags-secondary}`RAG`
:::
::::



[LlamaIndex]: https://www.llamaindex.ai/framework
[LlamaIndex: Building a RAG pipeline]: https://docs.llamaindex.ai/en/stable/understanding/rag/
[LlamaIndex: Building an Agent]: https://docs.llamaindex.ai/en/stable/understanding/agent/
[LlamaIndex: Using Workflows]: https://docs.llamaindex.ai/en/stable/understanding/workflows/
[LlamaIndex and CrateDB: Code Examples]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llama-index
[LlamaIndex and CrateDB: Tutorial]: https://community.cratedb.com/t/how-to-connect-your-cratedb-data-to-llm-with-llamaindex-and-azure-openai/1612
[llamaindex-nlquery-github]: https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llama-index/demo_nlsql.py
