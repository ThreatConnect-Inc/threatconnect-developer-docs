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
                "dateAdded": "2023-03-29T14:42:13Z",
                "type": "Aliases",
                "value": "APT28, Fancy Bear, Threat Group-4127, TG-4127",
                "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "owner": "Demo Organization"
                },
                "lastModified": "2023-03-29T14:42:13Z",
                "settings": {
                    "associable": true,
                    "pinnedByDefault": true,
                    "message": "Enter the Group's aliases."
                },
                "pinned": true,
                "default": true
            }, 
            {
                "id": 9,
                "dateAdded": "2023-03-28T15:56:46Z",
                "type": "Source",
                "value": "https://examplesite.com",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "owner": "Demo Organization"
                },
                "lastModified": "2023-03-28T15:56:46Z",
                "pinned": true,
                "default": true
            }, 
            {
                "id": 8,
                "dateAdded": "2023-03-08T15:55:59Z",
                "type": "Description",
                "value": "This malware is written in a new programming language and has the potential of targeting millions of routers and IOT devices.",
                "source": "Internal analysis",
                "createdBy": {
                    "id": 1,
                    "userName": "smithj@threatconnect.com",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmith",
                    "owner": "Demo Organization"
                },
                "lastModified": "2023-03-08T15:55:59Z",
                "pinned": false,
                "default": true
            }, 
            {...}
        ],
        "status": "Success"
    }

.. note::
    If an Attribute Type is configured as a default, pinned, or association Attribute Type, then the ``settings`` field will be included in the response for Attributes of that Attribute Type.

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
            "dateAdded": "2023-03-08T15:55:59Z",
            "type": "Description",
            "value": "This Incident is related to a recent ransomware attack.",
            "createdBy": {
                "id": 1,
                "userName": "smithj@threatconnect.com",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmith",
                "owner": "Demo Organization"
            },
            "lastModified": "2023-03-08T15:55:59Z",
            "pinned": false,
            "default": true
        },
        "status": "Success"
    }