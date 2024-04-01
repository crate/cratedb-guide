Post-install notes
==================

After successfully installing CrateDB, for example on your workstation, the web-based
Admin UI can be visited at::

    http://localhost:4200/

.. SEEALSO::

   If you are new to CrateDB, you may want to follow up by :ref:`taking the guided tour <use>`.

Also, let us outline those information entrypoints as suggestions to explore next:

* Read more details about the :ref:`crate-reference:config`.
* The background about :ref:`bootstrap-checks`.
* Multi-node configuration within the section about :ref:`crate-howtos:clustering`
  and :ref:`going-into-production`.
* When operating a CrateDB cluster in production, please also take
  :ref:`performance tuning <performance>` into consideration.

.. NOTE::

    This kind of installation flavor will let you quickly set up and start a
    **single-node cluster**. When adding additional CrateDB nodes, in order to
    make it form a **multi-node cluster**, you will need to reset (remove) the
    cluster state after changing the configuration.

.. CAUTION::

    Please make sure to read the :ref:`upgrade-planning`, and the guidelines about :ref:`rolling
    upgrades <rolling_upgrade>` and :ref:`full restart upgrades <full_restart_upgrade>`,
    before upgrading a running cluster.

