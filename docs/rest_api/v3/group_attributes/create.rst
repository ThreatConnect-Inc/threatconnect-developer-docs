Create Group Attributes
-----------------------

The basic format for creating a Group Attribute is:

.. code::

    POST /v3/groupAttributes/
    {
        "groupId": 12345,
        "type": "Attribute type goes here",
        "value": "Attribute value goes here"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a POST request for the ``groupAttributes`` object.

For example, the following query will create an Attribute and add it to the Group with ID 20:

.. code::

    POST /v3/groupAttributes/
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
        "message": "Created",
        "status": "Success"
    }

.. note::
    Group Attributes can also be created when creating a Group. See the “Create Groups” section of `Groups <https://docs.threatconnect.com/en/latest/rest_api/v3/groups/groups.html>`_ for more information.