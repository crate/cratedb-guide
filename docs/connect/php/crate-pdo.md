(crate-pdo)=

# CrateDB PDO

:::{div} .float-right .text-right
[![crate-pdo CI](https://github.com/crate/crate-pdo/actions/workflows/tests.yml/badge.svg)](https://github.com/crate/crate-pdo/actions/workflows/tests.yml)
:::
:::{div} .clearfix
:::

The PHP Data Objects (PDO) is a standard PHP extension that defines a common
interface for accessing databases in PHP.
The `crate/crate-pdo` driver implements this specification,
wrapping access to CrateDB's HTTP interface.

:::{rubric} Install
:::

```shell
composer require crate/crate-pdo
```

:::{rubric} Synopsis
:::

```php
<?php
require 'vendor/autoload.php';

use Crate\PDO\PDOCrateDB;
use PDO;

$dsn = 'crate:localhost:4200';
$user = 'crate';
$password = null;
$options = [PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC];
$connection = new PDOCrateDB($dsn, $user, $password, $options);

$stm = $connection->query("SELECT * FROM sys.summits ORDER BY height DESC LIMIT 3");
$result = $stm->fetch();
print_r($result);
?>
```

:::{rubric} See also
:::

:::::{grid} 2 2 2 3
:gutter: 2
:padding: 0

::::{grid-item-card} {octicon}`book;1.75em;sd-text-info` &nbsp; Documentation
:link: crate-pdo:index
:link-type: ref
:link-alt: crate/crate-pdo documentation
The full documentation for crate/crate-pdo.
::::

:::::
