.. highlight:: bash

.. _install-rpm:
.. _install-redhat:
.. _install-suse:

#######################################
CrateDB on Red Hat, SUSE, and Derivates
#######################################

This section of the documentation outlines how to install CrateDB RPM_ packages
using the YUM_ package manager.

This installation method is suitable for RedHat Enterprise Linux (RHEL) and compatible
systems like Fedora, CentOS, Rocky Linux, AlmaLinux, AWS Linux, Oracle Linux, or
Scientific Linux. Installation also works on openSUSE and SUSE Linux Enterprise Server
(SLES) systems.

Configure package repository
============================

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
===============

With everything set up, you can install CrateDB::

    sudo yum install crate


.. include:: _control-linux.rst
.. include:: _post-install.rst

.. _release workflow: https://github.com/crate/crate/blob/master/devs/docs/release.rst
.. _RPM: https://en.wikipedia.org/wiki/RPM_Package_Manager
.. _YUM: https://en.wikipedia.org/wiki/Yum_(software)
