(crate-pdo)=

# CrateDB PDO

:::{div} .float-right .text-right
[![crate-pdo CI](https://github.com/crate/crate-pdo/actions/workflows/tests.yml/badge.svg)](https://github.com/crate/crate-pdo/actions/workflows/tests.yml)
:::
:::{div} .clearfix
:::

The PHP Data Objects (PDO) is a standard PHP extension that defines a common
interface for accessing databases in PHP.
The {ref}`crate-pdo:index`, `crate/crate-pdo`, implements this specification,
wrapping access to CrateDB's HTTP interface.

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
