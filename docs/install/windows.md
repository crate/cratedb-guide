```{highlight} bash
```

(install-windows)=

# Running CrateDB on Windows

How to use the release archives to run CrateDB on Microsoft Windows.

:::{CAUTION}
We do not officially support CrateDB on Windows for production use. If
you would like to deploy CrateDB on Windows, please feel free to [contact
us][contact us] so we can work with you on a solution.
:::

1. Download the latest [CrateDB release archive] for Windows.

2. Once downloaded, extract the archive either using your favorite terminal or
   command-line shell or by using a GUI tool like [7-Zip]. We recommend
   using [PowerShell] when using terminal:

   ```
   # Extract Zip archive
   unzip -o crate-*.zip
   ```

3. On the terminal, change into the extracted `crate` directory:

   ```
   cd crate-*
   ```

4. Run a CrateDB single-node instance on the local network interface:

   ```
   ./bin/crate
   ```

5. You will be notified by an INFO message similar to this, when your
   single-node cluster is started successfully:

   ```
   [2022-07-04T19:41:12,340][INFO ][o.e.n.Node] [Aiguille Verte] started
   ```

6. In order to stop CrateDB again, use {kbd}`ctrl-c`. You will be asked to
   terminate the job. Input {kbd}`Y`:

   ```
   Terminate batch job (Y/N)? Y
   ```

:::{SEEALSO}
Consult the {ref}`crate-reference:cli` documentation for further information
about the `./bin/crate` command.
:::

:::{NOTE}
If you are installing CrateDB on a recent [Windows Server] edition,
setting up the latest *Microsoft Visual C++ 2019 Redistributable* package
is required. You can download it at [msvcrt x86-64], [msvcrt x86-32] or [msvcrt ARM64].

Within the terminal, as a Windows user, the prompt after
[starting PowerShell] will look like this.

```doscon
PS> ./bin/crate
```
:::

:::{include} _post-install.md
:::


[7-zip]: https://www.7-zip.org/
[contact us]: https://cratedb.com/contact/
[cratedb release archive]: https://cdn.crate.io/downloads/releases/cratedb/x64_windows/
[msvcrt arm64]: https://aka.ms/vs/16/release/VC_redist.arm64.exe
[msvcrt x86-32]: https://aka.ms/vs/16/release/vc_redist.x86.exe
[msvcrt x86-64]: https://aka.ms/vs/16/release/vc_redist.x64.exe
[powershell]: https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2
[starting powershell]: https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.4#how-to-launch-powershell
[windows server]: https://www.microsoft.com/en-us/windows-server
