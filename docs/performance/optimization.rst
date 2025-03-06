.. _performance-optimization:

########################
 Query Optimization 101
########################

.. _filtering-early:

**************************************
 Do all filtering as soon as possible
**************************************

Sometimes it may be tempting to define some VIEWs, some CTEs, do some JOINs, and
only filter results at the end, but in this context the optimizer may lose track
of how the fields we are filtering on relate to the indexes on the actual
tables.

Whenever there is an opportunity to filter data immediately next to the ``FROM``
clause, try to narrow down results as early as possible.

See `using common table expressions to speed up queries`_ for an example.

.. _minimise-result-sets:

*************************
 Avoid large result sets
*************************

Be aware of the number of rows you are returning in a ``SELECT`` query.
Analytical databases, such as CrateDB, excel at processing large data sets and
returning small to medium-sized result sets. Serializing, transporting them over
the network, and deserializing large result sets is expensive. When dealing with
large result sets in the range of several hundred thousand records, consider
whether your application needs the whole result set at once. Use :ref:`cursors
<server-side-cursor>` or ``LIMIT``/``OFFSET`` to fetch data in batches.

See also `Fetching large result sets from CrateDB`_ for examples.

.. _propagate-limit:

*****************************************
 Propagate LIMIT clauses when applicable
*****************************************

Similarly to the above, we may have for instance a ``LIMIT 10`` at the end of
the query and to get there it may have been sufficient to only pull 10 records
(or some other number of records) at an earlier stage from some given table, if
that is the case duplicate or move (depending on specific query) the ``LIMIT``
clause to the relevant place.

In some cases, we may not know how many rows we need in the intermediate working
sets but we may know for instance that for sure there will be 10 records on the
last day of data, doing such filtering earlier on can be super helpful for the
optimizer and may protect us from accidentally going through years of data.

So for instance instead of:

.. code:: sql

   SELECT
     factory_metadata.factory_name,
     device_data.device_name,
     device_data.reading_value
   FROM device_data
   INNER JOIN factory_metadata ON device_data.factory_id=factory_metadata.factory_id
   WHERE reading_time BETWEEN '2024-01-01' AND '2025-01-01'
   LIMIT 10;

do:

.. code:: sql

   WITH filtered_device_data AS (
      SELECT
            device_data.factory_id,
            device_data.device_name,
            device_data.reading_value
      FROM device_data
      WHERE
            reading_time BETWEEN '2024-12-01' AND '2025-01-01'
            /* we are sure one month of data is sufficient to find 10 results and it may help with partition pruning */
      LIMIT 10
   )
   SELECT
     factory_metadata.factory_name,
     filtered_device_data.device_name,
     filtered_device_data.reading_value
   FROM filtered_device_data
   INNER JOIN factory_metadata ON filtered_device_data.factory_id=factory_metadata.factory_id;

.. _only-sort-when-needed:

****************************
 Only sort data when needed
****************************

Indexing in CrateDB is optimized to support filtering and aggregations without
requiring expensive defragmentation operations, but it is not optimized for
sorting​.

Maintaining a sorted index would slow down ingestion​ and Redshift and other
analytical database systems like Cassandra make similar trade-offs​.

This means that when an ``ORDER BY`` is requested the whole dataset comes in
memory in a node and data is sorted there and then, hence it is important to not
request ``ORDER BY`` operations when not actually needed, there is, of course,
no problem sorting a few thousand rows in the final stage of a ``SELECT`` but we
need to avoid requesting sort operations over millions of rows.

Consider leveraging filters and aggregations like ``max_by`` and ``min_by`` to
get the desired results limiting the scope of ``ORDER BY`` operations or
avoiding them altogether.

So for instance instead of:

.. code:: sql

   SELECT reading_time,reading_value
   FROM device_data
   WHERE reading_time BETWEEN '2024-01-01' AND '2025-01-01'
   ORDER BY reading_time DESC
   LIMIT 10;

use:

.. code:: sql

   SELECT reading_time,reading_value
   FROM device_data
   WHERE reading_time BETWEEN '2024-12-20' AND '2025-01-01'
   ORDER BY reading_time DESC
   LIMIT 10;

.. _filter-with-array-expressions:

***************************************************************************
 Use filters with array expressions when filtering on the output of UNNEST
***************************************************************************

On denormalized data sets you may have records with an array of objects.

You may want to unnest the array in a subquery or CTE and later filter on a
property of the OBJECTs.

.. code:: sql

   SELECT *
   FROM (
      SELECT UNNEST(my_array_of_objects) obj
      FROM my_table
   )
   WHERE obj['field1'] = 1;

Just written like that this will result in every row in the table (not filtered
with other conditions) being read and unnested to check if it meets the criteria
on ``field1``, but CrateDB can do a lot better than this if we add an additional
condition like this:

