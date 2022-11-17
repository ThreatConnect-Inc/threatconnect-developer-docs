Retrieve Indicators
-------------------

Retrieve All Indicators
^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Indicators, use the following query:

.. code::

    GET /v3/indicators

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "ownerName": "Demo Organization",
                "dateAdded": "2021-11-02T13:07:08Z",
                "webLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=F5A2496CF66CB8CFFE66CB1B27D7DEDE",
                "type": "File",
                "lastModified": "2021-11-02T14:04:55Z",
                "summary": "F5A2496CF66CB8CFFE66CB1B27D7DEDE",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "md5": "F5A2496CF66CB8CFFE66CB1B27D7DEDE"
            }, 
            {
                "id": 9,
                "ownerName": "Demo Organization",
                "dateAdded": "2021-11-02T12:34:03Z",
                "webLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=badguy%40bad.com",
                "type": "EmailAddress",
                "lastModified": "2021-11-02T12:48:51Z",
                "description": "A bad email address",
                "summary": "badguy@bad.com",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "address": "badguy@bad.com"
            },
            {...}
        ], 
        "status": "Success"
    }


Retrieve a Single Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can retrieve a specific Indicator using its ID or summary. If using an Indicator's summary, the API request will search for the Indicator in the Organization to which your API user account belongs. To search for an Indicator by summary in a Community or Source to which your API user account has access, include the ``?owner=`` query parameter, followed by the owner's name, in your request. For more information about the ``?owner=`` query parameter, see `Specify an Owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_.

The basic format for retrieving an Indicator is:

.. code::

    GET /v3/indicators/{indicatorId or indicatorSummary}

For example, the following query will return information about the Indicator with ID 3:

.. code::

    GET /v3/indicators/3

JSON Response

.. code:: json

    {
        "data": {
            "id": 3,
            "ownerName": "Demo Organization",
            "dateAdded": "2021-10-26T12:40:00Z",
            "webLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=badguy.com",
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
            "whoisActive": false
        },
        "status": "Success"
    }

The same response would be returned if we used the following request, where the Indicator's ID is replaced with its summary:

.. code::

    GET /v3/indicators/badguy.com

Retrieve Deleted Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve Indicators that have been recently deleted from an owner, use the following query:

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

By default, this query will return all Indicators recently deleted in the Organization to which your API user account belongs. However, you can `specify a different owner <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ by including the ``?owner=`` query parameter in your query.

.. note::
    The number of days to retain deleted Indicators is configured by your System Administrator.

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
