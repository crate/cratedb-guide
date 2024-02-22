(ml)=
(machine-learning)=

# Machine Learning

Guidelines about integrating CrateDB with machine learning frameworks and tools.

(langchain)=
## LangChain

Tutorials and Notebooks about using [LangChain] together with CrateDB.

- [LangChain and CrateDB: Code Examples]

- CrateDB's `FLOAT_VECTOR` type and its `KNN_MATCH` function can be used for storing and
  retrieving embeddings, and for conducting similarity searches.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/vector_search.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/vector_search.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fvector_search.ipynb)

- Database tables in CrateDB can be used as a source provider for LangChain documents.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/document_loader.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/document_loader.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fdocument_loader.ipynb)

- CrateDB supports managing LangChain's conversation history.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/conversational_memory.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/llm-langchain/conversational_memory.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/crate/cratedb-examples/main?labpath=topic%2Fmachine-learning%2Fllm-langchain%2Fconversational_memory.ipynb)

- What can you build with LangChain?

  - [LangChain: Retrieval augmented generation]
  - [LangChain: Analyzing structured data]
  - [LangChain: Chatbots]


(mlflow)=
## MLflow

Tutorials and Notebooks about using [MLflow] together with CrateDB.

- Blog series on "Running Time Series Models in Production using CrateDB"
  - Part 1: [Introduction to Time Series Modeling using Machine Learning]

- [MLflow and CrateDB]: Guidelines and runnable code to get started with MLflow and
  CrateDB, exercising time series anomaly detection and timeseries forecasting /
  prediction using NumPy, Merlion, and Matplotlib.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb) [![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/mlops-mlflow/tracking_merlion.ipynb)


(pycaret)=
## PyCaret

Tutorials and Notebooks about using [PyCaret] together with CrateDB.

- [AutoML with PyCaret and CrateDB]
- The `automl_classification_with_pycaret.ipynb` example notebook explores the PyCaret
  framework and shows how to use it to train different classification models.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_classification_with_pycaret.ipynb) [![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_classification_with_pycaret.ipynb)

- The `automl_timeseries_forecasting_with_pycaret.ipynb` example notebook explores the PyCaret
  framework and shows how to use it to train various timeseries forecasting models.

  [![Open on GitHub](https://img.shields.io/badge/Open%20on-GitHub-lightgray?logo=GitHub)](https://github.com/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb) [![Open in Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/crate/cratedb-examples/blob/main/topic/machine-learning/automl/automl_timeseries_forecasting_with_pycaret.ipynb)


(scikit-learn)=
## scikit-learn

Using [pandas] and [scikit-learn] to run a regression analysis within a [Jupyter Notebook].

- [Machine Learning and CrateDB: An introduction]
- [Machine Learning and CrateDB: Getting Started With Jupyter]
- [Machine Learning and CrateDB: Experiment Design & Linear Regression]


(tensorflow)=
## TensorFlow

- {doc}`./tensorflow`



```{toctree}
:hidden:

tensorflow
```


[AutoML with PyCaret and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/automl
[Introduction to Time Series Modeling using Machine Learning]: https://cratedb.com/blog/introduction-to-time-series-modeling-with-cratedb-machine-learning-time-series-data
[Jupyter Notebook]: https://jupyter.org/
[LangChain]: https://python.langchain.com/
[LangChain: Analyzing structured data]: https://python.langchain.com/docs/use_cases/qa_structured/sql
[LangChain: Chatbots]: https://python.langchain.com/docs/use_cases/chatbots
[LangChain: Retrieval augmented generation]: https://python.langchain.com/docs/use_cases/question_answering/
[LangChain and CrateDB: Code Examples]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/llm-langchain
[Machine Learning and CrateDB: An introduction]: https://crate.io/blog/machine-learning-and-cratedb-part-one
[Machine Learning and CrateDB: Getting Started With Jupyter]: https://crate.io/blog/machine-learning-cratedb-jupyter
[Machine Learning and CrateDB: Experiment Design & Linear Regression]: https://crate.io/blog/machine-learning-and-cratedb-part-three-experiment-design-and-linear-regression
[MLflow]: https://mlflow.org/
[MLflow and CrateDB]: https://github.com/crate/cratedb-examples/tree/main/topic/machine-learning/mlops-mlflow
[pandas]: https://pandas.pydata.org/
[PyCaret]: https://www.pycaret.org
[scikit-learn]: https://scikit-learn.org/
