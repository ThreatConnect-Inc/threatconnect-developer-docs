Delete Case Objects in Bulk
---------------------------

Case objects (Artifacts, Case Attributes, Cases, Notes, Workflow Tasks, and Workflow Events) can be deleted in bulk by using a query in the following format:

.. code::

    DELETE /v3/{caseObject}/

.. note::
    A System Administrator must enable bulk deletion operations for v3 of the ThreatConnect API.

Objects to be deleted in bulk can be filtered by including the ``?tql=`` query parameter, followed by a query written in `ThreatConnect Query Language (TQL) <https://training.threatconnect.com/learn/article/using-threatconnect-query-language-tql-kb-article>`__, in your query.

For example, the following query will delete all Notes created between November 1 and 14, 2021, inclusive:

.. code::

    DELETE /v3/notes/?tql=dateAdded GEQ "2021-11-01" and dateAdded LEQ "2021-11-14"

.. note::
    Depending on the tool you're using to interact with the ThreatConnect API, it may be necessary to manually encode the URL in your request when including query parameters. For example, some tools may accept ``?tql=dateAdded GEQ "2021-11-01" and dateAdded LEQ "2021-11-14"`` as a valid URL and automatically encode it, while others may require you to manually encode the URL (e.g., ``?tql=dateAdded%20GEQ%20%222021-11-01%22%20and%20dateAdded%20LEQ%20%222021-11-14%22``). If you submit a request with query parameters and a ``401 Unauthorized`` error is returned, verify whether the URL in your request is encoded properly for your preferred API tool.