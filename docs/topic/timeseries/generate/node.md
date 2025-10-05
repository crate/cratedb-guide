(gen-ts-javascript)=

# Generate time series data using Node.js

This tutorial will show you how to generate {ref}`mock time series data
<gen-ts>` about the [International Space Station] (ISS) using [Node.js].

:::{SEEALSO}
{ref}`gen-ts`
:::

## Prerequisites

You must have CrateDB {ref}`installed and running <install>`.

Make sure you're running an up-to-date version of [Node.js].

Then, upgrade to the latest [npm] version:

```console
sh$ npm install -g npm@latest
```

Install the [node-postgres] and [Axios] libraries:

```console
sh$ npm install pg axios
```

The `node-postgres` and `axios` libraries both use [promises] when
performing network operations. Promises are a way of encapsulating the eventual
result of an asynchronous operation.

:::{seealso}
If you're not familiar with asynchronous operations and promises, check out
Mozilla's [detailed guide] on the topic.
:::

Most of this tutorial is designed for Node's [interactive REPL mode] so that
you can experiment with the commands as you see fit. Since both libraries use
promises, you should start `node` with support for the [await] operator:

```console
sh$ node --experimental-repl-await
```

## Get the current position of the ISS

[Open Notify] is a third-party service that provides an API to consume data
about the current position, or [ground point], of the ISS.

The endpoint for this API is [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json).

Start an interactive Node session (as above).

Next, import the [Axios] library:

```js
> const axios = require('axios').default;
```

Then, read the current position of the ISS with an HTTP GET request to the Open
Notify API endpoint:

```js
> let response = await axios.get('http://api.open-notify.org/iss-now.json')
```

```js
> response.data
{
  iss_position: { longitude: '-107.0497', latitude: '42.5431' },
  message: 'success',
  timestamp: 1582568638
}
```

As shown, the endpoint returns a JSON payload, which contains an
`iss_position` object with `latitude` and `longitude` data.

You can encapsulate this operation with a function that returns longitude and
latitude as a [WKT] string:

```js
> async function position() {
...     let response = await axios.get('http://api.open-notify.org/iss-now.json')
...     return `POINT (${response.data.iss_position.longitude} ${response.data.iss_position.latitude})`
... }
```

When you run this function, it should return your point string:

```js
> await position()
```

```js
'POINT (-99.4196 38.1642)'
```

## Set up CrateDB

First, import the [node-postgres] client:

```js
> const { Client } = require('pg')
```

Then [connect] to CrateDB, using the {ref}`crate-reference:interface-postgresql` port
(`5432`):

```js
> const client = new Client({connectionString: 'postgresql://crate@localhost:5432/doc'})
```

```js
> await client.connect()
```

Finally, {ref}`create a table <crate-reference:ddl-create-table>` suitable for writing
ISS position coordinates.

```js
> var query = `
...     CREATE TABLE iss (
...         timestamp TIMESTAMP GENERATED ALWAYS AS CURRENT_TIMESTAMP,
...         position GEO_POINT)`
```

```js
> await client.query(query)
```

```js
Result {
  command: 'CREATE',
  rowCount: 1,
  oid: null,
  rows: [],
  fields: [],
  _parsers: undefined,
  _types: TypeOverrides {
    _types: {
      getTypeParser: [Function: getTypeParser],
      setTypeParser: [Function: setTypeParser],
      arrayParser: [Object],
      builtins: [Object]
    },
    text: {},
    binary: {}
  },
  RowCtor: null,
  rowAsArray: false
}
```

Success!

In the {ref}`crate-admin-ui:index`, you should see the new table when you navigate to
the *Tables* screen using the left-hand navigation menu:

```{image} /_assets/img/getting-started/generate-time-series/table.png
```

## Record the ISS position

With the table in place, you can start recording the position of the ISS.

The following command calls your `position` function and will {ref}`insert
<crate-reference:dml-inserting-data>` the result into the `iss` table.

```js
> await client.query("INSERT INTO iss (position) VALUES (?)", [await position()])
```

```js
Result {
  command: 'INSERT',
  rowCount: 1,
  oid: 0,
  rows: [],
  fields: [],
  _parsers: undefined,
  _types: TypeOverrides {
    _types: {
      getTypeParser: [Function: getTypeParser],
      setTypeParser: [Function: setTypeParser],
      arrayParser: [Object],
      builtins: [Object]
    },
    text: {},
    binary: {}
  },
  RowCtor: null,
  rowAsArray: false
}
```

