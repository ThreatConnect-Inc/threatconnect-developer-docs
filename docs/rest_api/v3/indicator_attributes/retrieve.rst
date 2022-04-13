Retrieve Indicator Attributes
-----------------------------

The following section describes how to retrieve Indicator Attributes via the ``/v3/indicatorAttributes`` endpoint. In addition to the methods described in this section, you can retrieve Attributes added to a specific Indicator by using the following query:

.. code::

    GET /v3/indicators/{indicatorId}?fields=attributes

Retrieve All Indicator Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Indicator Attributes, use the following query:

.. code::

    GET /v3/indicatorAttributes

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "type": "Additional Analysis and Context",
                "value": "Host used by hacker conglomerate traced to Iran.",
                "source": "Phase of Intrusion",
                "createdBy": {
                    "id": 39,
                    "userName": "62693284927610908885",
                    "firstName": "API",
                    "lastName": "User",
                    "pseudonym": "APIUserNFmof",
                    "role": "Api User"
                },
                "dateAdded": "2021-11-09T13:32:37Z",
                "lastModified": "2021-11-09T13:32:37Z",
                "default": false
            }, 
            {
                "id": 9,
                "type": "First Seen",
                "value": "2021-11-07T04:00:35Z",
                "createdBy": {
                    "id": 2,
                    "userName": "pjones+analyst@threatconnect.com",
                    "firstName": "Pat",
                    "lastName": "Jones",
                    "pseudonym": "patjones",
                    "role": "User"
                }, 
                "dateAdded": "2021-11-09T06:03:54Z",
                "lastModified": "2021-11-09T06:03:54Z",
                "default": false
            }, 
            {
                "id": 8,
                "type": "Description",
                "value": "At the time of Analysis, the host of this URL resolved to Address 199.34.228.53",
                "dateAdded": "2021-11-09T06:03:54Z",
                "lastModified": "2021-11-09T06:03:54Z",
                "default": false
            },
            {...}
        ],
        "status": "Success"
    }

Retrieve a Single Indicator Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Indicator Attribute, use a query in the following format:

.. code::

    GET /v3/indicatorAttributes/{indicatorAttributeId}

For example, the following query will return information about the Indicator Attribute with ID 9:

.. code::

    GET /v3/indicatorAttributes/9

JSON Response

.. code:: json

    {
        "data": {
          "id": 9,
          "type": "First Seen",
          "value": "2021-11-07T04:00:35Z",
        	"createdBy": {
              "id": 2,
              "userName": "pjones+analyst@threatconnect.com",
              "firstName": "Pat",
              "lastName": "Jones",
              "pseudonym": "patjones",
              "role": "User"
          }, 
          "dateAdded": "2021-11-09T06:03:54Z",
          "lastModified": "2021-11-09T06:03:54Z",
          "default": false
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
