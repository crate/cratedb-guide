Prepare shortcut for {ref}`crate-crash:index` command.

::::{tab-set}

:::{tab-item} Linux, macOS, WSL
```shell
alias crash="docker compose exec cratedb crash"
alias uv="docker compose run --rm uv uv"
alias uvx="docker compose run --rm uv uvx"
```
:::
:::{tab-item} Windows PowerShell
```powershell
function crash { docker compose exec cratedb crash @args }
```
:::
:::{tab-item} Windows Command
```shell
doskey crash=docker compose exec cratedb crash $*
```
:::

::::
