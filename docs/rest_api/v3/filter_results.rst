Filter Results with TQL
-----------------------

When retrieving Case objects, including Artifacts, Artifact types, Cases, Notes, Tasks, Workflow Events, and Workflow Templates, results can be filtered by including ``?tql=`` in the query parameter followed by a query written in `ThreatConnect Query Language (TQL) <https://training.threatconnect.com/learn/article/using-threatconnect-query-language-tql-kb-article>`__.

For example, the following query will return all Cases created between April 1 and 30, 2021:

.. code::

    GET /v3/cases/?tql=dateAdded >= "2021-04-01" and dateAdded < "2021-04-30"

To view a list of available options to set in the ``?tql=`` query parameter for each Case object, use the following query:

.. code::

    OPTIONS /v3/{caseObject}/tql