.. _install-tarball:
.. _install-macos:

#################################
Installation from Tarball Archive
#################################

This section of the documentation outlines how to use the release archives to
install CrateDB. The walkthrough is suitable to install and run CrateDB on
`Unix-like`_ systems, for example Linux and macOS.

#. Download the latest `CrateDB release archive`_. Please make sure to select
   the right release archive matching your system.

#. Once downloaded, extract the archive either using your favorite terminal or
   command line shell or by using a GUI tool like `7-Zip`_::

       # Extract tarball on Unix-like systems
       tar -xzf crate-*.tar.gz

#. On the terminal, change into the extracted ``crate`` directory::

       cd crate-*

#. Run a CrateDB single-node instance on the local network interface::

       ./bin/crate

#. In order to stop CrateDB again, use :kbd:`ctrl-c`.

.. SEEALSO::

      Consult the :ref:`crate-reference:cli` documentation for further information
      about the ``./bin/crate`` command.


.. include:: _post-install.rst


.. _7-Zip: https://www.7-zip.org/
.. _CrateDB release archive: https://cdn.crate.io/downloads/releases/cratedb/
.. _Unix-like: https://en.wikipedia.org/wiki/Unix-like
