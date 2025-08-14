# MongoDB's data model

MongoDB stores data in collections and documents. CrateDB stores
data in schemas and tables.

- A **database** in MongoDB is a physical container for collections, similar 
  to a schema in CrateDB, which groups tables together within a database.
- A **collection** in MongoDB is a grouping of documents, similar to a table 
  in CrateDB, which is a structured collection of rows.
- A **document** in MongoDB is a record in a collection, similar to a row in 
  a CrateDB table. It is a set of key-value pairs, where each key represents
  a field, and the value represents the data.
- A **field** in MongoDB is similar to a column in a CrateDB table. In both
  systems, fields (or columns) define the attributes for the records
  (or rows/documents).
- A **primary key** in MongoDB is typically the _id field, which uniquely 
  identifies a document within a collection. In CrateDB, a primary key 
  uniquely identifies a row in a table.
- An **index** in MongoDB is similar to an index in CrateDB. Both are used to
  improve query performance by providing a fast lookup for fields (or columns)
  within documents (or rows).

-- [Databases and Collections]


[Databases and Collections]: https://www.mongodb.com/docs/manual/core/databases-and-collections/
