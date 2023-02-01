Update Group Attributes
-----------------------

The following example illustrates the basic format for updating a Group Attribute:

.. code::

    PUT /v3/groupAttributes/{groupAttributeId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following request will update the value of the Group Attribute whose ID is 10 and make it the default Attribute of its type:

.. code::

    PUT /v3/groupAttributes/10
    {
        "default": true,
        "value": "This is an extremely dangerous adversary."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 10,
            "dateAdded": "2021-11-09T14:42:13Z",
            "type": "Additional Analysis and Context",
            "value": "This is an extremely dangerous adversary.",
            "source": "Phase of Intrusion",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "lastModified": "2021-11-09T14:42:13Z",
            "pinned": false,
            "default": true
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request for the ``groupAttributes`` object.