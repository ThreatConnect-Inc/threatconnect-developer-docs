Update Indicator Attributes
---------------------------

The basic format for updating an Indicator Attribute is:

.. code::

    PUT /v3/indicatorAttributes/{indicatorAttributeId}
    {
        {updatedField}: {updatedValue}
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can included in the body of a PUT request for the ``indicatorAttributes`` object.

For example, the following query will update the value of the Indicator Attribute with ID 10 and make it the default Attribute of its type:

.. code::

    PUT /v3/indicatorAttributes/10
    {
        "default": true,
        "value": "Host used by hacker conglomerate traced to China."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 10,
            "type": "Additional Analysis and Context",
            "value": "Host used by hacker conglomerate traced to China.",
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
            "default": true
        },
        "message": "Updated",
        "status": "Success"
    }