.. code:: sql

   SELECT *
   FROM (
      SELECT unnest(my_array_of_objects) obj
      FROM my_table
      WHERE 1 = ANY (my_array_of_objects['field1'])
   ) AS subquery
   WHERE obj['field1'] = 1;

CrateDB leverages indexes to only unnest the relevant records from ``my_table``
which can make a huge difference.

.. _format-as-last-step:

******************************
 Format output as a last step
******************************

In many cases, data may be stored in an efficient format but we want to
transform it to make it more human-readable in the output of the query, we may
use `scalar functions`_ such as ``date_format`` or ``timezone``.

Sometimes queries apply these transformations in an intermediate step and later
do further operations like filtering on the transformed values.

The CrateDB optimizer is actually very good at seeing through many of these
situations and still using indexes on the original data. But there is always a
risk that something particular in the query prevents this from happening and we
end up applying the transformation on thousands or millions of records that
later will be discarded. So whenever makes sense we want to only apply these
transformations when we have already worked out the final result set to be sent
back to the client.

So instead of:

.. code:: sql

   WITH mydata AS (
     SELECT
           date_format(device_data.reading_time) AS formatted_reading_time,
           device_data.reading_value
     FROM device_data
     )
   SELECT *
   FROM mydata
   WHERE formatted_reading_time LIKE '2025%';

use:

.. code:: sql

   SELECT
     date_format(device_data.reading_time) AS formatted_reading_time,
     device_data.reading_value
   FROM device_data
   WHERE device_data.reading_time BETWEEN '2025-01-01' AND '2026-01-01'

.. _replace-case:

**********************************************************************
 Replace CASE in expressions used for filtering, JOINs, grouping, etc
**********************************************************************

It is not always obvious to the optimizer what we may be trying to do with a
``CASE`` expression (see for instance `Shortcut CASE evaluation Issue 16022`_).

If you are using CASE expression for “formatting” see the previous point about
formatting output as late as possible,

but if you are using a CASE expression as part of a filter of other operation
consider replacing it with an equivalent expression, for instance:

.. code:: sql

   SELECT SUM(a) as count_greater_than_10,...
   FROM (
     SELECT CASE WHEN field1 > 10 THEN 1 ELSE 0 END
           , ...
     FROM mytable
     ...
   ) subquery
   ...;

can be rewritten as

.. code:: sql

   SELECT COUNT(field1) FILTER (WHERE field1 > 10) as count_greater_than_10
   FROM mytable;

And

.. code:: text

   SELECT *
   FROM mytable
   WHERE
     CASE
           WHEN $1 = 'ALL COUNTRIES' THEN true
           WHEN $1 = mytable.country AND $2 = 'ALL CITIES' THEN true
           ELSE $1 = mytable.country AND $2 = mytable.city
     END;

can be rewritten as

.. code:: text

   SELECT *
   FROM mytable
   WHERE ($1 = 'ALL COUNTRIES')
   OR ($1 = mytable.country AND $2 = 'ALL CITIES')
   OR ($1 = mytable.country AND $2 = mytable.city)

(the exact replacement expressions of course depend on the semantics of each
case)

.. _groups-instead-distinct:

***********************************
 Use groupings instead of DISTINCT
***********************************

(Reference: `Issue 13818`_)

.. code:: sql

   SELECT DISTINCT country FROM customers;

use

.. code:: sql

   SELECT country FROM customers GROUP BY country;

and instead of

.. code:: sql

   SELECT COUNT(DISTINCT a) FROM t;

use

.. code:: sql

   SELECT COUNT(a)
   FROM (
           SELECT a
           FROM t
           GROUP BY a
           ) tmp;

.. _subqueries-instead-groups:

********************************************************************
 Use subqueries instead of GROUP BY if the groups are already known
********************************************************************

Consider the following query:

.. code:: sql

   SELECT customerid, SUM(order_amount) AS total
   FROM customer_orders
   GROUP BY customerid;

This looks simple but to execute it CrateDB needs to keep the full result set in
memory for all groups.

If we already know what the groups will be we can use correlated subqueries
instead:

.. code:: sql

   SELECT customerid,
     (SELECT SUM(order_amount)
      FROM customer_orders
      WHERE customer_orders.customerid = customers.customerid
     ) AS total
   FROM customers;

.. _batch-operations:

******************
 Batch operations
******************

If you need to perform lots of UPDATEs or expensive INSERTs from SELECT, instead
of doing them all in one go, adopt a batch approach where the operations are
done on groups of records each time.

So for instance instead of doing:

.. code:: sql

   UPDATE mytable SET field1=field1+1;

do

.. code:: shell

   for id in {1..100}; do
           crash -c "UPDATE mytable SET field1=field1+1 WHERE customer_id=$id;"
   done

.. _pagination-filters:

****************************************
 Paginate on filters instead of results
****************************************

For instance instead of

.. code:: sql

   SELECT deviceid, AVG(field1)
   FROM device_data
   GROUP BY deviceid
   LIMIT 1000 OFFSET 5000;

We can do something like

