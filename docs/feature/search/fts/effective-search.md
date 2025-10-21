(effective-fulltext-search)=

# Indexing Text for Both Effective Search and Accurate Analysis

```{article-info}
---
avatar: https://images.squarespace-cdn.com/content/v1/613289e53dda745d13a61433/1634312742942-5UOECGMLC277DP2NC7V9/dave.png
avatar-outline: muted
author: David Norton, Qualtrics Text iQ
date: June 29, 2018
read-time: 15 min read
class-container: sd-p-2 sd-outline-muted sd-rounded-1
---
```

## Introduction

At Qualtrics, Text iQ is the tool that allows our users to find insights from
their free-response questions.

Powering Text iQ are various microservices that analyze the text and build
models for everything from sentiment analysis to identifying key topics. In
addition, Text iQ provides a framework for users to explore their text data
through search. As the name suggests, we want all aspects of Text iQ, including
search, to be intuitive and feel smart. All of this requires a storage solution
that allows for effective text indexing as well as accurate and complete data
aggregation and retrieval.

In this article we examine CrateDB, the technology we use for storage in Text
iQ, as well as the actual text processing pipeline that we use to give us the
indexing capabilities that we need.

## Why CrateDB?

Elasticsearch is one of the most popular technologies for effective indexing of
text based data. So why did we choose CrateDB instead?

First, CrateDB actually uses Elasticsearch technology under the hood to manage
cluster creation and communication. It also exposes an Elasticsearch API
providing access to all indexing capabilities in Elasticsearch that we need.

Second, we need to be able to retrieve _exact_ aggregate information
efficiently, which functionality CrateDB provides. We need exact aggregates
because our text storage solution informs data reporting tools that are
frequently under heavy scrutiny.

Finally, CrateDB’s SQL interface provides a favorable protocol for retrieving
the extensive amounts of data that we use in various reporting tools and to
train machine learning models.

## An Introduction to CrateDB Analyzers

Most major text search engines are built on Lucene. CrateDB and Elasticsearch
are no exception. In Lucene, an analyzer is the processing pipeline used to
create an index from raw text. It consists of a single tokenizer, and zero or
more token/char filters.

The tokenizer is required as it separates a raw text field into individual terms
(or tokens) that can be indexed on. The most simple analyzers consist of nothing
more than a tokenizer. The most basic tokenizer is the _whitespace_ tokenizer
which separates terms with whitespace and ignores punctuation and symbols.

More sophisticated analyzers will include any number of token or character
filters. Token filters further process individual terms enabling more generic
searches. For example, the token filter _lowercase_ is used in nearly every
analyzer and, as you might expect, transforms all characters into lowercase.
This would enable a user to perform case-insensitive searches within a corpus.
Char filters are similar to token filters except that they process the raw text
before it is tokenized; so they can’t manipulate the term sequences that come
out of the tokenizers.

