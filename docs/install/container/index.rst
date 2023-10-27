.. _install-container:

###############
Container Setup
###############

CrateDB is ideal for containerized environments, creating and scaling a cluster
takes minutes and your valuable data is always in sync and available.

**********
Quickstart
**********

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


********
Advanced
********

This section demonstrates advanced container setup scenarios using Docker
and Kubernetes.

.. toctree::
   :maxdepth: 1

   Docker <docker>
   Kubernetes <kubernetes/index>

.. _Docker: https://www.docker.com/
.. _CrateDB Docker image: https://hub.docker.com/_/crate/
