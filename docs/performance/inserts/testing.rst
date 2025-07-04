.. _testing_inserts_performance:

==========================
Testing Insert Performance
==========================

The easiest way to test insert performance is by using the `cr8`_ tool.

Inserts generally scale linearly with cluster size, so it is a good idea start
by testing insert performance on a single node.

You should only increase the size of your cluster for testing once you have
established the baseline performance on a single node.

Test data
=========

Using real data
---------------

If you already have a table full of data that you want to test, the best thing
to do is to export that data and test inserting some portion of it into an
identical table that you have created for testing purposes.

You can export the data using :ref:`COPY TO <crate-reference:sql-copy-to>`,
like so:

.. code-block:: psql

    cr> COPY my_table TO DIRECTORY "/tmp/crate"
    COPY OK, 1000000 rows affected  (... sec)

After you have done this, run:

.. code-block:: psql

    cr> SHOW CREATE TABLE my_table;

Then, copy the output from this command, and use it to create a table for
testing purposes, called something like ``my_table_test``.

Generating fake data
--------------------

If you don't have data already, you can generate fake data. But do note that
any differences between fake data and real data may produce significant
performance differences.

Create a table specifically for performance testing:

.. code-block:: psql

    cr> CREATE TABLE my_table_test (
    ...   id integer,
    ...   name string
    ... );
    CREATE OK, 1 row affected  (... sec)

This is a simple example. You should create a table that mirrors the sort of
data you plan to use in production.

Next, generate some fake data:

.. code-block:: sh

    sh$ cr8 insert-fake-data \
          --hosts localhost:4200 \
          --table my_table_test \
          --num-records 1000000

This command will look at your table schema, generate appropriate test data for
the schema, and insert one million test records. You can adjust the number of
records if you wish.

It's important to generate the fake data as a separate step so that our
performance testing isn't also measuring the fake data generation, which in
some situations, might actually end up being the performance bottleneck.

Now, export the fake data as JSON using :ref:`COPY TO <crate-reference:sql-copy-to>`:

.. code-block:: psql

    cr> COPY my_table TO DIRECTORY "/tmp/crate"
    COPY OK, 1000000 rows affected  (... sec)

We're exporting to the ``/tmp/crate`` directory here, but you can export to any
directory you choose.

Truncate the table:

.. code-block:: psql

    cr> DELETE FROM my_table_test;
    DELETE OK, 1000000 rows affected  (... sec)

Running a test
==============

Now you have some test data, you can insert it into your test table and measure
performance, like so:

.. code-block:: sh

    sh$ cat /tmp/crate/my_table_*.json | cr8 insert-json \
          --hosts localhost:4200 \
          --table my_table_test \
          --bulk-size 1000 \
          --concurrency 25

.. NOTE::

   The ``--bulk-size`` and ``--concurrency`` values in the above example are
   set to the default values. If you omit these flags, this is the
   configuration that will be used.

The ``insert-json`` command should produce data like this::

    Executing inserts: bulk_size=1000 concurrency=25
    1000 requests [00:35, 27.84 requests/s]
    Runtime (in ms):
        mean:    103.556 ± 3.957
        min/max: 11.587 → 521.434
    Percentile:
        50:   89.764 ± 63.851 (stdev)
        95:   220.739
        99.9: 475.568

From here, you can adjust the configuration values, and compare the results to
understand the performance profile of your setup.

.. NOTE:

   Setting the bulk records size to `1` approximates the performance of single
   inserts.

.. _cr8: https://github.com/mfussenegger/cr8/