.. code:: sql

   WITH devices AS (
     SELECT deviceid
     FROM devices
     LIMIT 5 OFFSET 25
   )
   SELECT deviceid, AVG(field1)
   FROM device_data
   WHERE device_data.deviceid IN (SELECT devices.deviceid FROM devices)
   GROUP BY deviceid;

.. _staging-tables:

*****************************************************************************
 Use staging tables for intermediate results if you are doing a lot of JOINs
*****************************************************************************

If you have many CTEs or VIEWs and need to JOIN these in some cases it can be
effective to store the intermediate results from these into dedicated tables and
then use these tables, while there is a cost in writing to disk and reading data
back we can benefit from indexing and from giving the optimizer more
straightforward execution plans that it can optimize for parallel execution
using multiple nodes in the cluster.

.. _select-star:

********************
 Avoid ``SELECT *``
********************

CrateDB is a columnar database. The fewer columns you specify in a ``SELECT``
clause, the less data CrateDB needs to read from disk.

.. code:: sql

   -- Avoid selecting all columns
   SELECT *
   FROM customers

   -- Instead select explicitly the subset of columns you need
   SELECT customerid, country
   FROM customers

.. _consider-generated-columns:

****************************
 Consider generated columns
****************************

If you frequently find yourself extracting information from fields and then
using this extracted data on filters or aggregation it can be good to consider
doing this operation on ingestion with a `generated column`_, this way the value
we need for filtering and aggregations can be indexed.

See `Using regex comparisons and other features for inspection of logs`_ for an
example.

.. _udf-right-context:

*****************************************************************************************
 Be mindful of UDFs, leverage them in the right contexts, but only in the right contexts
*****************************************************************************************

UDFs run on a javascript virtual machine and on a single thread, so they can
have an impact on performance.

Also once we pass a value through an UDF the engine will have to work with the
results in memory and will not be able to leverage indexes on the underlying
fields anymore so the general considerations about delaying formatting as much
as possible apply.

However, some operations may be more straightforward to do in JavaScript than
SQL.

.. _positive-filters:

*******************************************************************
 Prefer positive filter expressions to negative filter expressions
*******************************************************************

Positive filter expressions can directly leverage indexing, sometimes the
optimizer may be able to rewrite a negative expression to still use indexes but
this may not always happen and the optimizer might not rewrite the query
optimally. Explicitly using positive conditions removes ambiguity and ensures
the most efficient path is chosen.

So instead of:

.. code:: sql

   SELECT
     customerid,
     status
   FROM customers_table
   WHERE NOT (customerid <= 2) AND NOT (status = 'inactive');

We can rewrite this as:

.. code:: sql

   SELECT
     customerid,
     status
   FROM customers_table
   WHERE customerid > 3 AND status = 'active';

.. _use-null-or-empty:

******************************************************************************
 Use the special null_or_empty function with OBJECTs and ARRAYs when relevant
******************************************************************************

CrateDB has a special scalar function called null_or_empty_ , using this in
filter conditions against OBJECTs and ARRAYs is much faster that look for ``IS
NULL`` if accepting empty objects and arrays is acceptable.

So instead of:

.. code:: sql

   SELECT ...
   FROM mytable
   WHERE array_column IS NULL OR array_column = [];

We can rewrite this as:

.. code:: sql

   SELECT ...
   FROM mytable
   WHERE null_or_empty(array_column);

.. _execution-plans:

************************
 Review execution plans
************************

If a query is slow but still completes in a certain amount of time, we can use
`EXPLAIN ANALYZE`_ to get a detailed execution plan. The main thing to watch for
on these is ``MatchAllDocsQuery`` and ``GenericFunctionQuery``. These operations
are full table scans, so you may want to review if that is expected in your
query (you may actually intentionally be pulling all records from a table with a
list of factory sites for instance) or if this is about a filter that is not
being pushed down properly.

.. _explain analyze: https://cratedb.com/docs/crate/reference/en/latest/sql/statements/explain.html

.. _fetching large result sets from cratedb: https://community.cratedb.com/t/fetching-large-result-sets-from-cratedb/1270

.. _generated column: https://cratedb.com/docs/crate/reference/en/latest/general/ddl/generated-columns.html

.. _issue 13818: https://github.com/crate/crate/issues/13818

.. _null_or_empty: https://cratedb.com/docs/crate/reference/en/latest/general/builtins/scalar-functions.html#null-or-empty-object

.. _scalar functions: https://cratedb.com/docs/crate/reference/en/latest/general/builtins/scalar-functions.html

.. _shortcut case evaluation issue 16022: https://github.com/crate/crate/issues/16022

.. _using common table expressions to speed up queries: https://community.cratedb.com/t/using-common-table-expressions-to-speed-up-queries/1719

.. _using regex comparisons and other features for inspection of logs: https://community.cratedb.com/t/using-regex-comparisons-and-other-advanced-database-features-for-real-time-inspection-of-web-server-logs/1564
