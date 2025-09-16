(langchain-tutorial)=
# How to set up LangChain with CrateDB

## Introduction

**LangChain** is a framework for developing applications powered by language models.
This tutorial uses LangChain to interact with CrateDB using only natural language without writing any SQL.
To achieve that, you will need a CrateDB instance running, an OpenAI API key, and some Python knowledge.

## Set up database

If you are new to CrateDB, check the deployment options available [here](https://cratedb.com/download) for download options or here for the [free cloud](https://cratedb.com/lp-crfree?hsCtaTracking=3d8a5114-8592-4ec6-adc7-3714f5fe403d%7Cf1d1dba0-a936-41c2-9c7f-1ffb2c24745a) deployment, choose the one that suits you best. Once CrateDB is set up, create and populate the table as seen below.

```psql
CREATE TABLE IF NOT EXISTS "doc"."people" (
   "name" TEXT,
   "info" OBJECT(DYNAMIC) AS (
      "like" ARRAY(BIGINT),
      "dislike" ARRAY(BIGINT)
   ),
   "house_id" INTEGER,
   "description" TEXT
);
```

```psql
INSERT INTO doc.people VALUES ('John M', {"like"=[1,2,3],"dislike"=[4,5]}, 1, 'nice person'),
                              ('John T', {"like"=[2],"dislike"=[1]}, 2, 'tall person'),
                              ('Mary P', {"like"=[2,3],"dislike"=[7]}, 3, 'smart person');
```

## Use LangChain

First, install the required libraries

```shell
pip install --upgrade langchain-community langchain-openai 'sqlalchemy-cratedb>=0.42.0.dev2'
```

Once installed, import the required components:
Also, before running the code snippet below, make sure to replace the
`<API_KEY>` with your OpenAI API key. Besides that, replace the URI with
the correct connection string to your CrateDB instance. Finally, enter
your question as a string replacing `<TEXT_QUESTION>` in the code.

```python
import os
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI

# Prefer exporting OPENAI_API_KEY in the shell (not in code).
# os.environ["OPENAI_API_KEY"] = "<API_KEY>"

# Change the database URI below to match your CrateDB instance.
# e.g., local: "crate://localhost:4200"
# e.g., Cloud (with TLS): "crate://<user>:<password>@<cluster>.cratedb.net:4200?ssl=true"
# Play around with the LLM temperature parameter.
db = SQLDatabase.from_uri("crate://")

llm = ChatOpenAI(temperature=0)
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

agent_executor.invoke("<TEXT_QUESTION>")
```

If you ask the question “Who is tall?“ to the model, the result will be as follows. As you can see, it queries all the tables and, based on their names and their columns' names, it decides which is relevant to the query. You can track the reasoning behind the decision-making process the model uses.

![Screenshot 2023-08-24 at 09.27.52|599x500](https://us1.discourse-cdn.com/flex020/uploads/crate/original/2X/8/8b84ca86108a641c944c880894c0b9ac19628a52.png){h=400px}

Now that everything is set up, feel free to explore with different questions
and tables. Keep in mind that connecting an LLM agent to CrateDB enables it
to run queries on your data. For production, use a least‑privileged database
user and avoid sending sensitive data to external providers unless
contractually approved.

If you are looking for a different model, you can explore the options
available on the [LangChain Introduction].

## Summary

This tutorial demonstrates how to use LangChain to interact with CrateDB by
writing questions in English.
If you explore different questions, you may encounter some wrong answers,
so we recommend you use this tool with caution and always check the reasoning
it provides behind every answer. If you are looking for more exciting
integrations, have a look at the {ref}`integrations section <integrations>`
in our documentation.


[LangChain Introduction]: https://python.langchain.com/docs/introduction/
