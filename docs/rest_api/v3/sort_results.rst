Sort Results
------------

When retrieving objects, you can sort results by including the ``?sorting=`` query parameter in your query. Sorting is specified by word pairs consisting of any valid TQL keywords followed by ``ASC``, ``DESC``, ``NULLSFIRST``, or ``NULLSLAST``.

For example, the following query will return all Indicators and sort them by owner name in alphabetical order.

.. code::

    GET /v3/indicators?sorting=ownerName ASC

You can specify additional sorting levels by appending additional sorting keywords with whitespace between each keyword. For example, the following query will return all Indicators and first sort them by owner name in reverse alphabetical order, and then sort them by Confidence Rating from highest to lowest.

.. code::

    GET /v3/indicators?sorting=ownerName DESC confidence DESC

.. note::
    Depending on the tool you're using to interact with the ThreatConnect API, it may be necessary to encode the URL in your request when including query parameters. For example, some tools may accept ``?sorting=ownerName ASC`` as a valid URL, while others require the URL be encoded (e.g., ``?sorting=ownerName%20ASC``). If you submit a request with query parameters and a ``401 Unauthorized`` error is returned, verify whether the URL in your request is encoded properly for your preferred API tool.