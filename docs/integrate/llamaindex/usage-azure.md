(llamaindex-usage-azure)=
# Text-to-SQL: Talk to your data using CrateDB, LlamaIndex, and Azure OpenAI

## Introduction

[LlamaIndex](https://www.llamaindex.ai/) is a data framework for Large Language Models (LLMs).
It integrates with models such as [GPT‑4](https://openai.com/index/gpt-4/) or [Llama 4](https://www.llama.com/models/llama-4/) and provides interfaces to external data sources for natural‑language querying of your private data.

[Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service) is a fully managed service on the Azure global infrastructure that lets developers integrate OpenAI models into applications. Through the Azure OpenAI API, you can access a wide range of AI models in a scalable and reliable way.

This usage guide shows how to augment LLMs with data stored in CrateDB using LlamaIndex and Azure OpenAI, enabling natural‑language queries over your data.

If you want to run this in your own environment, we've provided all of the code and supporting resources that you'll need in the [`cratedb-examples`](https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llama-index) GitHub repository.

## Prerequisites

* Python 3.10 or higher
* Recent version of LlamaIndex, please follow the [installation instructions](https://developers.llamaindex.ai/python/framework/getting_started/installation/)
* `openai` (Python SDK)
* `sqlalchemy-cratedb`
* `SQLAlchemy` (if not pulled transitively)
* Running instance of [CrateDB](https://console.cratedb.cloud/)
* [Azure subscription](https://azure.microsoft.com/en-gb/free/cognitive-services/) and [Azure OpenAI resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal)

## Deploy models in Azure OpenAI

Before we use OpenAI models to generate responses for queries, we need to deploy two models in Azure: for the text generation task and for embeddings. There are several pre-trained models available in Azure OpenAI Studio we can choose from, as well as the capability to customize AI models, fine-tuned with custom data and hyperparameters.

To deploy the models required for this usage guide, follow these steps:

1. In Azure OpenAI resource choose Model Deployments and then Manage Deployments as illustrated below.

![92c692f4-2cc8-4661-9fc3-7c037cccbd28|690x263](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/e/e0a411357b62eb67995b818b4e235d8c64aebc99.png)

2. This opens Azure AI Studio. Click *Create new deployment* and deploy:

  1. A chat/completions model (e.g., **gpt-4o-mini**)
  2. An embeddings model (e.g., **text-embedding-3-large**)

The basic deployment of each model is straightforward in Azure OpenAI Studio: You need to select the model you want to deploy and specify the unique name:

![d782073d-a756-4f74-97a6-92867bfba64e|683x500, 75%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/f/fa3e412d0ff06135cd8bb719305d575e5dc6889c.png){height=400px}

Finally, you should have an overview of all deployed models under the *Deployments* tab:

![b05265b5-4220-4680-af5a-19bbda64326a|690x179](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/9/995a8658a5e5e733ac45e8c9b483b392d7d51e53.png)

## Load time-series data to CrateDB

Let’s now create the `time_series_data` table in CrateDB that contains time series data, where each row represents a data point with the following information:

1. `timestamp`: The timestamp when the data point was recorded.
2. `value`: The numerical value associated with the data point.
3. `location`: The location or source of the data (either 'Sensor A' or 'Sensor B').
4. `sensor_id`: The ID of the sensor that generated the data.

```sql
CREATE TABLE IF NOT EXISTS time_series_data (
    timestamp TIMESTAMP,
    value DOUBLE,
    location STRING,
    sensor_id INT
);
```

Import a portion of the data we will use for learning and querying:

```sql
INSERT INTO time_series_data (timestamp, value, location, sensor_id)
VALUES
    ('2023-09-14T00:00:00', 10.5, 'Sensor A', 1),
    ('2023-09-14T01:00:00', 15.2, 'Sensor A', 1),
    ('2023-09-14T02:00:00', 18.9, 'Sensor A', 1),
    ('2023-09-14T03:00:00', 12.7, 'Sensor B', 2),
    ('2023-09-14T04:00:00', 17.3, 'Sensor B', 2),
    ('2023-09-14T05:00:00', 20.1, 'Sensor B', 2),
    ('2023-09-14T06:00:00', 22.5, 'Sensor A', 1),
    ('2023-09-14T07:00:00', 18.3, 'Sensor A', 1),
    ('2023-09-14T08:00:00', 16.8, 'Sensor A', 1),
    ('2023-09-14T09:00:00', 14.6, 'Sensor B', 2),
    ('2023-09-14T10:00:00', 13.2, 'Sensor B', 2),
    ('2023-09-14T11:00:00', 11.7, 'Sensor B', 2);
```

## Connect Azure OpenAI with LlamaIndex

Azure OpenAI resource differs slightly from the standard OpenAI resource as it requires the use of the embedding model, which we deployed in the previous step. The following code illustrates the setup of OpenAI API:

```python
import os

def configure_llm():
    """
    Configure LLM. Use either OpenAI or Azure OpenAI.
    """

    api_type = os.getenv("OPENAI_API_TYPE")
    azure_endpoint = os.getenv("OPENAI_AZURE_ENDPOINT")
    api_version = os.getenv("OPENAI_AZURE_API_VERSION")
    api_key = os.getenv("OPENAI_API_KEY")

    if api_type == "openai":
        llm = OpenAI(
            api_key=api_key,
            temperature=0.0
        )
    elif api_type == "azure":
        llm = AzureOpenAI(
            engine=os.getenv("LLM_INSTANCE"),
            azure_endpoint=azure_endpoint,
            api_key=api_key,
            api_version=api_version,
            temperature=0.0
        )
    else:
        raise ValueError(f"OpenAI API type not defined or invalid: {openai.api_type}")

    Settings.llm = llm
    if api_type == "openai":
        Settings.embed_model = LangchainEmbedding(OpenAIEmbeddings())
    elif api_type == "azure":
        Settings.embed_model = LangchainEmbedding(
            AzureOpenAIEmbeddings(
                azure_endpoint=azure_endpoint,
                model=os.getenv("EMBEDDING_MODEL_INSTANCE")
            )
        )
```

To find your `OPENAI_AZURE_ENDPOINT` and `OPENAI_API_KEY` check the Overview tab inside your OpenAI resource and look for the Endpoint and Manage keys values:

![c8861714-f25c-44ea-a4d7-e15e6cabf176|412x150, 75%](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/e/e5199d295ea08099a38cce88e9c2804c1bb63c9a.png){height=180px}

For the value of `OPENAI_AZURE_API_VERSION` use `2024-10-21`.

The code also initializes the LLM and embedding models. The value for `EMBEDDING_MODEL_INSTANCE` is the deployed embedding model's name from  Azure OpenAI (e.g., `my_embedding-model`). To set this configuration globally, we use the `llama_index.core.Settings`.

## Connect CrateDB with LlamaIndex

Finally, let’s explore some of the core LlamaIndex SQL capabilities with CrateDB. In the following example, we will use the `time_series_data` table with the test data points and query it with text-to-SQL capabilities.

Use SQLAlchemy to connect to CrateDB and the SQLDatabase wrapper to expose tables to LlamaIndex.
```python
engine_crate = sa.create_engine(os.getenv("CRATEDB_SQLALCHEMY_URL"))
```
The value of `CRATEDB_SQLALCHEMY_URL` should be a URL format connection string containing the hostname, username and password for your CrateDB instance:

```bash
crate://USER:PASSWORD@HOST:4200/?ssl=true
```

To query CrateDB using natural language we make an instance of `SQLDatabase` and provide a list of tables:

```python
sql_database = SQLDatabase(
    engine_crate, 
    include_tables=[os.getenv("CRATEDB_TABLE_NAME")]
)
```

Then create an instance of `NLSQLTableQueryEngine`:
```python
query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=[os.getenv("CRATEDB_TABLE_NAME")],
    llm=Settings.llm
)
```

At this point, we are ready to query CrateDB in plain English!

### Ask a question

With time‑series data you often care about aggregates. For example,
compute the average value for sensor 1:
```python
query_str = "What is the average value for sensor 1?"
answer = query_engine.query(query_str)
print(answer.get_formatted_sources())
print("Query was:", query_str)
print("Answer was:", answer)

# query was: What is the average value for sensor 1?
# answer was: The average value for sensor 1 is 17.03.
```

You can also inspect the SQL that produced the answer; it’s included in `answer.metadata`:
```python
print(answer.metadata)
# {'result': [(17.033333333333335,)], 'sql_query': 'SELECT AVG(value) FROM time_series_data WHERE sensor_id = 1'}
```

## Takeaway

This usage guide shows how to query CrateDB data using natural language with
LlamaIndex and Azure OpenAI.

Explore more CrateDB and generative‑AI resources as they become available.

Find the full example code and supporting resources in the
[`cratedb-examples` GitHub repository](https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llama-index).

In the meantime, explore the wide range of capabilities that CrateDB has
to offer and start your cluster on [CrateDB Cloud](https://console.cratedb.cloud/),
including a forever free [CRFREE](https://cratedb.com/lp-crfree) plan. If you have
further questions about CrateDB and its use cases, check our
{ref}`reference documentation <crate-reference:index>` or
ask [our growing community](https://community.cratedb.com/).
