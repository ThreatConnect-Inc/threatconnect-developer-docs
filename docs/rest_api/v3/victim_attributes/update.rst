Update Victim Attributes
------------------------

The following example illustrates the basic format for updating a Victim Attribute:

.. code::

    PUT /v3/victimAttributes/{victimAttributeId}
    {
        {updatedField}: {updatedValue}
    }

For example, the following request will update the value of the Victim Attribute whose ID is 1 and make it the default Attribute of its type:

.. code::

    PUT /v3/victimAttributes/1
    {
        "default": true,
        "value": "Based on additional analysis, it was determined that this victim's social media, bank, and email accounts were hacked as the result of a phishing attack."
    }

JSON Response

.. code:: json

    {
        "data": {
            "id": 1,
            "dateAdded": "2021-11-09T15:43:06Z",
            "type": "Additional Analysis and Context",
            "value": "Based on additional analysis, it was determined that this victim's bank account was hacked.",
            "source": "Phase of Intrusion",
            "createdBy": {
                "id": 3,
                "userName": "11112222333344445555"
            },
            "lastModified": "2021-11-09T15:43:06Z",
            "pinned": false,
            "default": true
        },
        "message": "Updated",
        "status": "Success"
    }

Refer to the `Available Fields <#available-fields>`_ section for a list of available fields that can be included in the body of a PUT request for the ``victimAttributes`` object.