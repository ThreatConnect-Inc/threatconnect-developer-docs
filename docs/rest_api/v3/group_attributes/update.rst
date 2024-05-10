Update Group Attributes
-----------------------

The following example illustrates the basic format for updating a Group Attribute:

.. code::

    PUT /v3/groupAttributes/{groupAttributeId}
    Content-Type: application/json

    {
        {updatedField}: {updatedValue}
    }

For example, the following request will update the value of the Group Attribute whose ID is 10 and and add a source to the Attribute:

.. code::

    PUT /v3/groupAttributes/10
    Content-Type: application/json

    {
        "source": "CAL",
        "value": "APT28, IRON TWILIGHT, SNAKEMACKEREL, Swallowtail, Group 74, Sednit, Sofacy, Pawn Storm, Fancy Bear, STRONTIUM, Tsar Team, Threat Group-4127, TG-4127"
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 10,
            "dateAdded": "2023-03-29T14:42:13Z",
            "type": "Aliases",
            "value": "APT28, IRON TWILIGHT, SNAKEMACKEREL, Swallowtail, Group 74, Sednit, Sofacy, Pawn Storm, Fancy Bear, STRONTIUM, Tsar Team, Threat Group-4127, TG-4127",
            "source": "CAL",
            "createdBy": {
                    "id": 3,
                    "userName": "11112222333344445555",
                    "firstName": "John",
                    "lastName": "Smith",
                    "pseudonym": "jsmithAPI",
                    "owner": "Demo Organization"
            },
            "lastModified": "2023-03-30T07:16:29Z",
            "settings": {
                "associable": true,
                "pinnedByDefault": true,
                "message": "Enter any aliases for the Group object."
            },
            "pinned": true,
            "default": true
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request to the ``/v3/groupAttributes`` endpoint.