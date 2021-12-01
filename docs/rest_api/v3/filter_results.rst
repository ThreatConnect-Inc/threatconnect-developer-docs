Filter Results with TQL
-----------------------

When retrieving objects, results can be filtered by including the ``?tql=`` query parameter, followed by a query written in `ThreatConnect Query Language (TQL) <https://training.threatconnect.com/learn/article/using-threatconnect-query-language-tql-kb-article>`__, in your query.

For example, the following query will return a list of Indicators that belong to the ``Demo Community`` owner.

.. code::

    GET /v3/indicators?tql=ownerName EQ "Demo Community"

To view a list of available options to set in the ``?tql=`` query parameter for each object, use the following query:

.. code::

    OPTIONS /v3/{objectName}/tql

.. note::
    The ``?tql=`` and ``?fields=`` query parameters can be combined in a single request. For example, the following query will return all Indicators, along with their respective Tags and Attributes, that belong to the ``Demo Community`` owner:

    ``GET /v3/indicators?tql=ownerName EQ "Demo Community"&fields=tags&fields=attributes``