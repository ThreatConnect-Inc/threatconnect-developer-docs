Retrieve Group Attributes
-------------------------

The following section describes how to retrieve Group Attributes via the ``/v3/groupAttributes`` endpoint. In addition to the methods described in this section, you can send the following request to retrieve Attributes added to a specific Group: ``GET /v3/groups/{groupId}?fields=attributes``.

Retrieve All Group Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send the following request to retrieve data for all Group Attributes:

.. code::

    GET /v3/groupAttributes

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "dateAdded": "2021-11-09T14:42:13Z",
                "type": "Additional Analysis and Context",
                "value": "This is a very dangerous adversary.",
                "source": "Phase of Intrusion",
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555"
                },
                "lastModified": "2021-11-09T14:42:13Z",
                "pinned": false,
                "default": false
            }, 
            {
                "id": 9,
                "dateAdded": "2021-11-08T15:56:46Z",
                "type": "Source",
                "value": "https://examplesite.com",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com"
                },
                "lastModified": "2021-11-08T15:56:46Z",
                "pinned": true,
                "default": true
            }, 
            {
                "id": 8,
                "dateAdded": "2021-11-08T15:56:46Z",
                "type": "Description",
                "value": "This malware is written in a new programming language and has the potential of targeting millions of routers and IOT devices.",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com"
                },
                "lastModified": "2021-11-08T15:56:46Z",
                "pinned": false,
                "default": true
            }, 
            {...}
        ],
        "status": "Success"
    }

Retrieve a Specific Group Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to retrieve data for a specific Group Attribute:

.. code::

    GET /v3/groupAttributes/{groupAttributeId}

For example, the following request will retrieve data for the Group Attribute whose ID is 7:

.. code::

    GET /v3/groupAttributes/7

JSON Response

.. code:: json

    {
        "data": {
            "id": 7,
            "dateAdded": "2021-11-08T15:56:46Z",
            "type": "Description",
            "value": "This Incident is related to a recent ransomware attack.",
            "createdBy": {
                "id": 1,
                "userName": "smithj@threatconnect.com"
            },
            "lastModified": "2021-11-08T15:56:46Z",
            "pinned": false,
            "default": true
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not included in the default response, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter results using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
