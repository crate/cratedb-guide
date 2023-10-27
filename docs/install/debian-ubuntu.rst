.. highlight:: bash

.. _install-deb:

########################################
CrateDB on Debian, Ubuntu, and Derivates
########################################

This section of the documentation outlines how to install CrateDB deb_ packages
using the apt_ package manager.


Configure package repository
============================

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
===============

With everything set up, you can install CrateDB::

    sudo apt install crate


.. include:: _control-linux.rst
.. include:: _post-install.rst

.. _apt: https://en.wikipedia.org/wiki/APT_(software)
.. _deb: https://en.wikipedia.org/wiki/Deb_(file_format)
.. _release workflow: https://github.com/crate/crate/blob/master/devs/docs/release.rst
