Retrieve Group Attributes
-------------------------

The following section describes how to retrieve Group Attributes via the ``/v3/groupAttributes`` endpoint. In addition to the methods described in this section, you can retrieve Attributes added to a specific Group by using the following query:

.. code::

    GET /v3/groups/{groupId}?fields=attributes

Retrieve All Group Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve all Group Attributes, use the following query:

.. code::

    GET /v3/groupAttributes

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 10,
                "type": "Additional Analysis and Context",
                "value": "This is a very dangerous adversary.",
                "source": "Phase of Intrusion",
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "role": "Api User"
                },
                "dateAdded": "2021-11-09T14:42:13Z",
                "lastModified": "2021-11-09T14:42:13Z",
                "default": false
            }, 
            {
                "id": 9,
                "type": "Source",
                "value": "https://examplesite.com",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "role": "Administrator"
                },
                "dateAdded": "2021-11-08T15:56:46Z",
                "lastModified": "2021-11-08T15:56:46Z",
                "default": true
            }, 
            {
                "id": 8,
                "type": "Description",
                "value": "This malware is written in a new programming language and has the potential of targeting millions of routers and IOT devices.",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "role": "Administrator"
                },
                "dateAdded": "2021-11-08T15:56:46Z",
                "lastModified": "2021-11-08T15:56:46Z",
                "default": true
            }, 
            {...}
        ],
        "status": "Success"
    }

Retrieve a Single Group Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To retrieve a specific Group Attribute, use a query in the following format:

.. code::

    GET /v3/groupAttributes/{groupAttributeId}

For example, the following query will return information about the Group Attribute with ID 7:

.. code::

    GET /v3/groupAttributes/7

JSON Response

.. code:: json

    {
        "data": {
            "id": 7,
            "type": "Description",
            "value": "This Incident is related to a recent ransomware attack.",
            "createdBy": {
                "id": 1,
                "userName": "smithj@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmith",
                "role": "Administrator"
            },
            "dateAdded": "2021-11-08T15:56:46Z",
            "lastModified": "2021-11-08T15:56:46Z",
            "default": true
        },
        "status": "Success"
    }

Request Additional Fields
^^^^^^^^^^^^^^^^^^^^^^^^^

To request additional fields not automatically included with each returned object, refer to `Include Additional Fields for Returned Objects <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_.

Filter Results
^^^^^^^^^^^^^^

To filter returned objects using ThreatConnect Query Language (TQL), refer to `Filter Results with TQL <https://docs.threatconnect.com/en/latest/rest_api/v3/filter_results.html>`_.
