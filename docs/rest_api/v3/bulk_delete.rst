Delete Case Objects in Bulk
---------------------------

To delete Case objects, including Artifacts, Cases, Notes, Tasks, and Workflow Templates, in bulk, use the following query:

.. code::

    DELETE /v3/{caseObject}/

.. note:: The system setting **v3ApiBulkDeleteAllowed** must be enabled to perform bulk deletions. Refer to the *ThreatConnect System Administration Guide* for instructions on enabling this setting.

To filter the Case objects to be deleted in bulk, include ``?tql=`` in the query parameter followed by a query written in `ThreatConnect Query Language (TQL) <https://training.threatconnect.com/learn/article/using-threatconnect-query-language-tql-kb-article>`__.

For example, the following query will delete all Notes created between April 1 and 30, 2021:

.. code::

    DELETE /v3/notes/?tql=dateAdded >= "2021-04-01" and dateAdded < "2021-04-30"

To view a list of available options to set in the ``?tql=`` query parameter for each Case object, use the following query:

.. code::

    OPTIONS /v3/{caseObject}/tql