Press the up arrow on your keyboard and hit *Enter* to run the same command a
few more times.

When you're done, you can {ref}`select <crate-reference:sql_dql_queries>` that data
back out of CrateDB.

```js
> let result = await client.query('SELECT * FROM iss')
```

```js
> result.rows
[
  {
    timestamp: 2020-02-24T18:32:09.744Z,
    position: { x: -80.7016, y: 21.5174 }
  },
  {
    timestamp: 2020-02-24T18:31:43.542Z,
    position: { x: -81.8096, y: 22.7667 }
  },
  {
    timestamp: 2020-02-24T18:32:03.622Z,
    position: { x: -80.9554, y: 21.8065 }
  }
]
```

Here you have recorded three sets of ISS position coordinates.

## Automate the process

Now you have key components, you can automate the data collection. Doing this
will require a change of approach.

Previously, you were using a [client] to connect to and insert data into
CrateDB. However, clients are ephemeral, and once closed, you need to recreate
them. Creating a new client requires a handshake with CrateDB, and this
overhead cost can be prohibitive if you are rapidly creating new clients.

Instead, use a [connection pool] to manage your connections. Connection pools
manage a collection of connected clients that you can request, use, and return
to the pool.

Create a new file called `iss-position.js`:

```javascript
const axios = require('axios').default;
const { Pool } = require('pg')
const pool = new Pool({connectionString: 'postgresql://crate@localhost:5432/doc'})

// Sampling resolution
const seconds = 10

// Get data from the API, and, if successful, insert it into CrateDB
function insert() {
    axios.get('http://api.open-notify.org/iss-now.json')
    .then(response => {
        longitude = response.data.iss_position.longitude
        latitude = response.data.iss_position.latitude
        current_position = `POINT (${longitude} ${latitude})`
        return pool.query(
            "INSERT INTO iss (position) VALUES (?)", [current_position])
    })
    .then(_ => console.log("INSERT OK"))
    .catch(err => console.error("INSERT ERROR", err))
}

// Loop indefinitely
async function loop() {
    while (true) {
        insert()
        console.log("Sleeping for 10 seconds...")
        await new Promise(r => setTimeout(r, seconds * 1000))
    }
}

loop()
```

In the above script, you have merged the `position` function with the
insertion. It uses [promise chaining] so that the API query and the CrateDB
insertion can happen sequentially, yet asynchronously.

You also have some basic error handling, in case either the API query or the
CrateDB operation fails.

Here, the script sleeps for 10 seconds after each sample. Accordingly, the time
series data will have a *resolution* of 10 seconds. If you wish to change this
resolution, you may want to configure your script differently.

Run the script from the command line:

```console
sh$ node iss-position.js
INSERT OK
Sleeping for 10 seconds...
INSERT OK
Sleeping for 10 seconds...
INSERT OK
Sleeping for 10 seconds...
```

:::{TIP}
If you get a `MODULE_NOT_FOUND` error when trying to run this script,
make sure you are running it from the same directory where the npm
libraries are installed.
:::

As the script runs, you should see the table filling up in the CrateDB Admin
UI:

```{image} /_assets/img/getting-started/generate-time-series/rows.png
```

Lots of freshly generated time series data, ready for use.

And, for bonus points, if you select the arrow next to the location data, it
will open up a map view showing the current position of the ISS:

```{image} /_assets/img/getting-started/generate-time-series/map.png
```

:::{TIP}
The ISS passes over large bodies of water. If the map looks empty, try
zooming out.
:::

[await]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await
[axios]: https://www.npmjs.com/package/axios
[client]: https://node-postgres.com/apis/client
[connect]: https://node-postgres.com/features/connecting
[connection pool]: https://node-postgres.com/apis/pool
[detailed guide]: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises
[ground point]: https://en.wikipedia.org/wiki/Ground_track
[input values]: https://node-postgres.com/features/queries#Parameterized%20query
[interactive repl mode]: https://www.oreilly.com/library/view/learning-node-2nd/9781491943113/ch04.html
[international space station]: https://www.nasa.gov/mission_pages/station/main/index.html
[node-postgres]: https://www.npmjs.com/package/pg
[node.js]: https://nodejs.org/en/
[npm]: https://www.npmjs.com/
[open notify]: http://open-notify.org/
[promise chaining]: https://javascript.info/promise-chaining
[promises]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
[wkt]: https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
