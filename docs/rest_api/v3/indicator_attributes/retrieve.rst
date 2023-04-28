Retrieve Indicator Attributes
-----------------------------

The following section describes how to retrieve Indicator Attributes via the ``/v3/indicatorAttributes`` endpoint. In addition to the methods described in this section, you can send the following request to retrieve Attributes added to a specific Indicator: ``GET /v3/indicators/{indicatorId or indicatorSummary}?fields=attributes``.

Retrieve All Indicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Indicator Attributes:

.. code::

    GET /v3/indicatorAttributes

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "dateAdded": "2021-11-09T13:32:37Z",
                "type": "Additional Analysis and Context",
                "value": "Host used by hacker conglomerate traced to Iran.",
                "source": "Phase of Intrusion",
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "owner": "Demo Organization"
                },
                "lastModified": "2021-11-09T13:32:37Z",
                "pinned": false,
                "default": false
            }, 
            {
                "id": 9,
                "dateAdded": "2021-11-09T06:03:54Z",
                "type": "First Seen",
                "value": "2021-11-07T04:00:35Z",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "owner": "Demo Organization"
                }, 
                "lastModified": "2021-11-09T06:03:54Z",
                "pinned": false,
                "default": false
            }, 
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Indicator Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Indicator Attribute:

.. code::

    GET /v3/indicatorAttributes/{indicatorAttributeId}

For example, the following request will retrieve data for the Indicator Attribute whose ID is 9:

.. code::

    GET /v3/indicatorAttributes/9

JSON Response

.. code:: json

    {
        "data": {
            "id": 9,
            "dateAdded": "2021-11-09T06:03:54Z",
            "type": "First Seen",
            "value": "2021-11-07T04:00:35Z",
            "createdBy": {
                "id": 1,
                "userName": "smithj@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmith",
                "owner": "Demo Organization"
            }, 
            "lastModified": "2021-11-09T06:03:54Z",
            "pinned": true,
            "default": false
        },
        "status": "Success"
    }