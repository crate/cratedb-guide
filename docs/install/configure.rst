.. _install-configure:

######################
Configuration Settings
######################

In order to configure CrateDB, please take note of the configuration file
locations and the available environment variables.


Configuration Files
===================

When using the package-based setup flavor for :ref:`install-deb` or
:ref:`install-rpm`, the main CrateDB configuration files are located within the
``/etc/crate`` directory.

When using the :ref:`install-adhoc` setup, or the :ref:`Microsoft Windows <windows-install>`
setup, the configuration files are located within the ``config/`` directory relative to the
working directory.

Environment Variables
=====================

For the vanilla package-based setup flavor, the CrateDB startup script reads
:ref:`crate-reference:conf-env` from the ``/etc/default/crate`` file as
environment variables.

.. Note::

    RPM packages of CrateDB versions up to `5.2.11`_, `5.3.8`_, `5.4.7`_
    and `5.5.2`_ are using the ``/etc/sysconfig/crate`` file instead.

When using the :ref:`install-adhoc` setup, or the :ref:`Microsoft Windows <windows-install>`
setup, the environment variables will be defined by ``bin/crate{.sh,.bat}`` relative to the
working directory.

Here is an example::

    # Configure heap size (defaults to 256m min, 1g max).
    CRATE_HEAP_SIZE=2g

    # Maximum number of open files, defaults to 65535.
    # MAX_OPEN_FILES=65535

    # Maximum locked memory size. Set to "unlimited" if you use the
    # bootstrap.mlockall option in crate.yml. You must also set
    # CRATE_HEAP_SIZE.
    MAX_LOCKED_MEMORY=unlimited

    # Provide additional Java OPTS.
    # CRATE_JAVA_OPTS=

    # Force the JVM to use IPv4 only.
    CRATE_USE_IPV4=true



.. _5.2.11: https://cratedb.com/docs/crate/reference/en/latest/appendices/release-notes/5.2.11.html
.. _5.3.8: https://cratedb.com/docs/crate/reference/en/latest/appendices/release-notes/5.3.8.html
.. _5.4.7: https://cratedb.com/docs/crate/reference/en/latest/appendices/release-notes/5.4.7.html
.. _5.5.2: https://cratedb.com/docs/crate/reference/en/latest/appendices/release-notes/5.5.2.html
.. _sources: https://en.wikipedia.org/wiki/Source_(command)
