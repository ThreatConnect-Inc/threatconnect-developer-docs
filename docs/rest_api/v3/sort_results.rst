Sort Results
------------

Overview
^^^^^^^^

When retrieving data, you can use the ``sorting`` query parameter to sort results based on a valid `TQL parameter <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_ for the endpoint, followed by one of the following sorting keywords:

- ``asc``: Sorts results in ascending order.
- ``desc``: Sorts results in descending order.
- ``nullsfirst``: Places the nulls before the non-null elements in the sort order.
- ``nullslast``: Places the non-null elements before the non-null elements in the sort order.

Example Requests
^^^^^^^^^^^^^^^^

This section provides example requests demonstrating sample use cases for the ``sorting`` query parameter.

.. note::
    Depending on the tool you are using to interact with the ThreatConnect API, it may be necessary to encode the request URL manually if it includes query parameters. For example, some tools may accept ``/v3/indicators?sorting=ownerName asc`` as a valid request URL and encode it automatically, while others may require you to encode the request URL manually. If you send a request with query parameters and a **401 Unauthorized** error is returned, verify whether the request URL is encoded properly for the API tool you are using.

Sort Results by Owner Name
==========================

The following request will retrieve data for all Indicators and sort the results by owner name in ascending order:

Request (Decoded URL)

.. code::

    GET /v3/indicators?sorting=ownerName asc

Request (Encoded URL)

.. code::

    GET /v3/indicators?sorting=ownerName%20asc

Place Null Values at the End of the Sort Order
==============================================

The following request will retrieve data for all Indicators and sort the results by Threat Rating, where Indicators without a Threat Rating will be placed at the end of the sorted results:

Request (Decoded URL)

.. code::

    GET /v3/indicators?sorting=rating nullslast

Request (Encoded URL)

.. code::

    GET /v3/indicators?sorting=rating%20nullslast

Perform Multi-Level Sorting
===========================

When using the ``sorting`` query parameter, you can perform multi-level sorting by appending additional TQL parameters and sorting keywords to the end of the request URL. When performing multi-level sorting, each TQL parameter and sorting keyword must be separated with whitespace.

For example, the following request will retrieve data for all Indicators. First, the results will be sorted by owner name in ascending order and then by Confidence Rating in descending order.

Request (Decoded URL)

.. code::

    GET /v3/indicators?sorting=ownerName asc confidence desc

Request (Encoded URL)

.. code::

    GET /v3/indicators?sorting=ownerName%20asc%20confidence%20desc