.. _windows-install:

=======
Windows
=======

This section of the documentation outlines how to use the release archives to
run CrateDB on Microsoft Windows.

.. CAUTION::

    We do not yet officially support CrateDB on Windows for production use. If
    you would like to deploy CrateDB on Windows, please feel free to `contact
    us`_ so we can work with you on a solution.

#. Download the latest `CrateDB release archive`_ for Windows.

#. Once downloaded, extract the archive either using your favorite terminal or
   command-line shell or by using a GUI tool like `7-Zip`_. We recommend
   using `PowerShell`_ when using terminal::

       # Extract Zip archive
       unzip -o crate-*.zip

#. On the terminal, change into the extracted ``crate`` directory::

       cd crate-*

#. Run a CrateDB single-node instance on the local network interface::

       ./bin/crate

#. You will be notified by an INFO message similar to this, when your
   single-node cluster is started successfully::

       [2022-07-04T19:41:12,340][INFO ][o.e.n.Node] [Aiguille Verte] started

#. In order to stop CrateDB again, use :kbd:`ctrl-c`. You will be asked to
   terminate the job. Input :kbd:`Y`::

       Terminate batch job (Y/N)? Y

.. SEEALSO::

      Consult the :ref:`crate-reference:cli` documentation for further information
      about the ``./bin/crate`` command.


.. NOTE::

    If you are installing CrateDB on a recent `Windows Server`_ edition,
    setting up the latest *Microsoft Visual C++ 2019 Redistributable* package
    is required. You can download it at `msvcrt x86-64`_, `msvcrt x86-32`_ or `msvcrt ARM64`_.

    Within the terminal, as a Windows user, the prompt after 
    `starting PowerShell`_ will look like this.

    .. code-block:: doscon

        PS> ./bin/crate


.. _7-Zip: https://www.7-zip.org/
.. _contact us: https://crate.io/contact/
.. _CrateDB release archive: https://cdn.crate.io/downloads/releases/cratedb/x64_windows/
.. _msvcrt ARM64: https://aka.ms/vs/16/release/VC_redist.arm64.exe
.. _msvcrt x86-32: https://aka.ms/vs/16/release/vc_redist.x86.exe
.. _msvcrt x86-64: https://aka.ms/vs/16/release/vc_redist.x64.exe
.. _Powershell: https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2
.. _starting PowerShell: https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.1#how-do-i-launch-powershell
.. _Windows Server: https://www.microsoft.com/en-us/windows-server
