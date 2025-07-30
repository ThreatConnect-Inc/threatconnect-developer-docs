======
Groups
======

Groups represent a collection of related behavior and intelligence.

Endpoint: ``/api/v3/groups``

.. note::
    When targeting a specific Group in an API request, you can use the Group's ID or, if one has been assigned, XID. In addition to the API, you can obtain a Group's ID from the Group's URL. On the **Details** screen, the URL looks like ``https://app.threatconnect.com/#/details/groups/123456/overview``. The number between ``groups/`` and ``/overview`` is the Group's ID. On the legacy **Details** screen, the URL looks like ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456``. The number following ``<GROUP-TYPE>=`` is the Group's ID.

    If you want to target a Group by its XID, you must use the ``owner`` query parameter to `specify the owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ in which the Group exists.

.. include:: fields.rst

.. include:: create.rst

.. include:: retrieve.rst

.. include:: update.rst

.. include:: delete.rst

.. include:: retrieve_upload_update_document.rst

.. include:: retrieve_pdf_report.rst

.. include:: associations.rst

.. include:: intelligence_reviews.rst

.. include:: event_status.rst

.. include:: unified_view_vulnerabilities.rst

----

*MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation.*