Retrieve Indicators
-------------------

Retrieve All Indicators
^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Indicators:

.. code::

    GET /v3/indicators

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
        "status": "Success"
    }

.. hint::
    To limit the results to a specific owner, append the ``?owner=`` query parameter to your request. For more information about the ``?owner=`` query parameter, see `Specify an Owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_.

Retrieve a Specific Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Indicator:

.. code::

    GET /v3/indicators/{indicatorId or indicatorSummary}

For example, the following request will return data for the Indicator whose ID is 3:

.. code::

    GET /v3/indicators/3

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-10-26T12:40:00Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/3/overview",
            "type": "Host",
            "lastModified": "2021-11-02T14:58:55Z",
            "rating": 3.00,
            "confidence": 74,
            "description": "A bad host.",
            "summary": "badguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "hostName": "badguy.com",
            "dnsActive": true,
            "whoisActive": false,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=badguy.com&owner=Demo+Organization"
        },
        "status": "Success"
    }

The same response will be returned for the following request was used, where the Indicator's ID is replaced with its summary:

.. code::

    GET /v3/indicators/badguy.com

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-10-26T12:40:00Z",
            "webLink": "https://app.threatconnect.com/#/details/indicators/3/overview",
            "type": "Host",
            "lastModified": "2021-11-02T14:58:55Z",
            "rating": 3.00,
            "confidence": 74,
            "description": "A bad host.",
            "summary": "badguy.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "hostName": "badguy.com",
            "dnsActive": true,
            "whoisActive": false,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=badguy.com&owner=Demo+Organization"
        },
        "status": "Success"
    }

Retrieve Deleted Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Indicators that have been deleted from your Organization recently:

.. code::

    GET /v3/indicators/deleted

JSON Response

.. code:: json

    {
        "data": [
            {
                "ownerName": "Demo Organization",
                "dateAdded": "2021-11-02T15:17:28Z",
                "type": "URL",
                "summary": "http://badsite.com"
            }
        ],
        "count": 1,
        "status": "Success"
    }

You can `specify a different owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ by appending the ``?owner=`` query parameter to your request. You can also use the ``?type=`` and ``?deletedSince=`` query parameters to limit the results by Indicator type and deletion date, respectively.

.. note::
    The number of days for which deleted Indicators are retained is configured by your System Administrator.

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not included in the default response, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter results using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
