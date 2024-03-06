.. highlight:: bash

.. _debian:
.. _ubuntu:
.. _install-deb:
.. _install-debian:
.. _install-ubuntu:

########################################
CrateDB on Debian, Ubuntu, and Derivates
########################################

Install CrateDB deb_ packages using the apt_ package manager.

This installation method is suitable for Debian systems and derivates
like Ubuntu.

Configure package repository
============================

You will need to configure your system to register with and trust packages from
the CrateDB package repository::

    # Install prerequisites.
    sudo apt update
    sudo apt install --yes apt-transport-https apt-utils curl gnupg lsb-release

    # Import the public GPG key for verifying the package signatures.
    curl -sS https://cdn.crate.io/downloads/debian/DEB-GPG-KEY-crate | \
        sudo tee /etc/apt/trusted.gpg.d/cratedb.asc

    # Add CrateDB repository to Apt
    echo "deb https://cdn.crate.io/downloads/debian/stable/ default main" | \
        sudo tee /etc/apt/sources.list.d/crate-stable.list

.. NOTE::

    CrateDB provides two repositories. A *stable* and a *testing* repository. To use
    the testing repository, replace ``stable`` with ``testing`` in the command
    above. You can read more about our `release workflow`_.

Now, update the package sources::

    sh$ sudo apt update

You should see a success message. This indicates that the CrateDB package
repository is correctly registered.

Install CrateDB
===============

With everything set up, you can install CrateDB::

    sh$ sudo apt install crate

After the installation is finished, you can start the ``crate`` service::

    sh$ sudo systemctl start crate

Once the service is up and running, you can access CrateDB by visiting::

    http://localhost:4200/


Configure CrateDB
=================

Please visit the :ref:`install-configure` documentation section to learn
about the location and meaning of CrateDB's configuration files.


.. include:: _control-linux.rst
.. include:: _post-install.rst

.. _apt: https://en.wikipedia.org/wiki/APT_(software)
.. _deb: https://en.wikipedia.org/wiki/Deb_(file_format)
.. _release workflow: https://github.com/crate/crate/blob/master/devs/docs/release.rst
