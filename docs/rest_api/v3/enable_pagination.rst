Enable Pagination
-----------------

To enable pagination in an API call, use a query in the following format:

.. code::

    GET /v3/{insert query here}?resultStart=0&resultLimit=50

For example, the query below will return 2 Indicators:

.. code::

    GET /v3/indicators?resultStart=0&resultLimit=2

JSON Response

.. code:: json

    {
        "next": "https://app.threatconnect.com/api/v3/indicators?resultStart=2&resultLimit=2",
        "data": [
            {
                "id": 18,
                "ownerName": "Demo Organization",
                "dateAdded": "2021-10-26T16:26:19Z",
                "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=verybadguy%40bad.com",
                "type": "EmailAddress",
                "lastModified": "2021-11-08T18:25:48Z",
                "summary": "verybadguy@bad.com",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "address": "verybadguy@bad.com"
            },
            {
                "id": 15,
                "ownerName": "Demo Organization",
                "dateAdded": "2021-10-26T13:08:37Z",
                "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=ultrabadguy%40bad.com",
                "type": "EmailAddress",
                "lastModified": "2021-11-02T15:00:32Z",
                "summary": "ultrabadguy@bad.com",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "address": "ultrabadguy@bad.com"
            }
        ],
        "status": "Success"
    }

.. note:: If the number of items in a result set exceeds the ``resultLimit``, a link to the next set of items will be included at the top of the result set.


Pagination works by specifying a starting result index, as well as a result limit of items to be returned as HTTP query parameters to the request. For example, requesting a result start index of 50 and a result limit of 100 will retrieve items 50 to 150. Refer to the following table for more information about the ``resultStart`` and ``resultLimit`` query parameters.

+------------------+---------------------------------------------------------------+----------+
| Query Parameter  | Description                                                   | Default  |
+==================+===============================================================+==========+
| resultStart      | The starting index of the result set that is returned         | 0        |
+------------------+---------------------------------------------------------------+----------+
| resultLimit      | The limit to the number of results returned with the request  | 100      |
+------------------+---------------------------------------------------------------+----------+

.. warning:: Specifying a ``resultStart`` other than 0 will omit the ``count`` field in the return data for performance reasons.

.. note:: The maximum value that can be specified for ``resultLimit`` is ``10000``.

A request that does not include the parameters indicated is assumed to use the default values above. A request having a ``resultStart`` value of 0 will return the current count of all items being queried. This count should be saved to iterate over the collection and to know when all items have been retrieved.

.. note:: Pagination counts and indices should not be stored in long-lived applications as a way to return to a result set. The dataset will change with time, so those range markers might cause objects to be skipped or duplicated if reused at a later time.