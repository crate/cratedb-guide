(jooq)=

# jOOQ

:::{include} /_include/links.md
:::

:::{div}
[jOOQ] is an internal DSL and source code generator, modelling the SQL
language as a type-safe Java API to help you write better SQL.
:::

```java
// Fetch records, with filtering and sorting.
Result<Record> result = db.select()
        .from(AUTHOR)
        .where(AUTHOR.NAME.like("Ja%"))
        .orderBy(AUTHOR.NAME)
        .fetch();

// Iterate and display records.
for (Record record : result) {
    Integer id = record.getValue(AUTHOR.ID);
    String name = record.getValue(AUTHOR.NAME);
    System.out.println("id: " + id + ", name: " + name);
}
```

:::{card}
:link: https://github.com/crate/cratedb-examples/tree/main/by-language/java-jooq
:link-type: url
:width: 50%
{material-regular}`play_arrow;2em`
Connect to CrateDB using jOOQ.
+++
Java jOOQ demo application with CrateDB using PostgreSQL JDBC.
:::


[![Java jOOQ](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-jooq.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-java-jooq.yml)
