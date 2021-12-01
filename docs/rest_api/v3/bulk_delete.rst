Delete Case Objects in Bulk
---------------------------

Case objects (Artifacts, Cases, Notes, Tasks, Workflow Events, Workflow Tasks, and Case Attributes) can be deleted in bulk by using a query in the following format:

.. code::

    DELETE /v3/{caseObject}/

.. note::
    The **v3ApiBulkDeleteAllowed** system setting must be enabled to perform bulk deletions. Refer to *ThreatConnect System Administration Guide* for instructions on enabling this setting.

Objects to be deleted in bulk can be filtered by including the ``?tql=`` query parameter, followed by a query written in `ThreatConnect Query Language (TQL) <https://training.threatconnect.com/learn/article/using-threatconnect-query-language-tql-kb-article>`__, in your query.

For example, the following query will delete all Notes created between November 1 and 14, 2021, inclusive:

.. code::

    DELETE /v3/notes/?tql=dateAdded GEQ "2021-11-01" and dateAdded LEQ "2021-11-14"