(vector-search)=
# Vector Search

:::{rubric} Overview
:::
Vector search is a method in artificial intelligence and data retrieval that
uses mathematical vectors to represent and efficiently search through complex,
unstructured data.

:::{rubric} About
:::
Vector search leverages machine learning (ML) to capture the meaning and
context of unstructured data, including text and images, transforming it
into a numeric representation.

Frequently used for semantic search, vector search finds similar data using
approximate nearest neighbor (ANN) algorithms. Compared to traditional keyword
search, vector search yields more relevant results and executes faster.

:::{rubric} Details
:::
CrateDB can be used as a [vector database] (VDBMS) for storing and retrieving
vector embeddings based on the [FLOAT_VECTOR] data type and its accompanying 
[KNN_MATCH] function, effectively conducting HNSW semantic similarity searches
on them, also known as vector search.


## Learn

To learn more about vector search, please visit the corresponding page about
[](#vector-store).


:::{todo}
Bring page into the same shape like the others in this section.
Maybe just move the [](#vector-store) page here without further ado.
:::


[FLOAT_VECTOR]: inv:crate-reference#type-float_vector
[KNN_MATCH]: inv:crate-reference#scalar_knn_match
[vector database]: https://en.wikipedia.org/wiki/Vector_database
