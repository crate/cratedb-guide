.. highlight:: bash

.. _install_basic:

===============
Getting started
===============

.. contents::
   :local:
   :depth: 1


Introduction
============

This part of the documentation covers the installation of CrateDB on Linux and
macOS systems.
The first step to using any software package is getting it properly installed.
Please read this section carefully.

By installing CrateDB the way outlined in this document, you will be able to
quickly set up and run a single-node cluster. The document describes different
installation methods. While we recommend using the package-based methods
for :ref:`install-deb` and :ref:`install-rpm` by subscribing to the respective
release channels, you can also download release archives and run CrateDB
manually using the :ref:`install-adhoc` method.

When the installation is finished, the CrateDB service should be up and
running. Then, you can access the :ref:`Admin UI <crate-admin-ui:index>` from your
local machine by navigating to::

    http://localhost:4200/

After successfully installing CrateDB, please also consider reading the
:ref:`post-install-notes`.


.. note::

    CrateDB requires a `Java virtual machine`_ to run.

    - Starting with CrateDB 4.2, Java is bundled with CrateDB and no extra
      installation is necessary.

    - CrateDB versions before 4.2 required a separate Java installation. For
      CrateDB 3.0 to 4.1, Java 11 is the minimum requirement. CrateDB versions
      before 3.0 require Java 8. We recommend using OpenJDK_ on Linux Systems.


.. _install-quick:

Try CrateDB without installing
==============================

If you want to try out CrateDB on Linux or macOS but would prefer to avoid the
hassle of manual installation or extracting release archives, you can get a
fresh CrateDB node up and running in your current working directory with a
single command:

.. code-block:: console

   sh$ bash -c "$(curl -L https://try.crate.io/)"


.. NOTE::

    This is a quick way to *try out* CrateDB. It is not the recommended method
    to *install* CrateDB in a durable way. The following sections will outline
    that method.


.. _install-linux:

Linux
=====

.. _install-deb:

Debian or Ubuntu
----------------

This section of the documentation outlines how to install CrateDB deb_ packages
using the apt_ package manager.


Configure package repository
""""""""""""""""""""""""""""

You will need to configure your system to register with and trust packages from
the CrateDB package repository::

    # Install prerequisites.
    sudo apt update
    sudo apt install --yes apt-transport-https apt-utils curl gnupg lsb-release

    # Import the public GPG key for verifying the package signatures.
    curl -sS https://cdn.crate.io/downloads/deb/DEB-GPG-KEY-crate | sudo tee /etc/apt/trusted.gpg.d/cratedb.asc

    # Compute CrateDB package repository location.
    [[ $(lsb_release --id --short) = "Debian" ]] && repository="apt"
    [[ $(lsb_release --id --short) = "Ubuntu" ]] && repository="deb"
    distribution=$(lsb_release --codename --short)

    # Register with the CrateDB package repository.
    echo "deb [signed-by=/etc/apt/trusted.gpg.d/cratedb.asc arch=amd64] https://cdn.crate.io/downloads/${repository}/stable/ ${distribution} main" \
        | sudo tee /etc/apt/sources.list.d/cratedb.list

.. NOTE::

    CrateDB provides both *stable release* and *testing release* channels. To
    use the testing channel, replace ``stable`` with ``testing`` in the command
    line above. You can read more about the `release workflow`_.

    The walkthrough is based on the ``sudo`` program. If it is not installed on
    your machine, run ``apt update; apt install --yes sudo`` as a ``root`` user.

Now, update the package sources::

    sudo apt update

You should see a success message. This indicates that the CrateDB package
repository is correctly registered.

Install CrateDB
"""""""""""""""

With everything set up, you can install CrateDB::

    sudo apt install crate


Control CrateDB
"""""""""""""""

You can control the ``crate`` service with the ``systemctl`` utility program::

    sudo systemctl COMMAND crate

Replace ``COMMAND`` with ``start``, ``stop``, ``restart``, ``status`` and
so on.


.. _install-rpm:

Red Hat or CentOS
-----------------

This section of the documentation outlines how to install CrateDB RPM_ packages
using the YUM_ package manager.


Configure package repository
""""""""""""""""""""""""""""

You will need to configure your system to register with and trust packages
from the CrateDB package repository::

    # Install prerequisites.
    yum install sudo

    # Import the public GPG key for verifying the package signatures.
    sudo rpm --import https://cdn.crate.io/downloads/yum/RPM-GPG-KEY-crate

    # Register with the CrateDB package repository.
    sudo rpm -Uvh https://cdn.crate.io/downloads/yum/7/x86_64/crate-release-7.0-1.x86_64.rpm

The command above will install the ``/etc/yum.repos.d/crate.repo`` package
repository configuration file.

