Update Group Attributes
-----------------------

The basic format for updating a Group Attribute is:

.. code::

    PUT /v3/groupAttributes/{groupAttributeId}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request for the ``groupAttributes`` object.

For example, the following query will update the value of the Group Attribute with ID 10 and make it the default Attribute of its type:

.. code::

    PUT /v3/groupAttributes/10
    {
        "default": true,
        "value": "This is an extremely dangerous adversary"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 10,
            "type": "Additional Analysis and Context",
            "value": "This is an extremely dangerous adversary.",
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
            "default": true
        },
        "message": "Updated",
        "status": "Success"
    }
