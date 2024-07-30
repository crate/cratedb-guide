(fts-analyzer)=
(fulltext-analyzer)=

# Analyzers, Tokenizers, and Filters

CrateDB provides the capabilities to adjust the full-text search behaviour
by using analyzers from the large array of open-source Lucene components,
or by employing proprietary analyzers.

Analyzers consist of two parts, filters, and tokenizers. Each analyzer must
contain one tokenizer and only one tokenizer can be used.

Tokenizers decide how to divide the given text into parts. Filters perform
a series of transformations by passing the given text through a number of
operations. They are divided into token filters and character filters,
discriminating between filters applied before, or after the tokenization
step.

Popular filters are stopword lists, lowercase transformations, or word
stemmers.
Those articles share more insights about the concepts of analyzers on behalf
of Apache Solr and Elasticsearch, likewise building upon Lucene technologies.

- [Understanding Analyzers, Tokenizers, and Filters]
- [Improve Your Text Search with Lucene Analyzers]

Through parameterization of filters and tokenizers, the ingredients of
analyzers, and the `CREATE ANALYZER` SQL command, analyzers can be created and
configured at runtime. 


## Adjusting Tokenization

A common approach in information retrieval is to use n-grams for fuzzy
search or spelling corrections. Each word will be split into tokens of
n number of grams. By decreasing the length of the n-grams, the search
will become more fuzzy.