.. NOTE::

    CrateDB provides both *stable release* and *testing release* channels. You
    can read more about the `release workflow`_.

    By default, yum_ (Red Hat's package manager) will use the stable
    repository. This is because the testing repository is disabled.
    If you would like to enable the testing repository, edit the ``crate.repo``
    file and set ``enabled=1`` within the ``[crate-testing]`` section.


Install CrateDB
"""""""""""""""

With everything set up, you can install CrateDB::

    sudo yum install crate

After the installation is finished, the ``crate`` service should be installed,
but not running. Use the following command to start CrateDB::

    sudo systemctl start crate

In order to make the service reboot-safe, invoke::

    sudo systemctl enable crate


Control CrateDB
"""""""""""""""

You can control the ``crate`` service with the ``systemctl`` utility program::

    sudo systemctl COMMAND crate

Replace ``COMMAND`` with ``start``, ``stop``, ``restart``, ``status`` and
so on.


Docker
======

CrateDB and Docker_ are great matches thanks to CrateDB's shared-nothing,
horizontally scalable architecture that lends itself well to containerization.

In order to spin up a container using the most recent stable version of the
official `CrateDB Docker image`_, use::

    docker run --publish=4200:4200 --publish=5432:5432 --pull=always crate

.. TIP::

    If this command aborts with an error, please consult the :ref:`Docker
    troubleshooting guide <docker-troubleshooting>`. You are also
    welcome to learn more about :ref:`resource_constraints` with respect
    to running CrateDB within containers.

.. CAUTION::

    This type of invoking CrateDB will get you up and running quickly.

    Please note, by default, the CrateDB Docker container is ephemeral, so
    data will not be stored in a persistent manner. When stopping the
    container, all data will be lost.

    When you are ready to start using CrateDB for data you care about, please
    consult the :ref:`full guide to CrateDB and Docker <cratedb-docker>`
    in order to configure the Docker setup appropriately by using persistent
    disk volumes.


.. _install-adhoc:

Ad-hoc (Unix, macOS)
====================

This section of the documentation outlines how to use the release archives to
install CrateDB. The walkthrough is suitable to install and run CrateDB on
`Unix-like`_ systems.

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

.. _install-configure:

Basic configuration
===================

In order to configure CrateDB, please take note of the configuration file
locations and the available environment variables.


Configuration files
-------------------

When using the package-based setup flavor for :ref:`install-deb` or
:ref:`install-rpm`, the main CrateDB configuration files are located within the
``/etc/crate`` directory.
When using the :ref:`install-adhoc` setup or the 
:ref:`Microsoft Windows <windows-install>` setup, the configuration files are
located within the ``config/`` directory.

Environment variables
---------------------

When using the package-based setup flavor for :ref:`install-deb` or
:ref:`install-rpm`, the CrateDB startup script uses :ref:`crate-reference:conf-env`
from the ``/etc/default/crate`` file. When using the :ref:`install-adhoc`
setup or the :ref:`Microsoft Windows <windows-install>` setup, the
environment variables will be set by ``bin/crate{.sh,.bat}``.

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


.. _post-install-notes:

Post-install notes
==================

After successfully installing the software, you might want to follow up by
:ref:`taking the guided tour <use>`.

Also, you might enjoy being guided through further information:

* Read more details about the :ref:`crate-reference:config` of CrateDB
* The background about :ref:`crate-howtos:bootstrap-checks`
* Multi-node configuration within the section about :ref:`crate-howtos:clustering` and :ref:`crate-howtos:going-into-production`
* When operating a CrateDB cluster in production, :ref:`performance tuning <crate-howtos:performance>` will also be of interest

.. NOTE::

    As noted within the introductory section, this kind of installation flavor
    will let you quickly set up and run a single-node cluster.

    To add additional CrateDB nodes to this kind of cluster in order to make it
    form a multi-node cluster, you will need to remove the cluster state after
    changing the configuration.



.. _7-Zip: https://www.7-zip.org/
.. _apt: https://en.wikipedia.org/wiki/APT_(software)
.. _CrateDB Docker image: https://hub.docker.com/_/crate/
.. _CrateDB release archive: https://cdn.crate.io/downloads/releases/cratedb/
.. _deb: https://en.wikipedia.org/wiki/Deb_(file_format)
.. _Docker: https://www.docker.com/
.. _Java virtual machine: https://en.wikipedia.org/wiki/Java_virtual_machine
.. _OpenJDK: https://openjdk.java.net/projects/jdk/
.. _Other releases of CrateDB: https://cdn.crate.io/downloads/releases/
.. _release workflow: https://github.com/crate/crate/blob/master/devs/docs/release.rst
.. _RPM: https://en.wikipedia.org/wiki/RPM_Package_Manager
.. _starting PowerShell: https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.1#how-do-i-launch-powershell
.. _Unix-like: https://en.wikipedia.org/wiki/Unix-like
.. _YUM: https://en.wikipedia.org/wiki/Yum_(software)
