(objects-basics)=
(objects-usage)=
(objects-tutorial-marketing)=

# Objects: Analyzing Marketing Data

:::{article-info}
---
avatar: https://avatars.githubusercontent.com/u/23557193?v=4
avatar-link: https://github.com/proddata
avatar-outline: muted
author: Georg Traar
date: September 29, 2023
read-time: 4 min read
class-container: sd-p-2 sd-outline-muted sd-rounded-1
---
:::

:::{include} /_include/links.md
:::

Marketers often need to handle multi-structured data from different platforms.
CrateDB's dynamic `OBJECT` data type allows us to store and analyze this complex,
nested data efficiently. In this tutorial, we'll explore how to leverage this
feature in marketing data analysis, along with the use of generated columns to
parse and manage URLs.

Consider marketing data that captures details of various campaigns.

:::{code} json
{
    "campaign_id": "c123",
    "source": "Google Ads",
    "metrics": {
        "clicks": 500,
        "impressions": 10000,
        "conversion_rate": 0.05
    },
    "landing_page_url": "https://example.com/products?utm_source=google"
}
:::

To begin, let's create the schema for this dataset.

::::::{stepper}

## Create the table

:::{div}
The fastest and easiest way to get started with CrateDB is by deploying a
free tier (CRFREE) cluster on [CrateDB Cloud][CrateDB Cloud Console]. Otherwise,
see the {ref}`install` section to run CrateDB yourself.
:::

CrateDB uses SQL, the most popular query language for database management. To
store the marketing data, create a table with columns tailored to the
dataset using the `CREATE TABLE` command:

:::{code} sql
CREATE TABLE marketing_data (
    campaign_id TEXT PRIMARY KEY,
    source TEXT,
    metrics OBJECT(DYNAMIC) AS (
        clicks INTEGER,
        impressions INTEGER,
        conversion_rate DOUBLE PRECISION
    ),
    landing_page_url TEXT,
    url_parts GENERATED ALWAYS AS parse_url(landing_page_url)
);
:::

Let's highlight two features in this table definition:

:metrics: An `OBJECT` column featuring a dynamic structure for
  performing flexible queries on its nested attributes like
  clicks, impressions, and conversion rate.
:url_parts: A generated column to
  decode an URL from the `landing_page_url` column. This is convenient
  to query for specific components of the URL later on.

The table is designed to accommodate both fixed and dynamic attributes,
providing a robust and flexible structure for storing your marketing data.

## Insert data

Now, insert the data using the `COPY FROM` SQL statement.

:::{code} sql
COPY marketing_data
FROM 'https://cdn.crate.io/downloads/datasets/cratedb-datasets/cloud-tutorials/data_marketing.json.gz'
WITH (format = 'json', compression='gzip');
:::

## Analyze data

Start with a basic `SELECT` statement on the `metrics` column, and limit the
output to display only 10 records, in order to quickly explore a few samples
worth of data.

:::{code} sql
SELECT metrics
FROM marketing_data
LIMIT 10;
:::

You can see that the `metrics` column returns an object in the form of a JSON.
If you just want to return a single property of this object, you can adjust the
query slightly by adding the property to the selection using bracket notation.

:::{code} sql
SELECT metrics['clicks']
FROM marketing_data
LIMIT 10;
:::

It's helpful to select individual properties from a nested object, but what if
you also want to filter results based on these properties? For instance, to find
`campaign_id` and `source` where `conversion_rate` exceeds `0.09`, employ
the same bracket notation for filtering as well.

:::{code} sql
SELECT campaign_id, source
FROM marketing_data
WHERE metrics['conversion_rate'] > 0.09
LIMIT 50;
:::

This allows you to narrow down the query results while still leveraging CrateDB's
ability to query nested objects effectively.

Finally, let's explore data aggregation based on UTM source parameters. The
`url_parts` generated column, which is populated using the `parse_url()`
function, automatically splits the URL into its constituent parts upon data
insertion.

To analyze the UTM source, you can directly query these parsed parameters. The
goal is to count the occurrences of each UTM source and sort them in descending
order. This lets you easily gauge marketing effectiveness for different sources,
all while taking advantage of CrateDB's powerful generated columns feature.

:::{code} sql
SELECT
    url_parts['parameters']['utm_source'] AS utm_source,
    COUNT(*)
FROM marketing_data
GROUP BY 1
ORDER BY 2 DESC;
:::

In this tutorial, we explored the versatility and power of CrateDB's dynamic
`OBJECT` data type for handling complex, nested marketing data.

::::::