The default CrateDB analyzer uses a tokenizer based on
[UAX #29: Unicode Text Segmentation], lowercases all tokens, and allows for
optional stopword removal. Furthermore, CrateDB allows users to build custom
analyzers from the same available tokenizers and filters that are available to
ElasticSearch. While this is a large selection, it is not sufficient to reach
the high bar we have set for Text iQ. Fortunately, it was relatively
straightforward in CrateDB to add our own custom analyzer components via a java
plugin.

## Processing Text for Intuitive and Smart Indexing

If a client was to search for "wlking to work", they would probably hope to get
responses back like: "I walked to work", "I enjoy walkng to work", and "I walk
to work every day". A human would have an easy time associating these responses;
however, there is no combination of analyzer tokens or filters built into
Elasticsearch that will allow you to get these results without other negative
consequences. First of all, “walking” is spelled wrong. Second, different forms
of the base word “walk” are desired but unlikely to be returned. We will
elaborate on these problems and others momentarily, but suffice it to say that
the off-the-shelf solutions for each are limited.

There is a fine line to walk, however. A savvy analyst experienced in querying
text and who knows their data, may be looking for misspelled words or particular
word forms for a legitimate reason. This is not a line we want to walk, so we
designed our indexing solution with both a _similar_ analyzer and _exact_
analyzer in mind. Our similar analyzer is the default method for straightforward
queries; but, if desired, double quotes can be used to dictate only an exact
match on keywords. The exact analyzer also ensures that we can extract tokens in
a more raw form for building models.

Much like CrateDB’s standard analyzer, our _similar_ analyzer separates words
according to the [UAX #29: Unicode Text Segmentation] specification and ignores
punctuation. However, it then performs conservative spell correction on the
terms and identifies their base forms (a process known as lemmatization). The
exact analyzer also separates words according to the same specification, but it
keeps all punctuation as unique tokens, giving even more querying power to
skilled users. Both analyzers are case-insensitive, and use a custom character
folding filter to enhance performance in non-English languages.

For the rest of this article, we will elaborate on the character folding,
lemmatization, and spell correction techniques we have developed to power the
indexing behind Text iQ.

## Character Folding

Did you know that there are at least 10 different apostrophe characters? When a
user types the apostrophe key (next to the semicolon key) on a standard American
keyboard, the Unicode value that is typed changes depending on the program used
and the symbol’s context.

For example, if I press the apostrophe key in a typical IDE, it’s going to be
Unicode #0027. But, in the word processor I’m using right now, it’s #2019 when
used as an actual apostrophe. But if used as single quotes as in ‘ ’ there are
two different Unicode characters: This makes matching an index on an apostrophe
potentially very difficult. What’s more, even if the UI you present to the user
is very strict in how it receives inputs from the keyboard, the user can copy
and paste text from anywhere. It’s the wild west when it comes to Unicode
representation and not just for apostrophes. How should you handle symbols like
ä, ǣ, and ç for example?

This is one of the reasons you should always use character folding when indexing
text. Character folding is the process of mapping multiple types of characters
into a single set of characters, usually one. Elasticsearch’s built-in
ASCIIFolding filter is particularly useful as it converts all Unicode characters
into the first 127 ASCII characters. So now there is only one representation of
apostrophes, #0027.

The ASCIIFolding filter works great for English, but it results in some
significant mistakes in other languages. For example, the filter will convert ä
into “a”; but, in German, this should be converted to “ae”. In French, ç should
not be changed at all. And one more example, most of those nasty apostrophe
characters mentioned above should actually be treated as double quotes in German
(I’ve come to really hate apostrophes).

We’ve developed our own custom folding filter for Text iQ that wraps around the
ASCIIFolding filter. This custom filter allows us to specify exceptional rules
for any combination of language and analyzer type (i.e. _similar_ vs. _exact_).

## Lemmatization

Lemmatization is the process of identifying the base or dictionary form of a
word. It differs from stemming which is the process of identifying the root part
of a word and does not always yield an actual word. For example, the stem of the
word “destabilized” is “stabil” where as the lemmatized form is “destabilize”.

Stemming is the only option available with built-in CrateDB filters. The
motivation for using stemmers over lemmatizers is that stemming is generally
easier to compute, and that the actual content of the index does not matter as
long as the search results are accurate–it doesn’t matter that the index is
populated with non-words.

However, we are using CrateDB as a working database in addition to a search
engine. Our web-app can return vocabulary frequencies for visualizations like
word clouds, and we don’t want non-words populating these. Furthermore, we have
found that all the default stemming options to be inaccurate compared to a
good lemmatizer. Returning to the “destabilize” example, would you want the
search terms “stabilize” and “destabilize” to return the same results? Or how
would you feel about the search term “organize” returning “organ”?

For our _similar_ analyzer, we developed our own lemmatization filter using
WordNet’s lemmatization library, Morphy. Compare the results of the Morphy
lemmatizer with 3 available CrateDB stemmers:

|                 | porter   | kstem       | hunspell       | WN Lemma    |
| --------------- | -------- | ----------- | -------------- | ----------- |
| **run**         | run      | run         | run            | run         |
| **ran**         | ran      | ran         | ran            | run         |
| **runs**        | run      | runs        | run            | run         |
| **running**     | run      | running     | running        | run         |
| **is**          | is       | is          | i              | be          |
| **are**         | ar       | are         | are            | be          |
| **was**         | wa       | was         | was            | be          |
| **race**        | race     | race        | race           | race        |
| **racing**      | race     | racing      | race, racing\* | race        |
| **races**       | race     | races       | race           | race        |
| **disorganize** | disorgan | disorganize | organize       | disorganize |

\* stemmers can sometimes produce multiple tokens at the same position.

Using Morphy, our lemmatizer is more comprehensive and accurate, and it
guarantees real words.

Morphy enables our English solution for lemmatization; however, there are far
fewer lemmatization libraries for non-english languages. To support
lemmatization in any language, we create large dictionaries that map numerous
words with their most common lemmatized form. The process for generating these
dictionaries varies language by language.
And while this approach isn't quite as powerful as our approach for lemmatizing
in English, it exceeds the built-in stemming available in Elasticsearch and CrateDB.

## Spelling Correction

Elasticsearch doesn’t have any spelling correction filters. There is the
hunspell stemmer, but it is just that, a stemmer. It uses hunspell dictionaries
to perform stemming, but doesn’t do any spell correction.

The _fuzziness_ option under the _match_ predicate can be used for a form of
spell correction. Tokens aren’t modified, but misspellings can be identified in
a search. This can be problematic for short terms. E.g. “car” matches “can” with
a fuzziness of 1. The _prefix_length_ option sets a minimum number of characters
at the beginning of a term that must match. This can mitigate the above problem,
but still isn’t a perfect solution. E.g. "mileage" matches "village" with a
fuzziness of 2 and _prefix_length_ of 3.

As a poor man’s spell corrector, Elasticsearch recommends a fuzziness of 1 and a
_prefix_length_ of 3. We wanted to do better than that.

We implemented our own spell correction filter that makes use of Lucene’s built
in SpellChecker but uses a unique heuristic that combines three distinct
dictionaries–each with a different purpose. We initialize Lucene’s Spellchecker
with one dictionary for checking misspellings and a different one for offering
suggestions based on Levenshtein distance. The checking dictionary
(CHECKING_DICT) is the larger of the two and contains over 300,000 terms
including proper nouns.

The suggesting dictionary (SUGGESTING_DICT) uses a selection of just over
100,000 words and no proper nouns. By using a more selective suggesting
dictionary, we mitigate unlikely corrections. The third dictionary (COMMON_DICT)
contains a mapping of about 5000 common spelling corrections such as _teh_ ->
_the_. This third dictionary handles common mistakes that Lucene’s SpellChecker
otherwise misses. In particular, it catches errors in small words (less than 4
characters) which are completely ignored by Lucene.

Our spell correction heuristic is as follows:

```text
For each token:
  If not in CHECKING_DICT
    If not in COMMON_DICT
       If token length > 3
          Get top 10 suggestions from SpellChecker(SUGGESTING_DICT)
          return first suggestion with the same first char as token
          otherwise return token
       else return token
    else return COMMON_DICT(token)
  else return token
```

## Summary

We have been able to develop the custom filters and analyzers described in this
article as a single java plugin for CrateDB making deployment and upgrades
straightforward. This has made all the difference in continuing to provide an
intuitive experience for the users of Text iQ.

Users can get back the types of responses they would expect without ever
realizing the processes occurring under the hood. And thanks to the level of control
CrateDB gives us, as developers, we can access our data in a way that can support
all the powerful models that make Text iQ a signature experience.

:::{note} The [original version] of this article was published on the former
Qualtrics engineering blog.
:::

[original version]: https://web.archive.org/web/20250210021928/https://www.qualtrics.com/eng/indexing-text-for-both-effective-search-and-accurate-analysis/
[UAX #29: Unicode Text Segmentation]: https://www.unicode.org/reports/tr29/
