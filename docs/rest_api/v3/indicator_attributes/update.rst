Update Indicator Attributes
---------------------------

The following example illustrates the basic format for updating an Indicator Attribute:

.. code::

    PUT /v3/indicatorAttributes/{indicatorAttributeId}
    Content-Type: application/json

    {
        {updatedField}: {updatedValue}
    }

For example, the following request will update the value of the Indicator Attribute whose ID is 10 and make it the default Attribute of its type:

.. code::

    PUT /v3/indicatorAttributes/10
    Content-Type: application/json
    
    {
        "default": true,
        "value": "Host used by hacker conglomerate traced to China."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 10,
            "dateAdded": "2021-11-09T13:32:37Z",
            "type": "Additional Analysis and Context",
            "value": "Host used by hacker conglomerate traced to China.",
            "source": "Phase of Intrusion",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555",
                "firstName": "John",
                "lastName": "Smith",
                "pseudonym": "jsmithAPI",
                "owner": "Demo Organization"
            },
            "lastModified": "2021-11-09T13:38:12Z",
            "pinned": true,
            "default": true
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request to the ``/v3/indicatorAttributes`` endpoint.