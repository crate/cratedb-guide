.. _install:

############
Installation
############

This section of the documentation covers the installation of CrateDB on different
kinds of operating systems and environments, both suitable for on-premises and
development sandbox operations.

The first step to using any software package is getting it properly installed.
Please read this section carefully.


.. toctree::
    :maxdepth: 3
    :hidden:

    Debian, Ubuntu <debian-ubuntu>
    Red Hat, SUSE <redhat>
    Windows <windows>
    Tarball <tarball>

    container/index
    cloud/index

    configure


.. Layout stolen from Streamlink.
.. https://github.com/streamlink/streamlink/blob/master/docs/install.rst?plain=1

.. Icons from sphinx{design}.
.. https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html#inline-icons
.. https://fontawesome.com/icons/

.. sphinx-design currently doesn't support autosectionlabel, so set labels for
.. the following sections explicitly


.. grid:: 2 2 2 4
    :padding: 0
    :class-container: installation-grid

    .. grid-item-card:: Debian, Ubuntu
        :link: install-debian
        :link-type: ref
        :link-alt: Debian and Ubuntu Linux
        :padding: 3
        :text-align: center
        :class-card: sd-pt-3
        :class-body: sd-fs-1
        :class-title: sd-fs-6

        :fab:`linux`
        :fab:`ubuntu`

    .. grid-item-card:: Red Hat, SUSE
        :link: install-rpm
        :link-type: ref
        :link-alt: RPM Linux: Red Hat, SUSE
        :padding: 3
        :text-align: center
        :class-card: sd-pt-3
        :class-body: sd-fs-1
        :class-title: sd-fs-6

        :fab:`redhat`
        :fab:`suse`

    .. grid-item-card:: macOS
        :link: install-macos
        :link-type: ref
        :link-alt: macOS
        :padding: 3
        :text-align: center
        :class-card: sd-pt-3
        :class-body: sd-fs-1
        :class-title: sd-fs-6

        :fab:`apple`

    .. grid-item-card:: Windows
        :link: install-windows
        :link-type: ref
        :link-alt: Windows
        :padding: 3
        :text-align: center
        :class-card: sd-pt-3
        :class-body: sd-fs-1
        :class-title: sd-fs-6

        :fab:`windows`

    .. grid-item-card:: Tarball Archive
        :link: install-tarball
        :link-type: ref
        :link-alt: Installation from Tarball
        :padding: 3
        :text-align: center
        :class-card: sd-pt-3
        :class-body: sd-fs-1
        :class-title: sd-fs-6

        :octicon:`archive`

    .. grid-item-card:: Container Setup
        :link: install-container
        :link-type: ref
        :link-alt: Container Setup
        :padding: 3
        :text-align: center
        :class-card: sd-pt-3
        :class-body: sd-fs-1
        :class-title: sd-fs-6

        :octicon:`container`

    .. grid-item-card:: Cloud Hosting
        :link: install-cloud
        :link-type: ref
        :link-alt: Cloud Hosting
        :padding: 3
        :text-align: center
        :class-card: sd-pt-3
        :class-body: sd-fs-1
        :class-title: sd-fs-6

        :fa:`cloud`

    .. grid-item-card:: Config Settings
        :link: install-configure
        :link-type: ref
        :link-alt: Configuration Settings
        :padding: 3
        :text-align: center
        :class-card: sd-pt-3
        :class-body: sd-fs-1
        :class-title: sd-fs-6

        :octicon:`gear`



We recommend to use the package-based installation methods for :ref:`install-deb` and
:ref:`install-rpm`, by subscribing to the corresponding package release channels.

Alternatively, you can also do an :ref:`install-tarball`.


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