:::{tip}
CrateDB also provides a dedicated option for conducting [](#fuzzy-search),
which is the recommended way to conduct fuzzy searches. This section
outlines how to achieve the same by using a custom analyzer.
:::

:::{rubric} Example
:::
```sql
-- Start with a blank canvas.
DROP TABLE IF EXISTS person;

-- Define a custom analyzer, configuring its tokenizer.
-- A 2-2 n-gram tokenizer will split a word into tokens
-- starting from length 2 up until length 2.
CREATE ANALYZER fuzzy_ngram (
  TOKENIZER _ WITH (
    type='ngram',
    min_gram=2,
    max_gram=2,
    token_chars=['letter']));

-- Define table schema using a full-text index 
-- and the custom analyzer defined above.
CREATE TABLE person (
  firstname VARCHAR,
  lastname VARCHAR, 
  INDEX lastname_ft 
    USING FULLTEXT (lastname) WITH (analyzer = 'fuzzy_ngram'));

-- Provide a few samples worth of data.
INSERT INTO person (firstname, lastname)
VALUES ('charly', 'brown'), ('charly', 'braun'), ('charly', 'browne');  

-- Synchronize writes.
REFRESH TABLE person;

-- Invoke a full-text query including a typing error.
SELECT firstname, lastname, _score
FROM person
WHERE MATCH(lastname_ft, 'bronw')
ORDER BY _score DESC;
```

```postgresql
+-----------+----------+------------+
| firstname | lastname |     _score |
+-----------+----------+------------+
| charly    | brown    | 0.17363958 |
| charly    | browne   | 0.1585405  |
| charly    | braun    | 0.13076457 |
+-----------+----------+------------+
SELECT 3 rows in set (0.016 sec)
```


(fts-synonyms)=
## Synonyms

> In a table with firstname and lastname, find matches that tolerate
> different variants of first names coming from user input, to find
> nicknames and diminutive names such as `William=Bill`.

CrateDB supports synonym files. The synonym file needs to be placed in the
config folder and must be in the Solr or WordNet synonym file format.

Inherited from Elasticsearch, this feature provides the same features
as illustrated at the documentation about its [synonym token filter]. 


:::{rubric} Apache Solr File Format
:::

Solr's synonym file format contains a list of synonyms, one per line. This may
also be a comma-separated list of multiple paths.
This format uses two different definitions:

:Equivalents:
    Groups of words that are equivalent. Define by separating words by commas. 
    :::{code} text
    couch, sofa, divan
    ipod, i-pod, i pod
    computer, pc, laptop 
    :::

:Mappings:
    Explicitly map a group of words to other words. Words on the left hand side
    of the rule definition are expanded into all the possibilities described on
    the right hand side.
    :::{code} text
    teh => the
    small => tiny,teeny,weeny
    huge,ginormous,humungous => large
    personal computer => pc
    sea biscuit, sea biscit => seabiscuit
    :::


:::{rubric} Wordnet File Format
:::

A typical Wordnet file defining synonyms looks like this.

:::{code} text
s(900516492,3,'Computer',n,1,0).
s(900516492,3,'PC',n,1,0).
s(900516492,3,'Laptop',n,1,0).
:::


:::{rubric} Examples
:::

To exercise the examples below, manifest two synonym files, and start CrateDB
using the Docker command. In a different setup, please adjust file system paths
accordingly.

File `synonyms-solr.txt`:
```text
William => Bill
```

File `synonyms-wordnet.txt`:
```text
s(900516492,3,'William',n,1,0).
s(900516492,3,'Bill',n,1,0).
```

```shell
docker run --rm -it --name=cratedb --publish=4200:4200 --env=CRATE_HEAP_SIZE=2g \
  --volume="$PWD/synonyms-solr.txt:/crate/config/synonyms-solr.txt" \
  --volume="$PWD/synonyms-wordnet.txt:/crate/config/synonyms-wordnet.txt" \
  crate -Cdiscovery.type=single-node 
```

This example uses the `synonyms-solr.txt` in Solr format.
```sql
-- Start with a blank canvas.
DROP TABLE IF EXISTS person;
DROP ANALYZER firstname_synonyms;

-- Define a custom analyzer using a synonym file in Solr format.
CREATE ANALYZER firstname_synonyms (
  TOKENIZER lowercase,
  TOKEN_FILTERS (
    _ WITH (
      type='synonym',
      synonyms_path='synonyms-solr.txt')));

-- Define table schema using a full-text index 
-- and the custom analyzer defined above.
CREATE TABLE person (
  firstname VARCHAR,
  lastname VARCHAR, 
  INDEX firstname_ft 
    USING FULLTEXT (firstname) WITH (analyzer = 'firstname_synonyms'));

-- Provide a few samples worth of data.
INSERT INTO person (firstname, lastname)
VALUES ('Bill', 'Gates'), ('William', 'Pereira'), ('William', 'Shatner');  

-- Synchronize writes.
REFRESH TABLE person;

-- Invoke a full-text query including a typing error.
SELECT firstname, lastname, _score
FROM person
WHERE MATCH(firstname_ft, 'William')
ORDER BY _score DESC;
```

```postgresql
+-----------+----------+------------+
| firstname | lastname |     _score |
+-----------+----------+------------+
| Bill      | Gates    | 0.13076457 |
| William   | Shatner  | 0.13076457 |
| William   | Pereira  | 0.13076457 |
+-----------+----------+------------+
SELECT 3 rows in set (0.070 sec)
```

This example uses the `synonyms-wordnet.txt` in Wordnet format.
```sql
-- Start with a blank canvas.
DROP TABLE IF EXISTS person;
DROP ANALYZER firstname_synonyms;

-- Define a custom analyzer using a synonym file in Wordnet format.
CREATE ANALYZER firstname_synonyms (
  TOKENIZER lowercase,
  TOKEN_FILTERS (
    _ WITH (
      type='synonym',
      format='wordnet',
      synonyms_path='synonyms-wordnet.txt')));

-- Define table schema using a full-text index 
-- and the custom analyzer defined above.
CREATE TABLE person (
  firstname VARCHAR,
  lastname VARCHAR, 
  INDEX firstname_ft 
    USING FULLTEXT (firstname) WITH (analyzer = 'firstname_synonyms'));

-- Provide a few samples worth of data.
INSERT INTO person (firstname, lastname)
VALUES ('Bill', 'Gates'), ('William', 'Pereira'), ('William', 'Shatner');  

-- Synchronize writes.
REFRESH TABLE person;

-- Invoke a full-text query including a typing error.
SELECT firstname, lastname, _score
FROM person
WHERE MATCH(firstname_ft, 'William')
ORDER BY _score DESC;
```

```postgresql
+-----------+----------+------------+
| firstname | lastname |     _score |
+-----------+----------+------------+
| Bill      | Gates    | 0.20922333 |
| William   | Pereira  | 0.1325975  |
| William   | Shatner  | 0.1325975  |
+-----------+----------+------------+
SELECT 3 rows in set (0.107 sec)
```


[custom-analyzers-fuzzy]: https://community.cratedb.com/t/fuzzy-search-synonyms/889
[Improve Your Text Search with Lucene Analyzers]: https://medium.com/@dagliberkay/elastic-text-search-6b778de9b753
[synonym token filter]: https://www.elastic.co/guide/en/elasticsearch/reference/8.9/analysis-synonym-tokenfilter.html
[Understanding Analyzers, Tokenizers, and Filters]: https://solr.apache.org/guide/solr/latest/indexing-guide/document-analysis.html
