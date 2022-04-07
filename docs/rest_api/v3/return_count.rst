Return a Count of Items
-----------------------

By default, a count of items returned in a result set is **not included**. To include a count of items returned in a result set, include the ``?count=true`` query parameter in your query.

For example, the following query will return all Indicators, and a count of how many Indicators were returned will be included:

.. code::

    GET /v3/indicators?count=true

JSON Response

.. code:: json

    {
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
            },
            {...}
        ],
        "count": 20,
        "status": "Success"
    }

.. note::
    If the ``?count=`` query parameter is set to ``false``, or if the ``resultStart`` query parameter is set to a value greater than 0, a count of items returned in a result set will not be included.