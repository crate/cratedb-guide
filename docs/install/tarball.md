(install-tarball)=
(install-macos)=

# Installation from Tarball Archive

:::{div} sd-text-muted
How to use the release archives to install CrateDB.
:::

The walkthrough is suitable to install and run CrateDB on
[Unix-like] systems, for example Linux and macOS.

:::{CAUTION}
You may experience performance issues when running releases from the public
archive on ARM-based macOS systems. For improved performance, we recommend
manually building CrateDB suited for ARM-based macOS. Detailed instructions
can be found in our [manual build guide].
:::

::::::{stepper}
:::::{step} Download
Download the latest [CrateDB release archive]. Please make sure to select
the right release archive matching your system.
:::::

:::::{step} Extract the archive
Once downloaded, extract the archive either using your favorite terminal or
command line shell or by using a GUI tool like [7-Zip]:

```shell
# Extract tarball on Unix-like systems
tar -xzf crate-*.tar.gz
```
:::::

:::::{step} Navigate to directory
On the terminal, change into the extracted `crate` directory:

```shell
cd crate-*
```
:::::

:::::{step} Run CrateDB
Run a CrateDB single-node instance on the local network interface:

```shell
./bin/crate
```

:::{NOTE}
When running a specific version of CrateDB from tarball on a macOS
system for the first time, it is possible that you will encounter an error
like: **"java" cannot be opened because developer cannot be verified.**

This is expected and can be fixed in your system settings:
: - Navigate to **System Preferences** -> **Security and Privacy**
  - On the page you will see an **Allow Anyway** button for "java"
  - After confirming, run the `/bin/crate` command again. You will be
    asked to confirm once more with **Open** button. After that CrateDB
    will run as expected.
:::
:::::

:::::{step} Stop CrateDB
In order to stop CrateDB again, use {kbd}`ctrl-c`.
:::::
::::::

:::{SEEALSO}
Consult the {ref}`crate-reference:cli` documentation for further information
about the `./bin/crate` command.
:::

:::{include} _post-install.md
:::


[7-zip]: https://www.7-zip.org/
[cratedb release archive]: https://cdn.crate.io/downloads/releases/cratedb/
[manual build guide]: https://github.com/crate/crate/blob/master/devs/docs/basics.rst
[unix-like]: https://en.wikipedia.org/wiki/Unix-like
