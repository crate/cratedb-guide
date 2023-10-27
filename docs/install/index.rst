.. _install:

############
Installation
############

This part of the documentation covers the installation of CrateDB on different
kinds of operating systems and environments, both suitable for on-premises and
development sandbox operations.
The first step to using any software package is getting it properly installed.
Please read this section carefully.


********
Variants
********

We recommend to use the package-based installation methods for :ref:`install-deb` and
:ref:`install-rpm`, by subscribing to the corresponding package release channels.

Alternatively, you can also download release archives and run CrateDB manually,
by using the :ref:`install-adhoc` method.

.. toctree::
    :maxdepth: 3
    :titlesonly:

    Debian, Ubuntu <debian-ubuntu>
    Red Hat, SUSE <redhat>
    Windows <windows>
    adhoc
    Tarball <tarball>

    container/index
    cloud/index

    configure


*****
Notes
*****

After the installation is finished, the CrateDB service should be up and
running, and will run a HTTP server on ``localhost:4200``. To access the
:ref:`Admin UI <crate-admin-ui:index>` from your local machine, navigate
to::

    http://localhost:4200/

.. note::

    CrateDB requires a `Java virtual machine`_ to run.

    - Starting with CrateDB 4.2, Java is bundled with CrateDB, and no extra
      installation is necessary.

    - CrateDB versions before 4.2 required a separate Java installation. For
      CrateDB 3.0 to 4.1, Java 11 is the minimum requirement. CrateDB versions
      before 3.0 require Java 8. We recommend to use OpenJDK_ on Linux Systems.


.. _Java virtual machine: https://en.wikipedia.org/wiki/Java_virtual_machine
.. _OpenJDK: https://openjdk.java.net/projects/jdk/
.. _Other releases of CrateDB: https://cdn.crate.io/downloads/releases/
