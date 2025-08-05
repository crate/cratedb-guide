.. _connect-javascript:

==========
JavaScript
==========

This section provides a quick overview of available Node.js modules and
drivers for CrateDB Cloud.

node-postgres
-------------

node-postgres is a collection of Node.js modules for interfacing with a CrateDB
Cloud database.

Example implementation will look like this:

.. code-block:: javascript

	const { Client } = require("pg");

	const crateClient = new Client({
	  host: "<name-of-your-cluster>.cratedb.net",
	  port: 5432,
	  user: "admin",
	  password: "<PASSWORD>",
	  ssl: true,
	});

	(async () => {
	  await crateClient.connect();
	  const result = await crateClient.query("SELECT name FROM sys.cluster");
	  console.log(result.rows[0]);
	})();

For more information see `node-postgres documentation`_.

node-crate
----------

node-crate is an independent Node.js driver driver for CrateDB that communicates via
the `_sql` HTTP endpoint.

Example implementation will look like this:

.. code-block:: javascript

	const crate = require("node-crate");

	crate.connect(`https://admin:${encodeURIComponent("<PASSWORD>")}@<name-of-your-cluster>.cratedb.net:4200`);

	(async () => {
	  const result = await crate.execute("SELECT name FROM sys.cluster");
	  console.log(result.rows[0]);
	})();


For more information see `node-crate documentation`_.

.. _node-postgres documentation: https://www.npmjs.com/package/pg
.. _node-crate documentation: https://www.npmjs.com/package/node-crate
