Return a Count of Items
-----------------------

By default, an API response does **not include** a count of items that are included in the response. To include a count of items that are included in an API response, append ``?count=true`` to your request.

For example, the following request will retrieve data for all Indicators. The response will include the ``count`` field, which will provide the total number of Indicators for which data were retrieved:

.. code::

    GET /v3/indicators?count=true

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "dateAdded": "2021-11-02T13:07:08Z",
                "webLink": "https://app.threatconnect.com/#/details/indicators/10/overview",
                "type": "File",
                "lastModified": "2021-11-02T14:04:55Z",
                "summary": "F5A2496CF66CB8CFFE66CB1B27D7DEDE",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "md5": "F5A2496CF66CB8CFFE66CB1B27D7DEDE",
                "legacyLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=F5A2496CF66CB8CFFE66CB1B27D7DEDE&owner=Demo+Organization"
            },
            {
                "id": 9,
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "dateAdded": "2021-11-02T12:34:03Z",
                "webLink": "https://app.threatconnect.com/#/details/indicators/9/overview",
                "type": "EmailAddress",
                "lastModified": "2021-11-02T12:48:51Z",
                "description": "A bad email address",
                "summary": "badguy@bad.com",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "address": "badguy@bad.com",
                "legacyLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=badguy%40bad.com&owner=Demo+Organization"
            },
            {...}
        ],
        "count": 10,
        "status": "Success"
    }

.. attention::
    If the ``count`` query parameter is set to ``false`` or not appended to the API request, or if the ``resultStart`` query parameter is set to a value greater than 0, then the API response will not include a count of items that are included in the response.