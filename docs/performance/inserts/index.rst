==================
Insert Performance
==================

A ``INSERT INTO`` statement is processed as follows:

- Parse the statement to create an `abstract syntax tree`_
- Do some basic semantic validation
- Plan the operation
- Execute the operation

CrateDB :ref:`calculates the shard ID <crate-reference:sharding-routing>` for
every row to be inserted when executing
the operation. Insert requests are then grouped and sent to the nodes that hold
each primary shard.

You can reduce the processing overhead by either eliminating the needless
repetition of some steps or by reducing the work needed to be done by one or
more steps.

This section of the guide will show you how.

.. rubric:: Table of contents

.. toctree::
   :maxdepth: 2

   methods
   bulk
   parallel
   tuning
   testing
   sequences

.. _Abstract Syntax Tree: https://en.wikipedia.org/wiki/Abstract_syntax_tree
