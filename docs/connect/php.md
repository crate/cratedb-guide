(connect-php)=

# PHP

:::{div} sd-text-muted
Available PHP drivers and adapters for CrateDB and CrateDB Cloud.
:::

## AMPHP PostgreSQL driver

The [AMPHP PostgreSQL driver], `amphp/postgres`, is an asynchronous
PostgreSQL client based on Amp.

:::{rubric} Synopsis
:::
```php
<?php
require 'vendor/autoload.php';

use Amp\Postgres\PostgresConfig;
use Amp\Postgres\PostgresConnectionPool;
use function Amp\async;
use function Amp\Future\await;

await(async(function () {
    $config = PostgresConfig::fromString("host=localhost user=crate");
    $pool = new PostgresConnectionPool($config);
    $statement = $pool->prepare("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3");
    $result = $statement->execute();
    foreach ($result as $row) {
        print_r($row);
    }
}));
?>
```
:::{rubric} Example
:::
- [Connect to CrateDB and CrateDB Cloud using AMPHP/PostgreSQL] &nbsp; [![PHP AMPHP](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-amphp.yml)

## PostgreSQL PDO driver

[PDO_PGSQL] is a PHP-native driver that implements the PHP Data Objects (PDO)
interface to enable access from PHP to PostgreSQL databases. 

:::{rubric} Synopsis
:::
```php
<?php
$connection = new PDO("pgsql:host=localhost;port=5432;user=crate");
$cursor = $connection->query("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3");
print_r($cursor->fetchAll(PDO::FETCH_ASSOC));
?>
```

:::{rubric} Example
:::
- [Use the PDO_PGSQL driver with CrateDB] &nbsp; [![PHP PDO](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml/badge.svg)](https://github.com/crate/cratedb-examples/actions/workflows/lang-php-pdo.yml)

## CrateDB PDO driver

The PHP Data Objects (PDO) is a standard PHP extension that defines a common
interface for accessing databases in PHP.
The {ref}`crate-pdo:index` implements this specification, wrapping access to
CrateDB's HTTP interface.

:::{rubric} Synopsis
:::
```php
<?php

require 'vendor/autoload.php';

use Crate\PDO\PDOCrateDB;

$dsn = '<DATA_SOURCE_NAME>';
$user = 'crate';
$password = null;
$options = null;
$connection = new PDOCrateDB($dsn, $user, $password, $options);

$stm = $connection->query("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3");
$result = $stm->fetch();
print_r($result);
?>
```

[![Tests](https://github.com/crate/crate-pdo/actions/workflows/tests.yml/badge.svg)](https://github.com/crate/crate-pdo/actions/workflows/tests.yml)

## CrateDB DBAL adapter

DBAL is a PHP database abstraction layer that comes with database schema
introspection, schema management, and PDO support.
The {ref}`crate-dbal:index` implements this specification, wrapping access to
CrateDB's HTTP interface. The adapter currently does not support recent
versions of the Doctrine ORM.

:::{rubric} Synopsis
:::
```php
<?php

require 'vendor/autoload.php';

$params = array(
    'driverClass' => 'Crate\DBAL\Driver\PDOCrate\Driver',
    'user' => 'admin',
    'password' => '<PASSWORD>',
    'host' => '<name-of-your-cluster>.cratedb.net',
    'port' => 4200
);

$connection = \Doctrine\DBAL\DriverManager::getConnection($params);
$sql = "SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3";
$result = $connection->query($sql)->fetch();

print_r($result);
?>
```

[![Tests](https://github.com/crate/crate-dbal/actions/workflows/tests.yml/badge.svg)](https://github.com/crate/crate-dbal/actions/workflows/tests.yml)


[AMPHP PostgreSQL driver]: https://github.com/amphp/postgres
[Connect to CrateDB and CrateDB Cloud using AMPHP/PostgreSQL]: https://github.com/crate/cratedb-examples/tree/main/by-language/php-amphp
[PDO_PGSQL]: https://www.php.net/manual/en/ref.pdo-pgsql.php
[Use the PDO_PGSQL driver with CrateDB]: https://github.com/crate/cratedb-examples/tree/main/by-language/php-pdo
