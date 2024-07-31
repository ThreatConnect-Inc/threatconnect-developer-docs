====
Tags
====

Tags can be used to add metadata, or keywords, to Groups, Indicators, Victims, and Workflow Cases. They provide a way to quickly identify or follow associated activities of a particular interest across ThreatConnect.

Endpoint: ``/api/v3/tags``

.. attention::
    When retrieving Tags, the response will include Tags in your Organization and system-generated ATT&CK® Tags by default. To retrieve Tags in a Community or Source your API user account has access to, include the ``owner`` query parameter in your request to `specify that Community or Source <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_.

.. include:: fields.rst

.. include:: create.rst

.. include:: retrieve.rst

.. include:: update.rst

.. include:: delete.rst

.. include:: assign_security_coverage.rst

----

*MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation.*