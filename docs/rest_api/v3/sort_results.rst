Sort Results
------------

When retrieving objects, you can sort results by including the ``?sorting=`` query parameter in your query. Sorting is specified by word pairs consisting of any valid TQL keywords followed by ``ASC``, ``DESC``, ``NULLSFIRST``, or ``NULLSLAST``.

For example, the following query will return all Indicators and sort them by owner name in alphabetical order.

.. code::

    GET /v3/indicators?sorting=ownerName%20ASC

You can specify additional sorting levels by appending additional sorting keywords with whitespace between each keyword. For example, the following query will return all Indicators and first sort them by owner name in reverse alphabetical order, and then sort them by Confidence Rating from highest to lowest.

.. code::

    GET /v3/indicators?sorting=ownerName%20DESC%20confidence%20DESC