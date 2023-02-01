======
Groups
======

Groups represent a collection of related behavior and intelligence.

Endpoint: ``/api/v3/groups``

.. note::
    When working with Groups using the ThreatConnect REST API, you may need to specify the ID of the Group with which you would like to work. While you can use the API to retrieve a Group's ID, you can also find it in the URL of each Group.

    If you navigate to the new **Details** screen, the URL should look like ``https://app.threatconnect.com/#/details/groups/123456/overview``. The number between ``groups/`` and ``/overview`` is the Group's ID. Similarly, if you navigate to the legacy **Details** screen for a Group, the URL should look like ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456``. The number following ``<GROUP-TYPE>=`` is the Group's ID.

.. include:: fields.rst

.. include:: create.rst

.. include:: retrieve.rst

.. include:: update.rst

.. include:: delete.rst

.. include:: retrieve_upload_update_document.rst

.. include:: retrieve_pdf_report.rst