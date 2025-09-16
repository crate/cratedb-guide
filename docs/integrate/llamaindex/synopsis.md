(llamaindex-synopsis)=
# Synopsis: Text-to-SQL with LlamaIndex

:::{div} sd-text-muted
Text-to-SQL: Talk to your data using human language and
contemporary large language models, optionally offline.
:::

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

## Walkthrough
::::{grid} 2
:padding: 0
:class-row: title-slim

:::{grid-item}
:columns: 4
Import Python modules.
:::
:::{grid-item}
:columns: 8
```python
import os
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI
from llama_index.core import SQLDatabase
from llama_index.core.indices.struct_store import NLSQLTableQueryEngine
import sqlalchemy as sa
```
:::

:::{grid-item}
:columns: 4
Provision LLM using OpenAI model.
:::
:::{grid-item}
:columns: 8
```python
llm = OpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4.1"),
    temperature=0.0,
    api_key=os.getenv("OPENAI_API_KEY"),
)
```
:::

:::{grid-item}
:columns: 4
Alternatively, provision LLM using self-hosted model.
:::
:::{grid-item}
:columns: 8
```python
llm = Ollama(
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
    model="gemma3:1b",
    temperature=0.0,
    request_timeout=120.0,
    keep_alive=-1,
)
```
:::

:::{grid-item}
:columns: 4
Connect to CrateDB.
:::
:::{grid-item}
:columns: 8
```python
database = sa.create_engine(os.getenv("CRATEDB_SQLALCHEMY_URL", "crate://crate@localhost:4200"))
database.connect()
```
:::

:::{grid-item}
:columns: 4
Invoke Text-to-SQL query.
:::
:::{grid-item}
:columns: 8
```python
sql_database = SQLDatabase(engine=database)
nlsql = NLSQLTableQueryEngine(sql_database=sql_database, llm=llm)
answer = nlsql.query("What is the average value for sensor 1?")
```
:::

:::{grid-item}
:columns: 4
Also try other languages.
:::
:::{grid-item}
:columns: 8
```python
answer = nlsql.query("Яке середнє значення для датчика 1?")
answer = nlsql.query("¿Cuál es el valor promedio del sensor 1?")
answer = nlsql.query("Was ist der Durchschnittswert für Sensor 1?")
answer = nlsql.query("Quelle est la valeur moyenne pour le capteur 1 ?")
```
:::

::::


## Full code example
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


:::{note}
Please find the executable example at [CrateDB Examples » llama-index].
:::


[CrateDB Examples » llama-index]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llama-index
