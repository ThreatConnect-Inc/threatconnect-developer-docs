Retrieve Indicator Attributes
-----------------------------

The following section describes how to retrieve Indicator Attributes via the ``/v3/indicatorAttributes`` endpoint. In addition to the methods described in this section, you can send the following request to retrieve Attributes added to a specific Indicator: ``GET /v3/indicators/{indicatorid or indicatorSummary}?fields=attributes``.

.. code::

    GET /v3/indicators/{indicatorId}?fields=attributes

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
                    "userName": "11112222333344445555"
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
                        "id": 2,
                        "userName": "pjones+analyst@threatconnect.com"
                    }, 
                "lastModified": "2021-11-09T06:03:54Z",
                "pinned": false,
                "default": false
            }, 
            {
                "id": 8,
                "dateAdded": "2021-11-09T06:03:54Z",
                "type": "Description",
                "value": "At the time of Analysis, the host of this URL resolved to Address 199.34.228.53",
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
                "id": 2,
                "userName": "pjones+analyst@threatconnect.com"
            }, 
            "lastModified": "2021-11-09T06:03:54Z",
            "pinned": true,
            "default": false
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not included in the default response, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter results using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
