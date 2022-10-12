======
Groups
======

Groups represent a collection of related behavior and intelligence.

Endpoint: ``/api/v3/groups``

.. note::
    When working with Groups using the ThreatConnect REST API, you may need to specify the ID of the Group with which you would like to work. While you can use the API to retrieve a Group's ID, you can also find it in the URL of each Group.

    When you navigate to a Group's **Details** screen, the URL should look like: ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456`` or ``https://app.threatconnect.com/auth/<GROUP-TYPE>/<GROUP-TYPE>.xhtml?<GROUP-TYPE>=123456&owner=Demo%20Organization``. The number after the ``<GROUP-TYPE>=`` key (``123456`` in this example) is the Group's ID.

.. include:: fields.rst

.. include:: create.rst

.. include:: retrieve.rst

.. include:: update.rst

.. include:: delete.rst

.. include:: retrieve_upload_update_document.rst

.. include:: retrieve_pdf_report.rst