Create Group Attributes
-----------------------

The following example illustrates the basic format for creating a Group Attribute:

.. code::

    POST /v3/groupAttributes
    {
        "groupId": 12345,
        "type": "Attribute type goes here",
        "value": "Attribute value goes here"
    }

For example, the following request will create an Attribute and add it to the Group whose ID is 20:

.. code::

    POST /v3/groupAttributes
    {
        "groupId": 20,
        "source": "Phase of Intrusion",
        "type": "Additional Analysis and Context",
        "value": "This is a very dangerous adversary."
    }

JSON Response

.. code:: json

    {
        "data": {
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
        "message": "Created",
        "status": "Success"
    }


Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request for the ``groupAttributes`` object.

.. hint::
    Group Attributes can also be created and added to a Group when creating the Group. See the “Create Groups” section of `Groups <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_ for more information.