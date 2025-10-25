(crate-dbal)=

# CrateDB DBAL

:::{div} .float-right .text-right
[![crate-dbal CI](https://github.com/crate/crate-dbal/actions/workflows/tests.yml/badge.svg)](https://github.com/crate/crate-dbal/actions/workflows/tests.yml)
:::
:::{div} .clearfix
:::

DBAL is a PHP database abstraction layer that comes with database schema
introspection, schema management, and PDO support.
The {ref}`crate-dbal:index`, `crate/crate-dbal`, implements this specification,
wrapping access to CrateDB's HTTP interface.
:::{warning}
The adapter currently does not support recent versions of the Doctrine ORM,
see [Add support for Doctrine 3] and [Add support for Doctrine 4]. Both
patches currently stalled, so please explicitly let us know if you have
any need for corresponding support.
:::

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


[Add support for Doctrine 3]: https://github.com/crate/crate-dbal/pull/122
[Add support for Doctrine 4]: https://github.com/crate/crate-dbal/pull/136
