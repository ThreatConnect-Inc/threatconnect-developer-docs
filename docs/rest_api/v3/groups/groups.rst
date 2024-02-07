======
Groups
======

Groups represent a collection of related behavior and intelligence.

Endpoint: ``/api/v3/groups``

.. note::
    When working with Groups using the ThreatConnect v3 API, you can target a specific Group by its ID or, if one has been assigned to it, XID. While you can use the API to retrieve a Group's ID, you can also find it in the URL of each Group. If you navigate to the new **Details** screen, the URL should look like ``https://app.threatconnect.com/#/details/groups/123456/overview``. The number between ``groups/`` and ``/overview`` is the Group's ID. Similarly, if you navigate to the legacy **Details** screen for a Group, the URL should look like ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456``. The number following ``<GROUP-TYPE>=`` is the Group's ID.

    If targeting a Group by its XID, you must use the ``owner`` query parameter to `specify the owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ in which the Group exists.

.. include:: fields.rst

.. include:: create.rst

.. include:: retrieve.rst

.. include:: update.rst

.. include:: delete.rst

.. include:: retrieve_upload_update_document.rst

.. include:: retrieve_pdf_report.rst

.. include:: associations.rst

----

*MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation.*