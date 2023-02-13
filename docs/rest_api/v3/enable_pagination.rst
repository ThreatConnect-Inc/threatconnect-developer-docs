Enable Pagination
-----------------

Overview
^^^^^^^^

Pagination works by specifying a starting index and a limit of items to be returned as HTTP query parameters in the request. For example, requesting data for all Indicators with a starting index of 50 and a limit of 100 will retrieve data for Indicators 50 to 150 in the result set.

In the ThreatConnect v3 API, use the ``resultStart`` and ``resultLimit`` query parameters to paginate an API response. Refer to the following table for more information about the resultStart and resultLimit query parameters.

.. list-table::
   :widths: 30 40 30
   :header-rows: 1

   * - Query Parameter
     - Description
     - Default Value
   * - resultStart
     - The starting index of the result set within the API response
     - 0
   * - resultLimit [1]_
     - The maximum number of items included in the result set within the API response
     - 100

.. [1] The maximum value that can be specified for the ``resultLimit`` query parameter is ``10000``.

.. note::
    If you do not include the ``resultStart`` and ``resultLimit`` query parameters in your request, the default values will be used automatically.

.. warning::
    Pagination counts and indices should not be stored in long-lived applications as a way to return to a result set. The dataset will change with time, so those range markers might cause objects to be skipped or duplicated if reused at a later time.

Example Request
^^^^^^^^^^^^^^^

Send a request in the following format to paginate the response returned from the API when retrieving data for an object:

.. code::

    GET /v3/{objectType}?resultStart={#}&resultLimit={#}

For example, the following request will retrieve data for all Indicators. However, the API response will start with the fifth item in the result set (i.e., the starting index will be 5) and it will display ten Indicators at a time:

.. code::

    GET /v3/indicators?resultStart=5&resultLimit=10

JSON Response

.. code:: json

    {
        "next": "https://app.threatconnect.com/api/v3/indicators?resultStart=15&resultLimit=10",
        "data": [
            {
                "id": 19,
                "dateAdded": "2023-01-26T20:07:35Z",
                "ownerId": 2,
                "ownerName": "Demo Source",
                "webLink": "https://app.threatconnect.com/#/details/indicators/19/overview",
                "type": "EmailAddress",
                "lastModified": "2023-01-27T18:20:51Z",
                "summary": "verybadguy@bad.com",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "address": "verybadguy@bad.com",
                "legacyLink": "https://app.threatconnect.com/auth/indicators/details/emailaddress.xhtml?emailaddress=verybadguy%40bad.com&owner=Demo+Source"
            },
            {
                "id": 27,
                "dateAdded": "2023-01-27T16:18:18Z",
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "webLink": "https://app.threatconnect.com/#/details/indicators/27/overview",
                "type": "File",
                "lastModified": "2023-01-27T16:19:33Z",
                "summary": "9D67E81C18101FC266057CD7851604B8",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "md5": "9D67E81C18101FC266057CD7851604B8",
                "legacyLink": "https://app.threatconnect.com/auth/indicators/details/file.xhtml?file=9D67E81C18101FC266057CD7851604B8&owner=Demo+Organization"
            },
            {...}
        ],
        "prev": "https://app.threatconnect.com/api/v3/indicators?resultStart=0&resultLimit=10",
        "status": "Success"
    }

.. note::
    If the number of items in a result set exceeds the value specified for the ``resultLimit`` query parameter, a link to the next set of items will be included at the top of the API response. Similarly, if the starting index for the current result set is not 0, a link to the previous result set will be included at the bottom of the API response.